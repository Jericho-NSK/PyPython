from turtle import Turtle, Screen

from Color import Colors
from Mover import Mover
from Speed import Speed


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
