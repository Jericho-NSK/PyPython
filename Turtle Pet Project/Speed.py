class Speed:
    _default_speed = 5

    def __init__(self):
        super().__init__()

    @property
    def Speed(self):
        return print(self._speed)

    @Speed.setter
    def Speed(self, speed):
        self.speed(speed)
        self._speed = self.pen()['speed']

    def default_values(self):
        super().default_values()
        self.speed(self._default_speed)
