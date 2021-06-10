from brick import *
import time
import random

def paddleCollision(ball, paddle):
    if ball.yPos == 48:
        if ball.xPos >= paddle.start and ball.xPos <= (paddle.start + paddle.size):
            change = int(paddle.start + paddle.size/2 - ball.xPos)
            change = abs(change)

            if ball.xSpeed < 0:
                newX = -1*change
            else:
                newX = change
            if newX == 0:
                newX = ball.xSpeed

            return newX, -1, 1
        else:
            return ball.xSpeed, ball.ySpeed, 0
    else:
        return ball.xSpeed, ball.ySpeed, 0

def wallCollision(ball):
    if ball.xPos == 0 or ball.xPos == 55:
        return -1*ball.xSpeed, ball.ySpeed
    elif ball.yPos == 0:
        return ball.xSpeed, -1*ball.ySpeed
    else:
        return ball.xSpeed, ball.ySpeed

def ufoCollision(ball, ufo):
    if ball.yPos <= 2 and ball.ySpeed < 0:
        if ball.xPos >= ufo.start and ball.xPos <= (ufo.start+ufo.size):
            ufo.health -= 1
            ball.ySpeed *= -1

        elif ball.xPos == ufo.start - 1 or ball.xPos == ufo.start+ufo.size+1:
            ufo.health -= 1
            ball.xSpeed *= -1
    return ball.ySpeed, ufo.health, ball.xSpeed

def ufoWallCollision(ball, ufo):
    if (ball.yPos == 4 and ball.ySpeed < 0) or (ball.yPos == 2 and ball.ySpeed > 0):
        if ufo.walls[ball.xPos//5].strength != 0:
            ufo.walls[ball.xPos//5].strength -= 1
            ball.ySpeed *= -1

    return ball.ySpeed, ufo

def bulletPaddleCollision(paddle, ufo):
    livesLost = 0
    bX = []
    bY = []
    for index, bullet in enumerate(ufo.bulletsX):
        if ufo.bulletsY[index] == 49:
            if bullet >= paddle.start and (bullet <= paddle.start+paddle.size):
                livesLost += 1
        else:
            bX.append(bullet)
            bY.append(ufo.bulletsY[index])

    return livesLost, bX, bY

def bulletBrickCollision(powerUp, score, bricks):
    newBricks = []
    newBX = []
    newBY = []
    collidedIndex = []
    for b in powerUp.bulletsY:
        collidedIndex.append(-1)

    for index1, bullet in enumerate(powerUp.bulletsX):
        for index2, brick in enumerate(bricks):
            if powerUp.bulletsY[index1] == (brick.x+1) and  brick.y <= bullet and bullet <= (brick.y+4):
                collidedIndex[index1] = index2
                break
        if collidedIndex[index1] == -1:
            newBX.append(bullet)
            newBY.append(powerUp.bulletsY[index1])

    for index, brick in enumerate(bricks):
        if index not in collidedIndex:
            newBricks.append(brick)
        else:
            if brick.strength != 5 and brick.brickid != 5:
                    brick.strength -= 1

            if brick.strength == 1:
                b = cyanBrick(brick.x, brick.y)
                newBricks.append(b)
            elif brick.strength == 2:
                b = yellowBrick(brick.x, brick.y)
                newBricks.append(b)
            elif brick.strength == 5:
                b = noBreakBrick(brick.x, brick.y)
                newBricks.append(b)
            elif brick.strength == 3:
                b = redBrick(brick.x, brick.y)
                newBricks.append(b)
            elif brick.strength == 0:
                score += 1

    if len(powerUp.bulletsX) == 0:
        return powerUp.bulletsX, powerUp.bulletsY, score, bricks
    else:
        return newBX, newBY, score, newBricks


def ballDrop(ball):
    if ball.yPos > 49:
        return 1
    else:
        return 0

def brickCollision(ball, bricks, score, nextPowerUp):
    nextY = ball.yPos + ball.ySpeed
    nextX = ball.xPos + ball.xSpeed
    newBricks = []

    collidedBrickX = 55 if ball.xSpeed > 0 else 0
    collidedBrickY = 0
    collidedIndex = -1
    overallCollided = 0

    newXSpeed = ball.xSpeed
    newYSpeed = ball.ySpeed

    newX = 0
    newY = 0

    collided = 0
    for index, brick in enumerate(bricks):
        longFace = 0
        collided = 0
        if brick.x == nextY:
            if (nextX >= brick.y and nextX <= (brick.y + 4)) or (brick.y-nextX == 1 or brick.y+5==nextX):
                collided = 1
                overallCollided = 1

        if collided:
            if ball.xSpeed > 0:
                if brick.y > collidedBrickX:
                    continue
                else:
                    if ball.ySpeed > 0 and (brick.y == collidedBrickX and brick.x > collidedBrickY):
                        continue
                    elif ball.ySpeed < 0 and (brick.y == collidedBrickX and brick.x < collidedBrickY):
                        continue
                    collidedBrickX = brick.y
                    collidedBrickY = brick.x
                    collidedIndex = index
            else:
                if brick.y < collidedBrickX:
                    continue
                else:
                    if ball.ySpeed > 0 and (brick.y == collidedBrickX and brick.x > collidedBrickY):
                        continue
                    elif ball.ySpeed < 0 and (brick.y == collidedBrickX and brick.x < collidedBrickY):
                        continue
                    collidedBrickX = brick.y
                    collidedBrickY = brick.x
                    collidedIndex = index

    if overallCollided != 0:
        if ball.xPos >= collidedBrickX and ball.xPos <= (collidedBrickX + 4):
            longFace = 1

        if longFace == 0:
            newXSpeed = -1*newXSpeed
            if ball.xSpeed > 0:
                newX =  collidedBrickX - 1
                newY = collidedBrickY
            else:
                newX = collidedBrickX + 5
                newY = collidedBrickY
        else:
            newYSpeed = -1*newYSpeed
            newY = ball.yPos
            newX = collidedBrickX + abs(ball.xPos - collidedBrickX)

    power = 0
    if overallCollided != 0 and bricks[collidedIndex].strength-1 == 0:
        chance = random.random()
        if chance <= 0.85:
            power = 1


    if collidedIndex == -1:
        for brick in bricks:
            newBricks.append(brick)
    else:
        for index, brick in enumerate(bricks):
            if index == collidedIndex:
                if brick.strength != 5 and brick.brickid != 5:
                    brick.strength -= 1

                if brick.strength == 1:
                    b = cyanBrick(brick.x, brick.y)
                    newBricks.append(b)
                elif brick.strength == 2:
                    b = yellowBrick(brick.x, brick.y)
                    newBricks.append(b)
                elif brick.strength == 5:
                    b = noBreakBrick(brick.x, brick.y)
                    newBricks.append(b)
                elif brick.strength == 3:
                    b = redBrick(brick.x, brick.y)
                    newBricks.append(b)
                elif brick.strength == 0:
                    score += 1
            else:
                newBricks.append(brick)


    if overallCollided == 0:
        return newXSpeed, newYSpeed, newBricks, score, ball.xPos, ball.yPos, 0, power, collidedBrickX, collidedBrickY
    else:
        return newXSpeed, newYSpeed, newBricks, score, newX, newY, 1, power, collidedBrickX, collidedBrickY

