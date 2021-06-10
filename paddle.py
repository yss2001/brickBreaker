class Paddle():
    def __init__(self):
        self.size = 7
        self.start = 25

    def updateSize(self):
        if (self.size+2) <= 25:
            self.size += 2

    def setPosition(self, change):
        if change < 0 and self.start > 0:
            self.start += change
            if self.start < 0:
                self.start = 0
        if change > 0 and (self.start + self.size) < 55:
            self.start += change
            if self.start > 49:
                self.start = 49

    def reset(self):
        self.size = 7
        self.start = 25
