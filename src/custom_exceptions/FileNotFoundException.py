from BlindleException import BlindleException

class FileNotFoundException(BlindleException):
    """Exception when file not found"""
    _EXCEPTION_NAME = "file-not-found"

    def __init__(self):
        print "Archivo no encontrado"
        self._exception_name = self._EXCEPTION_NAME
        super(FileNotFoundException, self).__init__()