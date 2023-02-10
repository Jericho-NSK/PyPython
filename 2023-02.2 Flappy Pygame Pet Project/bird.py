import pygame


class Bird(pygame.Surface):
    size = 40, 30
    images = 'bird_up.png', 'bird_down.png', 'bird_crash.png'

    timer = 30

    def __init__(self, window, width, height):
        super().__init__(size=self.size)
        self.rect = self.get_rect()
        self.rect.center = width // 10, height // 3
        self.image = window.bird_images[1]
        self.jump = 0
        self.wings_up = 0

    def flying(self, window, FPS, width=None, height=None):
        if self.jump:
            self.rect.centery -= int((0.1 * self.jump) ** 2) - 1
            self.jump -= 1
        if not self.timer:
            self.image = window.bird_images[self.wings_up]
            self.wings_up = not self.wings_up
            self.timer = FPS // 4
        else:
            self.timer -= 1

        if window.game_starts:
            self.rect.centery += 1
            if self.rect.centery > height - height / 24:
                window.end_window()
            if self.rect.centery < 0:
                self.rect.centery = 0

            key = pygame.key.get_pressed()
            if (key[pygame.K_a] or key[pygame.K_LEFT]) and self.rect.centerx > 0:
                self.rect.centerx -= 2
            if (key[pygame.K_d] or key[pygame.K_RIGHT]) and self.rect.right < width - self.rect.width:
                self.rect.centerx += 2
