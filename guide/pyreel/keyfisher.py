import os
import threading
import platform
import sys
if __name__ == "__main__":
    sys.path.append("../")
from pyreel import pyhooked

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

    def add_hotkey(self, key_list, callb, args):
        """
        Interface for adding a hotkey

        Will cause the hook to execute callb with args when
        the associated keys are pressed

        :param key_list: The sequence of keys
        :param callb: the callback function
        :param args: the args to send to the callback function
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
        self.hook = pyhooked.hook()
        self.listen_thread = None


    def __del__(self):
        """Have the hook stop listening so resources are cleaned up"""
        self.unhook()


    def add_hotkey(self, key_list, callb, args=None):
        """
        Interface for adding a hotkey

        Will cause the hook to execute callb with args when
        the associated keys are pressed

        :param key_list: The sequence of keys
        :param callb: the callback function
        :param args: the args to send to the callback function
        :returns: the hotkey id used for identifying the hotkey added
        """
        return self.hook.Hotkey(key_list, callb, args)


    def rm_hotkey(self, hotkey_id):
        """
        Interface for removing a hotkey associated with the hotkey id

        :param hotkey_id: the id of the hotkey to remove
        """
        self.hook.RemHotKey(hotkey_id)


    def listen(self):
        """
        Listen to keystrokes and run the provided callback
        """
        self.listen_thread = threading.Thread(target=self.hook.listen)
        self.listen_thread.start()


    def unhook(self):
        """
        Interface for stopping the key listening
        """
        if self.listen_thread is not None:
            self.hook.stop_listening()
            self.listen_thread.join()
            self.listen_thread = None


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


def do_things(lst):
    print("Before adding stuff: {0}".format(lst))
    lst.append("FUCKER! AH AH!")
    print("After adding stuff: {0}".format(lst))

