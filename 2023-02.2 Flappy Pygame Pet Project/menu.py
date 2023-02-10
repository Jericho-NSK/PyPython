import pygame_menu


class Menu(pygame_menu.Menu):
    theme = pygame_menu.themes.THEME_BLUE
    theme.set_background_color_opacity(0.5)

    def __init__(self, window):
        super().__init__(title='Welcome',
                         width=2 * window.window.get_rect()[2] // 3,
                         height=2 * window.window.get_rect()[3] // 3,
                         theme=self.theme)
        self.create_menu(window)

    def create_menu(self, window):

        self.add.text_input('Name: ', default='Player')
        label = self.add.label('Window mode: ')
        label_rect = label.get_rect()
        # print(label_rect)
        screen_mode = self.add.selector(title='Mode: ', items=[('Window', 1), ('Full screen', 2)], onchange=self.set_difficulty)
        screen_mode_rect = screen_mode.get_rect()
        print(screen_mode_rect.x)
        screen_mode_rect.x = 600
        screen_mode.set_position(2000, 400)
        screen_mode_rect.y = label_rect.y + label_rect.h

        print(screen_mode_rect.x)
        screen_mode.set_alignment('align-left')
        screen_mode.set_sformat('{0} {1}')
        # print(pygame_menu.locals)
        # [print(i) for i in dir(a) if not i.startswith('__')]
        self.add.button('Play', self.start_the_game(window))
        self.add.button('Quit', pygame_menu.events.EXIT)

    #
    # def mainloop(self):
    #     super().mainloop()


    def set_difficulty(self, value, difficulty):
        # Do the job here !
        pass

    def start_the_game(self, window):...
        # Do the job here !
        # if self:
        #     return window.start_window()



