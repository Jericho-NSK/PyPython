import pygame
import pygame_menu

from constants import HEIGHT, WIDTH, FPS


class Menus:
    main_theme = pygame_menu.themes.THEME_BLUE.copy()
    main_theme.set_background_color_opacity(0.5)
    main_menu = pygame_menu.Menu(title='Main Menu',
                                 width=2 * WIDTH // 3,
                                 height=2 * HEIGHT // 3,
                                 theme=main_theme,
                                 )

    def __init__(self, game):
        self.surface = game.main_window.window
        self.main_menu.add.button('Play', game.mainloop)
        self.main_menu.add.toggle_switch('Full screen', default=pygame.display.is_fullscreen(), onchange=lambda x: pygame.display.toggle_fullscreen())
        self.main_menu.add.button('Exit', pygame_menu.events.EXIT)

    # theme = pygame_menu.themes.THEME_BLUE.copy()
    # theme.set_background_color_opacity(0.5)
    #
    # def __init__(self, game):
    #     super().__init__(title='Main Menu',
    #                      width=2 * WIDTH // 3,
    #                      height=2 * HEIGHT // 3,
    #                      theme=self.theme,
    #                      )
    #     self.add.button('Play', game.mainloop)
    #     self.add.toggle_switch('Full screen', default=pygame.display.is_fullscreen(), onchange=lambda x: pygame.display.toggle_fullscreen())
    #     self.add.button('Exit', pygame_menu.events.EXIT)

    def call_menu(self, game):
        while True:
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
