import pygame
import pygame_menu
from webbrowser import open_new_tab

from constants import HEIGHT, WIDTH, FPS


class Menus:
    theme = pygame_menu.themes.THEME_BLUE.copy()
    theme.set_background_color_opacity(0.5)
    theme.widget_font_size = 40
    theme.widget_font_color = 'blue'
    theme.widget_selection_color = 'purple'
    theme.widget_padding = 10

    main_menu = pygame_menu.Menu(title='Main Menu',
                                 width=2 * WIDTH // 3,
                                 height=2 * HEIGHT // 3,
                                 theme=theme,
                                 )
    # main_menu.enable()
    settings_menu = pygame_menu.Menu(title='Settings',
                                     width=2 * WIDTH // 3,
                                     height=2 * HEIGHT // 3,
                                     theme=theme,
                                     )

    about_menu = pygame_menu.Menu(title='About',
                                     width=2 * WIDTH // 3,
                                     height=2 * HEIGHT // 3,
                                     theme=theme,
                                     )
    about_menu = pygame_menu.Menu(title='About',
                                     width=2 * WIDTH // 3,
                                     height=2 * HEIGHT // 3,
                                     theme=theme,
                                     )

    def __init__(self, game):
        self.surface = game.main_window.window
        self.main_menu.add.button('Play', game.mainloop)
        self.main_menu.add.button('Settings', self.settings_menu)
        self.main_menu.add.button('About', self.about_menu)
        self.main_menu.add.button('Exit', pygame_menu.events.EXIT)

        self.settings_menu.add.toggle_switch('Full screen',
                                             default=pygame.display.is_fullscreen(),
                                             onchange=lambda x: pygame.display.toggle_fullscreen(),
                                             )
        self.settings_menu.add.toggle_switch('Music',
                                             default=pygame.display.is_fullscreen(),
                                             onchange=lambda x: pygame.display.toggle_fullscreen(),
                                             )
        self.settings_menu.add.toggle_switch('Sounds',
                                             default=pygame.display.is_fullscreen(),
                                             onchange=lambda x: pygame.display.toggle_fullscreen(),
                                             )
        self.settings_menu.add.button('Back', pygame_menu.events.BACK)

        self.about_menu.add.label('NOT a flappy bird v1.0\nCreated by Jericho for Pet-project', font_color=(0, 135, 0))
        self.about_menu.add.vertical_margin(30)
        self.about_menu.add.button('Link to GitHub', lambda: open_new_tab('https://github.com/Jericho-NSK/PyPython/tree/main/2023-02.2%20Flappy%20Pygame%20Pet%20Project'))
        self.about_menu.add.button('Back', pygame_menu.events.BACK)

    def call_menu(self, game, crash=False):
        while True:
            if crash:
                self.about_menu.update(pygame.event.get())
                self.about_menu.mainloop(self.surface, game.main_window.update_window(game), disable_loop=True, clear_surface=False, fps_limit=FPS)
            else:
                self.main_menu.update(pygame.event.get())
                self.main_menu.mainloop(self.surface, game.main_window.update_window(game), disable_loop=True, clear_surface=False, fps_limit=FPS)

        # while True:
        #     # game.game_starts = False
        #     game.main_window.update_window(game)
            # pygame.display.update()
            # game.walls.draw(window)
            # window.blit(game.score, (20, 20))
            # window.blit(game.bg, (game.bg_rect.x, game.bg_rect.y))
            # window.blit(game.bird.image, (game.bird.rect.centerx, game.bird.rect.centery))
            # game.bird.flying(game)
            #
            # for event in pygame.event.get():
            #
            #     if event.type == pygame.KEYDOWN:
            #         if event.key == pygame.K_ESCAPE:
            #             game.mainloop()
            # if self.is_enabled():
            #     self.update(pygame.event.get())
            # self.draw(window)
            # game.update_window()
            # pygame.display.update()
            # pygame.time.Clock().tick(60)


class CrashMenu(pygame_menu.Menu):
    theme = pygame_menu.themes.THEME_BLUE.copy()
    theme.set_background_color_opacity(0.5)

    def __init__(self, game):
        super().__init__(title='Main Menu',
                         width=2 * WIDTH // 3,
                         height=2 * HEIGHT // 3,
                         theme=self.theme,
                         )
        self.add.button('Continue', self.next_try, game)
        self.add.button('Main Menu', game.menu.call_menu, game)
        self.add.button('Exit', pygame_menu.events.EXIT)

    def next_try(self, game):
        game.mainloop()

    def call_menu(self, game):
        self.enable()
        while True:
            # game.game_starts = False
            game.main_window.update_window(game)
