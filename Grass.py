import pygame as p
import Variables

class Grass():
    def __init__(self, x, y):  # x and y are coordinates in the grid and we will make them fields.
        self.x = x
        self.y = y  # we make it a field so that we can use and edit them later and move the sheep around.
        self.colors = [(187, 189, 79),  # (122, 124, 43)- teacher's starting(deadest) color
                       (151, 163, 44),
                       (128, 178, 42),
                       (117, 196, 39),
                       (101, 235, 21),
                       (66, 219, 15)]  # (118, 235, 21)- teacher's ending(brightest) color
        self.energy = Variables.MAX_GRASS_GRAZES
        self.framesToRegrowth = Variables.GRASS_REFRESH_RATE  # count down to 0, then regrow.

    def draw(self, screen):
        p.draw.rect(screen, self.colors[self.energy],
                    (self.x * Variables.SQ_LENGTH, self.y * Variables.SQ_LENGTH,
                     Variables.SQ_LENGTH, Variables.SQ_LENGTH))

    def update(self):
        if self.framesToRegrowth <= 0 and self.energy < Variables.MAX_GRASS_GRAZES:
            self.energy += 1  # photosynthesis
            self.framesToRegrowth = Variables.GRASS_REFRESH_RATE  # reset countdown
        else:
            self.framesToRegrowth -= 1  # counting down


