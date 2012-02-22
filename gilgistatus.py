# required general imports
import webapp2
import os
from google.appengine.ext.webapp import template

# imports for fetch-based status checking
from google.appengine.api import urlfetch
import lxml

# imports for logging (disable for production)
#import logging

# imports for datastore
from google.appengine.ext import db

class Status(db.model):
  site = db.StringProperty()
  status = db.StringProperty()

class MainPage(webapp2.RequestHandler):
  def get(self):
        # check www
        www = 'offline'
        url = "http://www.gilgi.org/"
        try:
            #t = lxml.html.parse(url)
            result = urlfetch.fetch(url)
            #logging.info(t.find(".//title").text)
            logging.info(result.)
            if t.find(".//title").text == 'Gilgi.org':
                www = 'online'
        except:
            www = 'offline'

        # check scgs
        scgs = 'offline'
        url = "http://scgs.gilgi.org/"
        #t = lxml.html.parse(url)
        try:
            result = urlfetch.fetch(url)
            #logging.info(t.find(".//title").text)
            #if t.find(".//title").text == 'Gilgi.org':
            if result.status_code == 200:
                scgs = 'online'
        except:
            scgs = 'offline'

        # check code
        code = 'offline'
        url = "http://code.gilgi.org/"
        try:
            t = lxml.html.parse(url)
            #logging.info(t.find(".//title").text)
            #if t.find(".//title").text == "scgs - Scoot\'s Canoe Game Studios, Inc. - Google Project Hosting":
            if 'scgs' in t.find(".//title").text:
                code = 'online'
        except:
            code = 'offline'

        # check git
        git = 'offline'
        url = "http://git.gilgi.org/"
        try:
            t = lxml.html.parse(url)
            #logging.info(t.find(".//title").text)
            if t.find(".//title").text == 'List of projects - ViewGit':
                git = 'online'
        except:
            git = 'offline'

        # check irc
        irc = 'unknown'

        # check spqr
        spqr = 'offline'
        url = "http://spqr.gilgi.org/"
        try:
            t = lxml.html.parse(url)
            #logging.info(t.find(".//title").text)
            if 'Roman Chickens' in t.find(".//title").text:
                spqr = 'online'
        except:
            spqr = 'offline'

        # check sccms
        sccms = 'offline'
        url = "http://sccms.gilgi.org/"
        try:
            t = lxml.html.parse(url)
            #logging.info(t.find(".//title").text)
            if 'SCCMS' in t.find(".//title").text:
                sccms = 'online'
        except:
            sccms = 'offline'

        # check school
        school = 'offline'
        url = "http://school.gilgi.org/"
        try:
            t = lxml.html.parse(url)
            #logging.info(t.find(".//title").text)
            if t.find(".//title").text == 'Princeton University Walking Navigation':
                school = 'online'
        except:
            school = 'offline'

        # check svn
        #svn = 'online'
        svn = 'offline'
        url = "https://svn.gilgi.org:5555/"
        try:
            #t = lxml.html.parse(url)
            result = urlfetch.fetch(url, validate_certificate=False)
            #logging.info(t.find(".//title").text)
            #if t.find(".//title").text == 'Gilgi.org':
            if result.status_code == 200:
                svn = 'online'
        except:
            svn = 'offline'

        # check ts
        ts = 'unknown'
      
        template_values = {
            'www': www,
            'scgs': scgs,
            'code': code,
            'git': git,
            'irc': irc,
            'spqr': spqr,
            'sccms': sccms,
            'school': school,
            'svn': svn,
            'ts': ts,
        }

        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.out.write(template.render(path, template_values))

app = webapp2.WSGIApplication([('/', MainPage)],
                              debug=True)
