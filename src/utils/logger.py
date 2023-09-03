import logging

# this item "module_logger" is visible only in this module,
# (but you can create references to the same logger object from other modules
# by calling getLogger with an argument equal to the name of this module)
# this way, you can share or isolate loggers as desired across modules and across threads
# ...so it is module-level logging and it takes the name of this module (by using __name__)
# recommended per https://docs.python.org/2/library/logging.html
# my_logger = logging.getLogger('my_logger')


class MyHandlerText(logging.StreamHandler):
    def __init__(self, textctrl):
        logging.StreamHandler.__init__(self) # initialize parent
        self.textctrl = textctrl

    def emit(self, record):
        msg = self.format(record)
        self.textctrl.config(state="normal")
        self.textctrl.insert("end", msg + "\n")
        self.flush()
        self.textctrl.config(state="disabled")
