from random import uniform

import pygame
from images_and_sounds import Images
from consts import HEIGHT, WIDTH


class Wall(pygame.sprite.Sprite):
    wall_width = 108
    speed = 1

    def __init__(self, game, track, reverse):
        super().__init__()
        if reverse:
            self.image = pygame.transform.flip(Images.wall_image, False, True)
            self.rect = self.image.get_rect(bottomleft=(WIDTH, track - 100))
            self.score_flag = False
        else:
            self.image = Images.wall_image
            self.rect = self.image.get_rect(topleft=(WIDTH, track + 100))
            self.score_flag = True
        self.add(game.walls)

    def update(self, window):
        if self.rect.x > -self.wall_width:
            self.rect.x -= self.speed
        else:
            self.kill()
            if self.score_flag:
                window.score_text += 100
                window.score = window.score_font.render(str(window.score_text), True, 'red')

    @staticmethod
    def create_wall(game):
        dy = int(HEIGHT * uniform(-0.1, 0.1))
        game.track += dy
        if game.track > HEIGHT - 150:
            game.track -= abs(2 * dy)
        elif game.track < 150:
            game.track += abs(2 * dy)

        for reverse in [0, 1]:
            Wall(game, game.track, reverse)
        return
