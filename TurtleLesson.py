from random import randint
from turtle import Turtle, colormode, bgcolor, exitonclick, Screen


class Speed:
    _default_speed = 1

    def __init__(self):
        super().__init__()

    @property
    def Speed(self):
        return print(self._speed)

    @Speed.setter
    def Speed(self, speed):
        self.speed(speed)
        self._speed = self.pen()['speed']

    def default_values(self):
        super().default_values()
        self.speed(self._default_speed)


class Colors:
    __colormode = 255
    _size = 3
    _back_ground_color = 'white'


    def __init__(self):
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

    def random_color(self):
        colormode(self.__colormode)
        r = randint(0, self.__colormode)
        g = randint(0, self.__colormode)
        b = randint(0, self.__colormode)
        self.pencolor(r, g, b)
        self._color = self.pen()['pencolor']
        self.fillcolor(self._color)

    def default_values(self):
        super().default_values()
        self.random_color()
        self.pensize(self._size)
        self.Color = self._color
        self.fillcolor(self._color)
        bgcolor(self._back_ground_color)
        Screen().onkey(self.random_color, 'space')


class Mover:
    def go_up(self):
        x = self.position()[0]
        y = self.position()[1]
        self.setposition(x, y + 100)

    def go_left(self):
        x = self.position()[0]
        y = self.position()[1]
        self.setposition(x - 100, y)

    def go_down(self):
        x = self.position()[0]
        y = self.position()[1]
        self.setposition(x, y - 100)

    def go_right(self):
        x = self.position()[0]
        y = self.position()[1]
        self.setposition(x + 100, y)

    def default_values(self):
        Screen().onkey(self.go_up, 'w')
        Screen().onkey(self.go_left, 'a')
        Screen().onkey(self.go_down, 's')
        Screen().onkey(self.go_right, 'd')


class Pointer(Turtle, Speed, Colors, Mover):
    def __init__(self):
        super().__init__()
        self.default_values()

    def default_values(self):
        super().default_values()


trt = Pointer()
Screen().listen()
Screen().mainloop()
Screen().update()
