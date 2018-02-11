class MyError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = ''

    def __str__(self):
        if self.message:
            return "Here is a MyError exception with a message:  {0}".format(self.message)
        else:
            return "Here is a MyError exception!"

# raise MyError
raise MyError('We have a problem')
