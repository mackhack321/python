import pygame as pg
from sys import exit
from nicecolors import *
import pickle as pkl
from random import choice
from time import sleep
### Initialize Pygame, make window ###
pg.init()
pg.display.set_caption("Software Developer Simulator 1989")
screen = pg.display.set_mode((1000,1000))
pg.display.update()
pg.mouse.set_visible(False)
### Set up classes and functions ###
class Player():
    def __init__(self, name):
        self.name = name
        self.mult = 1
        self.score = 0
    def setMult(self, newmult):
        self.mult = newmult
    def setScore(self, newscore):
        self.score = newscore
    def addPoints(self, amt):
        self.score += amt
    def subPoints(self,amt):
        self.score -= amt
    def loadData(self, filename):
        try:
            data = pkl.load(open(filename,"rb"))
            self.setScore(data["score"])
            self.setMult(data["mult"])
        except: pass
    def saveData(self,filename):
        pkl.dump({"score":self.score, "mult":self.mult}, open(filename,"wb"))
    def reset(self):
        self.mult = 1
        self.score = 0

class Sprite(object):
    def __init__(self, filepath):
        self.current_image = filepath
        self.image = pg.image.load(filepath)
        self.rect = self.image.get_rect()
    def reImage(self, filepath):
        self.current_image = filepath
        self.image = pg.image.load(filepath)
        self.rect = self.image.get_rect()
        self.resize(self.scale[0],self.scale[1])
        self.repos(self.currentx,self.currenty)
    def resize(self, l, w):
        self.scale = (l,w)
        self.image = pg.transform.scale(self.image, (l,w))
        self.rect = self.image.get_rect()
    def repos(self, centerx, centery):
        self.rect.centerx = self.currentx = centerx
        self.rect.centery = self.currenty = centery
    def draw(self):
        screen.blit(self.image,self.rect)
    pg.display.update()

def doClick(mult):
    pos = pg.mouse.get_pos()
    if keyboard.rect.collidepoint(pos) == 1:
        playSound("keypress")
        player.addPoints(mult)
        changeMonitorImage()

def drawAll():
    background.draw()
    keyboard.draw()
    monitor.draw()
    guido.draw()
    newkeeb.draw()

def playSound(sound):
    if sound == "keypress":
        keyChannel.play(keysound, 0)
    elif sound == "winshutdown":
        shutdownChannel.play(winshutdown, 0)
    elif sound == "bgmusic":
        musicChannel.play(bgmusic, -1)
        musicChannel.set_volume(.25)

def changeMonitorImage():
    images = ["data/monitor01.png","data/monitor02.png","data/monitor03.png"]
    monitor.reImage(choice(images))

def displayPoints(score):
    drawAll()
    myfont = pg.font.SysFont("Impact",30)
    text = myfont.render(f"Name: {player.name}, Score: {player.score}, Mult: {player.mult}",True,WHITE)
    screen.blit(text,(0,0))
    pg.display.update()

def doQuitSequence():
    musicChannel.fadeout(500)
    playSound("winshutdown")
    sleep(2)
    player.saveData(f"players/{player.name}.pkl")
    pg.quit()
    exit()
### Make Sprites ###
background = Sprite("data/background.jpg")
background.resize(1000,1000)
background.draw()

keyboard = Sprite("data/keyboard.png")
keyboard.resize(994,404)
keyboard.repos(500,800)
keyboard.draw()

monitor = Sprite("data/monitor00.png")
monitor.resize(716,512)
monitor.repos(500,300)
monitor.draw()

guido = Sprite("data/rossum.png")
guido.resize(70,105)
guido.draw()

newkeeb = Sprite("data/newkeeb.png")
newkeeb.resize(392,100)
newkeeb.repos(500,500)
newkeeb.draw()
### Make sound objects and channels, start bg music ###
keysound = pg.mixer.Sound("data/keypress.wav")
winshutdown = pg.mixer.Sound("data/winshutdown.wav")
bgmusic = pg.mixer.Sound("data/music.wav")
musicChannel = pg.mixer.Channel(0)
keyChannel = pg.mixer.Channel(1)
shutdownChannel = pg.mixer.Channel(2)
playSound("bgmusic")
### Make and get player data ###
player = Player("debug") # EDIT THIS ARGUMENT TO CHANGE PLAYER PROFILE!!!!!
player.loadData(f"players/{player.name}.pkl")
if player.name == "debug": print("Debugging!"); player.setMult(10)
### Game loop ###
running = True
while running:
    displayPoints(player.score)
    guido.repos(pg.mouse.get_pos()[0],pg.mouse.get_pos()[1])
    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT: doQuitSequence()
        if event.type == pg.MOUSEBUTTONDOWN: doClick(player.mult)
