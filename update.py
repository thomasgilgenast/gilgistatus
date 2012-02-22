# required general imports
import webapp2

# imports for fetch-based status checking
from google.appengine.api import urlfetch
#import lxml.html
#from xml.etree import ElementTree

# imports for datastore
from google.appengine.ext import db
from models import Status

import logging

def parse(url):
    #root = ElementTree.fromstring(urlfetch.fetch(url).content)
    #root = ElementTree.parse(url)
    #logging.info(list(root))
    #html = root.find('html')
    #logging.info(list(html))
    #head = html.find('head')
    #logging.info(list(head))
    #title = head.find('title')
    #title = ElementTree.fromstring('<xml>'+urlfetch.fetch(url).content+'</xml>').find(html/head/title)
    response = urlfetch.fetch(url).content
    [first, second] = response.split('<title>')
    [title, third] = second.split('</title>')
    return title

class Update(webapp2.RequestHandler):
    def get(self):
        # check www
        url = "http://www.gilgi.org/"
        try:
            title = parse(url)
            #t = lxml.html.parse(url)
            #result = urlfetch.fetch(url)
            #logging.info(t.find(".//title").text)
            #logging.info(result.)
            #if t.find(".//title").text == 'Gilgi.org':
            if title == 'Gilgi.org':
                s = Status.get_or_insert('www', status='online')
                s.status = 'online'
                s.put()
        except:
            s = Status.get_or_insert('www', status='offline')
            s.status = 'offline'
            s.put()

        # check scgs
        url = "http://scgs.gilgi.org/"
        try:
            result = urlfetch.fetch(url)
            if result.status_code == 200:
                s = Status.get_or_insert('scgs', status='online')
                s.status = 'online'
                s.put()
        except:
            s = Status.get_or_insert('scgs', status='offline')
            s.status = 'offline'
            s.put()

        # check code
        url = "http://code.gilgi.org/"
        try:
            t = lxml.html.parse(url)
            if 'scgs' in t.find(".//title").text:
                s = Status.get_or_insert('code', status='online')
                s.status = 'online'
                s.put()
        except:
            s = Status.get_or_insert('code', status='offline')
            s.status = 'offline'
            s.put()

        # check git
        url = "http://git.gilgi.org/"
        try:
            t = lxml.html.parse(url)
            if t.find(".//title").text == 'List of projects - ViewGit':
                s = Status.get_or_insert('git', status='online')
                s.status = 'online'
                s.put()
        except:
            s = Status.get_or_insert('git', status='offline')
            s.status = 'offline'
            s.put()

        # check irc
        s = Status.get_or_insert('irc', status='unknown')
        s.status = 'unknown'
        s.put()

        # check spqr
        url = "http://spqr.gilgi.org/"
        try:
            t = lxml.html.parse(url)
            if 'Roman Chickens' in t.find(".//title").text:
                s = Status.get_or_insert('spqr', status='online')
                s.status = 'online'
                s.put()
        except:
            s = Status.get_or_insert('spqr', status='offline')
            s.status = 'offline'
            s.put()

        # check sccms
        url = "http://sccms.gilgi.org/"
        try:
            t = lxml.html.parse(url)
            if 'SCCMS' in t.find(".//title").text:
                s = Status.get_or_insert('sccms', status='online')
                s.status = 'online'
                s.put()
        except:
            s = Status.get_or_insert('sccms', status='offline')
            s.status = 'offline'
            s.put()

        # check school
        url = "http://school.gilgi.org/"
        try:
            t = lxml.html.parse(url)
            if t.find(".//title").text == 'Princeton University Walking Navigation':
                s = Status.get_or_insert('school', status='online')
                s.status = 'online'
                s.put()
        except:
            s = Status.get_or_insert('school', status='offline')
            s.status = 'offline'
            s.put()

        # check svn
        url = "https://svn.gilgi.org:5555/"
        try:
            result = urlfetch.fetch(url, validate_certificate=False)
            if result.status_code == 200:
                s = Status.get_or_insert('svn', status='online')
                s.status = 'online'
                s.put()
        except:
            s = Status.get_or_insert('svn', status='offline')
            s.status = 'offline'
            s.put()

        # check ts
        s = Status.get_or_insert('ts', status='unknown')
        s.status = 'unknown'
        s.put()

app = webapp2.WSGIApplication([('/update/', Update)],
                              debug=True)
