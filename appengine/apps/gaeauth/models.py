from google.appengine.ext import db

class User(db.Model):
    # str_name = uid
    passwd = db.StringProperty(required=True)

