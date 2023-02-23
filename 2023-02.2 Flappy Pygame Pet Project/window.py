import pygame

from constants import WIDTH, FPS, WINDOW, HEIGHT
from elements import Elements
from images_and_sounds import Images


class Window:
    window = WINDOW

    def __init__(self, game):
        self.bg_rect = Images.bg.get_rect()
        self.elements = Elements(game, self)

    def update_window(self, game):
        self.window.blit(Images.bg, (self.bg_rect.x, 0))
        self.window.blit(Images.bg, (self.bg_rect.x + self.bg_rect.width, 0))
        if self.bg_rect.x <= - self.bg_rect.width:
            self.bg_rect.x = 0

        game.walls.draw(self.window)

        self.window.blits((
            (self.elements.score, (20, 20)),
            (self.elements.speed, (20, 60)),
            *((Images.heart, (WIDTH - self.elements.heart_rect.w * (heart + 1),
                              self.elements.heart_rect.y)) for heart in range(game.lives)),
            (game.bird.image, (game.bird.rect.centerx, game.bird.rect.centery)),
        ), False)

        if self.elements.escape_timer:
            self.window.blit(self.elements.escape_up,
                             (WIDTH // 2 - self.elements.escape_up_rect.w // 2, HEIGHT - 3 * self.elements.escape_up_rect.h))
            self.window.blit(self.elements.escape_down,
                             (WIDTH // 2 - self.elements.escape_down_rect.w // 2, HEIGHT - 2 * self.elements.escape_down_rect.h))
            self.elements.escape_timer -= 1
        if game.bird.image != Images.bird_images[-1]:
            game.bird.flying(game)
        if game.game_starts:
            pygame.display.update()
        pygame.time.Clock().tick(FPS)
