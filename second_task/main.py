import webapp2

from handlers.end_handler import EndHandler
from handlers.get_handler import GetHandler
from handlers.numequalto_handler import NumEqualToHandler
from handlers.set_handler import SetHandler
from handlers.undo_handler import UndoHandler
from handlers.unset_handler import UnsetHandler


def main():
    application = webapp2.WSGIApplication([
        ('/get', GetHandler),
        ('/set', SetHandler),
        ('/unset', UnsetHandler),
        ('/numequalto', NumEqualToHandler),
        ('/undo', UndoHandler),
        ('/end', EndHandler)
    ], debug=False)
    return application


app = main()
