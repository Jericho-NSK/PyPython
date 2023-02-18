from random import uniform

import pygame

from constants import HEIGHT, WIDTH, SPEED, FONT, DIFFICULTY_MODS
from images_and_sounds import Images
from time import perf_counter

class Wall(pygame.sprite.Sprite):
    wall_width = 108
    speed = SPEED

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

    def update(self, game):
        if self.rect.x > -self.wall_width:
            self.rect.x -= self.speed
        else:
            self.kill()
            if self.score_flag:
                game.main_window.score_text += 100
                game.main_window.score = FONT.render(f'SCORE: {game.main_window.score_text}', True, 'red')
                if (game.main_window.score_text // 100 in DIFFICULTY_MODS or
                        (game.main_window.score_text // 100 > DIFFICULTY_MODS[-1] and
                         game.main_window.score_text % 5000 == 0)):
                    Wall.speed += 1
                    pygame.time.set_timer(pygame.USEREVENT, 3000 // Wall.speed)
                    game.main_window.speed = FONT.render(f'SPEED: {Wall.speed}', True, 'red')

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
