class PathParser:
    NAME = "name"
    VALUE = "value"

    def __init__(self, request):
        self.request = request

    def get_name(self):
        return self.request.get(PathParser.NAME)

    def get_value(self):
        return self.request.get(PathParser.VALUE)
