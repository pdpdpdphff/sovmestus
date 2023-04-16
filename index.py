import random
from app import app, db, Result
from flask import Flask, render_template, url_for, request, flash, redirect


@app.route('/', methods=['GET', 'POST'])
def index():
    context = {}

    if request.method == 'POST':
        form = request.form
        if 'get_result' in form:
            result = Result.query.filter_by(
                born_1=form['born_1'],
                born_2=form['born_2'],
                name_1=form['name_1'],
                name_2=form['name_2'],
                zodiac_1=form['zodiac_1'],
                zodiac_2=form['zodiac_2']
            ).first()
            if not result:
                result = Result(
                    born_1=form['born_1'],
                    born_2=form['born_2'],
                    name_1=form['name_1'],
                    name_2=form['name_2'],
                    zodiac_1=form['zodiac_1'],
                    zodiac_2=form['zodiac_2'],
                    percent=random.randint(0, 100)
                )
                db.session.add(result)
                db.session.commit()
            
                flash(f'Совместимость: {result.percent}%')
                return redirect(url_for('index'))

            db.session.commit()
            
        flash(f'Совместимость: {result.percent}%')

    return render_template('index.html', context=context)
