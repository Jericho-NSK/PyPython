from tkinter import Tk, Entry

from Window import Window


class Calculator(Window, Tk):
    """Main program"""
    _font = 'Arial', 18, 'bold'

    def __init__(self):
        super().__init__()
        self.entry = Entry(bg='#CBCACA',
                           font=self._font,
                           bd=8,
                           relief='sunken',
                           justify='right',
                           state="normal")
        self.entry.grid(row=0, column=0, columnspan=4, sticky='we', padx=3)
        self.entry.insert(0, '0')
        self.entry['state'] = "readonly"
        self.bind('<Key>', self.pressing_key)

    @staticmethod
    def read_only(func):
        def wrapper(*args):
            self = args[0]
            self.entry['state'] = "normal"
            if '!' in self.entry.get():
                self.entry.delete(0, 'end')
                self.entry.insert(0, '0')
            func(*args)
            self.entry['state'] = "readonly"

        return wrapper

    def pressing_key(self, event):
        if event.keysym in '1234567890':
            self.click(event.char)
        elif event.keysym in ['plus', 'minus', 'slash', 'asterisk']:
            self.operation(event.char)
        elif event.keysym == 'BackSpace':
            self.delete()
        elif event.keysym == 'Escape':
            self.clean()
        elif event.keysym in ['Return', 'equal']:
            self.result()

    @read_only
    def click(self, symbol):
        value = self.entry.get()
        if value == '0':
            self.entry.delete(0)
        self.entry.insert(len(value), symbol)
        self.entry.icursor(len(value))

    @read_only
    def operation(self, symbol):
        value = self.entry.get()
        if value[-1] in '+-*/':
            value = value[:-1]
        elif '+' in value or '-' in value or '*' in value or '/' in value:
            self.result()
            self.entry['state'] = "normal"
            value = self.entry.get()
        self.entry.delete(0, 'end')
        self.entry.insert(0, value + symbol)

    @read_only
    def delete(self):
        value = self.entry.get()
        if not value:
            self.click('0')
        else:
            self.entry.delete(len(value) - 1)
            if not value:
                self.click('0')

    @read_only
    def clean(self):
        self.entry.delete(0, 'end')
        self.entry.insert(0, '0')

    @read_only
    def result(self):
        value = self.entry.get()
        self.entry.delete(0, 'end')
        try:
            if value[-1] in '+-*/':
                self.entry.insert(0, round(eval(value + value[:-1]), 6))
            else:
                self.entry.insert(0, round(eval(value), 6))
            value = self.entry.get()
            if value[-2:] == '.0':
                self.entry.delete(0, 'end')
                self.entry.insert(0, value[:-2])
        except ZeroDivisionError:
            self.entry.insert(0, 'На ноль делить нельзя!')


tk = Calculator()
tk.mainloop()
