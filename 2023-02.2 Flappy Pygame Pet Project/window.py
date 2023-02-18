import pygame

from constants import HEIGHT, WIDTH, START_TRACK, FPS, WINDOW, FONT
from images_and_sounds import Images
from walls import Wall
from menus import Menus


class Window:
    window = WINDOW
    lives = 3
    score_text = 0

    def __init__(self):
        self.score = FONT.render(f'SCORE: {self.score_text}', True, 'red')
        self.speed = FONT.render(f'SPEED: {Wall.speed}', True, 'red')
        self.bg_rect = Images.bg.get_rect()
        self.heart_rect = Images.heart.get_rect()
        # self.create_window()

    # def create_window(self):...
        # self.window.blit(Images.bg, (self.bg_rect.x, self.bg_rect.y))
        # self.window.blit(Images.heart, (self.heart_rect.x, self.heart_rect.y))

    def update_window(self, game):
        self.window.blit(Images.bg, (self.bg_rect.x, 0))
        self.window.blit(Images.bg, (self.bg_rect.x + self.bg_rect.width, 0))
        if self.bg_rect.x <= - self.bg_rect.width:
            self.bg_rect.x = 0
        game.walls.draw(self.window)
        self.window.blit(self.score, (20, 20))
        self.window.blit(self.speed, (20, 60))
        self.window.blit(Images.heart, (WIDTH - self.heart_rect.w, self.heart_rect.y))
        self.window.blit(game.bird.image, (game.bird.rect.centerx, game.bird.rect.centery))
        # if game.menu.main_menu.is_enabled():
        #     game.menu.main_menu.update(pygame.event.get())
            # game.menu.main_menu.draw(self.window)
        # if game.crash_menu.is_enabled():
        #     game.crash_menu.update(pygame.event.get())
        #     game.crash_menu.draw(self.window)
        if game.bird.image != Images.bird_images[-1]:
            game.bird.flying(game)
        if game.game_starts:
            pygame.display.update()
        pygame.time.Clock().tick(FPS)

    # def start_window(self, game):
    #     while True:
    #         for event in pygame.event.get():
    #             if event.type == pygame.KEYDOWN:
    #                 if event.key == pygame.K_SPACE:
    #                     return
    #         self.update_window(game)

    def end_window(self, game):
        game.game_starts = False
        game.track = START_TRACK
        game.bird.timer = 0
        game.bird.jump = 0
        game.bird.image = Images.bird_images[-1]
        game.menu.about_menu.enable()
        game.menu.call_menu(game, True)
        # while True:
        #     for event in pygame.event.get():
        #         if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        #             game.bird.rect.center = WIDTH // 10, HEIGHT // 3
        #             game.bird.image = Images.bird_images[0]
        #             for wall in game.walls:
        #                 wall.kill()
        #             # self.start_window(game)
        #             return
        #     self.update_window(game)
