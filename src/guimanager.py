import tkinter
import sys
if __name__ == "__main__":
    sys.path.append("../")

class GUIManager:
    """
    Manages the windows for the scripts
    """
    def __init__(self):
        self.windows = {}


    def register_window(self, win_id, window):
        """
        Registers the window with the GUIManager

        :param win_id: The unique id for the window to be registered
        :param window: The window to register under the id
        """
        if not isinstance(window, tkinter.Tk):
            raise TypeError("Registered window must be of type tkinter.Tk")
        elif win_id not in self.windows:
            self.windows[win_id] = window
        else:
            raise ValueError("Window id {0} is already registered".format(win_id))


    def cleanup_windows(self):
        """
        Destroy all the windows
        """
        for win_id in self.windows:
            win = self.windows[win_id]
            win.quit()
            win.destroy()
        self.windows = {}
