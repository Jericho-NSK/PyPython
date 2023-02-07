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
        self.window = None
        self.track = HEIGHT // 2
        self.bird = Bird(self, WIDTH, HEIGHT)
        self.create_window()
        self.wall_image = pygame.image.load('images/new_chair.png').convert_alpha()
        self.mainloop()

    def create_window(self):
        self.window = pygame.display.set_mode(size=(WIDTH, HEIGHT))
        self.window.blit(self.bird, (WIDTH // 10, HEIGHT // 2))

    def update_window(self):
        self.window.fill('black')
        self.walls.draw(self.window)
        self.walls.update(WIDTH, Wall.wall_size)
        self.window.blit(self.bird, (self.bird.rect.centerx, self.bird.rect.centery))
        pygame.display.flip()
        pygame.time.Clock().tick(FPS)

    def start_window(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        Bird.jump(self.bird, game=self)
                        Bird.jump(self.bird, game=self)
                        return
            self.update_window()

    def end_window(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.bird.rect.center = WIDTH//10, HEIGHT//2
                    self.start_window()
                    return
            self.update_window()

    def mainloop(self):
        # self.start_window()
        pygame.time.set_timer(pygame.USEREVENT, 3000)
        while True:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.USEREVENT:
                    Wall.create_wall(window=self, width=WIDTH, height=HEIGHT)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        Bird.jump(self.bird, game=self)

            key = pygame.key.get_pressed()
            if (key[pygame.K_a] or key[pygame.K_LEFT]) and self.bird.rect.centerx > 0:
                self.bird.rect.centerx -= 2
            elif (key[pygame.K_d] or key[pygame.K_RIGHT]) and self.bird.rect.right < WIDTH - self.bird.rect.width:
                self.bird.rect.centerx += 2

            self.bird.rect.centery += 1

            if self.bird.rect.bottom > HEIGHT - self.bird.rect.height // 2:
                self.bird.rect.bottom = HEIGHT - self.bird.rect.height // 2
                self.end_window()
            if self.bird.rect.top < -self.bird.rect.height // 2:
                self.bird.rect.top = -self.bird.rect.height // 2

            self.update_window()


Game()
