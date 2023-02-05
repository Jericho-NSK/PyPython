from pygame import *
from Balls import Ball

init()

W, H = 600, 400
FPS = 24
window = display.set_mode((W, H))
display.set_caption("Pet Game")
display.set_icon(image.load('Back.png'))

images = image.load('boom.png').convert_alpha(), image.load('FirstBoom.png').convert_alpha()

balls = sprite.Group()
balls.add()

while True:
    for event in event.get():
        if event.type == QUIT:
            exit()

    balls.draw(window)

    time.Clock().tick(FPS)
