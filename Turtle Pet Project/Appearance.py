from random import randint
from turtle import colormode, bgcolor


class Pointer:
    _pointer_size = 1.5
    _pen_size = 3

    def __init__(self):
        super().__init__()
        self.shapesize(self._pointer_size)
        self.pensize(self._pen_size)

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
    __colormode = 255
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
        colormode(self.__colormode)
        r = randint(0, self.__colormode)
        g = randint(0, self.__colormode)
        b = randint(0, self.__colormode)
        self.pencolor(r, g, b)
        self._color = self.pen()['pencolor']
        self.fillcolor(self._color)
