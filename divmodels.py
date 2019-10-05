from google.appengine.ext import ndb


class SaveProfile(ndb.Model):
  name = ndb.StringProperty()
  college = ndb.StringProperty()
  interests = ndb.TextProperty()

  comments = ndb.TextProperty(repeated=True)
  code = ndb.StringProperty()




  # post = ndb.TextProperty()
