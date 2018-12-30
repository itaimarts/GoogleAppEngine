import google.appengine.ext.ndb as ndb
import webapp2

from ds.command import Command
from ds.value_counter import ValueCounter
from ds.variable import Variable


class EndHandler(webapp2.RequestHandler):
    def get(self):
        keys = Command.query().fetch(keys_only=True)
        ndb.delete_multi(keys)

        keys = ValueCounter.query().fetch(keys_only=True)
        ndb.delete_multi(keys)

        keys = Variable.query().fetch(keys_only=True)
        ndb.delete_multi(keys)