import pygame

from constants import WIDTH, FPS, WINDOW, FONT
from images_and_sounds import Images
from walls import Wall


class Window:
    window = WINDOW

    def __init__(self, game):
        self.score = FONT.render(f'SCORE: {game.score}', True, 'red')
        self.speed = FONT.render(f'SPEED: {Wall.speed}', True, 'red')
        self.bg_rect = Images.bg.get_rect()
        self.heart_rect = Images.heart.get_rect()

    def update_window(self, game):
        self.window.blit(Images.bg, (self.bg_rect.x, 0))
        self.window.blit(Images.bg, (self.bg_rect.x + self.bg_rect.width, 0))
        if self.bg_rect.x <= - self.bg_rect.width:
            self.bg_rect.x = 0
        game.walls.draw(self.window)

        self.window.blit(self.score, (20, 20))
        self.window.blit(self.speed, (20, 60))
        for heart in range(game.lives):
            self.window.blit(Images.heart, (WIDTH - self.heart_rect.w * (heart + 1), self.heart_rect.y))

        self.window.blit(game.bird.image, (game.bird.rect.centerx, game.bird.rect.centery))
        if game.bird.image != Images.bird_images[-1]:
            game.bird.flying(game)
        if game.game_starts:
            pygame.display.update()
        pygame.time.Clock().tick(FPS)
