import traceback

# Our logger has two methods designed for regular use:
# log will print a log that you enter to the console
# throw will print an error message to the console, alongside the stack-trace
# The set method can turn logs on / off (on by default so messages in the window's init func are printed properly)
# The post method could be used to print custom console messages, though it wasn't intended to be used this way
class Logger():
    devMode : bool

    def __init__(self):
        self.devMode = True

    def post(self, type : str, *args):
        if self.devMode == False: return
        message = ""
        for arg in args:
            message += str(arg)
        print(type + ": " + message)

    def log(self, *args):
        self.post("LOG", *args)

    def throw(self, *args):
        self.post("ERROR", *args)
        traceback.print_exc()

    def set(self, p_devMode : bool):
        self.devMode = p_devMode

logger = Logger()