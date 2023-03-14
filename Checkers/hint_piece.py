import pygame
from .constants import *

class Hint:
    Padding = 10
    Outline = 2

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def draw(self, win):
        print("Draw from hint called")
        radius = SQUARE_SIZE//2 - self.Padding
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)
    