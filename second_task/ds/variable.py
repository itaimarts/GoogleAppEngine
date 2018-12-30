import google.appengine.ext.ndb as ndb


class Variable(ndb.Model):
    value = ndb.StringProperty()

    @staticmethod
    def query_name(name):
        query_result = ndb.Key(Variable, name).get()
        value = query_result if query_result is None else query_result.value
        return value

    @staticmethod
    def put_variable(name, value):
        Variable(id=name, value=value).put()

    @staticmethod
    def delete_variable(name):
        ndb.Key(Variable, name).delete()
