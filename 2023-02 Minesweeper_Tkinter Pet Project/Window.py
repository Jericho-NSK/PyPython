from random import shuffle
from tkinter import Tk, PhotoImage

from BottomPanel import BottomPanel
from Buttons import Buttons
from Menubar import Menubar


class Window(Tk):
    """Class for creating the main game window with fields in the form of buttons"""
    _title = 'Minesweeper'
    mods = {'easy': {'5': (4, 3), '10': (18, 4), '15': (35, 6)},
            'normal': {'5': (6, 2), '10': (24, 3), '15': (45, 5)},
            'hard': {'5': (8, 1), '10': (30, 2), '15': (55, 4)}}
    list_button = []

    def __init__(self, game):
        super().__init__()
        self.bottom_panel = None
        self.side = 10
        self.side_size = self.side * Buttons.button_size
        self.mode = 'normal'
        self.title(self._title)
        self.new_window(game=game)
        self.resizable(False, False)
        self.iconphoto(True, PhotoImage(file='FirstBoom.png', master=self))

    def new_window(self, game):
        """Creating window"""
        Menubar(self, game)
        self.side_size = self.side * Buttons.button_size
        self.geometry(f'{self.side_size}x{self.side_size + 65}+1000+200')
        self.create_default_buttons()
        self.create_buttons()
        self.create_bombs(game)
        self.bottom_panel = BottomPanel(window=self, game=game)
        self.alignment()
        self.count_bombs()

    def create_default_buttons(self):
        """Creating fields. Additional rows and columns are needed along the edges, so an increased number of fields are first created"""
        self.list_button = []
        for i in range(self.side + 2):
            temp_list = list()
            for j in range(self.side + 2):
                temp_list.append(Buttons())
            self.list_button.append(temp_list)

    def create_buttons(self):
        """Creating buttons"""
        temp_number = 1
        for row in range(self.side):
            for column in range(self.side):
                new_button = Buttons(row, column, temp_number)
                new_button.grid(stick='wens', row=row, column=column)
                self.list_button[row][column] = new_button
                temp_number += 1

    def create_bombs(self, game, button: Buttons = False):
        """Distribution of bombs by buttons depending on the selected difficulty"""
        temp_list = list(range(1, self.side ** 2 + 1))
        shuffle(temp_list)
        game.list_bombs_numbers = temp_list[:self.mods[self.mode][str(self.side)][0]]
        if button and button.number in game.list_bombs_numbers:
            return button
        for row in self.list_button:
            for btn in row:
                if btn.number in game.list_bombs_numbers:
                    btn.is_bomb = True
                else:
                    btn.is_bomb = False

    def alignment(self):
        """Alignment of the buttons and the bottom panel according to the width and height of the field"""
        for row in range(self.side):
            self.grid_rowconfigure(row, minsize=Buttons.button_size)
        for column in range(self.side):
            self.grid_columnconfigure(column, minsize=Buttons.button_size)
        self.grid_rowconfigure(self.side, minsize=25)
        self.grid_rowconfigure(self.side + 1, minsize=25)

    def count_bombs(self):
        """Counting mines from neighbors, assigning this number to button attributes"""
        for row in self.list_button:
            for btn in row:
                count_near_bombs = 0
                if not btn.is_bomb:
                    for dx in [-1, 0, 1]:
                        for dy in [-1, 0, 1]:
                            if self.list_button[btn.x + dx][btn.y + dy].is_bomb:
                                count_near_bombs += 1
                btn.count_near_bombs = count_near_bombs
