import os
from colorama import Fore, Style

class Board():
    width = 55
    height = 25

    def __init__(self):
        self.grid = [[' ' for x in range(55)] for y in range(25)]

    def printGrid(self, limit, level, score, livesLeft, gameTime, paddleStart, paddleSize, bricks, ball, powerUps, ufo):
        os.system('clear')
        gridString = ''
        printedUfo = 0


        for i in range(49):
            j = 0
            while j<56:

                if level == 3 and ufo.health > 0:
                    if i == 0 and j != 55:
                        if ufo.start == j:
                            gridString += '/'
                        elif ufo.start < j and j < (ufo.start+ufo.size-2):
                            gridString += '-'
                        elif j == ufo.start+ufo.size-2:
                            gridString += '\\'
                        elif ball.xPos == j and ball.yPos == i:
                            gridString += Style.RESET_ALL
                            gridString += 'O'
                        else:
                            gridString += ' '
                        j+=1
                        continue

                    elif i == 1 and j!=55:
                        if ufo.start == j:
                            gridString += '\\'
                        elif ufo.start < j and j < (ufo.start+ufo.size-2):
                            gridString += '-'
                        elif j == ufo.start+ufo.size-2:
                            gridString += '/'
                            printedUfo = 1
                        elif ball.xPos == j and ball.yPos == i:
                            gridString += Style.RESET_ALL
                            gridString += 'O'
                        else:
                            gridString += ' '
                        j+=1
                        continue

                    elif i == 3 and ufo.defense != 0 and j!=55:
                        if j%5==0 and ufo.walls[j//5].strength != 0:
                            gridString += Fore.YELLOW + '['
                            gridString += Fore.YELLOW + 'W'
                            gridString += Fore.YELLOW + 'W'
                            gridString += Fore.YELLOW + 'W'
                            gridString += Fore.YELLOW + ']'
                            j += 5
                        else:
                            if ball.xPos == j and ball.yPos == i:
                                gridString += Style.RESET_ALL
                                gridString += 'O'
                            else:
                                gridString += ' '
                            j += 1

                        continue


                if j == 55:
                    gridString += Style.RESET_ALL
                    gridString += '|'
                    j += 1

                elif ball.xPos == j and ball.yPos == i:
                    gridString += Style.RESET_ALL
                    gridString += 'O'
                    j += 1
                    continue

                elif i <= limit:
                    found = 0
                    for brick in bricks:
                        if brick.x == i and brick.y == j:
                            powerFound = 0
                            bombFound = 0
                            bulletFound = 0
                            shape = ''
                            offset = 0
                            for powerUp in powerUps:
                                if (powerUp.x >= j and powerUp.x <= j+4) and powerUp.y == i:
                                    powerFound = 1
                                    shape = powerUp.getShape()
                                    offset = powerUp.x - j
                                    break

                            if not powerFound and len(ufo.bulletsX)>0 and level==3:
                                for index, bomb in enumerate(ufo.bulletsX):
                                    if (bomb >= j and bomb <= j+4) and ufo.bulletsY[index] == i:
                                        bombFound = 1
                                        offset = bomb - j
                                        break
                            if brick.strength == 1:
                                gridString += Fore.CYAN

                                if powerFound and offset == 0:
                                    gridString += shape
                                elif bombFound and offset == 0:
                                    gridString += 'V'
                                else:
                                    gridString += '['
                                if powerFound and offset == 1:
                                    gridString += shape
                                elif bombFound and offset == 1:
                                    gridString += 'V'
                                else:
                                    gridString += 'H'
                                if powerFound and offset == 2:
                                    gridString += shape
                                elif bombFound and offset == 2:
                                    gridString += 'V'
                                else:
                                    gridString += 'H'
                                if powerFound and offset == 3:
                                    gridString += shape
                                elif bombFound and offset == 3:
                                    gridString += 'V'
                                else:
                                    gridString += 'H'
                                if powerFound and offset == 4:
                                    gridString += shape
                                elif bombFound and offset == 4:
                                    gridString += 'V'
                                else:
                                    gridString += ']'

                            elif brick.strength == 2:
                                gridString += Fore.YELLOW

                                if powerFound and offset == 0:
                                    gridString += shape
                                elif bombFound and offset == 0:
                                    gridString += 'V'
                                else:
                                    gridString += '['
                                if powerFound and offset == 1:
                                    gridString += shape
                                elif bombFound and offset == 1:
                                    gridString += 'V'
                                else:
                                    gridString += 'H'
                                if powerFound and offset == 2:
                                    gridString += shape
                                elif bombFound and offset == 2:
                                    gridString += 'V'
                                else:
                                    gridString += 'H'
                                if powerFound and offset == 3:
                                    gridString += shape
                                elif bombFound and offset == 3:
                                    gridString += 'V'
                                else:
                                    gridString += 'H'
                                if powerFound and offset == 4:
                                    gridString += shape
                                elif bombFound and offset == 4:
                                    gridString += 'V'
                                else:
                                    gridString += ']'

                            elif brick.strength == 3:
                                gridString += Fore.RED

                                if powerFound and offset == 0:
                                    gridString += shape
                                elif bombFound and offset == 0:
                                    gridString += 'V'
                                else:
                                    gridString += '['
                                if powerFound and offset == 1:
                                    gridString += shape
                                elif bombFound and offset == 1:
                                    gridString += 'V'
                                else:
                                    gridString += 'H'
                                if powerFound and offset == 2:
                                    gridString += shape
                                elif bombFound and offset == 2:
                                    gridString += 'V'
                                else:
                                    gridString += 'H'
                                if powerFound and offset == 3:
                                    gridString += shape
                                elif bombFound and offset == 3:
                                    gridString += 'V'
                                else:
                                    gridString += 'H'
                                if powerFound and offset == 4:
                                    gridString += shape
                                elif bombFound and offset == 4:
                                    gridString += 'V'
                                else:
                                    gridString += ']'

                            elif brick.strength == 5:
                                gridString += Fore.WHITE

                                if powerFound and offset == 0:
                                    gridString += shape
                                elif bombFound and offset == 0:
                                    gridString += 'V'
                                else:
                                    gridString += '['
                                if powerFound and offset == 1:
                                    gridString += shape
                                elif bombFound and offset == 1:
                                    gridString += 'V'
                                else:
                                    gridString += 'H'
                                if powerFound and offset == 2:
                                    gridString += shape
                                elif bombFound and offset == 2:
                                    gridString += 'V'
                                else:
                                    gridString += 'H'
                                if powerFound and offset == 3:
                                    gridString += shape
                                elif bombFound and offset == 3:
                                    gridString += 'V'
                                else:
                                    gridString += 'H'
                                if powerFound and offset == 4:
                                    gridString += shape
                                elif bombFound and offset == 4:
                                    gridString += 'V'
                                else:
                                    gridString += ']'

                            j += 5
                            found = 1
                            break

                    if found == 0:
                        powerFound = 0
                        bombFound = 0
                        bulletFound = 0
                        for powerUp in powerUps:
                            if powerUp.x == j and powerUp.y == i:
                                powerFound = 1
                                gridString += powerUp.getShape()
                                break
                        if not powerFound and len(ufo.bulletsX)>0 and level==3:
                            for index, bomb in enumerate(ufo.bulletsX):
                                if bomb == j and ufo.bulletsY[index] == i:
                                    gridString += 'V'
                                    bombFound = 1
                                    break
                        if not bombFound:
                            for index, bullet in enumerate(powerUps[3].bulletsX):
                                if bullet == j and powerUps[3].bulletsY[index] == i:
                                    gridString += '^'
                                    bulletFound = 1
                                    break
                        if not bombFound and not bulletFound and not powerFound:
                            gridString += ' '
                        j += 1

                elif i > limit and i < 48:
                    powerFound = 0
                    bombFound = 0
                    bulletFound = 0
                    for powerUp in powerUps:
                        if powerUp.x == j and powerUp.y == i:
                            powerFound = 1
                            gridString += powerUp.getShape()
                            break
                    if not powerFound and len(ufo.bulletsX)>0 and level==3:
                        for index, bomb in enumerate(ufo.bulletsX):
                            if bomb == j and ufo.bulletsY[index] == i:
                                gridString += 'V'
                                bombFound = 1
                                break
                    if not bombFound:
                        for index, bullet in enumerate(powerUps[3].bulletsX):
                            if bullet == j and powerUps[3].bulletsY[index] == i:
                                gridString += '^'
                                bulletFound = 1
                                break

                    if not bombFound and not bulletFound and not powerFound:
                        gridString += ' '
                    j += 1

                elif i == 48:
                    if j >= paddleStart and j < (paddleStart+paddleSize):
                        if powerUps[3].active == 2:
                            gridString += Fore.MAGENTA + '_'
                        else:
                            gridString += Style.RESET_ALL + '_'
                    else:
                        gridString += ' '
                    j += 1
            gridString += Style.RESET_ALL
            gridString += '\n'

        gridString += "\nTIME ELAPSED: "
        gridString += str(gameTime)
        gridString += "\nLIVES: "
        gridString += str(livesLeft)
        gridString += "\tLEVEL: "
        gridString += str(level)
        gridString += "\nSCORE: "
        gridString += str(score)
        if level == 3:
            gridString += "\nUFO HEALTH: "
            for i in range(ufo.health):
                gridString += '#'
        if powerUps[3].active == 2:
            gridString += "\nSHOOTER ABILITY EXPIRES IN: "
            gridString += str(powerUps[3].duration//10)
        print(gridString, end='')
