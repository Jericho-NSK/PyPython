from turtle import Screen


class Control:

    def __init__(self):
        super().__init__()
        Screen().onkeypress(self.random_color, 'space')
        Screen().onkeypress(self.go_up, 'w')
        Screen().onkeypress(self.go_left, 'a')
        Screen().onkeypress(self.go_down, 's')
        Screen().onkeypress(self.go_right, 'd')