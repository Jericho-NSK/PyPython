from random import shuffle
from tkinter import Tk, PhotoImage

from Buttons import Buttons


class Window(Tk):
    row = 5
    column = 5
    _total = row * column
    _difficult = {'easy': 7, 'normal': 5, 'hard': 3}
    _title = 'Minesweeper'
    _width = column * Buttons.button_size
    _height = row * Buttons.button_size
    list_button = []

    def __init__(self):
        super().__init__()
        self.title(self._title)
        self.geometry(f'{self._width}x{self._height}+1200+200')
        self.resizable(False, False)
        self.iconphoto(False, PhotoImage(file='Boom.png', master=self))
        self.create_default_buttons()
        self.create_buttons()
        self.create_bombs()
        self.alignment()
        self.count_bombs()

    def create_default_buttons(self):
        """Создание полей. По краям нужны дополнительные ряды и колонки, поэтому сначала создается увеличенное число полей, без кнопок"""
        for i in range(self.column + 2):
            temp_list = list()
            for j in range(self.row + 2):
                temp_list.append(Buttons())
            self.list_button.append(temp_list)

    def create_buttons(self):
        """Создание кнопок с полями"""
        temp_number = 1
        for i in range(self.column):
            for j in range(self.row):
                new_button = Buttons(i, j, temp_number)
                new_button.grid(stick='wens', row=i, column=j)
                self.list_button[i][j] = new_button
                temp_number += 1

    def create_bombs(self, button: Buttons = False):
        """Распределение по кнопкам бомб в зависимости от выбранной сложности"""
        temp_list = list(range(1, self._total + 1))
        shuffle(temp_list)
        bombs_numbers = temp_list[:self._total // self._difficult['hard']]
        print(len(bombs_numbers))
        if button and button.number in bombs_numbers:
            return button
        for row in self.list_button:
            for btn in row:
                if btn.number in bombs_numbers:
                    btn.is_bomb = True
                else:
                    btn.is_bomb = False

    def alignment(self):
        """Выравнивание кнопок по ширине и высоте поля с учетом размера и количества полей"""
        for i in range(self.grid_size()[0]):
            self.grid_columnconfigure(i, minsize=Buttons.button_size)
        for i in range(self.grid_size()[1]):
            self.grid_rowconfigure(i, minsize=Buttons.button_size)

    def count_bombs(self):
        """Подсчет мин у соседей, присвоение этого числа в атрибуты кнопки"""
        for i in range(self.row):
            for j in range(self.column):
                count_near_bombs = 0
                if not self.list_button[i][j].is_bomb:
                    for x in [-1, 0, 1]:
                        for y in [-1, 0, 1]:
                            if self.list_button[i + x][j + y].is_bomb:
                                count_near_bombs += 1
                self.list_button[i][j].count_near_bombs = count_near_bombs
                self.list_button[i][j]['text'] = self.list_button[i][j].count_near_bombs
