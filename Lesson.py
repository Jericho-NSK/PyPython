# import pygame
#
# pygame.init()
#
# W = 600
# H = 400
#
# window = pygame.display.set_mode((W, H))
# pygame.display.set_caption("Класс Rect")
#
# WHITE = (255, 255, 255)
# BLUE = (0, 0, 255)
# GREEN = (0, 255, 0)
# RED = (255, 0, 0)
#
# FPS = 24        # число кадров в секунду
# clock = pygame.time.Clock()
#
# ground = H-70           # высота земли
# jump_force = 20         # сила прыжка
# move = jump_force+1     # текущая вертикальная скорость
#
# hero = pygame.Surface((40, 50))
# hero.fill(BLUE)
# rect = hero.get_rect(centerx=W//2)
#
# rect.bottom = ground
#
# rect_update = pygame.Rect(rect.x, 0, rect.width, ground)
# window.fill(WHITE)
# pygame.display.update()
# print(pygame.image.get_extended())
# while 1:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             exit()
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_SPACE and ground == rect.bottom:
#                 move = -jump_force
#
#     if move <= jump_force:
#         if rect.bottom + move < ground:
#             rect.bottom += move
#             if move < jump_force:
#                 move += 1
#         else:
#             rect.bottom = ground
#             move = jump_force+1
#
#     window.fill(WHITE)
#     window.blit(hero, rect)
#     pygame.display.update(rect_update)
#
#     clock.tick(FPS)
a = -2570
b = -2570

for i in range(2600000):
    a +=1
    b+=1
    if a is b:
        print(a, id(a))
# print(a)
