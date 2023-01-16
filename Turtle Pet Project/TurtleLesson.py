from turtle import Turtle, Screen

from Appearance import Colors
from Control import Control
from Mover import Mover
from Speed import Speed


class Line(Control, Mover, Speed, Colors, Turtle):
    """Painter for lines with random colors"""
    def __init__(self):
        super().__init__()


trt = Line()
Screen().listen()
Screen().update()
Screen().mainloop()
