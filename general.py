from app import app, db
import index


with app.app_context():
    db.create_all()

app.run(host='0.0.0.0')
