from tkinter import PhotoImage, Button


class Window:
    """Decorating window"""
    _title = 'CALCULATOR'
    _width = 500
    _height = 500
    _bg = '#9D9DF2'
    _font = 'Arial', 15, 'bold'
    _default_text = ''

    def __init__(self):
        super().__init__()
        self.title(self._title)
        self.geometry(f'{self._width}x{self._height}+1300+200')
        self.resizable(False, False)
        self.iconphoto(True, PhotoImage(file='icon.png'))
        self.config(bg='#86d5d9')
        self.buttons()
        for i in range(self.grid_size()[0]):
            self.grid_columnconfigure(i, minsize=int(self._width / self.grid_size()[0]))
        for i in range(self.grid_size()[1]):
            self.grid_rowconfigure(i, minsize=int(self._height / self.grid_size()[1]))

    def make_button(self, digit):
        return Buttons(text=digit, command=lambda: self.click(digit))

    def make_operation(self, operation):
        return Buttons(text=operation,
                       command=lambda: self.click(operation) if self.entry.get()
                       and self.entry.get() != '0'
                       and not str(self.entry.get()).endswith(('+', '-', '*', '/'))
                       else None)

    def buttons(self):
        for i in range(1, 10):
            self.make_button(i).grid(row=int((i - 1) / 3) + 1, column=int((i - 1) % 3))
        else:
            self.make_button(0).grid(row=4, column=1)
        for i in enumerate('+-*/', 1):
            self.make_operation(i[1]).grid(row=i[0], column=3)




        Buttons(text='=', command=self.result).grid(row=5, column=3)
        Buttons(text='del', command=self.delete).grid(row=5, column=0)
        Buttons(text='C', command=self.clean).grid(row=5, column=1)


class Buttons(Button):
    """Buttons"""
    _bg = '#9D9DF2'
    _font = 'Arial', 16, 'bold'
    _pad = 3

    def __init__(self, text: str = '',
                 bg: str = _bg,
                 activebackground=_bg,
                 font: tuple = _font,
                 bd=7,
                 command=None):
        super().__init__(text=text, bg=bg, activebackground=activebackground, font=font, bd=bd, command=command)
        self.grid(stick='wens', padx=self._pad, pady=self._pad)
