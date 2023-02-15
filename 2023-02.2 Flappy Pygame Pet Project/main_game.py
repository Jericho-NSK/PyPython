import pygame

from bird import Bird
from consts import HEIGHT, score_font
from menu import Menu
from walls import Wall
from window import Window


class Game:
    walls = pygame.sprite.Group()
    score_text = 0

    def __init__(self):
        self.game_starts = False
        self.score = score_font.render(str(self.score_text), True, 'red')
        self.track = HEIGHT // 2
        self.window = Window()
        self.bird = Bird()
        self.menu = Menu(self)
        self.menu.call_menu(self)

    def crash(self):
        for wall in self.walls:
            if wall.rect.collidepoint(self.bird.rect.midright) or wall.rect.collidepoint(self.bird.rect.bottomright):
                return self.window.end_window(self)
            # self.sound_catch.play()
            # self.score_counter += bomb.score
            # self.score_text = self.score_font.render(str(self.score_counter), True, 'red')
            # wall.kill()

    def mainloop(self):
        self.menu.disable()
        self.game_starts = True
        pygame.time.set_timer(pygame.USEREVENT, 1000)
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
            self.window.update_window(self)


Game()
