
// Запрет перетягивания ссылок и изображений.
['a', 'img'].forEach((item) => {
    const elementList = document.querySelectorAll(item);

    if (elementList) {
        elementList.forEach(function(item) {
            item.setAttribute('draggable', 'false');
        });
    };
});


// Выравнивание текста в кнопках.
buttonList = document.querySelectorAll('.btn');

if (buttonList) {
    buttonList.forEach((item) => {
        var itemStyle = window.getComputedStyle(item);
        var itemHeight = itemStyle.height;
        item.style.lineHeight = itemHeight;

        // itemLength = itemStyle.length;
        // console.log(itemLength);
        // item.style.width = `${itemLength / 1.5}px`;
    });
};