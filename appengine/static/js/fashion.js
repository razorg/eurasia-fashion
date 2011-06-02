$(document).ready(function() {
    var home = $('#menu ul li a:eq(0)');
    var asia = $('#menu ul li a:eq(1)');
    var news = $('#menu ul li a:eq(2)');
    var events = $('#menu ul li a:eq(3)');
    var partners = $('#menu ul li a:eq(4)');
    var contacts = $('#menu ul li a:eq(5)');
    var path = document.location.pathname;
    if (path.search('^/$') != -1)
        home.addClass('selected');
    else if (path.search('^/asia') != -1)
        asia.addClass('selected');
    else if (path.search('^/news') != -1)
        news.addClass('selected');
    else if (path.search('^/events') != -1)
        events.addClass('selected');
    else if (path.search('^/partners') != -1)
        partners.addClass('selected');
    else if (path.search('^/contacts') != -1)
        contacts.addClass('selected');
});
