from gaesessions import get_current_session
from apps.gaeauth.models import User
import hashlib

def get_current_user():
    return get_current_session().get('user')

def hash_password(password):
    return hashlib.sha224(password).hexdigest()
 
def update_user(new_user):
    get_current_session()['user'] = new_user

def logout():
    del get_current_session()['user']

def user_exists(uid, passwd):
    return User.get_by_key_name(uid)

def is_logged():
    return (get_current_session().get('user') != None)
