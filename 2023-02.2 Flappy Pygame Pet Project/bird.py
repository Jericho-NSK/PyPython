import pygame


class Bird(pygame.Surface):
    size = 30, 30

    def __init__(self, window, width, height):
        super().__init__(size=self.size)
        self.fill('red')
        self.rect = self.get_rect()
        self.rect.center = width // 10, height // 2
        self.image = None

    def jump(self, game):
        game.bird.rect.centery -= 30
