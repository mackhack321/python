import pygame as pg
from nicecolors import *

pg.init()
pg.display.set_caption("Pong")
screen = pg.display.set_mode((500,500))
screen.fill(BLACK)
pg.display.update()
clock = pg.time.Clock()

class Paddle(object):
    def __init__(self, pos):
        if pos == "left":
            self.rect = pg.draw.rect(screen, WHITE, (0,200,20,100))
        elif pos == "right":
            self.rect = pg.draw.rect(screen, WHITE, (480,200,20,100))

    def draw(self):
        pg.draw.rect(screen, WHITE, self.rect)
        pg.display.update()

    def move(self,ychange):
        screen.fill(BLACK)
        rpaddle.draw()
        self.rect.move_ip(0,ychange)
        self.draw()
        pg.display.update()

lpaddle = Paddle(pos="left")
rpaddle = Paddle(pos="right")
lpaddle.draw()
rpaddle.draw()

gameover = False
while not gameover:
    clock.tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            gameover = True
        if event.type == pg.KEYDOWN:
            print(event)
            keys = pg.key.get_pressed()
            if keys[pg.K_UP]:
                print("up")
                #lpaddle.move(-1)
            if keys[pg.K_DOWN]:
                print("down")
                #lpaddle.move(1)
