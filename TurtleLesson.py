from turtle import Turtle, colormode, bgcolor
from random import randint


class Window:
    __default_size = 3
    __default_colormode = 255
    __default_back_ground_color = 'black'
    __default_color = 'red'
    __random_color = randint(0, __default_colormode), randint(0, __default_colormode), randint(0, __default_colormode)

    @property
    def Color(self):
        return print(self._color)

    @Color.setter
    def Color(self, color):
        if isinstance(color, str):
            self.pencolor(color)
        else:
            self.pencolor(self.__random_color)
        self._color = self.pen()['pencolor']

    def default_values(self):
        self.pensize(self.__default_size)
        self.pencolor(self.__default_color)
        bgcolor(self.__default_back_ground_color)
        colormode(self.__default_colormode)


class Speed:
    __default_speed = 2

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


class Pointer(Turtle, Speed, Window):
    def __init__(self):
        super().__init__()
        self.default_values()

    def default_values(self):
        super().default_values()


trt = Pointer()
print(trt.pen()['pencolor'])
# exitonclick()
