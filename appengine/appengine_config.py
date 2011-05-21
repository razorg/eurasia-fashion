from gaesessions import SessionMiddleware

COOKIE='fasjfasop jdaspo djaspo j42po1j4123921 j90J(@)J#(!@)J#()!@J# J@'

def webapp_add_wsgi_middleware(app):
    app = SessionMiddleware(app, cookie_key=COOKIE)
    return app
