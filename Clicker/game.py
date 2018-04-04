import pygame as pg
from sys import exit
from nicecolors import *
import pickle as pkl

pg.init()
pg.display.set_caption("Software Developer Simulator 1989")
screen = pg.display.set_mode((500,500))
pg.display.update()

class Sprite(object):
    def __init__(self, filepath):
        self.image = pg.image.load(filepath)
        self.rect = self.image.get_rect()
    def resize(self, l, w):
        self.image = pg.transform.scale(self.image, (l,w))
        self.rect = self.image.get_rect()
    def repos(self, centerx, centery):
        self.rect.centerx = centerx
        self.rect.centery = centery
    def draw(self):
        screen.blit(self.image,self.rect)
    pg.display.update()

class Score:
    def __init__(self, points):
        try:
            if points > 0:
                self.points = points
            else:
                self.points = 0
        except: self.points = 0
    def add(self, amt):
        self.points += amt
    def subtract(self,amt):
        self.points -= amt

def doClick():
    pos = pg.mouse.get_pos()
    if keyboard.rect.collidepoint(pos) == 1: points.add(1); print(points.points)

def displayPoints(score):
    background.draw()
    keyboard.draw()
    myfont = pg.font.SysFont("Comic Sans MS",30)
    text = myfont.render(f"Score: {score}",True,WHITE)
    screen.blit(text,(0,0))
    pg.display.update()

def loadData(filename):
    try:
        playerdata = pkl.load(open(filename,"rb"))
        score = playerdata["score"]
        return score
    except:
        pass

def saveData(score, filename):
    playerdata = {"score":score}
    pkl.dump(playerdata, open(filename,"wb"))

background = Sprite("data/background.jpg")
background.resize(500,500)
background.draw()

keyboard = Sprite("data/keyboard.png")
keyboard.resize(443,180)
keyboard.repos(250,400)
keyboard.draw()

quit = False
points = Score(loadData("player.pkl"))
while not quit:
    displayPoints(points.points)
    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT: saveData(points.points, "player.pkl"); pg.quit(); exit()
        if event.type == pg.MOUSEBUTTONDOWN: doClick()
