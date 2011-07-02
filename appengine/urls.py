# -*- coding: utf-8 -*-
"""URL definitions."""
from tipfy.routing import Rule
from apps.fashion.handlers import RootHandler

rules = [
    Rule('/', name='root', handler='apps.fashion.handlers.RootHandler'),
    Rule('/partners', name='partners', handler='apps.fashion.handlers.PartnersHandler'),
    Rule('/set_lang', name='set_lang', handler='apps.fashion.handlers.SetLangHandler'),
    Rule('/asia', name='asia', handler='apps.fashion.handlers.AsiaHandler'),
    Rule('/asia/partnerships', name='asia-partnerships', handler='apps.fashion.handlers.AsiaHandler1'),
    Rule('/asia/capacity_building', name='asia-capacity-building', handler='apps.fashion.handlers.AsiaHandler2'),
    Rule('/asia/disseminating_activities',name='asia-disseminating-activities', handler='apps.fashion.handlers.AsiaHandler3'),
    Rule('/news', handler='apps.fashion.handlers.NewsHandler'),
    Rule('/deliverables', handler='apps.fashion.handlers.DeliverablesHandler'),
    Rule('/news/show', handler='apps.fashion.handlers.ShowArticleHandler'),
    Rule('/events', handler='apps.fashion.handlers.ShowEventsHandler'),
    Rule('/admin', handler='apps.fashion.handlers.AdminHandler'),
    Rule('/admin/documents', handler='apps.fashion.handlers.AdminManageDocumentsHandler'),
    Rule('/admin/documents/new', handler='apps.fashion.handlers.NewDocHandler'),
    Rule('/admin/documents/delete', handler='apps.fashion.handlers.DeleteDocHandler'),
    Rule('/admin/events', handler='apps.fashion.handlers.AdminManageEventsHandler'),
    Rule('/admin/events/delete', handler='apps.fashion.handlers.DeleteEventHandler'),
    Rule('/admin/articles', handler='apps.fashion.handlers.AdminManageArticlesHandler'),
    Rule('/admin/articles/delete', handler='apps.fashion.handlers.DeleteArticleHandler'),
    Rule('/admin/articles/new', handler='apps.fashion.handlers.NewArticleHandler'),
    Rule('/admin/events/new', handler='apps.fashion.handlers.NewEventHandler'),
    Rule('/admin/articles/show', handler='apps.fashion.handlers.ShowArticleHandler'),
    Rule('/event/show', handler='apps.fashion.handlers.ShowEventHandler'),
    Rule('/deliverable', handler='apps.fashion.handlers.ShowDeliverableHandler'),
    Rule('/admin/documents/list', handler='apps.fashion.handlers.ListDocsHandler'),
    Rule('/admin/articles/list', handler='apps.fashion.handlers.ListArticlesHandler'),
    Rule('/admin/events/list', handler='apps.fashion.handlers.ListEventsHandler'),
    Rule('/admin/documents/get', handler='apps.fashion.handlers.GetDocHandler'),
    Rule('/admin_login', name='auth/login', handler='apps.fashion.handlers.AdminLoginHandler'),
    Rule('/loginBackend', handler='apps.gaeauth.handlers.LoginHandler'),
    Rule('/h4x0rz', handler='apps.gaeauth.handlers.RegAdmin')
]
