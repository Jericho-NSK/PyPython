import sys

import pygame

from bird import Bird
from walls import Wall

pygame.init()
WIDTH, HEIGHT = 1280, 720
FPS = 60


class Game:
    walls = pygame.sprite.Group()

    def __init__(self):
        self.game_starts = False
        self.jump = None
        self.is_jump = None
        self.window = None
        self.track = HEIGHT // 2

        self.create_window()
        self.mainloop()

    def create_window(self):
        self.window = pygame.display.set_mode(size=(WIDTH, HEIGHT))
        self.bird_images = [pygame.image.load('images/' + bird).convert_alpha() for bird in Bird.images]
        self.wall_image = pygame.image.load('images/column.png').convert_alpha()
        self.bird = Bird(self, WIDTH, HEIGHT)

    def update_window(self):
        if self.game_starts:
            self.crash()
        self.window.fill('black')
        self.walls.draw(self.window)
        if self.game_starts:
            self.walls.update(WIDTH, Wall.wall_size)
        self.window.blit(self.bird.image, (self.bird.rect.centerx, self.bird.rect.centery))
        pygame.display.flip()
        pygame.time.Clock().tick(FPS)

    def start_window(self):
        Wall.create_wall(window=self, width=WIDTH, height=HEIGHT)
        while True:
            self.bird.flying(self, FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
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
            if wall.rect.colliderect(self.bird.rect):
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
                    sys.exit()
                elif event.type == pygame.USEREVENT:
                    Wall.create_wall(window=self, width=WIDTH, height=HEIGHT)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.bird.jump = 35
                    elif pygame.key.get_mods() & pygame.KMOD_SHIFT:
                        self.bird.jump = 25

            self.bird.flying(self, FPS, WIDTH, HEIGHT)
            self.update_window()


Game()
