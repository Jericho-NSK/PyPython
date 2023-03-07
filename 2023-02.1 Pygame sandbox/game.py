from random import choice

import pygame

from bombs import Bombs

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()

WIDTH, HEIGHT = 1280, 720
# WIDTH, HEIGHT = 1920, 1010
FPS = 60


class Game:
    window: pygame.Surface
    music = 'Chi-Mai', 'Le-Vent-Le-Cri', 'Lonely', 'Memory', 'Requiem'
    title = 'Pet Game'
    bg = pygame.image.load('images/back.png')
    main_icon = pygame.image.load('images/Bomb_3.png')
    cart = pygame.image.load('images/cart.png')
    cart_speed = 20
    score_font = pygame.font.SysFont('comicsanms', size=48, italic=True)

    def __init__(self):
        self.score_counter = 0
        self.score_text = self.score_font.render(str(self.score_counter), True, 'red')
        self.sound_catch = pygame.mixer.Sound('sounds/catch.ogg')
        self.create_window()
        self.bombs_images = [pygame.image.load('images/' + bomb['file'] + '.png').convert_alpha() for bomb in Bombs.bombs_data]
        self.create_cart()
        self.create_music()
        self.mainloop()

    def create_music(self):
        pygame.mixer.music.load('music/' + choice(self.music) + '.ogg')
        pygame.mixer.music.set_volume(0.15)
        pygame.mixer.music.play(loops=0, fade_ms=5000)

    def create_window(self):
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(self.title)
        pygame.display.set_icon(self.main_icon)
        self.bg.convert()
        self.bg = pygame.transform.scale(self.bg, (WIDTH, HEIGHT))

    def create_cart(self):
        self.cart = self.cart.convert_alpha()
        self.cart_rect = self.cart.get_rect(centerx=WIDTH / 2.3, bottom=HEIGHT - 100)

    def catching_bombs(self):
        for bomb in Bombs.bombs:
            if self.cart_rect.collidepoint(bomb.rect.center):
                self.sound_catch.play()
                self.score_counter += bomb.score
                self.score_text = self.score_font.render(str(self.score_counter), True, 'red')
                bomb.kill()

    def window_updating(self):
        self.catching_bombs()
        self.window.blit(self.bg, (0, 0))
        Bombs.bombs.draw(self.window)
        self.window.blit(self.score_text, (20, 20))
        self.window.blit(self.cart, (self.cart_rect.x, self.cart_rect.y))
        Bombs.bombs.update(HEIGHT, Bombs.bomb_size)
        pygame.display.flip()
        pygame.time.Clock().tick(FPS)

    def mainloop(self):
        game_exit = False
        pygame.time.set_timer(pygame.USEREVENT, 1000)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True
                elif event.type == pygame.USEREVENT:
                    Bombs.create_bomb(window=self, width=WIDTH)
            if game_exit:
                break

            if not pygame.mixer.music.get_busy():
                self.create_music()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_a]:
                self.cart_rect.x += - self.cart_speed
                if self.cart_rect.x <= 0:
                    self.cart_rect.x = 0
            elif keys[pygame.K_d]:
                self.cart_rect.x += self.cart_speed
                if self.cart_rect.x + self.cart_rect.width >= WIDTH:
                    self.cart_rect.x = WIDTH - self.cart_rect.width

            self.window_updating()


if __name__ == '__main__':
    Game()
