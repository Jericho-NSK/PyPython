from tkinter import Tk, Entry

from Window import Window


class Calculator(Window, Tk):
    """Main program"""
    _result = 'sdv'
    _font = 'Arial', 18, 'bold'

    def __init__(self):
        super().__init__()
        self.entry = Entry(text='0',
                           bg='#CBCACA',
                           font=self._font,
                           bd=8,
                           relief='sunken',
                           justify='right')
        self.entry.grid(row=0, column=0, columnspan=4, sticky='we', padx=3)
        self.click(0)

    def click(self, symbol):
        if self.entry.get() == '0':
            self.entry.delete(0)
        self.entry.insert(len(self.entry.get()), symbol)
        self.entry.icursor(len(self.entry.get()))

    def delete(self):
        if self.entry.get():
            self.entry.delete(len(self.entry.get()) - 1)
            if not self.entry.get():
                self.click(0)

    def clean(self):
        for i in self.entry.get():
            self.delete()
        self.click(0)

    def result(self):
        self.entry.insert(0, exec(str(self.entry.get())))



tk = Calculator()
tk.mainloop()
