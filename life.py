import pygame
from cell import Cell
from cfg import screen, width, height, cellSize
import sys
from time import sleep
import random

running = True
cells = [[Cell(i, j, 0) for j in range(0, height, cellSize)] for i in range(0, width, cellSize)]

def main():
    genPulsar()
    # genRandom(p = 0.75)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        drawAll()
        pygame.display.update()
        genNext()
        sleep(0.25)

def drawAll():
    for row in cells:
        for c in row:
            c.draw()
    
    # for i in range(0, 1000, 5):
    #     pygame.draw.rect(screen, (0,255,0), (0, i, 1000, 1))
    #     pygame.draw.rect(screen, (0,255,0), (i, 0, 1, 1000))


def genNext():
    invert = []
    for i in range(len(cells)):
        for j in range(len(cells[0])):
            n = numNeighbors(i, j)
            if cells[i][j].alive:
                if n < 2 or n > 3: #fewer than 2 neighbors or more than 3 dies
                    invert.append((i,j))
            else:
                if n == 3: #dead cell with 3 neighbors becomes live
                    invert.append((i,j))
    for i,j in invert:
        alive = cells[i][j].alive
        cells[i][j].setAlive((alive + 1) % 2)

def numNeighbors(x, y):
    max_x = len(cells)-1
    max_y = len(cells[0])-1
    n = 0
    if x > 0: 
        n += cells[x-1][y].alive
    if x < max_x:
        n += cells[x+1][y].alive
    if y > 0:
        n += cells[x][y-1].alive
    if y < max_y:
        n += cells[x][y+1].alive
    if x > 0 and y > 0:
        n += cells[x-1][y-1].alive
    if x > 0 and y < max_y:
        n += cells[x-1][y+1].alive
    if x < max_x and y > 0:
        n += cells[x+1][y-1].alive
    if x < max_x and y < max_y:
        n += cells[x+1][y+1].alive
    
    return n
    
def genRandom(p = 0.5):
    num = 0
    for i in range(len(cells)):
        for j in range(len(cells[0])):
            if random.uniform(0,1) < p:
                num += 1
                cells[i][j].setAlive(1)
    print(f'Starting with {num} out of {200*200} alive...')

def genPulsar():
    #top left L
    cells[100][100].setAlive(1)
    cells[100][101].setAlive(1)
    cells[100][102].setAlive(1)
    cells[101][102].setAlive(1)
    #top right L
    cells[106][100].setAlive(1)
    cells[106][101].setAlive(1)
    cells[106][102].setAlive(1)
    cells[105][102].setAlive(1)
    #left top L
    cells[96][104].setAlive(1)
    cells[97][104].setAlive(1)
    cells[98][104].setAlive(1)
    cells[98][105].setAlive(1)
    #left bottom L
    cells[98][109].setAlive(1)
    cells[98][110].setAlive(1)
    cells[97][110].setAlive(1)
    cells[96][110].setAlive(1)
    #right top L
    cells[110][104].setAlive(1)
    cells[109][104].setAlive(1)
    cells[108][104].setAlive(1)
    cells[108][105].setAlive(1)
    #right bottom L
    cells[108][109].setAlive(1)
    cells[108][110].setAlive(1)
    cells[109][110].setAlive(1)
    cells[110][110].setAlive(1)
    #bottom right L
    cells[105][112].setAlive(1)
    cells[106][112].setAlive(1)
    cells[106][113].setAlive(1)
    cells[106][114].setAlive(1)
    #bottom left L
    cells[101][112].setAlive(1)
    cells[100][112].setAlive(1)
    cells[100][113].setAlive(1)
    cells[100][114].setAlive(1)
    #bottom left shape
    cells[101][110].setAlive(1)
    cells[102][110].setAlive(1)
    cells[102][109].setAlive(1)
    cells[101][108].setAlive(1)
    cells[100][108].setAlive(1)
    cells[100][109].setAlive(1)
    #bottom right shape
    cells[104][110].setAlive(1)
    cells[105][110].setAlive(1)
    cells[104][109].setAlive(1)
    cells[105][108].setAlive(1)
    cells[106][108].setAlive(1)
    cells[106][109].setAlive(1)
    #top right shape
    cells[105][106].setAlive(1)
    cells[106][106].setAlive(1)
    cells[106][105].setAlive(1)
    cells[105][104].setAlive(1)
    cells[104][104].setAlive(1)
    cells[104][105].setAlive(1)
    #top left shape
    cells[102][105].setAlive(1)
    cells[102][104].setAlive(1)
    cells[101][104].setAlive(1)
    cells[100][105].setAlive(1)
    cells[100][106].setAlive(1)
    cells[101][106].setAlive(1)

if __name__ == '__main__':
    main()