import pygame_menu


class Menu(pygame_menu.Menu):
    def __init__(self, window):
        super().__init__(title='Welcome',
                         width=400,
                         height=300,
                         theme=pygame_menu.themes.THEME_BLUE)
        self.create_menu()

    def create_menu(self):

        self.add.text_input('Name: ', default='Player')
        self.add.selector(title='Difficulty: ', items=[('Hard', 1), ('Easy', 2)], onchange=self.set_difficulty, style_fancy_arrow_margin=(0,0,0))
        self.add.button('Play', self.start_the_game)
        self.add.button('Quit', pygame_menu.events.EXIT)


    def set_difficulty(self, value, difficulty):
        # Do the job here !
        pass


    def start_the_game(self):
        # Do the job here !
        pass



