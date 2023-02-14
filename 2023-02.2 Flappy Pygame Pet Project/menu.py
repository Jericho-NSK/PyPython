import pygame
import pygame_menu


class Menu(pygame_menu.Menu):
    theme = pygame_menu.themes.THEME_BLUE
    theme.set_background_color_opacity(0.5)

    def __init__(self, game, window):
        super().__init__(title='',
                         width=2 * window.get_rect()[2] // 3,
                         height=2 * window.get_rect()[3] // 3,
                         theme=self.theme)

        self.create_menu(game, window)
        # self.call_menu(game, window)

    def call_menu(self, game, window):

        while True:
            self.enable()
            # game.game_starts = False
            game.update_window()
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

    def create_menu(self, game, window):
        self.add.text_input('Name: ', default='Player')
        self.add.button('Play', game.mainloop)
        self.add.toggle_switch('Full screen', default=pygame.display.is_fullscreen(), onchange=lambda x: pygame.display.toggle_fullscreen())
        # self.add.toggle_switch('Full screen', default=pygame.display.is_fullscreen(), onchange=lambda x: pygame.display.toggle_fullscreen())
        # self.add.toggle_switch('Full screen', default=pygame.display.is_fullscreen(), onchange=lambda x: pygame.display.toggle_fullscreen())


        self.add.button('Quit', pygame_menu.events.EXIT)


