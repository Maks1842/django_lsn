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
               // console.log('ok');
              //  $("#word-answer").text("Такой Email уже существует!");
                $("#text_word").attr("style", "background-color: GreenYellow; font-size: 32px");

            }
            else if (data == "no"){
                $("#text_word").attr("style", "background-color: red; font-size: 32px");
            }
        }
    });
});


$('#text_word').on("keydown", function(e) {
    console.log(e)
    if(e.keyCode == 13){
        e.preventDefault()
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
                        $("#text_word").attr("style", "background-color: GreenYellow; font-size: 32px");
                        $('#text_word').on("keydown", function(e) {
                        if(e.keyCode == 13){
                                e.preventDefault()
                                location.reload();
                                }
                            })
                    }
                    else if (data == "no"){
                        $("#text_word").attr("style", "background-color: red; font-size: 32px");
                    }
                }
            });
    }
})

/*
$('.btn btn-primary').on("keydown", function(e) {
    console.log(e)
    if(e.keyCode == 16){
    location.reload();
    }
})

*/


/*
$("#but2").click(function ()  {
    //Отправляю ajax запрос на сервер
    $.ajax({
        type: "GET",                                  //параметр запроса
        url: "word-help/",                          //По какому пути происходит запрос
        data: {
            'word-answer': $("#text_word").val(),          //Откуда: Куда ("name": "word-answer") из формы . Какие данные отправляю
        },
        dataType: "text",                           //Тип данных
        cache: false,
        success: function(data) {               //Что делать с данными, когда произойдет ответ
            if (data == "ok") {                     //Здест происходит обработка ответов с сервера
                console.log('ok');
                //console.log(data);
                $("#text_word").text('word_rus');
                $("#text_word").attr("style", "background-color: Yellow; font-size: 32px");

            }
            else if (data == "no"){
                console.log('no');
                $("#text_word").attr("style", "background-color: red; font-size: 32px");
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