import pygame

from consts import HEIGHT, WIDTH, FPS, window
from images_and_sounds import Images


class Window:
    window = window

    def __init__(self):
        self.bg_rect = Images.bg.get_rect()
        self.create_window()

    def create_window(self):
        self.window.blit(Images.bg, (self.bg_rect.x, self.bg_rect.y))

    def update_window(self, game):
        if game.game_starts and not game.menu.is_enabled():
            game.walls.update(game)
            game.crash()
            self.bg_rect.x -= 1
        self.window.blit(Images.bg, (self.bg_rect.x, 0))
        self.window.blit(Images.bg, (self.bg_rect.x + self.bg_rect.width, 0))
        if self.bg_rect.x <= - self.bg_rect.width:
            self.bg_rect.x = 0
        game.walls.draw(self.window)
        self.window.blit(game.score, (20, 20))
        self.window.blit(game.bird.image, (game.bird.rect.centerx, game.bird.rect.centery))
        if game.menu.is_enabled():
            game.menu.update(pygame.event.get())
            game.menu.draw(self.window)
        if game.bird.image != Images.bird_images[-1]:
            game.bird.flying(game)
        pygame.display.update()
        pygame.time.Clock().tick(FPS)

    def start_window(self, game):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        return
            self.update_window(game)

    def end_window(self, game):
        game.game_starts = False
        game.track = HEIGHT // 2
        game.bird.timer = 0
        game.bird.jump = 0
        game.bird.image = Images.bird_images[-1]
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    game.bird.rect.center = WIDTH // 10, HEIGHT // 3
                    game.bird.image = Images.bird_images[0]
                    for wall in game.walls:
                        wall.kill()
                    self.start_window(game)
                    return
            self.update_window(game)






