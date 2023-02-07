import pygame


class Wall(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.rect = None
        self.image = None
