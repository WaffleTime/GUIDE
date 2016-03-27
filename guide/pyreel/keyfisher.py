import os
import threading
import platform
import sys
if __name__ == "__main__":
    sys.path.append("../")


class KeyHandler(object):
    """
    
    """
    def __init__(self):
        pass


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
        raise NotImplemented("UniversalHook is an abstract class")


    def rm_hotkey(self):
        """
        Interface for removing a hotkey

        :param hotkey_id: the id of the hotkey to remove
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
    class Hotkey:
        """
        A class for representing a hotkey instance
        """
        def __init__(self, keys_list, callb, args=None):
            self.keys_list = []
            self.callb = callb
            self.args = args


        def do_callback(self):
            """Runs the Hotkey's callback"""
            if args is not None:
                self.callb(*args)
            else:
                self.callb()


        def has_keys(self, keydict):
            """
            Checks the keys in keydict against the keys of the hotkey

            :param keydict: dictionary of keys currently held down
            """
            for key in self.keys_list:
                if not self.keydict.get(key, False):
                    return False
            return True


    def __init__(self):
        """
        Initializes a LinuxHook object

        LinuxHook objects should have a hook of some kind for handling
        the keystrokes
        """
        self.hook = pyxhook.HookManager()
        self.hotkeys = []
        self.listening = False
        self.listen_thread = None
        self.keydict = {}


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
        self.hotkeys.append(Hotkey(key_list, callb, args))
        return len(self.hotkeys)


    def rm_hotkey(self, hotkey_id):
        """
        Interface for removing a hotkey

        :param hotkey_id: the id of the hotkey to remove
        """
        self.hotkeys.pop(hotkey_id)


    def _key_down_handler(self, event):
        """
        Handles the key down event of pyxhook
        :param event: object for representing key pressed event
                      (see pyxhook.pyxhookkeyevent)
        """
        # this will need looked up using the ascii value or a lookup table
        self.keydict[event.Key] = True


    def _key_up_handler(self, event):
        """
        Handles the key up event of pyxhook
        :param event: object for representing key pressed event
                      (see pyxhook.pyxhookkeyevent)
        """
        key = event.Key
        if key in self.keydict:
            del self.keydict[key]


    def listener(self):
        """Listens to keystrokes the user presses and runs the matching hotkey"""
        self.hook.start()
        while self.listening:
            for hotkey in self.hotkeys:
                if hotkey.has_keys(self.keydict):
                    hotkey.do_callback()
        self.hook.cancel()
            

    def listen(self):
        """
        Interface for listening to keystrokes and running the provided callback
        """
        self.listening = True
        self.listen_thread = threading.Thread(target=self.listener)
        self.listen_thread.start()

    def unhook(self):
        """
        Interface for "unhooking" all of the keys
        """
        self.listening = False
        if self.listen_thread is not None:
            self.listen_thread.join()
            self.listen_thread = None
        


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

Pyreel = None

if platform.system() == "Windows":
    from pyreel import pyhooked
    Pyreel = WindowsHook

elif platform.system() == "Linux":
    from pyreel.pyxhook import pyxhook
    Pyreel = LinuxHook

else:
    raise Exception("OS {0} is not supported".format(platform.system()))




