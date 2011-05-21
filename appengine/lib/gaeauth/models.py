from google.appengine.ext import db

class User(db.Model):
    ### key_name is uid ###
    passwd = db.StringProperty(required=True)

