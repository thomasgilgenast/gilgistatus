# required general imports
import webapp2

# imports for fetch-based status checking
from google.appengine.api import urlfetch

# imports for datastore
from google.appengine.ext import db
from models import Status

def parse(url):
    fetch_headers = {'Cache-Control':'no-cache,max-age=0', 'Pragma':'no-cache'}
    response = urlfetch.fetch(url, headers=fetch_headers).content
    [first, second] = response.split('<title>')
    [title, third] = second.split('</title>')
    return title

def checktitle(url, titlestring):
    try:
        title = parse(url)
        if titlestring in title:
            return 'online'
    except:
        return 'offline'
    return 'offline'

def updatetitle(site, url, titlestring):
    status = checktitle(url, titlestring)
    s = Status.get_or_insert(site, status=status)
    if s.status != status:
        s.status = status
        s.put()

def checkstatus(url):
    status = 'offline'
    try:
        fetch_headers = {'Cache-Control':'no-cache,max-age=0', 'Pragma':'no-cache'}
        result = urlfetch.fetch(url, validate_certificate=False, headers=fetch_headers)
        if result.status_code == 200:
            return 'online'
    except:
        return 'offline'
    return 'offline'

def updatestatus(site, url):
    status = checkstatus(url)
    s = Status.get_or_insert(site, status=status)
    if s.status != status:
        s.status = status
        s.put()

def checkcontent(url, contentstring):
    status = 'offline'
    try:
        fetch_headers = {'Cache-Control':'no-cache,max-age=0', 'Pragma':'no-cache'}
        response = urlfetch.fetch(url, headers=fetch_headers, deadline=60).content
        if contentstring in response:
            return 'online'
    except:
        return 'offline'
    return 'offline'

def updatecontent(site, url, contentstring):
    status = checkcontent(url, contentstring)
    s = Status.get_or_insert(site, status=status)
    if s.status != status:
        s.status = status
        s.put()

class Update(webapp2.RequestHandler):
    def get(self):
        # these update status by title
        updatetitle('www'  , 'http://www.gilgi.org/'  , 'Gilgi.org')
        updatetitle('code' , 'http://code.gilgi.org/' , 'scgs')
        updatetitle('git', 'http://git.gilgi.org/', 'List of projects - ViewGit')
        updatetitle('spqr', 'http://spqr.gilgi.org/', 'Roman Chickens')
        updatetitle('sccms', 'http://sccms.gilgi.org/', 'SCCMS')
        updatetitle('school', 'http://school.gilgi.org/', 'Princeton University Walking Navigation')

        # these update status by http status code
        updatestatus('scgs', 'http://scgs.gilgi.org/')
        updatestatus('svn', 'https://svn.gilgi.org:5555/')

        # these search for arbitrary content in the http response
        updatecontent('ts', 'http://ts.gilgi.org/', 'Scoot&#039;s Canoe TeamSpeak Server')
        updatecontent('irc', 'http://irc.gilgi.org', 'online');

app = webapp2.WSGIApplication([('/update/', Update)],
                              debug=True)
