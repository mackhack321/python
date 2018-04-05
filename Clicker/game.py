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
        self.candrag = False
        self.maxscore = False
    def setMult(self, newmult):
        self.mult = newmult
    def setScore(self, newscore):
        self.score = newscore
    def addPoints(self, amt):
        if not self.maxscore: self.score += amt
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
        resetChannel.play(resetsound,0)
        self.maxscore = False
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

class Upgrade:
    def __init__(self,name,cost,multupgrade):
        self.name = name
        self.cost = cost
        self.multupgrade = multupgrade
    def buy(self):
        if not player.maxscore:
            if player.score >= self.cost:
                player.setMult(player.mult+self.multupgrade)
                player.subPoints(self.cost)
                playSound("buysound")
                myfont = pg.font.SysFont("Comic Sans MS",30)
                text = myfont.render(f"Bought {self.name}!",True,WHITE)
                screen.blit(text,(350,500))
                pg.display.update()
                sleep(1)

def doClick(mult):
    if pg.mouse.get_pressed()[0]:
        pos = pg.mouse.get_pos()
        if keyboard.rect.collidepoint(pos) == 1:
            playSound("keypress")
            player.addPoints(mult)
            changeMonitorImage()
        if newkeeb.rect.collidepoint(pos) == 1:
            if player.candrag:
                newkeeb.repos(pg.mouse.get_pos()[0],pg.mouse.get_pos()[1])
                print("New Keeb: ",newkeeb.currentx,newkeeb.currenty)
            newkeeb_obj.buy()
        if newide.rect.collidepoint(pos) == 1:
            if player.candrag:
                newide.repos(pg.mouse.get_pos()[0],pg.mouse.get_pos()[1])
                print("New IDE: ",newide.currentx,newide.currenty)
            newide_obj.buy()
        if topkek.rect.collidepoint(pos) == 1:
            if player.candrag:
                topkek.repos(pg.mouse.get_pos()[0],pg.mouse.get_pos()[1])
                print("Topkek: ",topkek.currentx,topkek.currenty)
            topkek_obj.buy()
        if reset.rect.collidepoint(pos) == 1:
            player.reset()

def drawAll():
    background.draw()
    keyboard.draw()
    monitor.draw()
    newkeeb.draw()
    newide.draw()
    topkek.draw()
    upgradebanner.draw()
    instructions.draw()
    reset.draw()
    guido.draw() # this must be last to go over everything else

def playSound(sound):
    if sound == "keypress":
        keyChannel.play(keysound, 0)
    elif sound == "winshutdown":
        shutdownChannel.play(winshutdown, 0)
    elif sound == "bgmusic":
        musicChannel.play(bgmusic, -1)
        musicChannel.set_volume(.25)
    elif sound == "buysound":
        buysoundChannel.play(buysound, 0)

def changeMonitorImage():
    images = ["data/monitor01.png","data/monitor02.png","data/monitor03.png","data/monitor04.png","data/monitor05.png","data/monitor06.png","data/monitor07.png","data/monitorbsod.png"]
    monitor.reImage(choice(images))

def displayPoints(score):
    drawAll()
    myfont = pg.font.SysFont("Impact",30)
    text = myfont.render(f"Name: {player.name}, Lines of Code: {player.score}, Multiplier: {player.mult}",True,WHITE)
    screen.blit(text,(250,0))
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
keyboard.resize(497,202)
keyboard.repos(500,825)
keyboard.draw()

monitor = Sprite("data/monitor00.png")
monitor.resize(716,512)
monitor.repos(500,300)
monitor.draw()

newkeeb = Sprite("data/newkeeb.png")
newkeeb_obj = Upgrade("New Keeb",50,3)
newkeeb.resize(392,100)
newkeeb.repos(238,627)
newkeeb.draw()

newide = Sprite("data/newide.png")
newide_obj = Upgrade("New IDE",150,5)
newide.resize(245,75)
newide.repos(537,620)
newide.draw()

topkek = Sprite("data/topkek.png")
topkek_obj = Upgrade("Topkek",300,10)
topkek.resize(250,82)
topkek.repos(785,615)
topkek.draw()

upgradebanner = Sprite("data/upgradebanner.png")
upgradebanner.resize(782,132)
upgradebanner.repos(500,690)
upgradebanner.draw()

instructions = Sprite("data/instructions.png")
instructions.resize(966,163)
instructions.repos(500,960)
instructions.draw()

reset = Sprite("data/reset.png")
reset.resize(100,100)
reset.repos(75,300)
reset.draw()

guido = Sprite("data/rossum.png")
guido.resize(70,105)
guido.draw()
### Make sound objects and channels, start bg music ###
keysound = pg.mixer.Sound("data/keypress.wav")
winshutdown = pg.mixer.Sound("data/winshutdown.wav")
bgmusic = pg.mixer.Sound("data/music.wav")
buysound = pg.mixer.Sound("data/buysound.wav")
resetsound = pg.mixer.Sound("data/resetsound.wav")
musicChannel = pg.mixer.Channel(0)
keyChannel = pg.mixer.Channel(1)
shutdownChannel = pg.mixer.Channel(2)
buysoundChannel = pg.mixer.Channel(3)
resetChannel = pg.mixer.Channel(4)
playSound("bgmusic")
### Make and get player data ###
player = Player("debug") # EDIT THIS ARGUMENT TO CHANGE PLAYER PROFILE!!!!!
if player.name == "debug": player.candrag = False # CHANGE TO TRUE TO LET debug DRAG UPGRADES
player.loadData(f"players/{player.name}.pkl")
### Game loop ###
running = True
while running:
    if not player.maxscore:
        if player.score > 10000:
            player.maxscore = True
            player.setScore("Way too many")
    displayPoints(player.score)
    guido.repos(pg.mouse.get_pos()[0],pg.mouse.get_pos()[1])
    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT: doQuitSequence()
        if event.type == pg.MOUSEBUTTONDOWN: doClick(player.mult)
