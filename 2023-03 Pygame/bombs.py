from random import randint

import pygame
from pygame import sprite


class Bombs(sprite.Sprite):
    bomb_size = 80
    bombs_data = ({'file': 'Bomb_1', 'score': 100},
                  {'file': 'Bomb_2', 'score': 200},
                  {'file': 'Bomb_3', 'score': 300})
    bombs = pygame.sprite.Group()

    def __init__(self, x, speed, image, score):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(centerx=x, centery=-self.bomb_size / 2)
        self.speed = speed
        self.score = score
        self.add(Bombs.bombs)

    def update(self, height, size) -> None:
        if self.rect.y < height - size:
            self.rect.y += self.speed
        else:
            self.kill()

    @staticmethod
    def create_bomb(window, width):
        index = randint(0, len(window.bombs_images) - 1)
        x = randint(int(Bombs.bomb_size / 2), int(width - Bombs.bomb_size / 2))
        speed = randint(1, 40)
        return Bombs(x, speed, window.bombs_images[index], Bombs.bombs_data[index]['score'])
