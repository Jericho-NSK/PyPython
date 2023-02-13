import pygame
import pygame_menu

pygame.init()
surface = pygame.display.set_mode((1280, 720))


def set_difficulty(value, difficulty):
    # Do the job here !
    pass


def start_the_game():
    # Do the job here !
    pass


menu = pygame_menu.Menu('Welcome', 600, 500,
                        theme=pygame_menu.themes.THEME_BLUE)

menu.add.text_input('Name :', default='John Doe')
menu.add.selector('Difficulty :', [('Hard', 1), ('Easy', 2)], onchange=set_difficulty)
menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)
import math


def draw_update_function(widget, menu):
    t = widget.get_attribute('tk', 0)
    t += menu.get_clock().get_time()
    widget.set_padding(10 * (1 + math.sin(t)))  # Oscillating padding


button = menu.add.button('This button updates its padding', None)
button.draw(menu)

menu.mainloop(surface)
