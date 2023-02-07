import pygame


class Bird(pygame.Surface):
    size = 50, 50

    def __init__(self, window):
        super().__init__(size=self.size)
        self.fill('red')
        self.rect = self.get_rect()
        self.rect.center = window.WIDTH // 10, window.HEIGHT // 2
        self.image = None

    def jump(self, game):
        game.bird.rect.centery -= 25
