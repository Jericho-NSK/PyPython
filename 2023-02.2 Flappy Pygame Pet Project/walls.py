import pygame
from random import uniform


class Wall(pygame.sprite.Sprite):
    wall_size = 100, 1000
    speed = 1

    def __init__(self, window, width, track, reverse):
        super().__init__()
        if reverse:
            self.image = pygame.transform.flip(window.wall_image, 0, 1)
            self.rect = self.image.get_rect(bottomleft=(width, track - 80))
        else:
            self.image = window.wall_image
            self.rect = self.image.get_rect(topleft=(width, track + 80))
        self.add(window.walls)

    def update(self, wigth, size):
        if self.rect.x > -size[0]:
            self.rect.x -= self.speed
        else:
            self.kill()

    @staticmethod
    def create_wall(window, width, height):
        dy = int(height*uniform(-0.1, 0.1))
        window.track += dy
        print(window.track, dy)
        if window.track > height - 150:
            window.track -= abs(2* dy)
        elif window.track < 150:
            window.track += abs(2 * dy)

        for reverse in [0, 1]:
            Wall(window, width, window.track, reverse)

