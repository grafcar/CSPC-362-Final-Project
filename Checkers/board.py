import pygame
from .constants import Black, Rows, Red, SQUARE_SIZE, Cols, White
from .pieces import Piece

class Board():
    def __init__(self):
        self.board = []
        self.selected_piece = None
        self.red_left = 12
        self.white_left = 12
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
            for col in range(Cols):              
                if col % 2 == ((row + 1) % 2):
                    if row < 3:
                        self.board[row].append(Piece(row, col, White,0))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, Red,0))
                    else:
                        self.board[row].append(0) 
                else:
                    self.board[row].append(0)
        print(self.board)
                   
    def draw(self, win):
        self.draw_squares(win)
        for row in range(Rows):
            for col in range (Cols):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win) #This is a Piece object!!
        #print("draw function\n",self.board)

    def select(self,x,y):
        piece = self.board[x][y]
        if piece == 0:
            return 0
        else:
            self.selected_piece = piece
            print("selected piece",self.selected_piece)
            return 1
        
    def move(self,x,y):
        piece = self.board[x][y]
        if piece == self.selected_piece:
            print("Same piece")
        elif piece == 0:
            if abs(x-self.selected_piece.row) == 1 and abs(y-self.selected_piece.col) == 1:   
                self.board[x][y] = Piece(x,y,self.selected_piece.color,0)
                self.board[self.selected_piece.row][self.selected_piece.col] = 0
                self.selected_piece = 0

            elif abs(x-self.selected_piece.row) == 2 and abs(y-self.selected_piece.col) == 2:
                mid_x = (int)((self.selected_piece.row+x)/2)
                mid_y = (int)((self.selected_piece.col+y)/2)
                print("row, col, x, y",self.selected_piece.row,self.selected_piece.col,x,y)
                # if (x-1 < 0 or y-1 < 0) or (x+1 > 8 or y+1 > 8):
                #     return
                if self.board[mid_x][mid_y] == 0:
                    return 
                if self.selected_piece.color != self.board[mid_x][mid_y].color:
                    eaten_piece = self.board[mid_x][mid_y]
                    if eaten_piece.color == Red:
                        self.red_left -= 1
                    else: 
                        self.white_left -= 1
                    self.board[mid_x][mid_y] = 0
                    self.board[self.selected_piece.row][self.selected_piece.col] = 0
                    self.board[x][y] = Piece(x,y,self.selected_piece.color,0)
                    self.selected_piece = 0
                    print("red white",self.red_left,self.white_left)

                else:
                    pass

            
            