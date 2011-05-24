# -*- coding: utf-8 -*-
"""URL definitions."""
from tipfy.routing import Rule

rules = [
    Rule('/', name='root', handler='apps.fashion.handlers.RootHandler'),
    Rule('/set_lang', name='set_lang', handler='apps.fashion.handlers.SetLangHandler'),
    Rule('/news', handler='apps.fashion.handlers.NewsHandler'),
    Rule('/news/show', handler='apps.fashion.handlers.ShowArticleHandler'),
    Rule('/admin', handler='apps.fashion.handlers.AdminHandler'),
    Rule('/admin/documents/new', handler='apps.fashion.handlers.NewDocHandler'),
    Rule('/admin/articles/new', handler='apps.fashion.handlers.NewArticleHandler'),
    Rule('/admin/events/new', handler='apps.fashion.handlers.NewEventHandler'),
    Rule('/admin/articles/show', handler='apps.fashion.handlers.ShowArticleHandler'),
    Rule('/admin/documents/list', handler='apps.fashion.handlers.ListDocsHandler'),
    Rule('/admin/articles/list', handler='apps.fashion.handlers.ListArticlesHandler'),
    Rule('/admin/events/list', handler='apps.fashion.handlers.ListEventsHandler'),
    Rule('/admin/documents/get', handler='apps.fashion.handlers.GetDocHandler'),
    Rule('/admin_login', name='auth/login', handler='apps.fashion.handlers.AdminLoginHandler'),
    Rule('/loginBackend', handler='apps.gaeauth.handlers.LoginHandler'),
    Rule('/h4x0rz', handler='apps.gaeauth.handlers.RegAdmin')
]
