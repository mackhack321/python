from graphics import * #used for everything
from time import * #used for the flickering
import random #randomizes flickering
import math #needed for distance formula, see the def statement for checkPt()
#make window
win = GraphWin("Super Spooky Jack-O-Lantern Maker",500,500)
win.setBackground("#000000")
#make pumpkin and get name
pumpkin = Circle(Point(250,250),200)
pumpkin.setFill("#ed7c0b")
pumpkin.draw(win)
#func to check if point is in circle
def checkPt(pt,circle):
    global good
    dx = pt.getX() - circle.getCenter().getX()
    dy = pt.getY() - circle.getCenter().getY()
    dist = math.sqrt(dx**2+dy**2)
    if dist <= circle.getRadius():
        good = True
    else:
        good = False
#func to make eyes
def triDraw(seq):
    global tri
    points = []
    triText = Text(Point(250,10),f"Click at three points to make the {seq} eye")
    triText.setFill("#ed7c0b")
    triText.draw(win)
    while len(points) < 3:
        pt = win.getMouse()
        checkPt(pt,pumpkin)
        if good is True:
            pass
        elif good is False:
            badPt = Text(Point(250,10),"Please make your points on the pumpkin, not the void")
            badPt.setFill("#ed7c0b")
            triText.undraw()
            badPt.draw(win)
            sleep(2)
            badPt.undraw()
            triText.draw(win)
            continue
        points.append(pt)
        pt.draw(win)
        tri = Polygon(points)
        tri.setFill("#f4c22c")
        tri.draw(win)
    triText.undraw()
#draw eyes
triDraw("first")
tri.undraw()
triOne = tri.clone()
triOne.draw(win)

triDraw("second")
tri.undraw()
triTwo = tri.clone()
triTwo.draw(win)
#mouth
mouthText = Text(Point(250,10),"Click and hit enter before you make the final point to make the mouth")
mouthText.setFill("#ed7c0b")
mouthText.draw(win)
points = []
key = False
points = []
while key != "Return":
    pt = win.getMouse()
    checkPt(pt,pumpkin)
    if good is True:
        pass
    elif good is False:
        badPt = Text(Point(250,10),"Please make your points on the pumpkin, not the void")
        badPt.setFill("#ed7c0b")
        mouthText.undraw()
        badPt.draw(win)
        sleep(2)
        badPt.undraw()
        mouthText.draw(win)
        continue
    points.append(pt)
    key = win.checkKey()
    pt.draw(win)
    line = Line(points[len(points)-1],points[len(points)-2])
    line.draw(win)
mouth = Polygon(points)
mouth.setFill("#f4c22c")
mouth.draw(win)
mouse = None
mouthText.undraw()
#happy halloween, click to exit
halloweenText = Text(Point(250,10),"Happy (late) Halloween!")
halloweenText.setFill("#ed7c0b")
halloweenText.setStyle("bold italic")
halloweenText.setSize(18)
halloweenText.draw(win)

exitText = Text(Point(250,490),"Click anywhere to exit")
exitText.setFill("#ed7c0b")
exitText.draw(win)
#flickering
while mouse is None:
    rand = random.uniform(.05,.4)
    triOne.setFill("#d8a611")
    triTwo.setFill("#d8a611")
    mouth.setFill("#d8a611")
    sleep(rand)
    triOne.setFill("#f4c22c")
    triTwo.setFill("#f4c22c")
    mouth.setFill("#f4c22c")
    sleep(rand)
    mouse = win.checkMouse()
