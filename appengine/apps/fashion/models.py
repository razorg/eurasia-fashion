from google.appengine.ext import db

class Document(db.Model):
    title = db.StringProperty(required=True)
    desc = db.TextProperty()
    file_name = db.StringProperty(required=True)
    file = db.BlobProperty(required=True)

class Article(db.Model):
    title = db.StringProperty(required=True)
    article = db.TextProperty(required=True)
