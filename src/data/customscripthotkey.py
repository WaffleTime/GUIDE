class CustomScriptHotkey(object):
    def __init__(self):
        # The name of the hotkey
        self.name           = ""

        # A list of keys that trigger the executable when ALL are pressed simultaneously
        self.condition      = []

        # A python file's path that is to be executed
        self.executable     = ""
