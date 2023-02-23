import random
import sys

import pygame


class Microbe:
    pos_x = []
    pos_y = []
    sizes = []
    steps = 0
    alive = True

    def __init__(self, x, y, size):
        self.pos_x.append(x)
        self.pos_y.append(y)
        self.sizes.append(size)

    def getPos_X(self):
        return self.pos_x

    def getPos_Y(self):
        return self.pos_y

    def getSizes(self):
        return self.sizes

    def getSteps(self):
        return self.steps

    def isAlive(self):
        return self.alive

    def addPos_X(self, pos_x):
        pos_x += self.pos_x[-1]
        self.pos_x.append(pos_x)

    def addPos_Y(self, pos_y):
        pos_y += self.pos_y[-1]
        self.pos_x.append(pos_y)

    def addSize(self, size):
        size += self.sizes[-1]
        self.sizes.append(size)

    def addSteps(self, steps):
        self.steps += steps

    def setStepsZero(self):
        self.steps = 0

    def setLivingState(self, state):
        self.alive = state

    def killCell(self):
        self.alive = False

    def toString(self):
        return "Current Position X:", self.pos_x[len(self.pos_x) - 1], " Y: ", self.pos_y[len(self.pos_y) - 1], \
               "Current Size: ", self.sizes[len(self.sizes) - 1]


class PopulateMicrobes:
    x_max = 1000
    y_max = 1000
    x_min = 0
    y_min = 0

    amountOfMicrobes = 5
    microbes = []

    amountOfFood = 100
    food_x_pos = []
    food_y_pos = []

    maxSize = 15
    minSize = 0

    def spawnMicrobes(self):
        for i in range(self.amountOfMicrobes):
            self.microbes.append(Microbe(random.randint(100, 900), random.randint(100, 900), random.randint(1, 5)))

    def spawnFood(self):
        for i in range(self.amountOfFood):
            x_pos_food = random.randint(1 + self.x_min, self.x_max - 1)
            y_pos_food = random.randint(1 + self.y_min, self.y_max - 1)
            self.food_x_pos.append(x_pos_food)
            self.food_y_pos.append(y_pos_food)

    def randomWalkX(self):
        x_sign = random.randint(0, 1)
        x_pos = random.randint(1, 30)
        if x_sign == 0:
            x_pos *= -1
        return x_pos

    def randomWalkY(self):
        y_sign = random.randint(0, 1)
        y_pos = random.randint(1, 30)
        if y_sign == 0:
            y_pos *= -1
        return y_pos

    def checkSurvival(self, size, x_pos, y_pos):
        if self.minSize <= size <= self.maxSize and self.x_min <= x_pos <= self.x_max and \
                self.y_min <= y_pos <= self.y_max:
            return True
        else:
            return False

    def checkFood(self, pos_x, pos_y):
        foodInRange = False
        for i in range(len(self.food_x_pos)):
            if self.food_x_pos[i] - 30 <= pos_x <= self.food_x_pos[i] + 30 and \
                    self.food_y_pos[i] - 30 <= pos_y <= self.food_y_pos[i] + 30:
                foodInRange = True
                break
        return foodInRange

    def runSim(self):
        self.spawnMicrobes()
        self.spawnFood()
        cellsAlive = True
        deadCounter = 0
        while cellsAlive:
            for i in range(len(self.microbes)):  # change in pos
                self.microbes[i].addPos_X(self.randomWalkX())
                self.microbes[i].addPos_Y(self.randomWalkY())
            for i in range(len(self.microbes)):  # look for food at current pos
                if self.checkFood(self.microbes[i].getPos_X()[-1], self.microbes[i].getPos_X()[-1]) == True and \
                        self.microbes[i].getSteps() < 10:
                    self.microbes[i].addSize(1)
                    self.microbes[i].setStepsZero()
                elif self.checkFood(self.microbes[i].getPos_X()[-1], self.microbes[i].getPos_X()[-1]) == False and \
                        self.microbes[i].getSteps() < 10:
                    self.microbes[i].addSteps(1)
                elif self.microbes[i].getSteps() >= 10:
                    self.microbes[i].addSize(-1)
            for i in range(len(self.microbes)):  # see if cell is dead
                self.microbes[i].setLivingState(self.checkSurvival(self.microbes[i].getSizes()[-1],
                                                                   self.microbes[i].getPos_X()[-1],
                                                                   self.microbes[i].getPos_Y()[-1]))
            for i in range(len(self.microbes)):  # check if all cells are dead to end sim
                if not self.microbes[i].isAlive():
                    deadCounter += 1
            if deadCounter == len(self.microbes):
                cellsAlive = False
            else:
                deadCounter = 0

    def liveGame(self):
        self.runSim()

        pygame.init()
        screen = pygame.display.set_mode((1000, 1000))
        clock = pygame.time.Clock()
        clock.tick(60)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            screen.fill((0, 0, 0))
            for i in range(len(self.food_x_pos)):
                pygame.draw.circle(screen, (0, 0, 230), (self.food_x_pos[i], self.food_y_pos[i]), 5)
            for i in range(len(self.microbes)):
                pygame.draw.circle(screen, (0, 230, 0), (self.microbes[i].getPos_X()[-1], self.microbes[i].getPos_Y()[-1]), self.microbes[i].getSizes()[-1])
                pygame.display.update()
            clock.tick(1)


pm = PopulateMicrobes()
pm.liveGame()
