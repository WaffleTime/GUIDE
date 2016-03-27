
class Configuration(object):
    def __init__(self):
        # Instance of ProjectInfo
        self.project_info   = None

        # Maps an operating system string to a OsConfig object
        self.os_configs     = {}