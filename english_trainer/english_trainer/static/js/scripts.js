/*
Обучение:
jQuery   --Библиотека
$("#")   --Получение (поиск) элементов  по id

*/

//Блок скриптов для En>>>Rus

$("#but1").click(function ()  {
    //Отправляю ajax запрос на сервер
    $.ajax({
        type: "GET",                                  //параметр запроса
        url: "word-answer/",                          //По какому пути происходит запрос
        data: {
            'word-answer': $("#text_word").val(),     //Из какой формы и какие данные отправляю на сервер
        },
        dataType: "text",                             //Тип данных
        cache: false,
        success: function(data) {                     //Что делать с данными, когда произойдет ответ

            if (data == "ok") {                       //Здест происходит обработка ответов с сервера
               // console.log('ok');
                $("#text_word").attr("style", "background-color: GreenYellow; font-size: 32px");

            }
            else if (data == "no"){
                $("#text_word").attr("style", "background-color: red; font-size: 32px");
            }
        }
    });
})


$('#text_word').on("keydown", function(e) {
    console.log(e)
    if(e.keyCode == 13){
        e.preventDefault()
        $.ajax({
                type: "GET",                                 //параметр запроса
                url: "word-answer/",                         //По какому пути происходит запрос
                data: {
                    'word-answer': $("#text_word").val(),   //Из какой формы и какие данные отправляю на сервер
                },
                dataType: "text",                           //Тип данных
                cache: false,
                success: function(data) {                   //Что делать с данными, когда произойдет положительный ответ с сервера

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

$("#but2").click(function ()  {
    //Отправляю ajax запрос на сервер
    $.ajax({
        type: "GET",                                  //параметр запроса
        url: "word-help/",                            //По какому пути происходит запрос
        dataType: "text",
        success: function(word_rus) {
            $("#text_word").attr("style", "background-color: Yellow; font-size: 32px");
            $("#text_word").val(word_rus);
        }
    });
})

$('#text_word').on("keydown", function(e) {
    console.log(e)
    if(e.keyCode == 39){
        e.preventDefault()
        $.ajax({
                type: "GET",                                  //параметр запроса
                url: "word-help/",                            //По какому пути происходит запрос
                dataType: "text",
                success: function(word_rus) {
                    $("#text_word").attr("style", "background-color: Yellow; font-size: 32px");
                    $("#text_word").val(word_rus);
                    $('#text_word').on("keydown", function(e) {
                        if(e.keyCode == 39){
                                e.preventDefault()
                                location.reload();
                                }
                            })
                }
            });
        }
})


//Блок скриптов для Rus>>>En
/*
$("#but1.1").click(function ()  {
    console.log('click');
    //Отправляю ajax запрос на сервер
    $.ajax({
        type: "GET",                                  //параметр запроса
        url: "word-answer-rus/",                          //По какому пути происходит запрос
        data: {
            'word-answer': $("#text_word").val(),     //Из какой формы и какие данные отправляю на сервер
        },
        dataType: "text",                             //Тип данных
        cache: false,
        success: function(data) {                     //Что делать с данными, когда произойдет ответ

            if (data == "ok") {                       //Здест происходит обработка ответов с сервера
               // console.log('ok');
                $("#text_word").attr("style", "background-color: GreenYellow; font-size: 32px");

            }
            else if (data == "no"){
                $("#text_word").attr("style", "background-color: red; font-size: 32px");
            }
        }
    });
})

/*
$('#text_word').on("keydown", function(e) {
    console.log(e)
    if(e.keyCode == 13){
        e.preventDefault()
        $.ajax({
                type: "GET",                                 //параметр запроса
                url: "word-answer/",                         //По какому пути происходит запрос
                data: {
                    'word-answer': $("#text_word").val(),   //Какие данные отправляю на сервер
                },
                dataType: "text",                           //Тип данных
                cache: false,
                success: function(data) {                   //Что делать с данными, когда произойдет положительный ответ с сервера

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

$("#but2").click(function ()  {
    //Отправляю ajax запрос на сервер
    $.ajax({
        type: "GET",                                  //параметр запроса
        url: "word-help/",                            //По какому пути происходит запрос
        dataType: "text",
        success: function(word_rus) {
            $("#text_word").attr("style", "background-color: Yellow; font-size: 32px");
            $("#text_word").val(word_rus);
        }
    });
})

$('#text_word').on("keydown", function(e) {
    console.log(e)
    if(e.keyCode == 39){
        e.preventDefault()
        $.ajax({
                type: "GET",                                  //параметр запроса
                url: "word-help/",                            //По какому пути происходит запрос
                dataType: "text",
                success: function(word_rus) {
                    $("#text_word").attr("style", "background-color: Yellow; font-size: 32px");
                    $("#text_word").val(word_rus);
                    $('#text_word').on("keydown", function(e) {
                        if(e.keyCode == 39){
                                e.preventDefault()
                                location.reload();
                                }
                            })
                }
            });
        }
})
*/