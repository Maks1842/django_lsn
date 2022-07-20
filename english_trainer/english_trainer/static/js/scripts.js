/*
Обучение:
jQuery   --Библиотека
$("#")   --Получение (поиск) элементов  по id

*/
$("#but1").click(function ()  {
    //Отправляю ajax запрос на сервер
    $.ajax({
        type: "GET",                                  //параметр запроса
        url: "word-answer/",                          //По какому пути происходит запрос
        data: {
            'word-answer': $("#text_word").val(),          //Откуда: Куда ("name": "word-answer") из формы . Какие данные отправляю
        },
        dataType: "text",                           //Тип данных
        cache: false,
        success: function(data) {               //Что делать с данными, когда произойдет ответ

            if (data == "ok") {                     //Здест происходит обработка ответов с сервера
                console.log('ok');
                $("#word-answer").text("Такой Email уже существует!");
                $("#word-answer").attr("style", "color: red;");

            }
            else if (data == "no"){
                console.log('no');
               // $("#word-answer").text("Почта");
                $("#word-answer").attr("style", "color: green;");
            }
        }
    });
});

/*
//Отлавливаю нажатие кнопки
$(function ($) {
    $('#but1').submit(function (e) {
    e.preventDefault()
    console.log(this)
    })
})
*/