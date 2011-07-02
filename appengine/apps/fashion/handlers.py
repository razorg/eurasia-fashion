from google.appengine.ext import db
from gaeauth import is_logged
from apps.fashion.models import Document, Article, Event

from tipfy.app import Response, redirect
from tipfy.handler import RequestHandler
from tipfyext.jinja2 import Jinja2Mixin
from tipfy.auth import login_required, LoginRequiredMiddleware, UserRequiredMiddleware
from tipfy.sessions import SessionMiddleware
from datetime import datetime

class AsiaHandler(RequestHandler, Jinja2Mixin):
    def get(self):
        return self.render_response('asia.html')

class AsiaHandler1(RequestHandler, Jinja2Mixin):
    def get(self):
        return self.render_response('asia-1.html')

class AsiaHandler2(RequestHandler, Jinja2Mixin):
    def get(self):
        return self.render_response('asia-2.html')

class AsiaHandler3(RequestHandler, Jinja2Mixin):
    def get(self):
        return self.render_response('asia-3.html')



class ServeBasics(RequestHandler):
    def get(self):
        articles = Article.all().order('-date').fetch(3)
        events = Event.all().order('-date').fetch(3)
        self.context = {
            'articles' : articles,
            'events' : events,
            'lang' : self.request.cookies.get(self.i18n.config['locale_request_lookup'][0][1])
        }

class RootHandler(ServeBasics, Jinja2Mixin):
    def get(self):
        ServeBasics.get(self)
        return self.render_response('root.html', **self.context)

class AdminLoginHandler(ServeBasics, Jinja2Mixin):
    middleware = [SessionMiddleware()]
    
    def get(self):
        ServeBasics.get(self)
        self.context['retry'] = self.request.args.get('retry')
        self.context['need']  = self.request.args.get('need')
        return self.render_response('admin_login.html', **self.context)

class AdminHandler(RequestHandler, Jinja2Mixin):
    middleware = [SessionMiddleware(), LoginRequiredMiddleware()]
    
    def get(self, **kwargs):
        return self.render_response('admin.html')

class NewDocHandler(RequestHandler, Jinja2Mixin):
    middleware = [SessionMiddleware(), LoginRequiredMiddleware()]
    
    def get(self):
        return self.render_response('admin_new_doc.html')
    
    def post(self):
        title = self.request.form.get('title')
        desc = self.request.form.get('desc')
        desc_ru = self.request.form.get('desc_ru')
        file = self.request.files.get('file')
        
        if not title:
            return self.render_response('admin_new_doc.html', **{'no_title':True})
        
        if not file:
            return self.render_response('admin_new_doc.html', **{'no_file':True})
        
        doc = Document(title=title, desc=desc, desc_ru=desc_ru, file_name=file.filename, file=db.Blob(file.read()))
        doc.put()
        return self.redirect('/admin/documents?new=1')

class NewArticleHandler(RequestHandler, Jinja2Mixin):
    middleware = [SessionMiddleware(), LoginRequiredMiddleware()]
    
    def get(self):
        return self.render_response('admin_new_article.html')
    
    
    def post(self):
        title = self.request.form.get('title')
        article = self.request.form.get('article')
        article_ru = self.request.form.get('article_ru')
        
        if (not title) or (not article) or (not article_ru):
            return Response('no title or article content')
        
        article = Article(title=title, article=article, article_ru=article_ru)
        article.put()
        return self.redirect('/admin/articles?new=1')

class NewEventHandler(RequestHandler, Jinja2Mixin):
    middleware = [SessionMiddleware(), LoginRequiredMiddleware()]
    
    def get(self):
        return self.render_response('admin_new_event.html')
    
    def post(self):
        title = self.request.form.get('title')
        desc = self.request.form.get('desc')
        desc_ru = self.request.form.get('desc_ru')
        date = self.request.form.get('date')
        if (not title) or (not date):
            return self.render_response('admin_new_event.html', **{'not_all':True})
        
        try:
            d = datetime.strptime(date, '%m/%d/%Y')
        except ValueError:
            return Response('not a valid date')
        
        e = Event(title=title, desc=desc, desc_ru=desc_ru, date=d)
        e.put()
        return self.redirect('/admin/events?new=1')

class ListDocsHandler(RequestHandler, Jinja2Mixin):
    middleware = [SessionMiddleware(), LoginRequiredMiddleware()]
    
    def get(self):
        documents = Document.all().order('-date').fetch(300)
        context = {
            'new' : self.request.args.get('new'),
            'documents' : documents
        }
        return self.render_response('admin_list_doc.html', **context)

class ListArticlesHandler(RequestHandler, Jinja2Mixin):
    middleware = [SessionMiddleware(), LoginRequiredMiddleware()]
    
    def get(self):
        articles = Article.all().order('-date').fetch(300)
        context = {
            'new' : self.request.args.get('new'),
            'articles' : articles
        }
        return self.render_response('admin_list_articles.html', **context)

class ListEventsHandler(RequestHandler, Jinja2Mixin):
    middleware = [SessionMiddleware(), LoginRequiredMiddleware()]
    
    def get(self):
        events = Event.all().fetch(300)
        context = {
            'new' : self.request.args.get('new'),
            'events' : events
        }
        return self.render_response('admin_list_events.html', **context)

class AdminManageEventsHandler(RequestHandler, Jinja2Mixin):
    middleware = [SessionMiddleware(), LoginRequiredMiddleware()]
    
    def get(self):
        events = Event.all().fetch(300)
        context = {
            'events' : events,
            'new' : self.request.args.get('new')
        }
        return self.render_response('admin_events.html', **context)

class AdminManageDocumentsHandler(RequestHandler, Jinja2Mixin):
    middleware = [SessionMiddleware(), LoginRequiredMiddleware()]
    
    def get(self):
        documents = Document.all().order('-date').fetch(300)
        context = {
            'documents' : documents,
            'new' : self.request.args.get('new')
        }
        return self.render_response('admin_documents.html', **context)

class AdminManageArticlesHandler(RequestHandler, Jinja2Mixin):
    middleware = [SessionMiddleware(), LoginRequiredMiddleware()]
    
    def get(self):
        articles = Article.all().fetch(300)
        context = {
            'articles' : articles,
            'new' : self.request.args.get('new')
        }
        return self.render_response('admin_articles.html', **context)

class DeleteDocHandler(RequestHandler):
    middleware = [SessionMiddleware(), LoginRequiredMiddleware()]
    
    def get(self):
        id = int(self.request.args.get('id'))
        if not id:
            return Response('no id given')
        doc = Document.get_by_id(id)
        if not doc:
            return Response('no doc found')
        doc.delete()
        return self.redirect('/admin/documents?del=1')

class DeleteEventHandler(RequestHandler):
    middleware = [SessionMiddleware(), LoginRequiredMiddleware()]
    
    def get(self):
        id = int(self.request.args.get('id'))
        if not id:
            return Response('no id given')
        event = Event.get_by_id(id)
        if not event:
            return Response('no event found')
        event.delete()
        return self.redirect('/admin/events?del=1')

class PartnersHandler(ServeBasics, Jinja2Mixin):
    def get(self):
        ServeBasics.get(self)
        return self.render_response('partners.html', **self.context)

class DeleteArticleHandler(RequestHandler):
    middleware = [SessionMiddleware(), LoginRequiredMiddleware()]
    
    def get(self):
        id = int(self.request.args.get('id'))
        if not id:
            return Response('no id given')
        article = Article.get_by_id(id)
        if not article:
            return Response('no article found')
        article.delete()
        return self.redirect('/admin/articles?del=1')

class ShowEventsHandler(ServeBasics, Jinja2Mixin):
    def get(self):
        ServeBasics.get(self)
        self.context['events'] =  Event.all().fetch(300)
        return self.render_response('events.html', **self.context);
        
class GetDocHandler(RequestHandler, Jinja2Mixin):
    def get(self):
        id = int(self.request.args.get('id'))
        if not id:
            return Response('no id')
        
        doc = Document.get_by_id(id)
        if not doc:
            return Response('no doc found')
        
        r = Response(doc.file)
        r.headers['Content-Type'] = 'binary/octet-stream'
        r.headers['Content-Disposition'] = 'attachment; filename=%s;' % doc.file_name
        return r

class ShowArticleHandler(ServeBasics, Jinja2Mixin):
    def get(self):
        ServeBasics.get(self)
        id = int(self.request.args.get('id'))
        if not id:
            return Response('no id')
        
        article = Article.get_by_id(id)
        if not article:
            return Response('no article found')
        
        self.context['article'] = article
        return self.render_response('article.html', **self.context)

class ShowDeliverableHandler(ServeBasics, Jinja2Mixin):
    def get(self):
        ServeBasics.get(self)
        id = int(self.request.args.get('id'))
        if not id:
            return Response('no id')
        
        deliverable = Document.get_by_id(id)
        self.context['deliverable'] = deliverable
        
        if not deliverable:
            return Response('no deliverable found')
            
        return self.render_response('deliverable.html', **self.context)

class ShowEventHandler(ServeBasics, Jinja2Mixin):
    def get(self):
        ServeBasics.get(self)
        id = int(self.request.args.get('id'))
        if not id:
            return Response('no id')
        
        event = Event.get_by_id(id)
        if not event:
            return Response('no event found')
        
        self.context['event'] = event
        return self.render_response('event.html', **self.context)

class NewsHandler(ServeBasics, Jinja2Mixin):
    def get(self):
        ServeBasics.get(self)
        return self.render_response('articles.html', **self.context)

class DeliverablesHandler(ServeBasics, Jinja2Mixin):
    def get(self):
        ServeBasics.get(self)
        documents = Document.all().order('-date').fetch(300)
        self.context['documents'] = documents
        return self.render_response('deliverables.html', **self.context)

class SetLangHandler(RequestHandler):
    def get(self):
        lang = self.request.args.get('lang')
        if not lang:
            return Response('no lang given')
        
        r = redirect('/')
        r.set_cookie(self.i18n.config['locale_request_lookup'][0][1], value=lang, path='/')
        return r
