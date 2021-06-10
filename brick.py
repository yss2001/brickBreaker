class Brick():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class cyanBrick(Brick):
    brickid = 1
    strength = 1

    def __init__(self, x, y):
        super(cyanBrick, self).__init__(x, y)

class yellowBrick(Brick):
    brickid = 2
    strength = 2

    def __init__(self, x, y):
        super(yellowBrick, self).__init__(x, y)

class redBrick(Brick):
    brickid = 3
    strength = 3

    def __init__(self, x, y):
        super(redBrick, self).__init__(x, y)


class noBreakBrick(Brick):
    brickid = 4
    strength = 5

class rainbowBrick(Brick):
    brickid = 5
    strength = 1

def setBricks(level):
    bricks = []
    limit = 0
    unbreakable = 0
    if level == 1:
        limit = 16
        for i in range(4, 17):
            bType = i%4
            j = 5
            while j<=45:
                if j == 25:
                    brick = noBreakBrick(i, j)
                    bricks.append(brick)
                    unbreakable += 1
                else:
                    if abs(i-10) == 5:
                        if j == 20:
                            brick = cyanBrick(i, j)
                            bricks.append(brick)
                        elif j==30:
                            brick = rainbowBrick(i, j)
                            bricks.append(brick)
                    elif abs(i-10) >= 3 and abs(i-10) <= 4:
                        if j >= 15 and j <= 35:
                            brick = yellowBrick(i, j)
                            bricks.append(brick)
                    elif abs(i-10) >= 1 and abs(i-10) <= 2:
                        if j >= 10 and j <= 40:
                            brick = redBrick(i, j)
                            bricks.append(brick)
                    elif i==10:
                        if j==5 or j==45:
                            brick = noBreakBrick(i, j)
                            bricks.append(brick)
                            unbreakable += 1
                        elif j==10 or j==40:
                            brick = cyanBrick(i, j)
                            bricks.append(brick)
                        elif j==15 or j==35:
                            brick = yellowBrick(i, j)
                            bricks.append(brick)
                        elif j==20 or j==30:
                            brick = redBrick(i, j)
                            bricks.append(brick)
                j += 5

    if level == 2:
        btype = 1
        for i in range(8, 14):
            limit = 13
            if i%2 == 1:
                j = 0
            else:
                j = 5
            while j<=50:
                if btype == 1:
                    brick = cyanBrick(i, j)
                    bricks.append(brick)
                    btype = 2
                elif btype == 2:
                    brick = yellowBrick(i, j)
                    bricks.append(brick)
                    btype = 3
                elif btype == 3:
                    brick = redBrick(i, j)
                    bricks.append(brick)
                    btype = 4
                elif btype == 4:
                    brick = noBreakBrick(i, j)
                    bricks.append(brick)
                    unbreakable += 1
                    btype = 5
                elif btype == 5:
                    brick = rainbowBrick(i, j)
                    bricks.append(brick)
                    btype = 1
                j += 15

    if level == 3:
        for i in range(12, 17):
            limit = 16
            j = 5
            while j<=45:
                if i==14 and j==25:
                    brick = noBreakBrick(i, j)
                    bricks.append(brick)
                    unbreakable += 1
                elif i==12 and (j==20 or j==30):
                    brick = rainbowBrick(i, j)
                    bricks.append(brick)
                elif i==16 and (j==20 or j==30):
                    brick = redBrick(i, j)
                    bricks.append(brick)
                elif abs(i-14) == 1:
                    if j==15 or j==20 or j==30 or j==35:
                        brick = redBrick(i, j)
                        bricks.append(brick)
                    if j==10 or j==40:
                        brick = redBrick(i, j)
                        bricks.append(brick)
                elif i==14:
                    if j==15 or j==20 or j==30 or j==35:
                        brick = redBrick(i, j)
                        bricks.append(brick)
                    if j==5 or j==10 or j==40 or j==45:
                        brick = redBrick(i, j)
                        bricks.append(brick)
                j += 5

    return bricks, unbreakable, limit

def fallBricks(bricks):
    over = 0

    for brick in bricks:
        if (brick.x+1) == 48:
            over = 1
            break

    return over

def rainbowModify(bricks):
    for brick in bricks:
        if brick.brickid == 5:
            if brick.strength == 1:
                brick.strength = 2
            elif brick.strength == 2:
                brick.strength = 3
            elif brick.strength == 3:
                brick.strength = 1
    return bricks
