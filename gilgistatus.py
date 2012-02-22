# required general imports
import webapp2
import os
from google.appengine.ext.webapp import template

# imports for datastore
from google.appengine.ext import db
from models import Status

# imports for timestamp
from datetime import datetime

class MainPage(webapp2.RequestHandler):
  def get(self):
    template_values = dict()
    query = Status.all()
    mintimestamp = datetime.max
    for result in query:
      template_values[result.key().name()] = result.status
      if result.timestamp < mintimestamp:
        mintimestamp = result.timestamp
    template_values['timestamp'] = unicode(mintimestamp.strftime('%d %B %Y %H:%M:%S').lower() + ' utc')

    path = os.path.join(os.path.dirname(__file__), 'index.html')
    self.response.out.write(template.render(path, template_values))

app = webapp2.WSGIApplication([('/', MainPage)],
                              debug=True)
