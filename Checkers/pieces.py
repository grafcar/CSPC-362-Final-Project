import pygame
from .constants import Red, White, SQUARE_SIZE, Grey

class Piece:
    Padding = 10
    Outline = 2

    def __init__(self, row, col, color,king):
        self.row = row
        self.col = col
        self.color = color
        self.king = king
        
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

    def make_king(self):
        self.king = 1

    def draw(self, win):
        radius = SQUARE_SIZE//2 - self.Padding
        pygame.draw.circle(win, Grey, (self.x, self.y), radius + self.Outline)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)
    
    def change_location(self,x,y):
        self.row = x
        self.col = y
        self.calc_pos()
        
    def __str__(self):
        return str(self.row)+str(self.col)+str(self.color)
    
    def __repr__(self):
        return f"{self.row}{self.col}{self.color}"