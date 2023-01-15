from turtle import Turtle, Screen

from Colors import Colors
from Mover import Mover
from Speed import Speed
from Control import Control


class Pointer(Control, Mover, Speed, Colors, Turtle):
    def __init__(self):
        super().__init__()
        self.default_values()

    def default_values(self):
        super().default_values()


trt = Pointer()
Screen().listen()
Screen().mainloop()
