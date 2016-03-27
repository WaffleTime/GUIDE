import tkinter


def run(global_configs, project_configs, gui):
    root = tkinter.Tk()

    root.minsize(width=666, height=666)
    root.maxsize(width=666, height=666)

    button = tkinter.Button(root, text="Click me!!!")
    button.pack()
    gui.register_window("window_button_example", root)
    root.mainloop()


