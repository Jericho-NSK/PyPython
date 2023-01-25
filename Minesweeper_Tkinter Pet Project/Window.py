from tkinter import Tk, PhotoImage
from PIL import ImageTk, Image
from Buttons import Buttons
from random import sample


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
        self.count_mines()

    def create_buttons(self):
        for i in range(self.column + 2):
            temp_list = list()
            for j in range(self.row + 2):
                temp_list.append(Buttons())

            self.list_button.append(temp_list)

        number = 1
        mines_numbers = sample(range(1, self.total + 1), self.total // 9)
        for i in range(self.column):
            for j in range(self.row):
                new_button = Buttons(i, j, number)
                new_button.grid(stick='wens', row=i, column=j)
                new_button.boom = ImageTk.PhotoImage(self.boom, master=new_button)
                if new_button.number in mines_numbers:
                    new_button.is_mine = True
                self.list_button[i][j] = new_button
                number += 1

        for i in range(self.grid_size()[0]):
            self.grid_columnconfigure(i, minsize=self.button_size)
        for i in range(self.grid_size()[1]):
            self.grid_rowconfigure(i, minsize=self.button_size)

    def count_mines(self):

        for i in range(self.row):
            for j in range(self.column):
                count_near_mines = 0
                if not self.list_button[i][j].is_mine:
                    for x in [-1, 0, 1]:
                        for y in [-1, 0, 1]:
                            if self.list_button[i+x][j+y].is_mine:
                                count_near_mines += 1
                self.list_button[i][j].count_near_mines = count_near_mines
        # for i in self.list_button:
        #     for j in i:
        #         print(j.number, j.x, j.y)