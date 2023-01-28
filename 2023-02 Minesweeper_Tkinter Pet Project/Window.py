from random import shuffle
from tkinter import Tk, PhotoImage

from Buttons import Buttons
from Menubar import Menubar


class Window(Tk):
    _title = 'Minesweeper'
    list_button = []
    mods = {'easy': {5: 4, 10: 12, 15: 20},
            'normal': {5: 7, 10: 16, 15: 40},
            'hard': {5: 12, 10: 28, 15: 60}}

    def __init__(self, game):
        super().__init__()
        Menubar(self, game)
        self.side = 10
        self.side_size = self.side * Buttons.button_size
        self.mode = 'normal'
        self.title(self._title)
        self.new_window()
        self.resizable(False, False)
        self.iconphoto(False, PhotoImage(file='FirstBoom.png', master=self))

    def new_window(self):
        """Создание окна"""
        self.side_size = self.side * Buttons.button_size
        self.geometry(f'{self.side_size}x{self.side_size}+1000+100')
        self.create_default_buttons()
        self.create_buttons()
        self.create_bombs(mode=self.mode)
        self.alignment()
        self.count_bombs()

    def create_default_buttons(self):
        """Создание полей. По краям нужны дополнительные ряды и колонки, поэтому сначала создается увеличенное число полей, без кнопок"""
        self.list_button = []
        for i in range(self.side + 2):
            temp_list = list()
            for j in range(self.side + 2):
                temp_list.append(Buttons())
            self.list_button.append(temp_list)

    def create_buttons(self):
        """Создание кнопок с полями"""
        temp_number = 1
        for row in range(self.side):
            for column in range(self.side):
                new_button = Buttons(row, column, temp_number)
                new_button.grid(stick='wens', row=row, column=column)
                self.list_button[row][column] = new_button
                temp_number += 1

    def create_bombs(self, mode, button: Buttons = False):
        """Распределение по кнопкам бомб в зависимости от выбранной сложности"""
        temp_list = list(range(1, self.side ** 2 + 1))
        shuffle(temp_list)
        bombs_numbers = temp_list[:self.mods[mode][self.side]]
        print('Всего бомб', len(bombs_numbers))
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
