from random import uniform

import pygame


class Wall(pygame.sprite.Sprite):
    wall_width = 108
    speed = 5

    def __init__(self, game, width, track, reverse):
        super().__init__()
        if reverse:
            self.image = pygame.transform.flip(game.wall_image, False, True)
            self.rect = self.image.get_rect(bottomleft=(width, track - 100))
            self.score_flag = False
        else:
            self.image = game.wall_image
            self.rect = self.image.get_rect(topleft=(width, track + 100))
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
    def create_wall(game, width, height):
        dy = int(height * uniform(-0.1, 0.1))
        game.track += dy
        if game.track > height - 150:
            game.track -= abs(2 * dy)
        elif game.track < 150:
            game.track += abs(2 * dy)

        for reverse in [0, 1]:
            Wall(game, width, game.track, reverse)
