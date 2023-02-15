import pygame

pygame.init()

WIDTH, HEIGHT = 1280, 720
BIRD_SIZE = 40, 30
FPS = 60
score_font = pygame.font.SysFont('comicsanms', size=48, italic=True)
window = pygame.display.set_mode(size=(WIDTH, HEIGHT),
                                 flags=pygame.DOUBLEBUF | pygame.HWSURFACE | pygame.NOFRAME,
                                 depth=32,
                                 vsync=True,
                                 )