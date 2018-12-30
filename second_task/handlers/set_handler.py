import webapp2

from ds.command import Command
from ds.value_counter import ValueCounter
from ds.variable import Variable
from utils.constants import SET
from utils.path_parser import PathParser


class SetHandler(webapp2.RequestHandler):
    def get(self):
        path_parser = PathParser(self.request)
        saved_value = Variable.query_name(name=path_parser.get_name())

        Command.push_command(action=SET, key=path_parser.get_name(), new_value=path_parser.get_value(),
                             old_value=saved_value)
        self.update_value_counter(path_parser, saved_value)

        Variable.put_variable(name=path_parser.get_name(), value=path_parser.get_value())

    @staticmethod
    def update_value_counter(path_parser, saved_value):
        if saved_value is not None:
            ValueCounter.decrement(saved_value)
        ValueCounter.increment(path_parser.get_value())
