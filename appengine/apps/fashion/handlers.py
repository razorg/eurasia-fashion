from helpers import TemplatedRequest, translate
from google.appengine.ext import webapp, db
from gaeauth import is_logged
from apps.fashion.models import Document, Article
from gaesessions import get_current_session

class RootHandler(webapp.RequestHandler, TemplatedRequest):
    @translate
    def get(self):
        return self.render_response('root.html')

class AdminLoginHandler(webapp.RequestHandler, TemplatedRequest):
    @translate
    def get(self):
        context = {
            'retry' : self.request.get('retry'),
            'need'  : self.request.get('need')
        }
        return self.render_response('admin_login.html', context)

class AdminHandler(webapp.RequestHandler, TemplatedRequest):
    @translate
    def get(self):
        logged = is_logged() 
        if not logged:
            return self.redirect('/admin_login?need=1')
            
        return self.render_response('admin.html')

class NewDocHandler(webapp.RequestHandler, TemplatedRequest):
    @translate
    def get(self):
        logged = is_logged() 
        if not logged:
            return self.redirect('/admin_login?need=1')
        
        return self.render_response('admin_new_doc.html')
    
    @translate
    def post(self):
        logged = is_logged() 
        if not logged:
            return self.redirect('/admin_login?need=1')
        
        title = self.request.get('title')
        desc = self.request.get('desc')
        file = self.request.get('file')
        
        if not title:
            return self.render_response('admin_new_doc.html', {'no_title':True})
        
        if not file:
            return self.render_response('admin_new_doc.html', {'no_file':True})
        
        doc = Document(title=title, desc=desc, file_name=self.request.POST[u'file'].filename, file=db.Blob(file))
        doc.put()
        self.redirect('/admin/documents/list?new=1')

class NewArticleHandler(webapp.RequestHandler, TemplatedRequest):
    @translate
    def get(self):
        logged = is_logged() 
        if not logged:
            return self.redirect('/admin_login?need=1')
        
        return self.render_response('admin_new_article.html')
    
    @translate
    def post(self):
        logged = is_logged() 
        if not logged:
            return self.redirect('/admin_login?need=1')
        
        title = self.request.get('title')
        article = self.request.get('article')
        if (not title) or (not article):
            return self.response.out.write('no title or article')
        
        article = Article(title=title, article=article)
        article.put()
        return self.redirect('/admin/articles/list?new=1')

class ListDocsHandler(webapp.RequestHandler, TemplatedRequest):
    @translate
    def get(self):
        logged = is_logged()
        if not logged:
            return self.redirect('/admin_login?need=1')
        
        documents = Document.all().fetch(300)
        context = {
            'new' : self.request.get('new'),
            'documents' : documents
        }
        return self.render_response('admin_list_doc.html', context)

class ListArticlesHandler(webapp.RequestHandler, TemplatedRequest):
    @translate
    def get(self):
        logged = is_logged()
        if not logged:
            return self.redirect('/admin_login?need=1')
        
        articles = Article.all().fetch(300)
        context = {
            'new' : self.request.get('new'),
            'articles' : articles
        }
        return self.render_response('admin_list_articles.html', context)

class GetDocHandler(webapp.RequestHandler, TemplatedRequest):
    @translate
    def get(self):
        logged = is_logged() 
        if not logged:
            return self.redirect('/admin_login?need=1')
        
        id = int(self.request.get('id'))
        if not id:
            return self.response.out.write('no id')
        
        doc = Document.get_by_id(id)
        if not doc:
            return self.response.out.write('no doc found')
        
        self.response.headers['Content-Type'] = 'binary/octet-stream'
        self.response.headers['Content-Disposition'] = 'attachment; filename=%s;' % doc.file_name
        return self.response.out.write(doc.file)

class ShowArticleHandler(webapp.RequestHandler, TemplatedRequest):
    @translate
    def get(self):
        id = int(self.request.get('id'))
        if not id:
            return self.response.out.write('no id')
        
        article = Article.get_by_id(id)
        if not article:
            return self.response.out.write('no article found')
        
        self.render_response('article.html', {'article':article})

class NewsHandler(webapp.RequestHandler, TemplatedRequest):
    @translate
    def get(self):
        articles = Article.all().fetch(300)
        return self.render_response('articles.html', {'articles':articles})

class SetLangHandler(webapp.RequestHandler, TemplatedRequest):
    def get(self):
        lang = self.request.get('lang')
        if not lang:
            return self.response.out.write('no lang given')
        
        get_current_session()['lang'] = lang
        return self.redirect('/')
