import pygame as pg
from nicecolors import purple

pg.init()
pg.display.set_caption("My Game") # window caption
screen = pg.display.set_mode((500,500)) # resolution
screen.fill(purple) # bg color
pg.display.update() # apply color change

myfont = pg.font.SysFont("Comic Sans MS",30)
text = myfont.render("Hello, World!",True,pg.Color("black"))
textrect = text.get_rect()
textrect.centerx = screen.get_rect().centerx
textrect.centery = screen.get_rect().centery
screen.blit(text, textrect)
pg.display.update()

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
