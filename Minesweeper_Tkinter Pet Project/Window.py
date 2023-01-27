from random import shuffle
from tkinter import Tk, PhotoImage
from Menubar import Menubar
from Buttons import Buttons


class Window(Tk):
    row = 5
    column = 5
    _total = row * column
    _difficult = {'easy': 7, 'normal': 6, 'hard': 5}
    _title = 'Minesweeper'
    _width = column * Buttons.button_size
    _height = row * Buttons.button_size
    list_button = []

    def __init__(self, game):
        super().__init__()
        self.title(self._title)
        self.geometry(f'{self._width}x{self._height+25}+1000+100')
        self.resizable(True, True)
        self.iconphoto(False, PhotoImage(file='Boom.png', master=self))
        self.create_default_buttons()
        self.create_buttons()
        self.create_bombs()
        self.alignment()
        self.count_bombs()
        menubar = Menubar(self, game)
        self.config(menu=menubar)

    def create_default_buttons(self):
        """Создание полей. По краям нужны дополнительные ряды и колонки, поэтому сначала создается увеличенное число полей, без кнопок"""
        self.list_button = []
        for i in range(self.column + 2):
            temp_list = list()
            for j in range(self.row + 2):
                temp_list.append(Buttons())
            self.list_button.append(temp_list)

    def create_buttons(self):
        """Создание кнопок с полями"""
        temp_number = 1
        for row in range(self.column):
            for column in range(self.row):
                new_button = Buttons(row, column, temp_number)
                new_button.grid(stick='wens', row=row, column=column)
                self.list_button[row][column] = new_button
                temp_number += 1

    def create_bombs(self, button: Buttons = False):
        """Распределение по кнопкам бомб в зависимости от выбранной сложности"""
        temp_list = list(range(1, self._total + 1))
        shuffle(temp_list)
        bombs_numbers = temp_list[:self._total // self._difficult['normal']]
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
        for row in range(self.grid_size()[1]):
            self.grid_rowconfigure(row, minsize=Buttons.button_size)
        for column in range(self.grid_size()[0]):
            self.grid_columnconfigure(column, minsize=Buttons.button_size)

    def count_bombs(self):
        """Подсчет мин у соседей, присвоение этого числа в атрибуты кнопки"""
        for row in self.list_button:
            for btn in row:
                count_near_bombs = 0
                if not btn.is_bomb:
                    for dx in [-1, 0, 1]:
                        for dy in [-1, 0, 1]:
                            if self.list_button[btn.x + dx][btn.y + dy].is_bomb:
                                count_near_bombs += 1
                btn.count_near_bombs = count_near_bombs
                # btn['text'] = btn.count_near_bombs
