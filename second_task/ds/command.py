import google.appengine.ext.ndb as ndb


class Command(ndb.Model):
    action = ndb.StringProperty()
    key_name = ndb.StringProperty()
    old_value = ndb.StringProperty()
    new_value = ndb.StringProperty()
    date = ndb.DateTimeProperty(indexed=True, auto_now_add=True)

    @staticmethod
    def push_command(action, key, old_value, new_value):
        Command(action=action, key_name=key, old_value=old_value, new_value=new_value).put()

    @staticmethod
    def pop_last_command():
        command = Command.query().order(-Command.date).fetch(1)
        if len(command) > 0:
            command[0].key.delete()
            return command[0]
        return None
