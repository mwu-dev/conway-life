import pygame
from cfg import screen, black, white, cellSize

class Cell:
    def __init__(self, x, y, alive):
        self.x = x
        self.y = y
        self.alive = alive

    def setAlive(self, alive):
        self.alive = alive

    def draw(self):
        if self.alive:
            pygame.draw.rect(screen, white, (self.x, self.y, cellSize, cellSize))
        else:
            pygame.draw.rect(screen, black, (self.x, self.y, cellSize, cellSize))