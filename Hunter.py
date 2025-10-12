import Variables
import pygame as p
import random as r

class Hunter():

    WIDTH = HEIGHT = Variables.SQ_LENGTH
    RADIUS = Variables.SQ_LENGTH // 2

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = 'maroon'
        self.energy = Variables.INITIAL_HUNTER_ENERGY

    def draw(self, screen):
        # print("self.x and self.y = ", self.x, self.y)
        p.draw.circle(screen, self.color,
                      (self.x * Hunter.WIDTH + Hunter.WIDTH // 2,  # double // means integer division, we are rounding.
                       self.y * Hunter.WIDTH + Hunter.WIDTH // 2),
                       Hunter.RADIUS)

    def hunt(self, Animal, animalList):
        # conservation of energy
        print("sheep.energy = ", Animal.energy)

        if Animal.energy > 0:
            self.energy = self.energy + Animal.energy
            Animal.energy = 0
        animalList.remove(Animal)
        print("Hunter.energy = ",self.energy)

    def move(self):
        '''
        Move the sheep randomly in one of 4 directions.
        Keep the sheep on the screen (within boundaries)- 0 to 11
        Decrease the sheep's energy.
        '''

        print("Initial HUnter Energy = ", self.energy)

        direction = r.randint(1, 4)
        if direction == 1 and self.x > 0:
            self.x = self.x - 1
            self.energy -= 1

        if direction == 2 and self.x < Variables.NUM_OF_SQUARES-1:
            self.x = self.x + 1
            self.energy -= 1

        if direction == 3 and self.y > 0:
            self.y = self.y - 1
            self.energy -= 1

        if direction == 4 and self.y < Variables.NUM_OF_SQUARES - 1:
            self.y = self.y + 1
            self.energy -= 1

            print("self.x = ", self.x)
            print("self.y = ", self.y)

        #pass  # function that allows you to run the code without any errors and this function.

    def update(self, sheepList, wolfList):  # pass in sheep list as a parameter from the main.
        '''
        Check if this wolf is at the same location as each of the sheep.
        If so, this wolf should eat that sheep.
        Otherwise, the wolf should move in search of more sheep.
        '''

 #        print("sheepList = ", sheepList)
 #        print("wolfList = ", wolfList)
        for s in sheepList:
            if self.x == s.x and self.y == s.y:
                print("found sheep")
                self.hunt(s, sheepList)

        for w in wolfList:
            if self.x == w.x and self.y == w.y:
                print("found wolf")
                self.hunt(w, wolfList)


        if self.energy > 0:
            self.move()
        else:
            self.color = "purple"
        #return False  # don't need else because Return True exists the function.

