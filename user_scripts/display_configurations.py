import tkinter


def run(global_configs, project_configs, gui):
    root = tkinter.Tk("Configurations")
    global_key_lb = tkinter.Listbox(root)
    global_val_lb = tkinter.Listbox(root)
    i = 1
    for key in global_configs:
        global_key_lb.insert(i, key)
        global_val_lb.insert(i, global_configs[key])

    proj_key_lb = tkinter.Listbox(root)
    proj_val_lb = tkinter.Listbox(root)
    i = 1
    for key in project_configs:
        proj_key_lb.insert(i, key)
        proj_val_lb.insert(i, project_configs[key])
    
    global_key_lb.grid(row=0, column=0)
    global_val_lb.grid(row=0, column=1)
    proj_key_lb.grid(row=1, column=0)
    proj_val_lb.grid(row=1, column=1)
    gui.register_window("configs-gui", root)
    root.mainloop()

