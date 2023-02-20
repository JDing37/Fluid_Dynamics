import pymunk
import pygame
import sys


class Counter:
    amountOfPegs = 36
    amountOfBalls = 50
    i = 0
    j = 0
    space = pymunk.Space()
    xPositionOfPeg = 100
    yPositionOfPeg = 300
    space.gravity = (0, 100)
    pegs = []
    balls = []
    fixPoint = []

    def placePegs(self):
        while self.amountOfPegs > self.i:
            self.pegs.append(self.makePegs())
            self.i = self.i + 1

    def makePegs(self):
        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        body.position = (self.xPositionOfPeg, self.yPositionOfPeg)
        self.xPositionOfPeg += 100
        if self.xPositionOfPeg == 1000:
            self.xPositionOfPeg = 150
            self.yPositionOfPeg += 100
        elif self.xPositionOfPeg == 1050:
            self.xPositionOfPeg = 100
            self.yPositionOfPeg += 100
        shape = pymunk.Circle(body, 20)
        self.space.add(body, shape)
        return shape

    def placeBalls(self):
        while self.amountOfBalls > self.j:
            self.balls.append(self.makeBalls())
            self.j = self.j + 1

    def makeBalls(self):
        body = pymunk.Body(1, 100, body_type=pymunk.Body.DYNAMIC)
        body.position = (500, 0)
        shape = pymunk.Circle(body, 30)
        self.space.add(body, shape)
        return shape

    def placeFixPoint(self):
        self.fixPoint.append(self.makeFixPointLeft())
        self.fixPoint.append(self.makeFixPointRight())

    def makeFixPointLeft(self):
        triangleShape = pymunk.Poly(None, ((0, 0), (0, 100), (470, 100)))
        triMoment = pymunk.moment_for_poly(1, triangleShape.get_vertices())
        triangleBody = pymunk.Body(1, triMoment, body_type=pymunk.Body.STATIC)
        triangleShape.body = triangleBody
        self.space.add(triangleBody, triangleShape)
        return triangleShape

    def makeFixPointRight(self):
        triangleShape = pymunk.Poly(None, ((1000, 0), (1000, 100), (530, 100)))
        triMoment = pymunk.moment_for_poly(1, triangleShape.get_vertices())
        triangleBody = pymunk.Body(1, triMoment, body_type=pymunk.Body.STATIC)
        triangleShape.body = triangleBody
        self.space.add(triangleBody, triangleShape)
        return triangleShape

    def positionCounter(self):
        a = 0
        for ball in self.balls:
            if ball.position == (500, 0):  # bug - if ball doesn't hit exact position it wont count
                a += 1
                print(a)

    def runner(self):
        self.placePegs()
        self.placeBalls()
        self.placeFixPoint()

    def runGame(self):

        self.runner()

        pygame.init()
        screen = pygame.display.set_mode((1000, 2000))
        clock = pygame.time.Clock()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            screen.fill((217, 217, 217))
            for ball in self.balls:
                pos_x = int(ball.body.position.x)
                pos_y = int(ball.body.position.y)
                pygame.draw.circle(screen, (0, 0, 0), (pos_x, pos_y), 30)
            for peg in self.pegs:
                pos_x = int(peg.body.position.x)
                pos_y = int(peg.body.position.y)
                pygame.draw.circle(screen, (0, 0, 0), (pos_x, pos_y), 20)
            self.space.step(1 / 50)
            pygame.display.update()
            clock.tick(120)


A = Counter()
A.runGame()
A.positionCounter()
