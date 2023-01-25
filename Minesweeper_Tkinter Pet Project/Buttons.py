from tkinter import Button


class Buttons(Button):
    _font = 'Arial', 14, 'bold'
    _bd = 3

    def __init__(self, x=0, y=0, number=None):
        super().__init__(bd=self._bd,
                         font=self._font)
        self.boom = None
        self.coordinates = (x + 1, y + 1)
        self.is_mine = False
        self.number = number
        self.count_near_mines = 0



