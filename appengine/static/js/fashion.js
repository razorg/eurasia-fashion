$(document).ready(function() {
    var home = $('#menu li a:eq(0)');
    var asia = $('#menu ul li a:eq(1)');
    var news = $('#menu ul li a:eq(2)');
    var events = $('#menu ul li a:eq(3)');
    var deliverables = $('#menu ul li a:eq(4)');
    var partners = $('#menu ul li a:eq(5)');
    var path = document.location.pathname;
    var en = $('#en');
    var ru = $('#ru');
    var lang = $.cookie('lang') || 'en_US';
    if (path.search('^/$') != -1)
        home.addClass('active');
    else if (path.search('^/asia') != -1)
        asia.addClass('active');
    else if (path.search('^/news') != -1)
        news.addClass('active');
    else if (path.search('^/events') != -1)
        events.addClass('active');
    else if (path.search('^/deliverables') != -1)
        deliverables.addClass('active');
    else if (path.search('^/partners') != -1)
        partners.addClass('active');
    function fix(elem) {
        elem.css('background-image', '-moz-linear-gradient(center top,rgb(255,198,138) 43%,rgb(255,170,79) 72%)');
        elem.css('background-image', '-webkit-gradient(linear,right top,right bottom,color-stop(0.43, rgb(255,198,138)),color-stop(0.72, rgb(255,170,79)))');
    }
    if (lang == 'en_US')
        fix(en);
    else if (lang == 'ru_RU')
        fix(ru);
    
    $('.editor').each(function() {
            CKEDITOR.replace(this.id, {});
    });
});

$(window).load(function() {
    $('#slider').nivoSlider({
        controlNav:false,
         prevText: '',
         nextText: '',
         pauseTime:4000,
    });
});
