import os, sys, gettext

if 'lib' not in sys.path:
    sys.path[0:0] = ['lib']

from jinja2 import Environment, FileSystemLoader
from gaesessions import get_current_session


jinja_dirs = [os.path.join(os.path.dirname(__file__), 'templates')]
jinja_env = Environment(loader=FileSystemLoader(jinja_dirs), extensions=['jinja2.ext.i18n'])
_ = gettext.translation('messages', os.path.join(os.path.dirname(__file__), 'babel'), ['en_US', 'ru_RU'])
_ = _.gettext
jinja_env.install_gettext_callables(_, None)
import re

from jinja2 import evalcontextfilter, Markup, escape
_paragraph_re = re.compile(r'(?:\r\n|\r|\n){2,}')
@evalcontextfilter
def nl2br(eval_ctx, value):
    result = u'\n\n'.join(u'%s<br>' % p.replace('\n', '<br>\n') \
        for p in _paragraph_re.split(escape(value)))
    if eval_ctx.autoescape:
        result = Markup(result)
    return result

jinja_env.filters['nl2br'] = nl2br
    
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from apps.fashion import handlers as fashion_handlers
from apps.gaeauth import handlers as gaeauth_handlers
rules = [
  ('/', fashion_handlers.RootHandler),
  ('/set_lang', fashion_handlers.SetLangHandler),
  ('/news', fashion_handlers.NewsHandler),
  ('/news/show', fashion_handlers.ShowArticleHandler),
  ('/admin', fashion_handlers.AdminHandler),
  ('/admin/documents/new', fashion_handlers.NewDocHandler),
  ('/admin/articles/new', fashion_handlers.NewArticleHandler),
  ('/admin/articles/show', fashion_handlers.ShowArticleHandler),
  ('/admin/documents/list', fashion_handlers.ListDocsHandler),
  ('/admin/articles/list', fashion_handlers.ListArticlesHandler),
  ('/admin/documents/get', fashion_handlers.GetDocHandler),
  ('/admin_login', fashion_handlers.AdminLoginHandler),
  ('/loginBackend', gaeauth_handlers.LoginHandler),
  ('/h4x0rz', gaeauth_handlers.RegAdmin)
]
app = webapp.WSGIApplication(rules, debug=True)

def main():
    run_wsgi_app(app)


if __name__ == '__main__':
    main()
