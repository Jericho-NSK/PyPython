import pygame

class Images:
    images = 'bird_up.png', 'bird_down.png', 'bird_crash.png'
    wall_image = pygame.image.load('images/column.png').convert_alpha()
    bird_images = [pygame.image.load('images/' + bird).convert_alpha() for bird in images]
    wall_image = pygame.image.load('images/column.png').convert_alpha()
    bg = pygame.image.load('images/bg2.png').convert()
    # bg_rect = bg.get_rect()
    pygame.display.set_caption('NOT a flappy bird')
    pygame.display.set_icon(bird_images[-1])