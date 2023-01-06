class FullColumnError(Exception):
    def __init__(self, message):
        self.__message = message


class InputError(Exception):
    def __init__(self, message):
        self.__message = message
