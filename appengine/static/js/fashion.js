$(document).ready(function() {
    var home = $('#menu li a:eq(0)');
    var asia = $('#menu ul li a:eq(1)');
    var news = $('#menu ul li a:eq(2)');
    var events = $('#menu ul li a:eq(3)');
    var partners = $('#menu ul li a:eq(4)');
    var path = document.location.pathname;
    if (path.search('^/$') != -1)
        home.addClass('active');
    else if (path.search('^/asia') != -1)
        asia.addClass('active');
    else if (path.search('^/news') != -1)
        news.addClass('active');
    else if (path.search('^/events') != -1)
        events.addClass('active');
    else if (path.search('^/partners') != -1)
        partners.addClass('active');
});
