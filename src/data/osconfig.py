
class OsConfig(object):
    def __init__(self, os):
        # The operating system that this object's namespaces and hotkeys are valid for.
        # Possible values: "global", "windows", "linux", "osx"
        self.os                     = os

        # Maps a namespace's name to a dictionary that contains the namespace's information.
        # Each namespace's dictionary maps strings to strings.
        # Namespaces essentially just store useful information.
        self.namespaces             = {}

        # The hotkeys that trigger some command that is to be executed within a terminal.
        self.external_tool_hotkeys  = {}

        # The hotkeys that trigger a custom python script.
        self.custom_script_hotkeys  = {}