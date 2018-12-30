import webapp2

from ds.value_counter import ValueCounter
from utils.path_parser import PathParser


class NumEqualToHandler(webapp2.RequestHandler):
    def get(self):
        path_parser = PathParser(self.request)
        amount = ValueCounter.query_value(value=path_parser.get_value())
        response = amount if amount is not None else 0
        self.response.write(response)
