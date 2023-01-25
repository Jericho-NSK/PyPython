from tkinter import Button


class Buttons(Button):
    _font = 'Arial', 14, 'bold'
    _bd = 3

    def __init__(self, x, y, count):
        super().__init__(bd=self._bd,
                         font=self._font)
        self.boom = None
        self.x = x + 1
        self.y = y + 1
        self.is_mine = False
        self.number = count


