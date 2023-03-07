from random import uniform

import pygame

from constants import HEIGHT, WIDTH, SPEED, FONT, DIFFICULTY_MODS
from images_and_sounds import Images


class Wall(pygame.sprite.Sprite):
    """Class for creating moving walls"""
    wall_width = 108
    speed = SPEED

    def __init__(self, game, track, reverse):
        """Creating two walls - on the top and on the bottom of main window"""
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
        """
        Updating for moving walls.
        Deleting walls if it goes beside of main window.
        Adding score and speed
        """
        self.rect.x -= self.speed * 2
        if self.rect.right < 0:
            self.kill()
            if self.score_flag:
                game.score += 100
                game.main_window.elements.score = FONT.render(f'SCORE: {game.score}', True, 'red')
                if (game.score // 100 in DIFFICULTY_MODS or
                        (game.score // 100 > DIFFICULTY_MODS[-1] and
                         game.score % 5000 == 0)):
                    Wall.speed += 1
                    pygame.time.set_timer(pygame.USEREVENT, 3000 // Wall.speed)
                    game.main_window.elements.speed = FONT.render(f'SPEED: {Wall.speed}', True, 'red')

    @staticmethod
    def create_wall(game):
        """Determining the position of walls relative to the tracker (higher and lower than tracker)"""
        dy = int(HEIGHT * uniform(-0.1, 0.1))
        game.track += dy
        if game.track > HEIGHT - 150:
            game.track -= abs(2 * dy)
        elif game.track < 150:
            game.track += abs(2 * dy)

        for reverse in [0, 1]:
            Wall(game, game.track, reverse)
        return
