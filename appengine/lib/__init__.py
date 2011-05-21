from gaesessions import get_current_session
import hashlib

def get_current_user():
    return get_current_session().get('user')

def hash_password(password):
    return hashlib.sha224(password).hexdigest()
 
def update_user(new_user):
    get_current_session()['user'] = new_user

def logout():
    del get_current_session()['user']
