import pygame as pg
from nicecolors import *
from random import choice
COLORLIST = [BLACK, PURPLE, WHITE, YELLOW]

def drawTitleText(text):
    myfont = pg.font.SysFont("Comic Sans MS",30)
    textsurface = myfont.render(text, True, BLACK)
    screen.blit(textsurface,(0,0))
    pg.display.update()

def drawRect(color):
    rectangle = pg.rect.Rect(200,200,100,100)
    pg.draw.rect(screen, color, rectangle)
    pg.display.update()

class MovableBlock(object):
    def __init__(self):
        self.rect = pg.draw.rect(screen, BLACK, (200,200,100,100))

    def draw(self,surface):
        pg.draw.rect(screen, BLACK, self.rect)
        pg.display.update()

    def move(self):
        key = pg.key.get_pressed()
        dist = 5

        if key[pg.K_LEFT]:
            screen.fill(WHITE)
            print("left")
            self.rect = self.rect.move(-dist,0)
        if key[pg.K_RIGHT]:
            screen.fill(WHITE)
            print("right")
            self.rect = self.rect.move(dist,0)
        if key[pg.K_UP]:
            screen.fill(WHITE)
            print("up")
            self.rect = self.rect.move(0,-dist)
        if key[pg.K_DOWN]:
            screen.fill(WHITE)
            print("down")
            self.rect = self.rect.move(0,dist)
        self.draw(screen)
        pg.display.update()

pg.init()
pg.display.set_caption("My Game") # window caption
screen = pg.display.set_mode((500,500)) # resolution
screen.fill(WHITE) # bg color
pg.display.update() # apply color change

block = MovableBlock()
block.draw(screen)

# drawTitleText("Rect Color: WHITE")
# drawRect(WHITE)

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            block.move()
        if event.type == pg.QUIT:
            running = False
        # if event.type == pg.MOUSEBUTTONDOWN:
        #     screen.fill(WHITE)
        #     randcolor = choice(COLORLIST)
        #     drawTitleText(f"Rect Color: {randcolor}")
        #     drawRect(randcolor)
        #     pg.display.update()
