import pygame

from bird import Bird
from constants import HEIGHT, START_TRACK, FONT, DIFFICULTY_MODS
from menus import Menus, CrashMenu
from walls import Wall
from window import Window


class Game:
    walls = pygame.sprite.Group()
    # score_text = 0

    def __init__(self):
        self.game_starts = False
        # self.score = FONT.render(str(self.score_text), True, 'red')
        self.track = START_TRACK
        self.main_window = Window()
        self.bird = Bird()
        self.menu = Menus(self)
        self.menu.call_menu(self)
        # self.menu.main_menu.enable()
        # self.crash_menu = CrashMenu(self).disable()
        # self.menu.call_menu(self)

    def crash(self):
        for wall in self.walls:
            if wall.rect.collidepoint(self.bird.rect.midright) or wall.rect.collidepoint(self.bird.rect.bottomright):
                return self.main_window.end_window(self)
            # self.sound_catch.play()
            # self.score_counter += bomb.score
            # self.score_text = self.score_font.render(str(self.score_counter), True, 'red')
            # wall.kill()

    def mainloop(self):
        self.menu.main_menu.disable()
        # self.crash_menu.disable()
        self.game_starts = True
        pygame.time.set_timer(pygame.USEREVENT, 3000 // Wall.speed)
        while True:
            self.game_starts = True
            for event in pygame.event.get():

                if event.type == pygame.USEREVENT:
                    Wall.create_wall(game=self)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        ...
                    # self.menu.call_menu(self, self.window)  # no pauses, only hardcore!
                    elif event.key == pygame.K_SPACE:
                        self.bird.jump = 35
                    elif event.key == pygame.K_w:
                        self.bird.jump = 25
            self.walls.update(self)

            self.crash()
            self.main_window.bg_rect.x -= 1
            self.main_window.update_window(self)


Game()
