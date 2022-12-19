from  captosexceptions import CaptosExceptions
from send_error import SendException
def exception_handler(func):
    def inner_function(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:
            print(e.__str__())
    return inner_function
SendException.send_exception("TESTQEUE")