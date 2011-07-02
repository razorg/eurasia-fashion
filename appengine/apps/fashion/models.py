from google.appengine.ext import db

class Document(db.Model):
    title = db.StringProperty(required=True)
    desc = db.TextProperty()
    desc_ru = db.TextProperty()
    file_name = db.StringProperty(required=True)
    file = db.BlobProperty(required=True)
    date = db.DateTimeProperty(required=True, auto_now_add=True)

class Article(db.Model):
    title = db.StringProperty(required=True)
    article = db.TextProperty(required=True)
    article_ru = db.TextProperty(required=True)
    date = db.DateTimeProperty(required=True, auto_now_add=True)

class Event(db.Model):
    title = db.StringProperty(required=True)
    desc = db.TextProperty(required=True)
    desc_ru = db.TextProperty(required=True)
    date = db.DateTimeProperty(required=True)
    date = db.DateTimeProperty(required=True, auto_now_add=True)

