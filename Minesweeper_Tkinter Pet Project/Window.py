from tkinter import Tk, PhotoImage
from Buttons import Buttons
from random import sample


class Window(Tk):
    row = 5
    column = 5
    _total = row * column
    _difficult = {'easy': 6, 'normal': 5, 'hard': 4}
    _title = 'Minesweeper'
    _width = column * Buttons.button_size
    _height = row * Buttons.button_size
    list_button = []

    def __init__(self):
        super().__init__()
        self.title(self._title)
        self.geometry(f'{self._width}x{self._height}+1200+200')
        self.resizable(False, False)
        self.iconphoto(False, PhotoImage(file='Icon.png', master=self))
        self.create_default_buttons()
        self.create_buttons()
        self.alignment()
        self.count_mines()

    def create_default_buttons(self):
        """Создание полей. По краям нужны дополнительные ряды и колонки, поэтому сначала создается увеличенное число полей, без кнопок"""
        for i in range(self.column + 2):
            temp_list = list()
            for j in range(self.row + 2):
                temp_list.append(Buttons())
            self.list_button.append(temp_list)

    def create_buttons(self):
        """Создание кнопок с полями и распределение по ним мин в зависимости от выбранной сложности"""
        number = 1
        mines_numbers = sample(range(1, self._total + 1), self._total // self._difficult['easy'])
        for i in range(self.column):
            for j in range(self.row):
                new_button = Buttons(i, j, number)
                new_button.grid(stick='wens', row=i, column=j)
                new_button.mine = False
                if new_button.number in mines_numbers:
                    new_button.is_mine = True
                self.list_button[i][j] = new_button
                number += 1

    def alignment(self):
        """Выравнивание кнопок по ширине и высоте поля с учетом размера и количества полей"""
        for i in range(self.grid_size()[0]):
            self.grid_columnconfigure(i, minsize=Buttons.button_size)
        for i in range(self.grid_size()[1]):
            self.grid_rowconfigure(i, minsize=Buttons.button_size)

    def count_mines(self):
        """Подсчет мин у соседей, присвоение этого числа в атрибуты кнопки"""
        for i in range(self.row):
            for j in range(self.column):
                count_near_mines = 0
                if not self.list_button[i][j].is_mine:
                    for x in [-1, 0, 1]:
                        for y in [-1, 0, 1]:
                            if self.list_button[i+x][j+y].is_mine:
                                count_near_mines += 1
                self.list_button[i][j].count_near_mines = count_near_mines
