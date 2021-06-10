import random
class Ball():
    def __init__(self, xPos, yPos, xSpeed, ySpeed):
        self.xPos = xPos
        self.yPos = yPos
        self.xSpeed = xSpeed
        self.ySpeed = ySpeed

    def move(self, boost):
        if self.xSpeed < 0:
            boost = -1*boost
        self.xPos += self.xSpeed + boost
        self.yPos += self.ySpeed
        if self.xPos < 0:
            self.xPos = 0
            self.xSpeed = -1*self.xSpeed
        elif self.xPos > 54:
            self.xPos = 54
            self.xSpeed = -1*self.xSpeed

        if self.yPos < 0:
            self.yPos = 0
            self.ySpeed = -1*self.ySpeed


    def place(self):
        initial = random.randint(25, 31)
        self.xPos = initial
        self.yPos = 49
        self.xSpeed = 1
        self.ySpeed = -1
