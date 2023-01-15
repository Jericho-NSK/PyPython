from turtle import Screen


class Mover:
    _default_step = 10

    def __init__(self):
        super().__init__()

    def go_up(self):
        x, y = self.position()
        self.setposition(x, y + self._default_step)

    def go_left(self):
        x, y = self.position()
        self.setposition(x - self._default_step, y)

    def go_down(self):
        x, y = self.position()
        self.setposition(x, y - self._default_step)

    def go_right(self):
        x, y = self.position()
        self.setposition(x + self._default_step, y)

    def default_values(self):
        super().default_values()

