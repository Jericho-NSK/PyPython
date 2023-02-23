# import pygame
# import pygame_menu
#
# pygame.init()
# surface = pygame.display.set_mode((1280, 720))
#
#
# def set_difficulty(value, difficulty):
#     # Do the job here !
#     pass
#
#
# def start_the_game():
#     # Do the job here !
#     pass
#
#
# menu = pygame_menu.Menu('Welcome', 600, 500,
#                         theme=pygame_menu.themes.THEME_BLUE)
#
# menu.add.text_input('Name :', default='John Doe')
# menu.add.selector('Difficulty :', [('Hard', 1), ('Easy', 2)], onchange=set_difficulty)
# menu.add.button('Play', start_the_game)
# menu.add.button('Quit', pygame_menu.events.EXIT)
# import math
#
#
# def draw_update_function(widget, menu):
#     t = widget.get_attribute('tk', 0)
#     t += menu.get_clock().get_time()
#     widget.set_padding(10 * (1 + math.sin(t)))  # Oscillating padding
#
#
# button = menu.add.button('This button updates its padding', None)
# button.draw(menu)
#
# menu.mainloop(surface)
import inspect
import sys
i = 1
def f1():
    global i
    i+=1
    if i == 98:
        return
    return f2()

def f2():
    global i
    i+=1
    return f3()

def f3():
    global i
    i+=1
    print(f'i={i}', len(inspect.getouterframes(inspect.currentframe())))
    return f1()
sys.setrecursionlimit(100)
# f1()
def f4():
    print(len(inspect.getouterframes(inspect.currentframe())))
    if len(inspect.getouterframes(inspect.currentframe())) + 50 < sys.getrecursionlimit():
        sys.setrecursionlimit(sys.getrecursionlimit() + 50)
    #     print('dfghjk', len(inspect.getouterframes(inspect.currentframe())).__sizeof__())
    return f5()
def f5():
    return f4()
f4()