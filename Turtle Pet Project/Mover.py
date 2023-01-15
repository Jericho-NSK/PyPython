class Mover:
    _step = 100

    def __init__(self):
        super().__init__()

    def go_up(self):
        x, y = self.position()
        self.setposition(x, y + self._step)

    def go_left(self):
        x, y = self.position()
        self.setposition(x - self._step, y)

    def go_down(self):
        x, y = self.position()
        self.setposition(x, y - self._step)

    def go_right(self):
        x, y = self.position()
        self.setposition(x + self._step, y)

    def step_big(self):
        if self._step < 500:
            self._step += 10

    def step_small(self):
        if self._step > 10:
            self._step -= 10
