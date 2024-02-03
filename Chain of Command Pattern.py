from enum import Enum
from abc import ABC, abstractmethod

class RequestType(Enum):
    INFO = 1
    ERROR = 2
    DEBUG = 3

class LogProcessor(ABC):
    @abstractmethod
    def set_next(self, handler):
        pass
    @abstractmethod
    def handle(self, request):
        pass

class AbstractLogProcessor(LogProcessor):
    def __init__(self):
        self.next_handler = None

    def set_next(self, handler: LogProcessor):
        self.next_handler = handler
        return self

    @abstractmethod
    def handle(self, request):
        pass

class InfoLogProcessor(AbstractLogProcessor):
    def __init__(self):
        super().__init__()

    def handle(self, request):
        if request.value == RequestType.INFO.value:
            print('info')
        else:
            try:
                return self.next_handler.handle(request)
            except:
                return


class DebugLogProcessor(AbstractLogProcessor):
    def __init__(self):
        super().__init__()
    def handle(self, request):
        if request.value == RequestType.DEBUG.value:
            print('debug')
        else:
            print(request.value, RequestType.DEBUG.value)
            return self.next_handler.handle(request)

class ErrorLogProcessor(AbstractLogProcessor):
    def __init__(self):
        super().__init__()
    def handle(self, request):
        if request.value == RequestType.ERROR.value:
            print('error')
        else:
            return self.next_handler.handle(request)

error = ErrorLogProcessor()
debug = DebugLogProcessor()
info = InfoLogProcessor()

error.set_next(debug.set_next(info))

request = RequestType.DEBUG
error.handle(request)
