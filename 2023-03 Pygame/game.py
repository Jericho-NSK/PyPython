from random import randint

from pygame import *

from balls import Ball

init()
time.set_timer(USEREVENT, 1000)

W, H = 800, 600
ball_size = W / 10
FPS = 24
window = display.set_mode((W, H))
display.set_caption("Pet Game")
bg = image.load('Back.png').convert_alpha()
bg = transform.scale(bg, (W, H))


balls = sprite.Group()

images_no_scale = 'Bomb_1.png', 'Bomb_2.png', 'Bomb_3.png'
balls_surf = []
for img in images_no_scale:
    img = image.load(img).convert_alpha()
    img = transform.scale(img, (ball_size, ball_size))
    balls_surf.append(img)


def create_ball(group, size=ball_size):
    index = randint(0, len(balls_surf) - 1)
    x = randint(20, W - 20)
    speed = randint(1, 4)
    return Ball(x, speed, balls_surf[index], group, size)


while True:
    for e in event.get():
        if e.type == QUIT:
            exit()
        elif e.type == USEREVENT:
            create_ball(balls)

    window.blit(bg, (0, 0))
    balls.draw(window)
    display.update()
    time.Clock().tick(FPS)
    balls.update(H, ball_size)
