$(document).ready(function () {
    $('#active').click(function () {
        if ($('#map-show').hasClass('map-block') | $('#info-show').hasClass('info-block')) {
            $('#map-show').removeClass();
            $('#map-show').addClass('map-block-after');
            $('#map-show').addClass('animate__animated');
            $('#map-show').addClass('animate__fadeInLeft');
            $('#info-show').removeClass();
            $('#info-show').addClass('info-block-after');
            $('#info-show').addClass('animate__animated');
            $('#info-show').addClass('animate__fadeInLeft');
        }
        else {
            $('#map-show').removeClass();
            $('#map-show').addClass('map-block');
            $('#info-show').removeClass();
            $('#info-show').addClass('info-block');
        }
    });
});
$(document).ready(function () {
    $('#close1').click(function () {
        $('#map-show').removeClass();
        $('#map-show').addClass('map-block');
    });
});

$(document).ready(function () {
    $('#close2').click(function () {
        $('#info-show').removeClass();
        $('#info-show').addClass('info-block');
        $('#map-show').removeClass();
        $('#map-show').addClass('map-block-after1');
    });
});
$(document).ready(function () {
    $('#forma-pet').click(function () {
        if ($('#window').hasClass('window-give-me-pet')) {
            $('#window').removeClass('window-give-me-pet');
            $('#window').addClass('window-give-me-pet-after');
            $('#window').addClass('animate__animated');
            $('#window').addClass('animate__fadeInDown');
        }
    });
});
$(document).ready(function () {
    $('#close3').click(function () {
        $('#window').removeClass('window-give-me-pet-after');
        $('#window').addClass('window-give-me-pet');
        $('#window').removeClass('animate__animated');
        $('#window').removeClass('animate__fadeInDown');
    });
});
var proof=0;
(function ($) {
    $(function () {
        $('.rf').each(function () {
            // Объявляем переменные (форма и кнопка отправки)
            var form = $(this),
                btn = form.find('.btn_submit');
            // Добавляем каждому проверяемому полю, указание что поле пустое
            form.find('.rfield').addClass('empty_field');
            // Функция проверки полей формы
            function checkInput() {
                form.find('.rfield').each(function () {
                    if ($(this).val() != '') {
                        // Если поле не пустое удаляем класс-указание
                        $(this).removeClass('empty_field');
                    } else {
                        // Если поле пустое добавляем класс-указание
                        $(this).addClass('empty_field');
                    }
                });
            }
            // Функция подсветки незаполненных полей
            function lightEmpty() {
                form.find('.empty_field').css({ 'border-color': '#d8512d' });
                // Через полсекунды удаляем подсветку
                setTimeout(function () {
                    form.find('.empty_field').removeAttr('style');
                }, 500);
            }
            // Проверка в режиме реального времени
            setInterval(function () {
                // Запускаем функцию проверки полей на заполненность
                checkInput();
                // Считаем к-во незаполненных полей
                var sizeEmpty = form.find('.empty_field').size();
                // Вешаем условие-тригер на кнопку отправки формы
                if (sizeEmpty > 0) {
                    if (btn.hasClass('disabled')) {
                        return false
                    } else {
                        btn.addClass('disabled')
                    }
                } else {
                    btn.removeClass('disabled')
                }
            }, 500);
            // Событие клика по кнопке отправить
            btn.click(function () {
                if ($(this).hasClass('disabled')) {
                    // подсвечиваем незаполненные поля и форму не отправляем, если есть незаполненные поля
                    lightEmpty();
                    return false
                } else {
                    // Все хорошо, все заполнено, отправляем форму
                    proof=1;
                    form.submit();
                }
            });
        });
    });
})(jQuery);
$(document).ready(function () {//надо выводить после проверки(она выше) 
    if (proof == 1) {
        $('#enter').click(function () {
            $('#win-thx').removeClass();
            $('#win-thx').addClass('thank-you-after');
            $('#win-thx').addClass('animate__animated');
            $('#win-thx').addClass('animate__fadeInDown');
        });
    };
});

$(document).ready(function () {
    $('#ok').click(function () {
        $('#win-thx').removeClass();
        $('#win-thx').addClass('thank-you');
        $('#window').removeClass();
        $('#window').addClass('window-give-me-pet');
    });
});