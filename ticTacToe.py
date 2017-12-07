from random import *

board = [0,1,2,
         3,4,5,
         6,7,8]

def show():
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print("-|-|-")
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print("-|-|-")
    print(f"{board[6]}|{board[7]}|{board[8]}")

def getPos():
    valid = False
    while valid is False:
        try:
            spot = int(input("Choose a postion: "))
            if spot > 8 or spot < 0:
                print("Position out of range")
                continue
            if board[spot] != "X" and board[spot] != "Z":
                board[spot] = "X"
            else:
                print("This spot is taken")
                continue
            valid = True

        except ValueError:
            print("Invalid position")

def compPos():
    good = False
    while good is False:
        compSpot = randint(0,8)
        if board[compSpot] != "X" and board[compSpot] != "Z":
            good = True
            board[compSpot] = "Z"
            show()
            print(f"The computer chose position {compSpot}!")
        else:
            continue

def winCheck(p):
    if ((board[0]==p and board[1]==p and board[2]==p) or 
    (board[3]==p and board[4]==p and board[5]==p) or
    (board[6]==p and board[7]==p and board[8]==p) or
    (board[0]==p and board[3]==p and board[6]==p) or
    (board[1]==p and board[4]==p and board[7]==p) or
    (board[2]==p and board[5]==p and board[8]==p) or
    (board[0]==p and board[4]==p and board[8]==p) or
    (board[2]==p and board[4]==p and board[6]==p)):
        if p == "X":
            global playerWin
            playerWin = True
        else:
            global compWin
            compWin = True


print("Let's play Tic Tac Toe!\n")
show()
playerWin = False
compWin = False
while playerWin is False and compWin is False:
    getPos()
    winCheck("X")
    compPos()
    winCheck("Z")

if playerWin is True:
    print("You win!")
elif compWin is True:
    print("The computer won")
