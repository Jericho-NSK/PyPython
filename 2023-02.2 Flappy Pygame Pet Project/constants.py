import pygame
from pygame_menu.examples.game_selector import DIFFICULTY

pygame.init()


WIDTH, HEIGHT = 1280, 720
START_TRACK = HEIGHT // 2.5
BIRD_SIZE = 40, 30
FPS = 60
SPEED = 20
DIFFICULTY_MODS = (1, 10, 20, 35, 55, 75, 100, 130, 165, 200)
FONT = pygame.font.SysFont('comicsanms', size=48, italic=True)
WINDOW = pygame.display.set_mode(size=(WIDTH, HEIGHT),
                                 flags=pygame.DOUBLEBUF | pygame.HWSURFACE | pygame.NOFRAME,
                                 depth=32,
                                 vsync=True,
                                 )