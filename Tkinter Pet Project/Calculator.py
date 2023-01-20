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
        self.entry.insert(0, '0')

    def click(self, symbol):
        value = self.entry.get()
        if value == '0':
            self.entry.delete(0)
        self.entry.insert(len(value), symbol)
        self.entry.icursor(len(value))

    def operation(self, symbol):
        value = self.entry.get()
        if value[-1] in '+-*/':
            value = value[:-1]
        elif '+' in value or '-' in value or '*' in value or '/' in value:
            self.result()
            value = self.entry.get()
        self.entry.delete(0, 'end')
        self.entry.insert(0, value + symbol)

    def delete(self):
        if self.entry.get():
            self.entry.delete(len(self.entry.get()) - 1)
            if not self.entry.get():
                self.click('0')

    def clean(self):
        self.entry.delete(0, 'end')
        self.entry.insert(0, '0')

    def result(self):
        value = self.entry.get()
        self.entry.delete(0, 'end')
        if value[-1] in '+-*/':
            self.entry.insert(0, round(eval(value + value[:-1]), 6))
        else:
            self.entry.insert(0, round(eval(value), 6))
        value = self.entry.get()
        if value[-2:] == '.0':
            self.entry.delete(0, 'end')
            self.entry.insert(0, value[:-2])

tk = Calculator()
tk.mainloop()
