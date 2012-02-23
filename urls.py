# general imports
from google.appengine.ext import webapp

# urlconf imports
from google.appengine.ext.webapp.util import run_wsgi_app

# import views
import views

application = webapp.WSGIApplication([
        # main page
        ('/', views.MainPage),
    ], debug = True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
