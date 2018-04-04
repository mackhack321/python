import pygame as pg
from sys import exit
from nicecolors import *
import pickle as pkl
from random import choice
from time import sleep

pg.init()
pg.display.set_caption("Software Developer Simulator 1989")
screen = pg.display.set_mode((500,500))
pg.display.update()

class Sprite(object):
    def __init__(self, filepath):
        self.current_image = filepath
        self.image = pg.image.load(filepath)
        self.rect = self.image.get_rect()
    def reImage(self, filepath):
        self.current_image = filepath
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
    if keyboard.rect.collidepoint(pos) == 1:
        playSound("keypress")
        points.add(1)
        changeMonitorImage()

def drawAll():
    background.draw()
    keyboard.draw()
    monitor.draw()

def playSound(sound):
    if sound == "keypress":
        pg.mixer.music.load("data/keypress.wav")
        pg.mixer.music.play(0)
    elif sound == "winshutdown":
        pg.mixer.music.load("data/winshutdown.wav")
        pg.mixer.music.play(0)

def changeMonitorImage():
    images = ["data/monitor01.png","data/monitor02.png","data/monitor03.png"]
    monitor.reImage(choice(images))
    monitor.resize(358,256)
    monitor.repos(250,150)
    monitor.draw()

def displayPoints(score):
    drawAll()
    myfont = pg.font.SysFont("Impact",30)
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

def doQuitSequence():
    playSound("winshutdown")
    sleep(2)
    saveData(points.points, "playerdata.pkl")
    pg.quit()
    exit()

background = Sprite("data/background.jpg")
background.resize(500,500)
background.draw()

keyboard = Sprite("data/keyboard.png")
keyboard.resize(497,202)
keyboard.repos(250,400)
keyboard.draw()

monitor = Sprite("data/monitor00.png")
monitor.resize(358,256)
monitor.repos(250,150)
monitor.draw()

quit = False
points = Score(loadData("playerdata.pkl"))
while not quit:
    displayPoints(points.points)
    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT: doQuitSequence()
        if event.type == pg.MOUSEBUTTONDOWN: doClick()
