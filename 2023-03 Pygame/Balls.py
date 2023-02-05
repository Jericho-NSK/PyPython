from pygame import sprite


class Ball(sprite.Sprite):
    def __init__(self, x, speed, surf, group):
        super().__init__(self)
        self.image = surf
        self.rect = self.image.get_rect(center=(x, 0))
        self.speed = speed
        self.add(group)

    def update(self, *args: Any, **kwargs: Any) -> None:
