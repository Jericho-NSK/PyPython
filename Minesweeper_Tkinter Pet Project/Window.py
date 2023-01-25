from tkinter import Tk, PhotoImage
from PIL import ImageTk, Image
from Buttons import Buttons


class Window(Tk):
    _title = 'Minesweeper'
    row = 5
    column = 5
    total = row * column
    button_size = 50
    icon_size = int(button_size * 0.8)
    boom = Image.open('Boom.png').resize((icon_size, icon_size))
    _width = column * button_size
    _height = row * button_size
    list_button = []

    def __init__(self):
        super().__init__()
        self.title(self._title)
        self.geometry(f'{self._width}x{self._height}+1200+200')
        self.resizable(False, False)
        self.iconphoto(False, PhotoImage(file='Icon.png', master=self))
        self.create_buttons()

    def create_buttons(self):
        count = (i for i in range(1, self.total + 1))
        for i in range(self.column):
            for j in range(self.row):
                self.list_button.append(Buttons(i, j, count.__next__()))
                self.list_button[-1].grid(stick='wens', row=i, column=j)
                self.list_button[-1].boom = ImageTk.PhotoImage(self.boom, master=self.list_button[-1])

        for i in range(self.grid_size()[0]):
            self.grid_columnconfigure(i, minsize=self.button_size)
        for i in range(self.grid_size()[1]):
            self.grid_rowconfigure(i, minsize=self.button_size)
