# DISCLAIMER: Atom makes this code look a lot nicer, IDLE is ugly
import pygame as pg # duh
from sys import exit, argv # exit lets us kill python, argv gives us CLI arg access
from nicecolors import * # my homemade library for common color constants
import pickle as pkl # used to save and load playerdata
from random import choice, randint # choice picks a random monitor image, randint determines whether or not the gambler plays
from time import sleep # general purpose
import textbox as tb # developer console
### Initialize Pygame, make window ###
pg.init()
pg.display.set_caption("Software Developer Simulator 1989")
screen = pg.display.set_mode((1000,1000))
clock = pg.time.Clock() # fps counter
pg.display.update() # show screen
pg.mouse.set_visible(False) # hide cursor, will be replaced by guido
### Set up classes and functions ###
class Player():
    def __init__(self, name): # build player vars with default vals
        self.name = name
        self.mult = 1
        self.score = 0
        self.candrag = False
        self.maxscore = False
        self.hasConsole = False
    def setMult(self, newmult):
        self.mult = newmult
    def setScore(self, newscore):
        self.score = newscore
    def addPoints(self, amt):
        if not self.maxscore: self.score += amt
    def subPoints(self,amt):
        self.score -= amt
    def loadData(self, filename): # load playerdata from pickle file
        try:
            data = pkl.load(open(filename,"rb"))
            self.setScore(data["score"])
            self.setMult(data["mult"])
            self.maxscore = data["hasmax"]
        except: pass
    def saveData(self,filename): # builds a dict with player data, dumps to YourName.meme
        pkl.dump({"score":self.score, "mult":self.mult, "hasmax":self.maxscore}, open(filename,"wb"))
    def reset(self): # start player back at 0
        resetChannel.play(resetsound,0)
        self.maxscore = False
        self.mult = 1
        self.score = 0

class Sprite(object):
    def __init__(self, filepath): # build sprite vars
        self.current_image = filepath
        self.image = pg.image.load(filepath)
        self.rect = self.image.get_rect()
    def reImage(self, filepath): # change image of sprite, same pos and size
        self.current_image = filepath
        self.image = pg.image.load(filepath)
        self.rect = self.image.get_rect()
        self.resize(self.scale[0],self.scale[1])
        self.repos(self.currentx,self.currenty)
    def resize(self, l, w): # change sprite scale
        self.scale = (l,w)
        self.image = pg.transform.scale(self.image, (l,w))
        self.rect = self.image.get_rect()
    def repos(self, centerx, centery): # change pos, uses center coords
        self.rect.centerx = self.currentx = centerx
        self.rect.centery = self.currenty = centery
    def draw(self): # draw to screen
        screen.blit(self.image,self.rect)

class Upgrade:
    def __init__(self,name,cost,multupgrade): # build upgrade object and vars
        self.name = name
        self.cost = cost
        self.multupgrade = multupgrade
    def buy(self):
        if not player.maxscore: # if player hasn't hit the max score
            if player.score >= self.cost: # if player has enough points
                player.setMult(player.mult+self.multupgrade) # add to multiplier
                player.subPoints(self.cost) # take away cost
                playSound("buysound") # cha ching!
                myfont = pg.font.SysFont("Comic Sans MS",30) # make font var
                text = myfont.render(f"Bought {self.name}!",True,WHITE) # make purchase confirmation text
                screen.blit(text,(350,500)) # put text on screen surface
                pg.display.update() # show it to the user
                sleep(1) # pause, then get rid of the purchase text

def doClick(mult):
    if pg.mouse.get_pressed()[0] or keydown: # if mouse is clicked or any key is pressed
        pos = pg.mouse.get_pos() # get mouse pos
        if keyboard.rect.collidepoint(pos) == 1 or keydown: # if click on keyboard or any key is pressed
            playSound("keypress") # play keypress sound
            player.addPoints(mult) # add (1xMultiplier) to score
            changeMonitorImage() # change monitor image
        if newkeeb.rect.collidepoint(pos) == 1 and not keydown: # if click on new keyboard and no key is pressed
            if player.candrag: # just ask mack what this does
                newkeeb.repos(pg.mouse.get_pos()[0],pg.mouse.get_pos()[1]) # still, ask mack
                print("New Keeb: ",newkeeb.currentx,newkeeb.currenty) # no really, ask mack
            newkeeb_obj.buy() # buy new keyboard upgrade
        if newide.rect.collidepoint(pos) == 1 and not keydown: # if click on new ide and no key is pressed
            if player.candrag: # again, ask mack
                newide.repos(pg.mouse.get_pos()[0],pg.mouse.get_pos()[1]) # likewise, ask mack
                print("New IDE: ",newide.currentx,newide.currenty) # please, just ask mack
            newide_obj.buy() # buy new ide upgrade
        if topkek.rect.collidepoint(pos) == 1 and not keydown: # if click on topkek and no key is pressed
            if player.candrag: # you know the drill
                topkek.repos(pg.mouse.get_pos()[0],pg.mouse.get_pos()[1]) # mack will tell you
                print("Topkek: ",topkek.currentx,topkek.currenty) # it's too long of an explanation to commentate
            topkek_obj.buy() # buy topkek upgrade
        if reset.rect.collidepoint(pos) == 1 and not keydown: # if click on reset and no key is pressed
            player.reset() # reset player data

def drawAll(): # draw every sprite back onto the screen
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

def playSound(sound): # this function is used all over the place
    if sound == "keypress": # if you wanna play the key sound
        keyChannel.play(keysound, 0) # play the key sound
    elif sound == "winshutdown": # if you wanna play the shutdown sound
        shutdownChannel.play(winshutdown, 0) # play the shutdown sound
    elif sound == "bgmusic": # if you wanna play the background music
        musicChannel.play(bgmusic, -1) # play the background music ON REPEAT (-1)
        musicChannel.set_volume(.25) # turn down the volume or else it's too heckin loud
    elif sound == "buysound": # if you wanna play the cha ching sound
        buysoundChannel.play(buysound, 0) # play the cha ching sound

def changeMonitorImage(): # pick random monitor image out of list, set monitor picture to that random selection
    images = [
    "data/monitors/monitor01.png","data/monitors/monitor02.png","data/monitors/monitor03.png",
    "data/monitors/monitor04.png","data/monitors/monitor05.png","data/monitors/monitor06.png",
    "data/monitors/monitor07.png","data/monitors/monitor08.png","data/monitors/monitor09.png"
    ]
    monitor.reImage(choice(images))

def displayPoints(score): # displays more than points now, too lazy to change func name
    drawAll() # draw all sprites
    fpsfont = pg.font.SysFont("Comic Sans MS", 25) # make font
    fps = fpsfont.render(f"FPS: {str(int(clock.get_fps()))}", True, YELLOW) # show fps counter
    myfont = pg.font.SysFont("Impact",30) # make font
    text = myfont.render(f"Name: {player.name}, Lines of Code: {player.score}, Multiplier: {player.mult}",True,WHITE) # display player data
    screen.blit(text,(250,0)) # put player data on screen surface
    screen.blit(fps, (0,0)) # put fps counter on screen surface
    pg.display.update() # let user see the above text

def console():
    if player.hasConsole:
        command = tb.ask(screen, "> ")
        exec(command)

def doQuitSequence(): # gets run when you try to close the game
    musicChannel.fadeout(500) # fancy background music fadeout
    playSound("winshutdown") # play the windows shutdown sound
    sleep(2) # pause so it can play
    player.saveData(f"players/{player.name}.meme") # dump player data
    pg.quit() # kill pygame
    exit() # kill python
### Make Sprites ###
background = Sprite("data/sprites/background.jpg")
background.resize(1000,1000)
background.draw()

keyboard = Sprite("data/sprites/keyboard.png")
keyboard.resize(497,202)
keyboard.repos(500,825)
keyboard.draw()

monitor = Sprite("data/monitors/monitor00.png")
monitor.resize(716,512)
monitor.repos(500,300)
monitor.draw()

newkeeb = Sprite("data/sprites/newkeeb.png")
newkeeb_obj = Upgrade("New Keeb",50,3)
newkeeb.resize(392,100)
newkeeb.repos(238,627)
newkeeb.draw()

newide = Sprite("data/sprites/newide.png")
newide_obj = Upgrade("New IDE",150,5)
newide.resize(245,75)
newide.repos(537,620)
newide.draw()

topkek = Sprite("data/sprites/topkek.png")
topkek_obj = Upgrade("Topkek",300,10)
topkek.resize(250,82)
topkek.repos(785,615)
topkek.draw()

upgradebanner = Sprite("data/sprites/upgradebanner.png")
upgradebanner.resize(782,132)
upgradebanner.repos(500,690)
upgradebanner.draw()

instructions = Sprite("data/sprites/instructions.png")
instructions.resize(966,163)
instructions.repos(500,960)
instructions.draw()

reset = Sprite("data/sprites/reset.png")
reset.resize(100,100)
reset.repos(75,300)
reset.draw()

guido = Sprite("data/sprites/rossum.png")
guido.resize(70,105)
guido.draw()
### Make sound objects and channels, start bg music ###
keysound = pg.mixer.Sound("data/sounds/keypress.wav")
winshutdown = pg.mixer.Sound("data/sounds/winshutdown.wav")
if randint(1,5) == 3: bgmusic = pg.mixer.Sound("data/sounds/gambler.wav") # 1/5 chance that Kenny Rogers's The Gambler plays as background music
else: bgmusic = pg.mixer.Sound("data/sounds/music.wav") # do regular music if you don't get the 1/5 chance
buysound = pg.mixer.Sound("data/sounds/buysound.wav")
resetsound = pg.mixer.Sound("data/sounds/resetsound.wav")
musicChannel = pg.mixer.Channel(0)
keyChannel = pg.mixer.Channel(1)
shutdownChannel = pg.mixer.Channel(2)
buysoundChannel = pg.mixer.Channel(3)
resetChannel = pg.mixer.Channel(4)
playSound("bgmusic") # start background music
### Make and get player data ###
try: player = Player(argv[1]) # check for name arg, make new player object
except: print("FATAL: Name argument not found"); exit() # happens when you don't give a name in the CLI args
if player.name == "debug": player.candrag = False # please... just ask mack...
if player.name == "Mack": player.hasConsole = True # let mack use the dev con
player.loadData(f"players/{player.name}.meme") # load playerdata from PlayerName.meme
### Game loop ###
running = True # yes, the game is running
while running: # while the game is running
    if not player.maxscore: # if the player hasn't hit the max score
        if player.score > 100000: # if the player's score is over the max
            player.maxscore = True # say the player hit the max
            player.setScore("Way too many") # set score to way too many
    displayPoints(player.score) # show playerdata and other stuff
    guido.repos(pg.mouse.get_pos()[0],pg.mouse.get_pos()[1]) # move guido head to cursor
    pg.display.update() # show guido head movement
    keydown = False
    for event in pg.event.get(): # for everything you can possibly do
        if event.type == pg.QUIT: doQuitSequence() # if you're trying to quit, run the quit sequence
        if event.type == pg.MOUSEBUTTONDOWN: doClick(player.mult) # if you're clicking, do the click func
        if event.type == pg.KEYDOWN and event.key != pg.K_RETURN and event.key != pg.K_BACKQUOTE: keydown = True; doClick(player.mult) # if you're typing, do the click func but keydown is True
        if event.type == pg.KEYDOWN and event.key == pg.K_BACKQUOTE: console() # open console if you push ~
    clock.tick(30) # set fps (i think pygame caps at 30)
# add it all together and you get a game-of-the-year worthy product
# dlc coming soon
# purchase upgraded code commentary from the app store for $9.99
# omg i just realized that github is like soundcloud for programmers
# like "guys go check out my github, i just dropped a fire program"
# ---> github.com/mackhack321/Python <---
# link and build?
# shoutout to stackoverflow for making it look like i have a clue what im doing
# shoutout to guido van rossum for letting me turn his head into a cursor
# oh wait i didnt ask lol
# so this the end of the program
# my "big final project"
# ive never spent so much effort on a meme in my life
# k bye
