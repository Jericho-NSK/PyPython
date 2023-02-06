from pygame import sprite


class Ball(sprite.Sprite):
    def __init__(self, x, speed, surf, group, size):
        super().__init__()
        self.image = surf
        self.rect = self.image.get_rect(center=(x, -size))
        self.speed = speed
        self.add(group)

    def update(self, height, size) -> None:
        if self.rect.y < height - size:
            self.rect.y += self.speed
        else:
            self.kill()
