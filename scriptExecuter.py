#!/usr/bin/python3
import subprocess
import logging

LOG_FILENAME = 'GUIDE.log'

logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)

class ExternalTools:

    def __init__(self, command, working_dir, env_variables ):
        """
        Construct a new 'External Tool' object.

        :param name: The cammand  to runXC
        :param age: The working directory of the project
        :return: returns nothing
        """
        self.command = command
        self.working_dir = working_dir
        self.env_variables = env_variables
    
    def run():
       with subprocess.Popen(args=self.command, stdin=PIPE, stdout=PIPE, env=self.env_variables, cwd=str(self.working_dir)) as runner:
           print(runner.stdout.read())


test = ExternalTools("ls","/Users/gus/Desktop","")
