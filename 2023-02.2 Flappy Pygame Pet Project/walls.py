from random import uniform

import pygame


class Wall(pygame.sprite.Sprite):
    wall_width = 108
    speed = 4

    def __init__(self, window, width, track, reverse):
        super().__init__()
        if reverse:
            self.image = pygame.transform.flip(window.wall_image, False, True)
            self.rect = self.image.get_rect(bottomleft=(width, track - 100))
        else:
            self.image = window.wall_image
            self.rect = self.image.get_rect(topleft=(width, track + 100))
        self.add(window.walls)

    def update(self, window):
        if self.rect.x > -self.wall_width:
            self.rect.x -= self.speed
        else:
            self.kill()
            window.score_text += 50
            window.score = window.score_font.render(str(window.score_text), True, 'red')

    @staticmethod
    def create_wall(window, width, height):
        dy = int(height * uniform(-0.1, 0.1))
        window.track += dy
        if window.track > height - 150:
            window.track -= abs(2 * dy)
        elif window.track < 150:
            window.track += abs(2 * dy)

        for reverse in [0, 1]:
            Wall(window, width, window.track, reverse)
