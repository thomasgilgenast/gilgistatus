# required general imports
import webapp2

# imports for fetch-based status checking
from google.appengine.api import urlfetch

# imports for datastore
from google.appengine.ext import db
from models import Status

# helper method that parses the title out of the html recieved from a url
def parsetitle(url):
    # make sure we're not getting cached content
    fetch_headers = {'Cache-Control':'no-cache,max-age=0', 'Pragma':'no-cache'}

    # fetch the content
    response = urlfetch.fetch(url, headers=fetch_headers).content

    # parse the content
    [first, second] = response.split('<title>')
    [title, third] = second.split('</title>')

    # return the title
    return title

# update a particular instance of Status
# according to the directions specified in its properties
def update(status_instance):
    # this update_type should be left alone
    if status_instance.update_type = 'none':
        return

    # check the status
    status = check(status_instance.url,
                   check_type=status_instance.update_type,
                   content=status_instance.update_content,
                   title=status_instance.update_title)

    # if the status has changed, update it
    # and write the new status instance to the datastore
    if status_instance.status != status:
        status_instance.status = status
        status_instance.put()
    return

def check(url, check_type='status', content='', title=''):
    fetch_headers = {'Cache-Control':'no-cache,max-age=0', 'Pragma':'no-cache'}
    if check_type == 'status':
        try:
            response = urlfetch.fetch(url, headers=fetch_headers, deadline=60, validate_certificate=False)
            if response.status_code == 200:
                return 'online'
        except:
            pass
    elif check_type == 'title':
        try:
            parsedtitle = parsetitle(url)
            if titlestring in parsedtitle:
                return 'online'
        except:
            pass
    elif check_type == 'content':
        try:
            response = urlfetch.fetch(url, headers=fetch_headers, deadline=60, validate_certificate=False).content
            if content in response:
                return 'online'
        except:
            pass
    return 'offline'

# update "view" class
class Update(webapp2.RequestHandler):
    def get(self):
        # update all the statuses
        query = Status.all()
        for result in query:
            update(result)
        return

# urlconf for update
# separate from main urlconf because this url should be secured for cron only
app = webapp2.WSGIApplication([('/update/', Update)],
                              debug=True)
