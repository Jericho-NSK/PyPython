from turtle import Screen


class Control:

    def __init__(self):
        super().__init__()
        Screen().onkeypress(self.random_color, 'space')
        Screen().onkeypress(self.go_up, 'w')
        Screen().onkeypress(self.go_left, 'a')
        Screen().onkeypress(self.go_down, 's')
        Screen().onkeypress(self.go_right, 'd')
        Screen().onkeypress(self.hidding, 'q')
        Screen().onkeypress(self.scaling_big, '+')
        Screen().onkeypress(self.scaling_small, '-')
        Screen().onkeypress(self.speed_up, 'Right')
        Screen().onkeypress(self.speed_down, 'Left')
        Screen().onkeypress(self.step_big, 'Up')
        Screen().onkeypress(self.step_small, 'Down')
