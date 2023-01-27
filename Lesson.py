import tkinter as tk

class Example(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.l1 = tk.Radiobutton(self, text="Hover over me")
        self.l1.pack(side="top")
        self.l1.bind("<Enter>", self.on_enter)
        self.l1.bind("<Leave>", self.on_leave)

    def on_enter(self, event):
        self.l1.configure(background='red')

    def on_leave(self, enter):
        self.l1.configure(background="white")

if __name__ == "__main__":
    root = tk.Tk()
    Example(root).pack(side="top", fill="both", expand="true")
    root.mainloop()