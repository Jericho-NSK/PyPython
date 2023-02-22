from inspect  import getouterframes, currentframe
from  sys import exit, getrecursionlimit, setrecursionlimit

import pygame

from bird import Bird
from constants import START_LIVES, START_TRACK, BIRD_START, SPEED
from images_and_sounds import Images
from menus import Menus
from walls import Wall
from window import Window


class Game:
    walls = pygame.sprite.Group()
    lives = START_LIVES
    score = 0

    def __init__(self):
        self.game_starts = False
        self.track = START_TRACK
        self.main_window = Window(self)
        self.bird = Bird()
        self.menu = Menus(self)
        self.menu.call_menu(self)

    def crash(self):
        for wall in self.walls:
            if wall.rect.collidepoint(self.bird.rect.midright) or wall.rect.collidepoint(self.bird.rect.bottomright):
                self.game_starts = False
                self.track = START_TRACK
                self.bird.timer = 0
                self.bird.jump = 0
                self.bird.image = Images.bird_images[-1]
                self.lives -= 1
                self.menu.crash_menu.enable()
            # self.sound_catch.play()

    def new_game(self):
        self.lives = START_LIVES
        self.score = 0
        Wall.speed = SPEED
        self.main_window = Window(self)
        return self.resume_game()

    def resume_game(self):
        self.bird.rect.center = BIRD_START
        self.bird.image = Images.bird_images[0]
        for wall in self.walls:
            wall.kill()
        self.mainloop()

    def mainloop(self):
        self.menu.disable()
        self.game_starts = True
        pygame.time.set_timer(pygame.USEREVENT, 3000 // Wall.speed)
        if len(getouterframes(currentframe())) > getrecursionlimit() - 100:
            setrecursionlimit(getrecursionlimit() + 100)

        while True:
            self.game_starts = True
            for event in pygame.event.get():
                if event.type == pygame.USEREVENT:
                    Wall.create_wall(game=self)
                elif event.type == pygame.QUIT:
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        ...
                    # self.menu.call_menu(self, self.window)  # no pauses, only hardcore!
                    elif event.key == pygame.K_SPACE:
                        self.bird.jump = 35
                    elif event.key == pygame.K_w or event.key == pygame.K_UP:
                        self.bird.jump = 25
            self.walls.update(self)

            self.crash()
            if not self.game_starts:
                self.menu.call_menu(self, crash=True)

            self.main_window.bg_rect.x -= 1
            self.main_window.update_window(self)


Game()
