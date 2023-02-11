import pygame_menu
import pygame


class Menu(pygame_menu.Menu):
    theme = pygame_menu.themes.THEME_BLUE
    theme.set_background_color_opacity(0.5)

    def __init__(self, game, window):
        super().__init__(title='Welcome',
                         width=2 * window.get_rect()[2] // 3,
                         height=2 * window.get_rect()[3] // 3,
                         theme=self.theme)

        self.create_menu(game, window)

    def create_menu(self, game, window):

        self.add.text_input('Name: ', default='Player')
        full_screen = self.add.toggle_switch('Full screen', default=pygame.display.is_fullscreen())


        self.add.button('Play', game.mainloop)
        self.add.button('Quit', pygame_menu.events.EXIT)

    #
    # def mainloop(self, window):
    #     print(window)
    #     # window.mainloop()


    def set_difficulty(self, value, difficulty):
        # Do the job here !
        pass

    def start_the_game(self, window):...
        # Do the job here !
        # if self:
        #     return window.start_window()



