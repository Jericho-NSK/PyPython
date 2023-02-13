import pygame
import pygame_menu


class Menu(pygame_menu.Menu):
    theme = pygame_menu.themes.THEME_BLUE
    theme.set_background_color_opacity(0.5)

    def __init__(self, game, window):
        super().__init__(title='Welcome',
                         width=2 * window.get_rect()[2] // 3,
                         height=2 * window.get_rect()[3] // 3,
                         theme=self.theme)

        self.create_menu(game, window)

    @staticmethod
    def qwerty(*args):
        print(1, args)

    def create_menu(self, game, window):
        self.add.text_input('Name: ', default='Player')
        self.add.button('Play', game.mainloop, align='align-left')
        self.add.toggle_switch('Full screen', default=pygame.display.is_fullscreen(), onchange=lambda x: pygame.display.toggle_fullscreen())
        # self.add.toggle_switch('Full screen', default=pygame.display.is_fullscreen(), onchange=lambda x: pygame.display.toggle_fullscreen())
        # self.add.toggle_switch('Full screen', default=pygame.display.is_fullscreen(), onchange=lambda x: pygame.display.toggle_fullscreen())


        self.add.button('Quit', pygame_menu.events.EXIT)

    #
    # def mainloop(self, window):
    #     print(window)
    #     # window.mainloop()

    def set_difficulty(self, value, difficulty):
        # Do the job here !
        pass

    def start_the_game(self, window): ...
    # Do the job here !
    # if self:
    #     return window.start_window()
