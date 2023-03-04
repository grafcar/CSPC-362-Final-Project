import pygame
from .constants import Red, White, SQUARE_SIZE, Grey

class Piece:
    Padding = 10
    Outline = 2

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        
        if self.color == Red:
            self.direction = -1
        else:
            self.direction = 1
        
        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2 
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2 
        # print(SQUARE_SIZE)
        # print(self.col,self.row, "Col, Row")
        # print(self.x, "x")
        # print(self.y, "y")

    def make_king(self):
        self.king = True

    def draw(self, win):
        radius = SQUARE_SIZE//2 - self.Padding
        pygame.draw.circle(win, self.color, (self.x, self.y), radius + self.Outline)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)
        
    def __repr__(self):
        return str(self.color)