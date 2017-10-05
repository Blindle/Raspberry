from BlindleException import BlindleException

class PendriveDisconnectedException(BlindleException):
    """Exception when pendrive is disconnect"""
    _EXCEPTION_NAME = "pendrive-dissconected"

    def __init__(self):
        print "Pendrive no conectado"
        self._exception_name = self._EXCEPTION_NAME
        super(PendriveDisconnectedException, self).__init__()