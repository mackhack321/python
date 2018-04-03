import pygame as pg
from nicecolors import purple

pg.init()
pg.display.set_caption("My Game")
screen = pg.display.set_mode((500,500))
screen.fill(purple)
pg.display.update()

#pg.rect.Rect(screen, pg.color.Color("black"), (200,200,100,100),0)
rectangle = pg.rect.Rect(200,200,100,100)
pg.draw.rect(rectangle)
pg.display.update()

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEBUTTONDOWN:
            print("mouse down")
