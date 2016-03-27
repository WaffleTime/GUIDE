from sys import platform as _platform
import sys
sys.path.append("../antlr4")

import time
import configparser
from scriptexecuter import *
from pyreel.keyfisher import *
import logging
LOG_FILENAME = 'GUIDE.log'

logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)

class Loader:
    def __init__(self, global_config, proj_config, executer, pyreel):
        """
        Construct a new 'project loader' object.
        :param global_config: the global cofiguration across all projects
        :param proj_config: the proj_config for the current project
        :param executer: the script executer object
        :para pyreel: the pyreel object
        :return: returns nothing                                                                                                                       
        """
        self.global_config = global_config
        self.proj_config = proj_config

        self.extern_hkeys = {}
        self.intern_hkeys = {}

        self.executer = executer
        self.pyreel = pyreel

    def combine(self, config_path):
        """
        Method combines config parameters and checks for duplication.
        
        """
        config      = configparser.parse(config_path)
        osconfigs   = config.os_configs

        system_config = osconfigs.get(self.set_system(), None)
        global_config = osconfigs.get("global", None)

        extern_hkeys = []
        intern_hkeys = []

        if (system_config != None):
            extern_hkeys += system_config.external_tool_hotkeys.values()
            intern_hkeys += system_config.custom_script_hotkeys.values()

        if (global_config != None):
            extern_hkeys += global_config.external_tool_hotkeys.values()
            intern_hkeys += global_config.custom_script_hotkeys.values()

        for key in extern_hkeys:
            self.extern_hkeys[",".join(key.condition)]=key

        for key in intern_hkeys:
            self.intern_hkeys[",".join(key.condition)]=key

        return config

    def set_system(self):
        """
        Method figures out the operating system the user is on.
        """
        if _platform == "linux" or _platform == "linux2":
            return "linux"
        elif _platform == "darwin":
            return "osx"
        elif _platform == "win32":
            return "windows"
        

    def make_external_hkeys(self):
        """
        Method creates the external tool hotkeys.
        """
        for key in self.extern_hkeys.values():
            pointer=self.executer.create_external_tool(key.executable, key.working_dir, key.env_vars)
            self.pyreel.add_hotkey(key.condition, pointer)
    
    def make_internal_hkeys(self):
        """
        Method creates the internal srcipt hotkeys.
        """
        for key in self.intern_hkeys.values():
            pointer=self.executer.create_internal_tool(self.proj_config, self.global_config, key.executable)
            self.pyreel.add_hotkey(key.condition, pointer)

if __name__ == "__main__":
    projconfig      = ""
    globalconfig    = ""

    if (len(sys.argv) >= 3):
        globalconfig = sys.argv[1]
        projconfig = sys.argv[2]

    else:
        print("Usage:\npython projectloader.py <global_config> <project_config>")
        sys.exit(1)

    pyreel              = Pyreel()
    executive           = Executer()

    load_it             = Loader(globalconfig, projconfig, executive, pyreel)
    global_config_obj   = load_it.combine(globalconfig)
    proj_config_obj     = load_it.combine(projconfig)

    load_it.make_external_hkeys()
    load_it.make_internal_hkeys()

    pyreel.listen()

    try:
        while True:
            time.sleep(1)
    except:
        sys.exit(0)
