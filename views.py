# required general imports
from google.appengine.ext import webapp

# imports for templates
from google.appengine.ext.webapp import template

# imports for datastore
import models

# imports for timestamp
from datetime import datetime, timedelta

# imports for pathing
import os

# main view class
class MainPage(webapp.RequestHandler):
    def get(self):
        # get all the statuses
        query = models.Status.all()

        # logic to find the oldest timestamp
        #mintimestamp = datetime.max
        #for result in query:
        #    if result.timestamp < mintimestamp:
        #        mintimestamp = result.timestamp
        #timestamp = unicode(
        #        mintimestamp.strftime('%d %B %Y %H:%M:%S').lower()+' utc')
        updatetime = datetime.now() - timedelta(minutes=1)
        timestamp = unicode(
                updatetime.strftime('%d %B %Y %H:%M:%S').lower()+' utc')

        # pass all the statuses and the timestamp to the template
        template_values = {
            'timestamp': timestamp,
            'statuses': query,
        }

        # find the template
        path = os.path.join(os.path.dirname(__file__), 'index.html')

        # render the template
        self.response.out.write(template.render(path, template_values))
