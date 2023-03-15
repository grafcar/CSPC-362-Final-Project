from Checkers.board import *
from Checkers.hint_piece import *

class Main_Game():

    def __init__(self):
        self.selected_piece = 0
        self.selected = False
        self.board = Board()
        self.draw_board = self.board
        self.board = self.board.board
        self.player_turn = 0
        #self.x = self.y = 0
        self.reds_left = self.whites_left = 12
        self.red_direction = -1
        self.white_direction = 1
        self.hint = []
        #print("BOARD FROM MAIN",self.board)
        # self.board.draw(WIN)

    def draw(self):
        self.draw_board.draw(WIN)
        if self.selected:
            print("inside the for loop for hint",self.hint)
            for x in self.hint:
                x.draw(WIN)

    def select(self,x,y):
        if not self.selected:
            self.hint = []
            piece = self.board[x][y]
            if piece == 0:
                print("No piece selected")
                
            else:
                if piece.color == Red and self.player_turn % 2 == 0:
                    self.selected = True
                    self.selected_piece = piece
                    self.player_turn += 1
                    print("RED TURN")
                elif piece.color == White and self.player_turn % 2 == 1:
                    self.selected = True
                    self.selected_piece = piece
                    self.player_turn += 1
                    print("WHITE TURN")
                
                #piece.draw_target(WIN,x,y)
                #if (x-1 > 0 and x +1 < 7)and(y-1 > 0 and y+1 < 7):
                print("X AND Y FROM HINT",x,y)
                if piece.color == White:
                    if x+1 <= 7:
                        if y-1 >= 0:
                            if self.board[x+1][y-1] == 0:
                                self.hint.append(Hint(x+1,y-1,Green))
                                # hint.draw(WIN)
                                
                                print("HELLO1")
                        if y+1 <= 7:
                            if self.board[x+1][y+1] == 0:
                                self.hint.append(Hint(x+1,y+1,Green))
                                # hint.draw(WIN)
                                
                                print("HELLO2")
                if piece.color == Red:
                    if x-1 >= 0:
                        if y-1 >= 0:
                            if self.board[x-1][y-1] == 0:
                                self.hint.append(Hint(x-1,y-1,Green))
                                # hint.draw_target(WIN)
                                
                                print("HELLO3")
                        if y+1 <= 7:
                            if self.board[x-1][y+1] == 0:
                                self.hint.append(Hint(x-1,y+1,Green))
                                # hint.draw(WIN)
                                
                                print("HELLO4")
                print("selected piece",self.selected_piece)
    
    def move(self,x,y):
        print("OUTSIDE OF MOVE")
        if self.selected:
            print("INSIDE OF MOVE")
            self.draw_hint = False
            #self.hint = []
            piece = self.board[x][y]

            if piece == 0:
                if abs(x-self.selected_piece.row) == 1 and abs(y-self.selected_piece.col) == 1:   
                    # self.board[x][y] = Piece(x,y,self.selected_piece.color,0)
                    # self.board[self.selected_piece.row][self.selected_piece.col] = 0
                    # self.selected_piece = 0
                    if self.selected_piece.color == Red and self.selected_piece.row-1 == x:
                        self.board[x][y] = self.selected_piece
                        self.board[self.selected_piece.row][self.selected_piece.col] = 0
                        self.selected_piece.row = x
                        self.selected_piece.col = y
                        self.selected_piece.calc_pos()
                        self.selected_piece = 0
                        self.selected = False
                        print("MOVEMENT FROM RED")
                    elif self.selected_piece.color == White and self.selected_piece.row+1 == x:
                        self.board[x][y] = self.selected_piece
                        self.board[self.selected_piece.row][self.selected_piece.col] = 0
                        self.selected_piece.row = x
                        self.selected_piece.col = y
                        self.selected_piece.calc_pos()
                        self.selected_piece = 0
                        self.selected = False
                        print("MOVEMENT FROM WHITE")
                elif abs(x-self.selected_piece.row) == 2 and abs(y-self.selected_piece.col) == 2:
                    mid_x = (int)((self.selected_piece.row+x)/2)
                    mid_y = (int)((self.selected_piece.col+y)/2)
                    self.selected = False
                    print("row, col, x, y",self.selected_piece.row,self.selected_piece.col,x,y)
                    # if (x-1 < 0 or y-1 < 0) or (x+1 > 8 or y+1 > 8):
                    #     return
                    if self.board[mid_x][mid_y] == 0:
                        return 
                    if self.selected_piece.color != self.board[mid_x][mid_y].color:
                        eaten_piece = self.board[mid_x][mid_y]
                        if eaten_piece.color == Red:
                            self.reds_left -= 1
                        else: 
                            self.whites_left -= 1
                        
                        self.board[mid_x][mid_y] = 0
                        self.board[x][y] = self.selected_piece
                        self.board[self.selected_piece.row][self.selected_piece.col] = 0
                        self.selected_piece.row = x
                        self.selected_piece.col = y
                        self.selected_piece.calc_pos()
                        self.selected_piece = 0
                        #Previous method, it creates a new Piece 
                        # self.board[self.selected_piece.row][self.selected_piece.col] = 0
                        # self.board[x][y] = Piece(x,y,self.selected_piece.color,0)
                        # self.selected_piece = 0
                        print("red white",self.reds_left,self.whites_left)
            # elif piece == self.selected_piece:
            #     print("Same piece")
            #     self.selected = False
            # else:
            #     return                   