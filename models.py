# imports for datastore
from google.appengine.ext import db

class Status(db.Model):
    status = db.StringProperty(indexed=False)
    timestamp = db.DateTimeProperty(auto_now=True)
