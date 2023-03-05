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

    def make_king(self):
        self.king = True

    def draw(self, win):
        radius = SQUARE_SIZE//2 - self.Padding
        pygame.draw.circle(win, self.color, (self.x, self.y), radius + self.Outline)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)
    
    def piece_location(self):
        xy_location = [self.y,self.x]
        print("from piece location",xy_location)
        return xy_location
        
    def __str__(self):
        return str(self.row)+str(self.col)+str(self.color)
    
    def __repr__(self):
        return f"{self.row}{self.col}{self.color}"