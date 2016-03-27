#!/usr/bin/python3
"""
script executer module 
author Gus Tropea

"""

import logging
import sys
from subprocess import Popen, PIPE
import importlib.util
import guimanager

root = logging.getLogger()
root.setLevel(logging.DEBUG)

fh = logging.FileHandler('GUIDE.log')
fh.setLevel(logging.DEBUG)
root.addHandler(fh)

ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.DEBUG)
root.addHandler(ch)

class ExternalTool:

    def __init__(self, command, working_dir=None, env_variables={}):
        """
        Construct a new 'External Tools' object.
        :param command: the cammand  to runC)
        :param working_dir: the working directory of the project
        :param env_variables: enviornment variables being past to the shell
        :return: returns nothing
        """
        logging.debug("Registering External Command")
        logging.debug("Command: {}".format(command))
        logging.debug("Working Dir: {}".format(working_dir))
        logging.debug("Env Vars: {}".format(env_variables))
        logging.debug("")

        self.command = []

        if (" " in command):
            self.command = command.split(" ")
        elif (len(command) > 0):
            self.command = [command]

        self.command = command
        self.working_dir = working_dir
        self.env_variables = env_variables
    
    def run(self):
        """
        Method trys to run command. If the command is invalid throw and error. If the command is valid but fails print error to log

        """
        logging.debug("Executing External CMD: {}".format(" ".join(self.command)))
        logging.debug("Working Dir: {}".format(self.working_dir))
        logging.debug("Env Vars: {}".format(self.env_variables))
        logging.debug("")
        
        try:
            runner = Popen(self.command, stdout=PIPE, stderr=PIPE, env=self.env_variables, cwd=self.working_dir, shell=True)
            data, err = runner.communicate()
            if data:
                logging.info(" {} executed successfully!".format(self.command))
            if err:
                logging.error(" {}".format(err.decode("UTF-8")))
        except Exception as e:
            logging.error(" Uhgg! this isn't working!... but {} is not a valid command so thats probably why!".format(self.command), e)

class InternalTool:
    def __init__(self, project_config, global_config, path, gui):
        """
        Construct a new 'Internal Tools' object.
        :param projec_config: preset information about the project
        :param global_config: preset informaiton about the global environment
        :param path: path to internal python scipt
        :param gui:  gui object
        :return: returns nothing
        """

        logging.debug("Registering User Script")
        logging.debug("User Script: {}".format(path))
        logging.debug("")

        self.project_config = project_config
        self.global_config = global_config
        self.path = path
        self.gui = gui
        self.mod = None


    def run(self):
        """
        Method starts internal python script.
        """
        logging.debug("Executing User Script: {}".format(self.path))
        logging.debug("")

        convert = self.path.replace('\\','/')
        module_name = ""
        for i in convert.split('/'):
            if i.endswith(".py"):
                module_name += i.split(".py")[0]
        try:
            spec = importlib.util.spec_from_file_location(module_name, self.path)
            self.mod  = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(self.mod)
            self.mod.run(self.global_config, self.project_config, self.gui)
        except Exception as e:
            logging.error(" Problem executing custom user script", e)

        self.gui.cleanup_windows()
        
        def __init__(self, project_config, global_config, path, gui):
            """
            Construct a new 'Internal Tools' object.
            :param projec_config: preset information about the project
            :param global_config: preset informaiton about the global environment
            :param path: path to internal python scipt
            :param gui:  gui object
            :return: returns nothing
            """
        
            self.project_config = project_config
            self.global_config = global_config
            self.path = path
            self.gui = gui
        
        
        def run(self):
            """
            Method starts internal python script.
            """
            convert = self.path.replace('\\','/')
            module_name = ""
            for i in convert.split('/'):
                if i.endswith(".py"):
                    module_name += i.split(".py")[0]
            try:
                spec = importlib.util.spec_from_file_location(module_name, self.path)
                mod  = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(mod)
                mod.run(self.global_config, self.project_config, self.gui)
                logging.info(" "+module_name+" started successfully!")
            except:
                raise
                
            self.gui.cleanup_windows()

class Executer:
    def __init__(self):
        """
        Construct a new "Executer" object.
        :return: returns nothing
        
        """
        self.external_tools=[]
        self.internal_tools=[]
        
        self.gui_manager = guimanager.GUIManager()
    
    def create_external_tool(self, command, working_dir=None, env_variables={}):
        """
        Method starts external tool and stores it.
        :return: returns function pointer to the objects run method.
        """
        tool = ExternalTool(command, working_dir, env_variables)
        self.external_tools.append(tool)
        return tool.run

    def create_internal_tool(self, project_config, global_config, path):
        """
        Method starts internal tool and stores it.
        :return: returns function pointer to the objects run method.
        """
        tool = InternalTool(project_config, global_config, path, self.gui_manager)
        self.internal_tools.append(tool)
        return tool.run
