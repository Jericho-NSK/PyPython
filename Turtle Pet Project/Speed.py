class Speed:
    __speed = 5

    def __init__(self):
        super().__init__()
        self.speed(self.__speed)

    def speed_up(self):
        if 1 <= self.__speed < 10:
            self.__speed += 1
            self.speed(self.__speed)
        elif self.__speed == 10:
            self.__speed = 0
            self.speed(self.__speed)

    def speed_down(self):
        if 1 < self.__speed <= 10:
            self.__speed -= 1
            self.speed(self.__speed)
        elif self.__speed == 0:
            self.__speed = 10
            self.speed(self.__speed)
