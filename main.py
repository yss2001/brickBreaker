from board import *
from paddle import *
from brick import *
from ball import *
from collision import *
from powerup import *
from ufo import *
import time
import random
import termios, fcntl, sys, os
fd = sys.stdin.fileno()

oldterm = termios.tcgetattr(fd)
newattr = termios.tcgetattr(fd)
newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
termios.tcsetattr(fd, termios.TCSANOW, newattr)

oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)

os.system('clear')

c = ''
bricks = []
unbreakable = 0
limit = 16
returns = setBricks(1)
bricks = returns[0]
unbreakable = returns[1]
limit = returns[2]

powerUps = []
powerUps.append(Expand(-1, -1))
powerUps.append(Shrink(-1, -1))
powerUps.append(FastBall(-1, -1))
powerUps.append(Shooter(-1, -1))
nextPowerUp = 3

timeoutLevel = 3000
timeAttack = 0
board = Board()
paddle = Paddle()
ufo = UFO()
initial = random.randint(25, 31)
ball = Ball(initial, 48, 1, -1)
begin = 0
gameTime = 0
livesLeft = 3
level = 1
score = 0
collided = 0
buildDefense = 0
try:
    while(livesLeft or level>3):
        time.sleep(0.1)
        timeoutLevel -= 1
        if timeoutLevel == 0:
            timeAttack = 1

        bricks = rainbowModify(bricks)

        board.printGrid(limit, level, score, livesLeft, int(gameTime/10), paddle.start, paddle.size, bricks, ball, powerUps, ufo)

        c = sys.stdin.read(1)
        if c=='q' or c=='Q':
            termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
            fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)
            os.system('clear')
            break
        elif c=='a' or c=='A':
            if not begin:
                begin = 1
            paddle.setPosition(-4)
            ufo.setPosition(paddle.start)
        elif c=='d' or c=='D':
            if not begin:
                begin = 1
            paddle.setPosition(4)
            ufo.setPosition(paddle.start)
        elif c=='x' or c=='X':
            if powerUps[3].active == 2:
                if powerUps[3].cooldown == 0:
                    powerUps[3].shoot(paddle)
                    powerUps[3].cooldown = 10
        elif c=='s' or c=='S':
            if level == 3:
                break
            begin = 0
            ball.place()
            paddle.reset()
            ufo.reset()
            returns = setBricks(level+1)
            bricks = returns[0]
            unbreakable = returns[1]
            limit = returns[2]
            powerUps = resetPowers(powerUps)
            timeAttack = 0
            timeoutLevel = 3000
            level += 1
            print("\nENTERING LEVEL: ", level)
            time.sleep(1)

        if begin and not collided:
            if powerUps[2].active == 2:
                ball.move(powerUps[2].boost)
            else:
                ball.move(0)


        newSpeeds = paddleCollision(ball, paddle)
        ball.xSpeed = newSpeeds[0]
        ball.ySpeed = newSpeeds[1]

        if timeAttack and newSpeeds[2]:
            over = fallBricks(bricks)
            if over == 1:
                break
            else:
                for brick in bricks:
                    brick.x += 1
                limit += 1


        if ball.yPos > 3 and buildDefense:
            ufo.createDefense()
            buildDefense = 0

        if ufo.health > 0 and level == 3:
            returns = ufoCollision(ball, ufo)
            ball.ySpeed = returns[0]
            ufo.health = returns[1]
            if ufo.health < 13:
                buildDefense = 1
            ball.xSpeed = returns[2]
            if ufo.health == 0:
                ufo.delete()


        if ufo.defense != 0:
            returns = ufoWallCollision(ball, ufo)
            ball.ySpeed = returns[0]
            ufo = returns[1]

        if level == 3 and ufo.health > 0:
            if ufo.cooldown == 0:
                ufo.shoot()
                ufo.cooldown = 40
            else:
                ufo.cooldown -= 1

        if len(ufo.bulletsX) > 0:
            ufo.bulletsY = ufo.updateBullets()

        if len(powerUps[3].bulletsX) > 0:
            powerUps[3].bulletsY = powerUps[3].updateBullets()

        returns = bulletPaddleCollision(paddle, ufo)
        if (livesLeft - returns[0]) < 0:
            break
        elif returns[0] != 0:
            powerUps = resetPowers(powerUps)
            print("\nHIT BY BOMBS!")
            livesLeft = livesLeft - returns[0]
            time.sleep(1)

        ufo.bulletsX = returns[1]
        ufo.bulletsY = returns[2]

        if len(powerUps[3].bulletsX) > 0:
            returns = bulletBrickCollision(powerUps[3], score, bricks)
            powerUps[3].bulletsX = returns[0]
            powerUps[3].bulletsY = returns[1]
            score = returns[2]
            bricks = returns[3]

        if powerUps[3].active == 2 and powerUps[3].cooldown > 0:
            powerUps[3].cooldown -= 1

        newValues = brickCollision(ball, bricks, score, nextPowerUp)
        ball.xPos = newValues[4]
        ball.yPos = newValues[5]
        ball.xSpeed = newValues[0]
        ball.ySpeed = newValues[1]
        bricks = newValues[2]
        score = newValues[3]
        collided = newValues[6]
        power = newValues[7]

        if power:
            found = 0
            for p in powerUps:
                if p.active == 1:
                    found = 1
                    break

            if not found:
                powerUps[nextPowerUp].active = 1
                powerUps[nextPowerUp].x = newValues[8]
                powerUps[nextPowerUp].y = newValues[9]
                nextPowerUp = (nextPowerUp+1)%4

        for powerUp in powerUps:
            if powerUp.active != 0:
                paddle = powerUp.updatePower(paddle)


        if ballDrop(ball):
            begin = 0
            ball.place()
            paddle.reset()
            ufo.reset()
            livesLeft -= 1
            powerUps = resetPowers(powerUps)
            print("\nLOST A LIFE!")
            time.sleep(1)

        if (len(bricks) <= unbreakable):
            if level == 3 and ufo.health ==  0:
                break
            begin = 0
            ball.place()
            paddle.reset()
            ufo.reset()
            returns = setBricks(level+1)
            bricks = returns[0]
            unbreakable = returns[1]
            limit = returns[2]
            powerUps = resetPowers(powerUps)
            timeAttack = 0
            timeoutLevel = 3000
            level += 1
            if level < 3:
                print("\nENTERING LEVEL: ", level)
                time.sleep(1)

        if begin:
            gameTime += 1
finally:
    termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
    fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)
    print('\nGame Over!')
