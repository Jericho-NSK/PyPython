from turtle import Screen


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
