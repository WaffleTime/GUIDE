class ExternalToolHotkey(object):
    def __init__(self):
        # Name of the hotkey
        self.name           = ""

        # A list of keys that trigger the executable when ALL are pressed simultaneously
        self.condition      = []

        # Maps strings to strings and represents the environment variables for the executable.
        self.env_vars       = {}

        # Directory that the executable will be executed within
        self.working_dir    = "."

        # A command that is to be executed on the command line.
        self.executable     = ""
