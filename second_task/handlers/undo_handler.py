import webapp2

from ds.command import Command
from ds.value_counter import ValueCounter
from ds.variable import Variable
from utils.constants import SET, NO_COMMANDS


class UndoHandler(webapp2.RequestHandler):
    def get(self):
        last_command = Command.pop_last_command()
        if last_command is not None:
            if last_command.action == SET:
                self.undo_set_command(last_command)
            else:
                self.undo_unset_command(last_command)
        else:
            self.response.write(NO_COMMANDS)

    @staticmethod
    def undo_unset_command(last_command):
        Variable.put_variable(name=last_command.key_name, value=last_command.old_value)
        ValueCounter.increment(last_command.old_value)

    @staticmethod
    def undo_set_command(last_command):
        if last_command.old_value is not None:
            Variable.put_variable(name=last_command.key_name, value=last_command.old_value)
            ValueCounter.increment(last_command.old_value)
            ValueCounter.decrement(last_command.new_value)
        else:
            Variable.delete_variable(name=last_command.key_name)
            ValueCounter.decrement(last_command.new_value)
