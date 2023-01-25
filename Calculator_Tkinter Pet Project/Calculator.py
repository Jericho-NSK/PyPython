from tkinter import Tk, Entry, messagebox

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
        elif event.keysym in ['period', 'comma']:
            self.decimal()

    @read_only
    def click(self, symbol):
        value = self.entry.get()
        match list(value):
            case ['0']:
                self.entry.delete(len(value) - 1)
            case *_, '+' | '-' | '*' | '/', '0':
                self.entry.delete(len(value) - 1)
        self.entry['state'] = "normal"
        self.entry.insert(len(value), symbol)
        self.entry.icursor(len(value))

    @read_only
    def operation(self, symbol):
        value = self.entry.get()
        if value[-1] in '+-*/':
            value = value[:-1]
        elif any((value.count('+'), value.count('-'), value.count('*'), value.count('/'), value[-1].count('.'))):
            self.result()
            value = self.entry.get()
            if '!' in value:
                return
            self.entry['state'] = "normal"
        self.entry.delete(0, 'end')
        self.entry.insert(0, value + symbol)

    @read_only
    def decimal(self):
        value = self.entry.get()
        if value[-1] in '+-*/':
            if any((value[1:-1].count('+'), value[1:-1].count('-'), value[1:-1].count('*'), value[1:-1].count('/'))):
                self.result()
                value = self.entry.get()
                self.entry['state'] = "normal"
            self.entry.delete(0, 'end')
            self.entry.insert(0, value + '0.')
        elif value.count('+') or value[1:].count('-') or value.count('*') or value.count('/'):
            for i in '+-*/':
                if '.' in value[1:][value[1:].rfind(i):]:
                    break
            else:
                self.entry.insert('end', '.')
        elif '.' in value:
            for i in '+-*/':
                if i in value[value.rfind('.'):]:
                    self.entry.insert('end', '.')
        else:
            self.entry.insert('end', '.')

    @read_only
    def delete(self):
        value = self.entry.get()
        if not value:
            self.click('0')
        else:
            self.entry.delete(len(value) - 1)
            value = self.entry.get()
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

    @read_only
    def exponentiation(self):
        messagebox.showinfo(message='Button not realized')

    @read_only
    def plus_minus(self):
        messagebox.showinfo(message='Button not realized')


if __name__ == '__main__':
    tk = Calculator()
    tk.mainloop()
