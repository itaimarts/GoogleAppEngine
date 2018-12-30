import google.appengine.ext.ndb as ndb


class ValueCounter(ndb.Model):
    amount = ndb.IntegerProperty()

    @staticmethod
    def query_value(value):
        query_result = ndb.Key(ValueCounter, value).get()
        return query_result if query_result is None else query_result.amount

    @staticmethod
    def increment(value):
        old_counter = ndb.Key(ValueCounter, value).get()
        if old_counter is not None:
            old_counter.amount += 1
            old_counter.put()
        else:
            ValueCounter(id=value, amount=1).put()

    @staticmethod
    def decrement(value):
        old_counter = ndb.Key(ValueCounter, value).get()
        if old_counter is not None:
            old_counter.amount -= 1
            old_counter.put()
            if old_counter.amount is 0:
                old_counter.key.delete()
