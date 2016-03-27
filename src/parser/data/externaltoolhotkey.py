class ExternalToolHotkey(object):
    def __init__(self):
        self.name           = ""
        self.condition      = []
        self.env_vars       = {}
        self.working_dir    = "."
        self.executable     = ""
