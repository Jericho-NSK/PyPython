from random import random
from turtle import bgcolor


class Pointer:
    """Pointer appearance. Can hide him and change scale by buttons"""
    _pointer_size = 1.5
    _pen_size = 3

    def __init__(self):
        super().__init__()
        self.shapesize(self._pointer_size)
        self.pensize(self._pen_size)
        self.shape('turtle')

    def hidding(self):
        if self.isvisible():
            self.hideturtle()
        else:
            self.showturtle()

    def scaling_big(self):
        if self._pointer_size < 4.5 and self._pen_size < 9:
            self._pointer_size += 0.5
            self.shapesize(self._pointer_size)
            self._pen_size += 1
            self.pensize(self._pen_size)

    def scaling_small(self):
        if self._pointer_size > 0.5 and self._pen_size > 1:
            self._pointer_size -= 0.5
            self.shapesize(self._pointer_size)
            self._pen_size -= 1
            self.pensize(self._pen_size)

class Colors(Pointer):
    """Setter for background color and pointer. Setter used just for example.
    Can change color by buttons to random color"""
    _back_ground_color = 'white'

    def __init__(self):
        super().__init__()
        self.random_color()
        bgcolor(self._back_ground_color)

    @property
    def Color(self):
        return print(self._color)

    @Color.setter
    def Color(self, color):
        if isinstance(color, str) and color != 'random':
            self.pencolor(color)
        else:
            self.random_color()

    def random_color(self):
        r = random()
        g = random()
        b = random()
        self.pencolor(r, g, b)
        self._color = self.pen()['pencolor']
        self.fillcolor(self._color)
