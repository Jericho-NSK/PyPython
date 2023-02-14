import sys

import pygame
from time import perf_counter

from bird import Bird
from walls import Wall
from menu import Menu

pygame.init()
# WIDTH, HEIGHT = 1920, 1080
WIDTH, HEIGHT = 1280, 720
FPS = 60


class Game:
    walls = pygame.sprite.Group()
    score_font = pygame.font.SysFont('comicsanms', size=48, italic=True)
    score_text = 0
    window = pygame.display.set_mode(size=(WIDTH, HEIGHT),
                                     flags=pygame.DOUBLEBUF | pygame.HWSURFACE | pygame.NOFRAME,
                                     depth=32,
                                     vsync=True)

    def __init__(self):
        self.last_wall_time = 0
        self.wall_timer = 1000
        self.game_starts = False
        self.score = self.score_font.render(str(self.score_text), True, 'red')
        self.track = HEIGHT // 2
        self.create_window()
        self.bird = Bird(self, WIDTH, HEIGHT)
        self.menu = Menu(self, self.window)
        self.menu.call_menu(self, self.window)

        # self.menu.mainloop(self.window)

    def create_window(self):
        self.bird_images = [pygame.image.load('images/' + bird).convert_alpha() for bird in Bird.images]
        self.wall_image = pygame.image.load('images/column.png').convert_alpha()
        self.bg = pygame.image.load('images/bg2.png').convert()
        self.bg_rect = self.bg.get_rect()
        self.window.blit(self.bg, (self.bg_rect.x, self.bg_rect.y))
        pygame.display.set_caption('NOT a flappy bird')
        pygame.display.set_icon(self.bird_images[-1])

    def update_window(self):
        if self.game_starts and not self.menu.is_enabled():
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
        if self.bird.image != self.bird_images[-1]:
            self.bird.flying(self, FPS, WIDTH, HEIGHT)
        if self.menu.is_enabled():
            self.menu.update(pygame.event.get())
            self.menu.draw(self.window)
        pygame.display.update()
        pygame.time.Clock().tick(FPS)

    def start_window(self):
        # Wall.create_wall(game=self, width=WIDTH, height=HEIGHT)

        while True:
            # self.bird.flying(self, FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:

                        # self.game_starts = True
                        # pygame.time.set_timer(pygame.USEREVENT, 1000)
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
                    self.bird.image = self.bird_images[0]
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
        self.menu.disable()
        # self.start_window()
        # Wall.create_wall(game=self, width=WIDTH, height=HEIGHT)
        self.game_starts = True
        self.last_wall_time = perf_counter()
        pygame.time.set_timer(pygame.USEREVENT, int(self.wall_timer))

        while True:
            self.game_starts = True
            for event in pygame.event.get():

                if event.type == pygame.USEREVENT and (perf_counter() - self.last_wall_time) >= 1:
                    print(1, self.wall_timer, perf_counter() - self.last_wall_time)
                    self.last_wall_time = perf_counter()
                    self.wall_timer = 1000
                    print(2, self.wall_timer, (perf_counter() - self.last_wall_time)*1000)
                    Wall.create_wall(game=self, width=WIDTH, height=HEIGHT)
                    break
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        print(3, self.wall_timer, (perf_counter() - self.last_wall_time)*1000)
                        self.wall_timer -= (perf_counter() - self.last_wall_time)*1000
                        print(4, self.wall_timer, (perf_counter() - self.last_wall_time)*1000)
                        self.menu.call_menu(self, self.window)
                    elif event.key == pygame.K_SPACE:
                        self.bird.jump = 35
                    elif event.key == pygame.K_w:
                        self.bird.jump = 25

            # self.bird.flying(self, FPS, WIDTH, HEIGHT)
            self.update_window()


Game()
