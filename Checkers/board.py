import pygame
from .constants import Black, Rows, Red, SQUARE_SIZE, Cols, White
from .pieces import Piece

class Board:
    def __init__(self):
        self.board = []
        self.xyCoordinate = []
        self.selected_piece = None
        self.red_left = self.white_left = 12
        self.red_kings = self.white_kings = 0
        self.create_board()

    def draw_squares(self, win):
        win.fill(Black)
        for row in range (Rows):
            for col in range(row % 2, Rows, 2):
                pygame.draw.rect(win, Red, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def create_board(self):
        for row in range(Rows):
            self.board.append([]) # 2d array at the start of each row
            self.xyCoordinate.append([])
            for col in range(Cols):
                print("start of for loop")
                if col % 2 == ((row + 1) % 2):
                    if row < 3:
                        self.xyCoordinate[row].append([row*SQUARE_SIZE,col*SQUARE_SIZE])
                        print(self.xyCoordinate)
                        self.board[row].append(Piece(row, col, White))
                    elif row > 4:
                        self.xyCoordinate[row].append([row*SQUARE_SIZE,col*SQUARE_SIZE])
                        print(self.xyCoordinate)
                        self.board[row].append(Piece(row, col, Red))
                    else:
                        self.xyCoordinate[row].append([])
                        self.board[row].append(0)
                    print("end of for loop")
                else:
                    self.xyCoordinate[row].append([])
                    self.board[row].append(0)
    
    def draw(self, win):
        self.draw_squares(win)
        for row in range(Rows):
            for col in range (Cols):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)

    def getPieceCoordinates(self,x,y):
        print("X Mouse Coordinate:",x,"Y Mouse Coordinate:",y)
        print(self.xyCoordinate[y//100][x//100])
