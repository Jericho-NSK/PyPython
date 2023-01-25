from tkinter import Button


class Buttons(Button):
    _font = 'Arial', 1, 'bold'
    _bd = 3
    _count = 0
    _size = 1

    def __init__(self, x, y):
        super().__init__(bd=self._bd,
                         font=self._font)
        self.x = x + 1
        self.y = y + 1
        self.is_mine = False
        self.number = self._count + 1
        Buttons._count += 1
        # if self._number
