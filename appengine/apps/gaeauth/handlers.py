from google.appengine.ext import webapp
import gaeauth

class LoginHandler(webapp.RequestHandler):
    def post(self):
        uid = self.request.get('uid')
        passwd = self.request.get('passwd')
        if (not uid) or (not passwd):
            return self.redirect('/wrong_call')
            
        onSucc = self.request.get('onSucc')
        if not onSucc or onSucc[0] != '/':
            return self.redirect('/wrong_call')
        
        onFail = self.request.get('onFail')
        if not onFail or onFail[0] != '/':
            return self.redirect('/wrong_call')
        
        
        passwd = gaeauth.hash_password(passwd)
        exists = gaeauth.user_exists(uid, passwd)
        if not exists:
            return self.redirect('%s%s%s' %(self.request.host_url, onFail, '?retry=1'))
        
        gaeauth.update_user(exists)
        return self.redirect('%s%s' % (self.request.host_url, onSucc))

class RegAdmin(webapp.RequestHandler):
    def get(self):
        from apps.gaeauth.models import User
        from gaeauth import hash_password
        u = User(key_name='admin', passwd=hash_password('admin'))
        u.put()
        return self.redirect('/')
