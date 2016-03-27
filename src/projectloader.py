from sys import platform as _platform
from parser.configparser  import *

#parser(parser/test_config.text)

class Loader:
    def __init__(self, parser):
        self.parser
        self.osconfigs = self.parser.osconfigs
        self.system = self.setSystem()

    def setSystme(self):
        if _platform == "linux" or _platform == "linux2":
            print("Linux")
        elif _platform == "darwin":
            print("osx")
        elif _platform == "win32":
            print("windows")

load = Loader(parser/test_config.txt)
