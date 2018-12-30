import webapp2

from ds.command import Command
from ds.value_counter import ValueCounter
from ds.variable import Variable
from utils.constants import UNSET
from utils.path_parser import PathParser


class UnsetHandler(webapp2.RequestHandler):
    def get(self):
        path_parser = PathParser(self.request)
        saved_value = Variable.query_name(name=path_parser.get_name())

        if saved_value is not None:
            Command.push_command(action=UNSET, key=path_parser.get_name(), new_value=None, old_value=saved_value)
            Variable.delete_variable(path_parser.get_name())
            ValueCounter.decrement(saved_value)
