import sys

import pygame

from bird import Bird
from walls import Wall
from menu import Menu

pygame.init()
WIDTH, HEIGHT = 1280, 720
FPS = 60


class Game:
    walls = pygame.sprite.Group()
    score_font = pygame.font.SysFont('comicsanms', size=48, italic=True)
    score_text = 0
    window = pygame.display.set_mode(size=(WIDTH, HEIGHT),
                                     flags=pygame.DOUBLEBUF | pygame.HWSURFACE | pygame.SCALED | pygame.RESIZABLE,
                                     depth=32,
                                     vsync=True)

    def __init__(self):
        self.game_starts = False
        self.score = self.score_font.render(str(self.score_text), True, 'red')
        self.track = HEIGHT // 2
        self.create_window()
        self.bird = Bird(self, WIDTH, HEIGHT)
        self.menu = Menu(self)
        self.menu.mainloop(self.window)
        self.mainloop()

    def create_window(self):
        self.bird_images = [pygame.image.load('images/' + bird).convert_alpha() for bird in Bird.images]
        self.wall_image = pygame.image.load('images/column.png').convert_alpha()
        self.bg = pygame.image.load('images/bg2.png').convert()
        self.bg_rect = self.bg.get_rect()
        self.window.blit(self.bg, (self.bg_rect.x, self.bg_rect.y))
        pygame.display.set_caption('NOT a flappy bird')
        pygame.display.set_icon(self.bird_images[-1])

    def update_window(self):
        if self.game_starts:
            self.walls.update(self)
            self.crash()
            self.bg_rect.x -= 1
        self.window.blit(self.bg, (self.bg_rect.x, 0))
        self.window.blit(self.bg, (self.bg_rect.x + self.bg_rect.width, 0))
        if self.bg_rect.x <= - self.bg_rect.width:
            self.bg_rect.x = 0
        self.walls.draw(self.window)
        self.window.blit(self.score, (20, 20))
        self.window.blit(self.bird.image, (self.bird.rect.centerx, self.bird.rect.centery))
        pygame.display.update()
        pygame.time.Clock().tick(FPS)

    def start_window(self):
        Wall.create_wall(window=self, width=WIDTH, height=HEIGHT)
        while True:
            self.bird.flying(self, FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.WINDOWMAXIMIZED:
                    self.window = pygame.display.set_mode(size=(WIDTH, HEIGHT),
                                                          flags=pygame.DOUBLEBUF | pygame.HWSURFACE | pygame.SCALED | pygame.FULLSCREEN,
                                                          depth=32,
                                                          vsync=True)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.game_starts = True
                        pygame.time.set_timer(pygame.USEREVENT, 1000)
                        return
            self.update_window()

    def end_window(self):
        self.game_starts = False
        self.track = HEIGHT // 2
        self.bird.timer = 0
        self.bird.jump = 0
        self.bird.image = self.bird_images[-1]
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.bird.rect.center = WIDTH // 10, HEIGHT // 3
                    for wall in self.walls:
                        wall.kill()
                    self.start_window()
                    return
            self.update_window()

    def crash(self):
        for wall in self.walls:
            if wall.rect.collidepoint(self.bird.rect.midright) or wall.rect.collidepoint(self.bird.rect.bottomright):
                return self.end_window()
            # self.sound_catch.play()
            # self.score_counter += bomb.score
            # self.score_text = self.score_font.render(str(self.score_counter), True, 'red')
            # wall.kill()

    def mainloop(self):
        self.start_window()
        # Wall.create_wall(window=self, width=WIDTH, height=HEIGHT)
        # self.game_starts = True
        # pygame.time.set_timer(pygame.USEREVENT, 1000)

        while True:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.USEREVENT:
                    Wall.create_wall(window=self, width=WIDTH, height=HEIGHT)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.bird.jump = 35
                    elif event.key == pygame.K_w:
                        self.bird.jump = 25

            self.bird.flying(self, FPS, WIDTH, HEIGHT)
            self.update_window()


Game()
