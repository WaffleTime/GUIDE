import pyhooked


class UniversalHook(object):
    """
    Abstract class that provides the generic interface for logging keystrokes
    on any operating system
    """
    def __init__(self):
        """
        Initializes a UniversalHook object

        UniversalHook objects should have a hook of some kind for handling
        the keystrokes
        """
        raise NotImplemented("UniversalHook is an abstract class")

    def add_hotkey(self):
        """
        Interface for adding a hotkey
        """
        raise NotImplemented("UniversalHook is an abstract class")


    def rm_hotkey(self):
        """
        Interface for removing a hotkey
        """
        raise NotImplemented("UniversalHook is an abstract class")


    def listen(self):
        """
        Interface for listening to keystrokes and running the provided callback
        """
        raise NotImplemented("UniversalHook is an abstract class")


    def unhook(self):
        """
        Interface for "unhooking" all of the keys
        """
        raise NotImplemented("UniversalHook is an abstract class")


class OSXHook(UniversalHook):
    """
    Interface for collecting keystrokes on OSX
    """
    


class LinuxHook(UniversalHook):
    """
    Interface for collecting keystrokes on Linux
    """
    


class WindowsHook(UniversalHook):
    """
    Interface for collecting keystrokes on Windows
    """
    def __init__(self):
        """
        Initializes a WindowsHook object
        """
        

    def add_hotkey(self):
        """
        Interface for adding a hotkey
        """
        

    def rm_hotkey(self):
        """
        Interface for removing a hotkey
        """
        

    def listen(self):
        """
        Interface for listening to keystrokes and running the provided callback
        """
        

    def unhook(self):
        """
        Interface for "unhooking" all of the keys
        """
        

class PyReel(object):
    """
    Provides the interface for 
    """
    def __init__(self):
        self.hook = self._determine_hook()


    def _determine_hook(self):
        """
        Determines the hook to use for PyReel based on the user's OS

        :return: The appropriate UniversalHook object
        """
        return WindowsHook()
