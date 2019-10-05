from google.appengine.ext import ndb


class SaveProfile(ndb.Model):
  name = ndb.StringProperty()
  college = ndb.StringProperty()
  info = ndb.TextProperty()

  code = ndb.StringProperty()




  # post = ndb.TextProperty()
