from  captosexceptions import CaptosExceptions
from send_error import SendException
from SQLTableNotFound import SQLTableNotFoundException
def exception_handler(func):
    def inner_function(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:
            print(e.__str__())
            sender = SendException()
            sender.send_exception(e)
    return inner_function

@exception_handler
# def sql_table_not_found(self):
#     raise SQLTableNotFoundException
#
# sql_table_not_found()
