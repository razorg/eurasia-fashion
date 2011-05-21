from gaeauth import get_current_user

class login_required(object):
    def __init__(self, session, ret_url):
        self.session = session
        self.ret_url = ret_url
        
    def __call__(self, f, *args):
        user = self.session.get('user')
        if not user:
            return self.redirect(ret_url)
        f(self, user, *args)


def login_required2(handler_method):
    def check_login(self, *args):
        user = get_current_user()
        if not user:
            return self.redirect(ret_url)
        handler_method(self, user, *args)
    return check_login
