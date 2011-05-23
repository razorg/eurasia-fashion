from google.appengine.ext import webapp
import gaeauth
from tipfy.app import Response
from tipfy.handler import RequestHandler
from tipfy.auth import MultiAuthStore

class LoginHandler(RequestHandler):
    def post(self):
        uid = self.request.form.get('uid')
        passwd = self.request.form.get('passwd')
        if (not uid) or (not passwd):
            return self.redirect('/wrong_call1')
            
        onSucc = self.request.form.get('onSucc')
        if not onSucc:
            return self.redirect('/wrong_call2')
        
        onFail = self.request.form.get('onFail')
        if not onFail:
            return self.redirect('/wrong_call3')
        
        a = MultiAuthStore(self.request)
        res = a.login_with_form(uid, passwd)
        if not res:
            return self.redirect('%s%s%s' %(self.request.host_url, onFail, '?retry=1'))
        return self.redirect('%s%s' % (self.request.host_url, onSucc))

class RegAdmin(RequestHandler):
    def get(self):
        a = BaseAuthStore(self.request)
        u = a.create_user('admin','own|admin', password='admin')
        return self.redirect('/')
