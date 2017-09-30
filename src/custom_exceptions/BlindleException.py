import helpers.musicHelper as musicHelper

class BlindleException(Exception):
    """Blindle Exception base class"""
    _exception_name = ""

    def __init__(self):
        super(Exception, self).__init__()
        self._play_exception_sound()

    def _play_exception_sound(self):
        musicHelper.play_exception_sound(self._exception_name)