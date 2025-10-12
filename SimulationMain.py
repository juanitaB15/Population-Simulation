import Variables, Sheep, Wolves, Grass, Hunter
import pygame as p
import random as r

global WIDTH, HEIGHT
WIDTH = Variables.NUM_OF_SQUARES * Variables.SQ_LENGTH + 200
HEIGHT = Variables.NUM_OF_SQUARES * Variables.SQ_LENGTH
PANEL_HEIGHT = 100
PANEL_WIDTH = 200
NUM_OF_BUTTONS = 2
BUTTON_WIDTH = PANEL_WIDTH / NUM_OF_BUTTONS  # Because each button should be the same size.

def drawButtons(screen):
    buttons = []
    colors = ['Skyblue1', 'Skyblue2']
    labels = ['START', 'STOP']
    font = p.font.SysFont('DejaVu Sans Mono', 18)

    button = p.draw.rect(screen, colors[0],
                          (HEIGHT, 200, BUTTON_WIDTH, HEIGHT+150))
    text = font.render(labels[0], True, 'black')
    screen.blit(text, button.move(19, 100))
    buttons.append(button)

    button1 = p.draw.rect(screen, colors[1],
                         (HEIGHT+100, 200, BUTTON_WIDTH, HEIGHT + 200))
    text = font.render(labels[1], True, 'black')
    screen.blit(text, button1.move(19, 100))
    buttons.append(button1)

    return buttons

def setup():
    global screen, clock
    p.init()  # initialize all pygame stuff
    screen = p.display.set_mode((WIDTH, HEIGHT))  # create display object
    clock = p.time.Clock()  # create time object

def drawPanel(screen, stats):
    background = p.draw.rect(screen, 'white', (HEIGHT, 0, 200, HEIGHT-150))
    font = p.font.SysFont('David', 16)

    for i in range(len(stats)):
        text = font.render(stats[i], True, 'black')
        screen.blit(text, background.move(0, 25*i))  # blit all of the text to the top left area of the background.

def spawnSheep(num):
    sheepList = []
    for i in range(num):

        colorCode = r.randint(1, 2)

        x_coo = r.randint(0, Variables.NUM_OF_SQUARES - 1)
        while x_coo == (Variables.NUM_OF_SQUARES - 1) or x_coo == 0:
            x_coo = r.randint(0, Variables.NUM_OF_SQUARES - 1)

        y_coo = r.randint(0, Variables.NUM_OF_SQUARES - 1)
        while y_coo == (Variables.NUM_OF_SQUARES - 1) or y_coo == 0:
            y_coo = r.randint(0, Variables.NUM_OF_SQUARES - 1)

        s = Sheep.Sheep(x_coo, y_coo, colorCode)  # from the file Sheep, we are accessing the class Sheep and telling it what coordinates to spawn in.
        sheepList.append(s)
    return sheepList

def spawnWolves(num):
    wolfList = []
    # i = 0
    for i in range(num):
        # print("wolf i = ", i)
        x_coo = r.randint(0, Variables.NUM_OF_SQUARES - 1)
        while x_coo == (Variables.NUM_OF_SQUARES - 1) or x_coo == 0:
            x_coo = r.randint(0, Variables.NUM_OF_SQUARES - 1)

        y_coo = r.randint(0, Variables.NUM_OF_SQUARES - 1)
        while y_coo == (Variables.NUM_OF_SQUARES - 1) or y_coo == 0:
            y_coo = r.randint(0, Variables.NUM_OF_SQUARES -1)

        w = Wolves.Wolf(x_coo, y_coo)  # from the file Wolves, we are accessing the class Wolf and telling it what coordinates to spawn in.
        wolfList.append(w)
    return wolfList

def spawnHunter(num):
    hunterList = []
    # i = 0
    for i in range(num):
        # print("wolf i = ", i)
        x_coo = r.randint(0, Variables.NUM_OF_SQUARES - 1)
        while x_coo == (Variables.NUM_OF_SQUARES - 1) or x_coo == 0:
            x_coo = r.randint(0, Variables.NUM_OF_SQUARES - 1)

        y_coo = r.randint(0, Variables.NUM_OF_SQUARES - 1)
        while y_coo == (Variables.NUM_OF_SQUARES - 1) or y_coo == 0:
            y_coo = r.randint(0, Variables.NUM_OF_SQUARES -1)

        h = Hunter.Hunter(x_coo, y_coo)  # from the file Wolves, we are accessing the class Wolf and telling it what coordinates to spawn in.
        hunterList.append(h)
    return hunterList

def spawnGrass():
    grassList = []
    for i in range(Variables.NUM_OF_SQUARES):  # for each row.
        grassRow = []
        for j in range(Variables.NUM_OF_SQUARES):
            grassRow.append(Grass.Grass(j, i))  # from the file Grass, we are accessing the class Grass and telling it what coordinates to spawn in.
        grassList.append(grassRow)
    return grassList


def main():
    Simulate = False
    stats = []
    FramesElapsed = 0
    setup()  # call the setup function that we defined above
    grassList = spawnGrass()  # grassList is a 2D list
    sheepList = spawnSheep(Variables.NUM_OF_SHEEP)
    wolfList = spawnWolves(Variables.NUM_OF_WOLVES)
    hunterList = spawnHunter(Variables.NUM_OF_HUNTERS)
    buttons = drawButtons(screen)
    # drawButtons(screen)

    done = False
    while not done:  # loop continues until done = True
        for event in p.event.get():  # iterate through event queue
            if event.type == p.QUIT:  # if we click the red X to close the window
                done = True  # end loop
            if event.type == p.MOUSEBUTTONDOWN:
                if buttons[0].collidepoint(event.pos):  # press START button # if you dont have this code, wherever you click, the simulation is going to start instead of clicking exactly at the Start Point
                    # how do we start the simulation?
                    print('start button pressed')
                    Simulate = True

                if buttons[1].collidepoint(event.pos):  # press STOP button
                    print('stop button pressed')
                    Simulate = False


        # update every species
        if  Simulate == True:
            FramesElapsed = FramesElapsed + 1
            for row in grassList:
                for grassSquare in row:
                    grassSquare.update()
                 #   FramesElapsed = FramesElapsed + 1
            for s in sheepList:
                s.update(grassList[s.y][s.x])  # update grassList w/ coordinates of sheep.
                # FramesElapsed = FramesElapsed + 1
                if s.color == "gray":
                    sheepList.remove(s)
            for w in wolfList:
                w.update(sheepList)
            #    FramesElapsed = FramesElapsed + 1
                if w.color == "gray":
                    wolfList.remove(w)
            for h in hunterList:
                h.update(sheepList, wolfList)
             #   FramesElapsed = FramesElapsed + 1
                if h.color == "purple":
                    hunterList.remove(h)

            for row in grassList:
                for grassSquare in row:  # row is outer list and grassSquares is the inner list.
                    grassSquare.draw(screen)
            for s in sheepList:  # for each sheep,...
                s.draw(screen)  # ...draw each sheep on the screen.

            for w in wolfList:
                w.draw(screen)
            for h in hunterList:
                h.draw(screen)
            print("clock.tick = ", clock.tick(Variables.MAX_FPS))
    #        clock.tick(Variables.MAX_FPS)  # FPS of screen updating

            stats = ['Welcome to the Population Simulation', '',
                     'Click START to start the simulation',
                     'You can also STOP',
                     'the simulation.',
                     'Number of frames elapsed:'
                     + str(FramesElapsed),
                     'Number of alive Sheep:' + str(len(sheepList)),
                     'Number of dead Sheep:' + str(Variables.NUM_OF_SHEEP - len(sheepList)),
                     'Number of alive Wolves: ' + str(len(wolfList)),
                     'Number of dead Wolves: ' + str(Variables.NUM_OF_WOLVES - len(wolfList)),
                     'Grass regrowth rate:' + str(Variables.GRASS_REFRESH_RATE),
                     'Frames per second:' + str(Variables.MAX_FPS)]
        p.display.flip()  # update the screen

        drawPanel(screen, stats)

    p.quit()  # close display window (and all pygame stuff) after ending loop


# python script to run the main function
if __name__ == "__main__":
    main()