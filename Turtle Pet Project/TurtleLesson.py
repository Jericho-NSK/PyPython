from turtle import Turtle, Screen

from Appearance import Colors
from Control import Control
from Mover import Mover
from Speed import Speed


class Painter(Control, Mover, Speed, Colors, Turtle):
    def __init__(self):
        super().__init__()


trt = Painter()
Screen().listen()
Screen().mainloop()
