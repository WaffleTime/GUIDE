#!/usr/bin/python3
"""
script executer module 
author Gus Tropea

"""

import logging
from subprocess import Popen, PIPE
import importlib.util

LOG_FILENAME = 'GUIDE.log'

logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)

class ExternalTool:

    def __init__(self, command, working_dir=".", env_variables={}):
        """
        Construct a new 'External Tools' object.
        :param command: the cammand  to runC
        :param working_dir: the working directory of the project
        :param env_variables: enviornment variables being past to the shell
        :return: returns nothing
        """
        self.command = command
        self.working_dir = working_dir
        self.env_variables = env_variables
    
    def run(self):
        """
        Method trys to run command. If the command is invalid throw and error. If the command is valid but fails print error to log

        """
        try:
            runner = Popen(args=self.command, stdout=PIPE, stderr=PIPE, env=self.env_variables, cwd=self.working_dir)
            data, err = runner.communicate()
            if data:
                logging.info(" "+self.command+" executed successfully!")
                runner.close()
            if err:
                logging.error(" "+err.decode("UTF-8"))
        except:
            logging.error(" Uhgg! this isn't working!... but '"+self.command+" is not a valid command so thats probably why!")


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
        
            self.project_config = project_config
            self.global_config = global_config
            self.path = path
            self.gui = gui
            self.mod = None
        
        
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
                spec = importlib.util.spec_from_file_location("module.name", self.path)
                self.mod  = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(self.mod)
                self.mod.run()
                logging.info(" "+module_name+" started successfully!")
            except:
                raise

class Executer:
    def __init__(self):
        """
        Construct a new "Executer" object.
        :return: returns nothing
        
        """
        self.external_tools=[]
        self.internal_tools=[]
    
    def create_external_tool(self, command, working_dir=".", env_variables={}):
        """
        Method starts external tool and stores it.
        :return: returns function pointer to the objects run method.
        """
        tool = ExternalTool(command, working_dir, env_variables)
        self.external_tools.append(tool)
        logging.info("external tool stored")
        return tool.run

    def create_internal_tool(self, project_config, global_config, path, gui):
        """
        Method starts internal tool and stores it.
        :return: returns function pointer to the objects run method.
        """
        tool = InternalTool(project_config, global_config, path, gui)
        self.internal_tools.append(tool)
        logging.info("Internal Tool stored")
        return tool.run
