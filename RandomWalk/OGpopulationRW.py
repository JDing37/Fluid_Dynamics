"""
Goals:
- create individual
- allow them to travel 360 deg and a step where minStep<=step<=maxStep
- they may travel until death
- causes of death = travel outside of grid or can't get food
- food exists in random parts of grid
- individual may eat if in food radius
- food may respawn throughout grid
"""

import random
import matplotlib.pyplot as plt
import pygame
import sys


class MicrobialAdam:
    max_x = 1000
    max_y = 1000
    min_x = 0
    min_y = 0
    x_pos = 500
    y_pos = 500
    x_map = []
    y_map = []
    stepsBeforeFood = 0
    food_x = []
    food_y = []

    def deltaPosition(self):
        self.spawnFood()
        while self.max_x > self.x_pos > self.min_x and self.max_y > self.y_pos > self.min_y and self.stepsBeforeFood < 10:
            if self.checkForFood(self.x_pos, self.y_pos):
                self.stepsBeforeFood = 0
            else:
                self.stepsBeforeFood += 1
            delta_x = random.randint(10, 50)
            delta_y = random.randint(10, 50)
            x_subStep = random.random()
            y_subStep = random.random()
            rand_sign_x = random.randint(0, 1)
            rand_sign_y = random.randint(0, 1)
            if rand_sign_x == 0:
                self.x_pos += delta_x + x_subStep
            else:
                self.x_pos += (-1 * delta_x + x_subStep)
            if rand_sign_y == 0:
                self.y_pos += delta_y + y_subStep
            else:
                self.y_pos += (-1 * delta_y + y_subStep)
            self.x_map.append(self.x_pos)
            self.y_map.append(self.y_pos)

    def spawnFood(self):
        food = 0
        while food < 100:
            rand_food_x = random.randint(1, 999)
            rand_food_y = random.randint(1, 999)
            self.food_x.append(rand_food_x)
            self.food_y.append(rand_food_y)
            food += 1

    def checkForFood(self, x_pos, y_pos):
        answer = False
        for i in range(len(self.food_x)):
            if self.food_x[i] - 30 <= x_pos <= self.food_x[i] + 30 and self.food_y[i] - 30 <= y_pos <= self.food_y[
                i] + 30:
                answer = True
        return answer

    def printPositions(self):
        self.deltaPosition()
        plt.scatter(self.x_map, self.y_map)
        plt.scatter(self.food_x, self.food_y)
        plt.show()

    def liveGame(self):
        self.deltaPosition()

        pygame.init()
        screen = pygame.display.set_mode((1000, 1000))
        clock = pygame.time.Clock()
        clock.tick(60)

        for i in range(len(self.food_x)):
            pygame.draw.circle(screen, (0, 0, 230), (self.food_x[i], self.food_y[i]), 5)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            screen.fill((0, 0, 0))
            for i in range(len(self.food_x)):
                pygame.draw.circle(screen, (0, 0, 230), (self.food_x[i], self.food_y[i]), 5)
            for i in range(len(self.x_map)):
                pygame.draw.circle(screen, (0, 230, 0), (self.x_map[i], self.y_map[i]), 5)
                pygame.display.update()
            clock.tick(1)


ma = MicrobialAdam()
ma.liveGame()
