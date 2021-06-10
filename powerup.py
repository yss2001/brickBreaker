class PowerUp():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.utility1 = 0
        self.utility2 = 1
        self.active = 0

class Expand(PowerUp):
    def __init__(self, x, y):
        self.type = 1
        self.shape = 'E'
        self.duration = 150
        super(Expand, self).__init__(x, y)

    def getType(self):
        return self.type

    def getShape(self):
        return self.shape

    def getDuration(self):
        return self.duration

    def updatePower(self, paddle):

        if self.active == 2:
            self.duration -= 1
            if self.duration == 0:
                paddle.size = 7
                self.active = 0
                self.duration = 150
            return paddle
        else:

            if self.y == 48:
                if self.x >= paddle.start and self.x <= (paddle.start + paddle.size):
                    paddle.size = 10
                    self.active = 2
                else:
                    self.active = 0
                    self.duration = 150
            else:
                 if self.utility1 != self.utility2:
                    self.y += 1
                    self.utility1 = self.utility2
                 else:
                    self.utility1 = 1 - self.utility2
            return paddle

class Shrink(PowerUp):
    def __init__(self, x, y):
        self.type = 2
        self.shape = 'S'
        self.duration = 150
        super(Shrink, self).__init__(x, y)

    def getType(self):
        return self.type

    def getShape(self):
        return self.shape

    def getDuration(self):
        return self.duration

    def updatePower(self, paddle):

        if self.active == 2:
            self.duration -=1
            if self.duration == 0:
                paddle.size = 7
                self.active = 0
                self.duration = 150
            return paddle
        else:
            if self.y == 48:
                if self.x >= paddle.start and self.x <= (paddle.start + paddle.size):
                    paddle.size = 5
                    self.active = 2
                else:
                    self.active = 0
                    self.duration = 150
            else:
                if self.utility1 != self.utility2:
                    self.y += 1
                    self.utility1 = self.utility2
                else:
                    self.utility1 = 1 - self.utility2
            return paddle

class FastBall(PowerUp):
    def __init__(self, x, y):
        self.type = 3
        self.shape = 'F'
        self.duration = 150
        self.boost = 2
        super(FastBall, self).__init__(x, y)

    def getShape(self):
        return self.shape

    def updatePower(self, paddle):
        if self.active == 2:
            self.duration -= 1
            if self.duration == 0:
                self.duration = 150
                self.active = 0
        else:
            if self.y == 48:
                if self.x >= paddle.start and self.x <= (paddle.start + paddle.size):
                    self.boost = 2
                    self.active = 2
                else:
                    self.active = 0
                    self.duration = 150
            else:
                if self.utility1 != self.utility2:
                    self.y += 1
                    self.utility1 = self.utility2
                else:
                    self.utility1 = 1 - self.utility2
        return paddle

class Shooter(PowerUp):
    def __init__(self, x, y):
        self.type = 4
        self.shape = 'B'
        self.duration = 100
        self.cooldown = 0
        self.bulletsX = []
        self.bulletsY = []
        self.butil1 = 0
        self.butil2 = 1
        super(Shooter, self).__init__(x, y)


    def getShape(self):
        return self.shape

    def shoot(self, paddle):
        self.bulletsX.append(paddle.start + paddle.size//2)
        self.bulletsY.append(48)

    def updateBullets(self):
        if self.butil1 != self.butil2:
            newY = []
            for bullet in self.bulletsY:
                newY.append(bullet - 1)
            self.butil1 = self.butil2
            return newY
        else:
            self.butil1 = 1 - self.butil2
            return self.bulletsY

    def updatePower(self, paddle):
        if self.active == 2:
            self.duration -= 1
            if self.duration == 0:
                self.duration = 100
                self.active = 0
                self.cooldown = 0
        else:
            if self.y == 48:
                if self.x >=paddle.start and self.x <= (paddle.start + paddle.size):
                    self.active = 2
                else:
                    self.active = 0
                    self.duration = 100
            else:
                if self.utility1 != self.utility2:
                    self.y += 1
                    self.utility1 = self.utility2
                else:
                    self.utility1 = 1 - self.utility2

        return paddle


def resetPowers(powerUps):
    for powerUp in powerUps:
        powerUp.active = 0
        powerUp.duration = 150
        powerUp.x = -1
        powerUp.y = -1

    powerUps[3].duration = 100
    powerUps[3].bulletsX = []
    powerUps[3].bulletsY = []
    powerUps[3].cooldown = 0
    return powerUps
