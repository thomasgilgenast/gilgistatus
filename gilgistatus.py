# required general imports
import webapp2
import os
from google.appengine.ext.webapp import template

# imports for datastore
from google.appengine.ext import db
from models import Status

# imports for timestamp
from datetime import datetime

# imports for appengine_admin
import appengine_admin

# main view class
class MainPage(webapp2.RequestHandler):
    def get(self):
        # get all the statuses
        query = Status.all()

        # logic to find the oldest timestamp
        mintimestamp = datetime.max
        for result in query:
            if result.timestamp < mintimestamp:
                mintimestamp = result.timestamp
        timestamp = unicode(mintimestamp.strftime('%d %B %Y %H:%M:%S').lower() + ' utc')

        # pass all the statuses and the timestamp to the template
        template_values = {
            'timestamp': timestamp,
            'statuses': query,
        }

        # find the template
        path = os.path.join(os.path.dirname(__file__), 'index.html')

        # render the template
        self.response.out.write(template.render(path, template_values))

# urlconf for main application
# doesn't include /update/ because that url is secured for cron only
app = webapp2.WSGIApplication([
                               ('/', MainPage),
                               (r'^(/admin)(.*)$', appengine_admin.Admin)
                               ], debug=True)
