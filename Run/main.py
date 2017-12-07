import pygame

import state
import title
import game

pygame.init()

"""CODE GOES HERE"""
pygame.joystick.Joystick(0).init()
""" end of fill up"""

display = pygame.display.set_mode((1000,600))
pygame.display.set_caption("Run! Buttons to Jump - Axis to Throw")

class RBR():
    def __init__(self):
        self.sm = state.StateMachine(self, title.Title())

    def start(self):
        while True:
            self.sm.update()

if __name__ == "__main__":
    game = RBR()
    game.start()
