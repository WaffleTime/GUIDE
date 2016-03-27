
class OsConfig(object):
    def __init__(self, os):
        self.os         = os
        self.namespaces = {}
        self.hotkeys    = {}