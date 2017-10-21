from BlindleException import BlindleException

class FormatException(BlindleException):
    """Exception when txt file has invalid format"""
    _EXCEPTION_NAME = "format"

    def __init__(self):
        print "Formato invalido"
        self._exception_name = self._EXCEPTION_NAME
        super(FormatException, self).__init__()