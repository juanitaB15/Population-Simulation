import pygame as p
import random as r
import Variables
import SimulationMain

class Sheep():
    WIDTH = HEIGHT = Variables.SQ_LENGTH
    RADIUS = Variables.SQ_LENGTH // 2

    def __init__(self, x, y, colorCode):  # this is constructor and they can take in parameters. x and y define the location of the sheep in the grid.
        self.x = x
        self.y = y
        if colorCode == 1:
            self.color = 'sea green'
        else:
            self.color = 'coral'
        self.energy = Variables.INITIAL_SHEEP_ENERGY

    def draw(self, screen):
        # print("self.x and self.y = ", self.x, self.y)
        p.draw.circle(screen, self.color,
                      (self.x * Sheep.WIDTH + Sheep.WIDTH // 2,  # double // means integer division, we are rounding.
                       self.y * Sheep.WIDTH + Sheep.WIDTH // 2),
                      Sheep.RADIUS)

    def move(self):
        '''
        Move the sheep randomly in one of 4 directions.
        Keep the sheep on the screen (within boundaries)- 0 to 11
        Decrease the sheep's energy.
        '''

        direction = r.randint(1, 4)
        if direction == 1 and self.x < Variables.NUM_OF_SQUARES-1:
            self.x = self.x + 1
            self.energy -= 1

        if direction == 2 and self.x > 0:
            self.x = self.x - 1
            self.energy -= 1

        if direction == 3 and self.y < Variables.NUM_OF_SQUARES-1:
            self.y = self.y + 1
            self.energy -= 1

        if direction == 4 and self.y > 0:
            self.y = self.y - 1
            self.energy -= 1



    def canGraze(self, grassSquare):
        if grassSquare.energy > 0:
            return True
        return False  # don't need else because Return True exists the function.

    def graze(self, grassSquare):
        # conservation of energy
        #        print("grassSquare.energy = ", grassSquare.energy)
        if grassSquare.energy > 0:
            self.energy += 1
            grassSquare.energy -= 1
        # print("grassSquare.energy = ",grassSquare.energy)

    def update(self, grassSquare):
        '''
        Depending (location, energy level, turns to regrowth) on the conditions of the sheep and the grass,
        the sheep might move or graze or die each frame.
        '''
        # print("self.energy = ",self.energy)
        if self.energy > 0:
            # later, can come back and change the options of moving/grazing, perhaps AI.
            if self.canGraze(grassSquare):
                self.graze(grassSquare)
            else:
                self.move()
        else:  # sheep is dead
            self.color = 'gray'








