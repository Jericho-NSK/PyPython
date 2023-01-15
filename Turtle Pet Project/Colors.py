from random import randint
from turtle import colormode, bgcolor, Screen


class Colors:
    __colormode = 255
    _size = 3
    _back_ground_color = 'white'

    def __init__(self):
        super().__init__()
        self.Color = self._color

    @property
    def Color(self):
        return print(self._color)

    @Color.setter
    def Color(self, color):
        if isinstance(color, str) and color != 'random':
            self.pencolor(color)
        else:
            self.random_color()

    def hidding(self):
        if self.isvisible():
            self.hideturtle()
        else:
            self.showturtle()


    def random_color(self):
        colormode(self.__colormode)
        r = randint(0, self.__colormode)
        g = randint(0, self.__colormode)
        b = randint(0, self.__colormode)
        self.pencolor(r, g, b)
        self._color = self.pen()['pencolor']
        self.fillcolor(self._color)

    def default_values(self):
        self.random_color()
        self.pensize(self._size)
        self.Color = self._color
        self.fillcolor(self._color)
        bgcolor(self._back_ground_color)

