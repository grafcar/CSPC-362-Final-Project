import pygame
from .constants import Black, Rows, Red, SQUARE_SIZE, Cols, White
from .pieces import Piece

class Board():
    def __init__(self):
        self.board = []
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
            for col in range(Cols):              
                if col % 2 == ((row + 1) % 2):
                    if row < 3:
                        self.board[row].append(Piece(row, col, White))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, Red))
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
                    
    def selection(self,x,y):
        piece = self.board[x//100][y//100]
        if self.valid_selection(x,y):
            return piece.piece_location()
        else:
            return 0

    def valid_selection(self,x,y):
        print("Inside select")
        print("X Mouse Coordinate:",x,"\nY Mouse Coordinate:",y)        
        piece = self.board[x//100][y//100]
        print("from valid selection, piece",piece)
        if piece == 0: #if the sprintelection (or click) is NOT on a piece
            #print("Please select a piece!")
            return False
        else: #elif the selection is a piece
            print("from else, valid selection",piece.piece_location())
            return True

    def move(self,x,y,selection):
        print("Inside move")
        print("X Mouse Coordinate:",x,"\nY Mouse Coordinate:",y)
        print("this is the selection",selection)
        move = self.board[x//100][y//100]
        print("this is the move",move)
        print("this is x//100",x//100,"this is y//100",y//100)
        #move_x = move.get_x_location()//100
        #move_y = move.get_y_location()//100
        selection_x = selection[0]//100
        selection_y = selection[1]//100
        #print("this is the board",self.board[y//100][x//100])

        if abs((x//100)-selection_x) == 0 and abs((y//100)-selection_y) == 0: 
            print("Your selected piece is the same as your move")
            return False
        if abs((x//100)-selection_x) == 1 and abs((y//100)-selection_y) == 1:
            print("hello")
            if move == 0:
                print("the move was read")
                print(self.board)
                print("selection x ",selection_x,"selection y",selection_y)
                print("move x",x//100,"move y",y//100)
                temp = self.board[selection_x][selection_y]
                #temp2 = self.board[x//100][y//100]
                print("temp(selection board)",temp)
                print("board before temp",self.board[x//100][y//100])
                self.board[x//100][y//100] = Piece(x//100,y//100,temp.color)
                print("board after temp",self.board[x//100][y//100])  
                self.board[selection_x][selection_y] = 0
                print("the selection board",self.board[selection_x][selection_y])
                print(self.board)
                
            else:
                print("Piece already there!")
        else:
            print("Invalid move")
