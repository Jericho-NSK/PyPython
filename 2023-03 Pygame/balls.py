from pygame import sprite


class Ball(sprite.Sprite):
    def __init__(self, x, speed, image, score, group, size):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(centerx=x, centery=-size/2)
        self.speed = speed
        self.score = score
        self.add(group)

    def update(self, height, size) -> None:
        if self.rect.y < height - size:
            self.rect.y += self.speed
        else:
            self.kill()
