from random import randint

import pygame

from balls import Ball

WIDTH, HEIGHT = 1280, 720
FPS = 60


class Game:
    window: pygame.Surface
    pygame.init()
    ball_size = 80
    bombs_data = ({'file': 'Bomb_1.png', 'score': 100},
                  {'file': 'Bomb_2.png', 'score': 200},
                  {'file': 'Bomb_3.png', 'score': 300})
    bg = pygame.image.load('back.png')
    main_icon = pygame.image.load('Bomb_3.png')
    cart = pygame.image.load('cart.png')
    title = 'Pet Game'
    cart_speed = 20
    score_font = pygame.font.SysFont('comicsanms', size=48, italic=True)

    def __init__(self):
        self.score_counter = 0
        self.score_text = self.score_font.render(str(self.score_counter), True, 'red')
        self.create_window()
        self.create_cart()
        self.bombs = pygame.sprite.Group()
        self.bombs_images = [pygame.image.load(bomb['file']).convert_alpha() for bomb in self.bombs_data]
        self.mainloop()

    def create_window(self):
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(self.title)
        pygame.display.set_icon(self.main_icon)
        self.bg.convert()
        self.bg = pygame.transform.scale(self.bg, (WIDTH, HEIGHT))

    def create_cart(self):
        self.cart = self.cart.convert_alpha()
        self.cart_rect = self.cart.get_rect(centerx=WIDTH / 2.3, bottom=HEIGHT - 100)

    def create_bomb(self):
        index = randint(0, len(self.bombs_images) - 1)
        x = randint(int(self.ball_size / 2), int(WIDTH - self.ball_size / 2))
        speed = randint(1, 4)
        return Ball(x, speed, self.bombs_images[index], self.bombs_data[index]['score'], self.bombs, self.ball_size)

    def catching_bombs(self):
        for bomb in self.bombs:
            if self.cart_rect.collidepoint(bomb.rect.center):
                self.score_counter += bomb.score
                self.score_text = self.score_font.render(str(self.score_counter), True, 'red')
                bomb.kill()

    def window_updating(self):
        self.catching_bombs()
        self.window.blit(self.bg, (0, 0))
        self.window.blit(self.score_text, (20, 20))
        self.bombs.draw(self.window)
        self.window.blit(self.cart, (self.cart_rect.x, self.cart_rect.y))
        self.bombs.update(HEIGHT, self.ball_size)
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
                    self.create_bomb()
            if game_exit:
                break

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
