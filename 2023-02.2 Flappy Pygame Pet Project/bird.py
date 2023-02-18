import pygame

from constants import HEIGHT, WIDTH, FPS, BIRD_SIZE
from images_and_sounds import Images


class Bird(pygame.Surface):
    timer = FPS // 2

    def __init__(self):
        super().__init__(size=BIRD_SIZE)
        self.rect = self.get_rect()
        self.rect.center = WIDTH // 10, HEIGHT // 3
        self.image = Images.bird_images[1]
        self.jump = 0
        self.wings_up = False

    def flying(self, game):
        if self.jump:
            self.rect.centery -= int((0.1 * self.jump) ** 2) - 1
            self.jump -= 1
        if not self.timer:
            self.image = Images.bird_images[self.wings_up]
            self.wings_up = not self.wings_up
            self.timer = FPS // 3
        else:
            self.timer -= 1

        if game.game_starts and not game.menu.main_menu.is_enabled():
            self.rect.centery += 1
            if self.rect.bottom > HEIGHT - self.rect.height // 2:
                self.rect.bottom = HEIGHT - self.rect.height // 2
            if self.rect.top < -self.rect.height // 2:
                self.rect.top = -self.rect.height // 2

            key = pygame.key.get_pressed()
            if (key[pygame.K_a] or key[pygame.K_LEFT]) and self.rect.centerx > 0:
                self.rect.centerx -= 4
            if (key[pygame.K_d] or key[pygame.K_RIGHT]) and self.rect.right < WIDTH - self.rect.width:
                self.rect.centerx += 4
            if key[pygame.K_s] or key[pygame.K_DOWN]:
                self.rect.centery += 1
