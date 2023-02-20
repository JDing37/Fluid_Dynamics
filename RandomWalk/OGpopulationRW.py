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

class MicrobialAdam:

    max_x = 100
    max_y = 100
    min_x = 0
    min_y = 0
    x_pos = 50
    y_pos = 50
    x_map = []
    y_map = []

    def deltaPosition(self):
        while self.max_x > self.x_pos > self.min_x and self.max_y > self.y_pos > self.min_y:
            delta_x = random.randint(1, 5)
            delta_y = random.randint(1, 5)
            rand_sign_x = random.randint(0, 1)
            rand_sign_y = random.randint(0, 1)
            if rand_sign_x == 0:
                self.x_pos += delta_x
            else:
                self.x_pos += (-1*delta_x)
            if rand_sign_y == 0:
                self.y_pos += delta_y
            else:
                self.y_pos += (-1*delta_y)
            self.x_map.append(self.x_pos)
            self.y_map.append(self.y_pos)

    def printPosition(self):
        self.deltaPosition()
        plt.scatter(self.x_map, self.y_map)
        plt.show()


ma = MicrobialAdam()
ma.printPosition()

