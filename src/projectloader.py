from sys import platform as _platform
import sys
import configparser
from scriptexecuter import *
from pyreel.keyfisher import *

class Loader:
    def __init__(self, global_config, proj_config, executer, pyreel):
        self.global_config = global_config
        self.proj_config = proj_config

        self.extern_hkeys = {}
        self.intern_hkeys = {}

        self.executer = executer
        self.pyreel = pyreel

    def combine(self, config_path):
        config      = configparser.parse(config_path)
        osconfigs   = config.os_configs

        system_config = osconfigs.get(self.set_system(), None)
        global_config = osconfigs.get("global",None)

        extern_hkeys = []
        intern_hkeys = []

        if (system_config != None):
            extern_hkeys += system_config.extern_tool_hotkeys.values()
            intern_hkeys += system_config.custom_script_hotkeys.values()

        elif (global_config != None):
            extern_hkeys += global_config.extern_tool_hotkeys.values()
            intern_hkeys += global_config.custom_script_hotkeys.values()

        for key in extern_hkeys:
            self.extern_hkeys[set(key.condition)]=key

        for key in intern_hkeys:
            self.intern_hkeys[set(key.condition)]=key
        

    def set_system(self):
        if _platform == "linux" or _platform == "linux2":
            return "linux"
        elif _platform == "darwin":
            return "osx"
        elif _platform == "win32":
            return "win32"
        

    def make_external_hkeys(self):
        for key in self.extern_hkeys.values():
            pointer=self.executer.create_external_tool(key.executable, key.working_dir, key.env_vars)
            self.pyreel.add_hotkey(key.condition, pointer)
    
    def make_internal_hkeys(self):
        for key in self.intern_hkeys.values():
            pointer=self.executer.create_internal_tool(self.proj_config, self.global_config, key.executable)

if __name__ == "__main__":
    projconfig  = ""
    globalconfig = ""

    if (len(sys.argv) >= 3):
        globalconfig = sys.argv[1]
        projconfig = sys.argv[2]
        
        sys.path.append("../antlr4")

    else:
        print("Usage:\npython projectloader.py <global_config> <project_config>")
        sys.exit(1)

    pyreel = Pyreel()

    executive = Executer()

    load_it = Loader(globalconfig, projconfig, executive, pyreel)
    load_it.combine(globalconfig)
    load_it.combine(projconfig)
    load_it.make_external_hkeys()
    load_it.make_internal_hkeys()

    pyreel.listen()
    
