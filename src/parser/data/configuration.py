import logging

VALID_OS = ["global", "windows", "linux", "osx"]

class Configuration(Object):
    def __init__(self):
        self.project_info   = None
        self.os_configs     = {}