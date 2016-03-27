import tkinter


def run(global_configs, project_configs, gui):
    root = tkinter.Tk()
    button = tkinter.Button(root, text="Click me!!!")
    button.pack()
    gui.register_window("window_button_example")
    root.mainloop()


