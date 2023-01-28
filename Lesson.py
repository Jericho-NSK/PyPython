from tkinter import Tk, Menu, IntVar

root = Tk()
menubar = Menu(root)
size = Menu(tearoff=0)
size_var = IntVar(value=10)
size.add_radiobutton(label='5x5', variable=size_var, command=lambda: None)
size.add_radiobutton(label='10x10', variable=size_var, value=10, command=lambda: None)
size.add_radiobutton(label='15x15', variable=size_var, command=lambda: None)

menubar.add_cascade(label='Size', menu=size)
root.config(menu=menubar)
root.mainloop()



# import tkinter as tk
#
# root = tk.Tk()
#
# radio_var = tk.IntVar(value=10)  # Option 10 is the default.
#
# menubar = tk.Menu(root)
# size = tk.Menu(menubar, tearoff=0)
# size.add_radiobutton(label='5x5', variable=radio_var, value=5)
# size.add_radiobutton(label='10x10', variable=radio_var, value=10)
# size.add_radiobutton(label='15x15', variable=radio_var, value=15)
# menubar.add_cascade(label='Size', menu=size)
# root.config(menu=menubar)
#
# root.mainloop()