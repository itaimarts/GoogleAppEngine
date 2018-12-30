import webapp2

from ds.variable import Variable
from utils.path_parser import PathParser


class GetHandler(webapp2.RequestHandler):
    def get(self):
        path_parser = PathParser(self.request)
        value = Variable.query_name(name=path_parser.get_name())
        self.response.write(value)
