import sys

import pygame

from bird import Bird

pygame.init()


class Game:
    WIDTH, HEIGHT = 1280, 720
    FPS = 60

    def __init__(self):
        self.window = None
        self.bird = Bird(self)
        self.create_window()
        self.mainloop()

    def create_window(self):
        self.window = pygame.display.set_mode(size=(self.WIDTH, self.HEIGHT))
        self.window.blit(self.bird, (self.WIDTH // 10, self.HEIGHT // 2))

    def window_update(self):
        self.window.fill('black')
        self.window.blit(self.bird, (self.bird.rect.centerx, self.bird.rect.centery))
        pygame.display.flip()
        pygame.time.Clock().tick(self.FPS)

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
            self.window_update()

    def end_window(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.bird.rect.center = self.WIDTH//10, self.HEIGHT//2
                    self.start_window()
                    return
            self.window_update()

    def mainloop(self):
        self.start_window()
        while True:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        Bird.jump(self.bird, game=self)

            key = pygame.key.get_pressed()
            if key[pygame.K_a] or key[pygame.K_LEFT]:
                self.bird.rect.centerx -= 2
            elif key[pygame.K_d] or key[pygame.K_RIGHT]:
                self.bird.rect.centerx += 2

            self.bird.rect.centery += 0

            if self.bird.rect.bottom > self.HEIGHT - self.bird.rect.height / 2:
                self.bird.rect.bottom = self.HEIGHT - self.bird.rect.height / 2
                self.end_window()
            if self.bird.rect.top < -self.bird.rect.height / 2:
                self.bird.rect.top = -self.bird.rect.height / 2
                self.end_window()
            if self.bird.rect.right > self.WIDTH - self.bird.rect.width / 2:
                self.bird.rect.right = self.WIDTH - self.bird.rect.width / 2
            if self.bird.rect.left < -self.bird.rect.width / 2:
                self.bird.rect.left = -self.bird.rect.width / 2

            self.window_update()


Game()
