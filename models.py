# imports for datastore
from google.appengine.ext import db

# imports for appengine_admin
import appengine_admin

# represents the status of a site and associated information
class Status(db.Model):
    # short description of the site
    description = db.StringProperty()

    # comment about the site
    comment = db.StringProperty()
    
    # link to the site
    link_url = db.StringProperty()

    # update information
    # should we check the status, title, or contents of the webpage?
    update_type = db.StringProperty(default='none',
                                    choices=set(['status', 'title', 'contents', 'none']))

    # if contents, what should we look for in the contents?
    update_content = db.StringProperty()

    # if title, what should we look for in the title
    update_title = db.StringProperty()

    # what url should we use to check the service
    # if different from the link_url above?
    update_url = db.StringProperty(default=self.link_url)

    # the status of the site
    status = db.StringProperty()

    # the last time this entity was updated
    timestamp = db.DateTimeProperty(auto_now=True)

    def __unicode__(self):
        return self.key().name()

# wrapper classes for admin interface
class AdminStatus(appengine_admin.ModelAdmin):
    model = Status
    listFields =     ('description',
                      'status',)
    editFields =     ('description',
                      'link_url',
                      'comment',
                      'check_type',
                      'check_url',
                      'status',)
    readonlyFields = ('timestamp',)

# register admin wrapper classes with the admin interface
appengine_admin.register(AdminStatus)
