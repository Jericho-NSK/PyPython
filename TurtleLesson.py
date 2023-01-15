from random import randint
from turtle import Turtle, colormode, bgcolor, exitonclick, Screen


class Speed:
    __default_speed = 1

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
        self.speed(self.__default_speed)


class Colors:
    __size = 3
    __colormode = 255
    __back_ground_color = 'white'
    __color = 'red'


    def __init__(self):
        self.Color = self.__color

    @property
    def Color(self):
        return print(self.__color)

    @Color.setter
    def Color(self, color):
        if isinstance(color, str) and color != 'random':
            self.pencolor(color)
        else:
            self.random_color()

    def random_color(self):
        r = randint(0, self.__colormode)
        g = randint(0, self.__colormode)
        b = randint(0, self.__colormode)
        self.pencolor(r, g, b)
        self.__color = self.pen()['pencolor']
        self.fillcolor(self.__color)

    def default_values(self):
        super().default_values()
        self.pensize(self.__size)
        self.Color = self.__color
        self.fillcolor(self.__color)
        bgcolor(self.__back_ground_color)
        colormode(self.__colormode)
        self.random_color()
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
exitonclick()
