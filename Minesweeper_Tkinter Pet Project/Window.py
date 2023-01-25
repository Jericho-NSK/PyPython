from tkinter import Tk, PhotoImage

from Buttons import Buttons


class Window(Tk):
    _title = 'Minesweeper'
    _row = 3
    _column = 3
    _button_size = 50
    _width = _column * _button_size
    _height = _row * _button_size
    list_button = []

    def __init__(self):
        super().__init__()
        self.title(self._title)
        self.geometry(f'{self._width}x{self._height}+1200+200')
        self.resizable(False, False)
        self.iconphoto(False, PhotoImage(file='Icon.png', master=self))
        self.create_buttons()

    def create_buttons(self):
        for i in range(self._column):
            for j in range(self._row):
                self.list_button.append(Buttons(i, j))
                self.list_button[-1].grid(stick='wens', column=i, row=j)

        for i in range(self.grid_size()[0]):
            self.grid_columnconfigure(i, minsize=self._button_size)
        for i in range(self.grid_size()[1]):
            self.grid_rowconfigure(i, minsize=self._button_size)
