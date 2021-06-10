from brick import *
class UFO():
    def __init__(self):
        self.size = 7
        self.start = 25
        self.health = 25
        self.defense = 0
        self.walls = []
        self.cooldown = 40
        self.bulletsX = []
        self.bulletsY = []
        self.utility1 = 0
        self.utility2 = 0

    def setPosition(self, start):
        self.start = start

    def reset(self):
        self.size = 7
        self.start = 25
        self.cooldown = 40
        self.bulletsX = []
        self.bulletsY = []

    def updateHealth(self):
        self.health -= 1

    def createDefense(self):
        self.defense = 1
        for i in range(11):
            brick = yellowBrick(3, i*5)
            self.walls.append(brick)

    def delete(self):
        self.health = 0
        self.walls = []
        self.bulletsX = []
        self.bulletsY = []
        self.defense = 0

    def shoot(self):
        self.bulletsX.append(self.start + self.size//2)
        self.bulletsY.append(4)

    def updateBullets(self):
        if self.utility1 != self.utility2:
            newY = []
            for bullet in self.bulletsY:
                newY.append(bullet + 1)
            return newY
            self.utility1 = self.utility2
        else:
            self.utility1 = 1 - self.utility2
            return self.bulletsY
