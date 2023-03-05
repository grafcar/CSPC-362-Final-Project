<<<<<<< Updated upstream
rows, cols = 8,8
pieces = []
select = ''
move = ''
board = [[0 for x in range(rows)] for y in range(cols)] 
=======
import pygame
import time
from Checkers.constants import Width, Height
from Checkers.board import Board
>>>>>>> Stashed changes

def pieceInt():
    count = 0
    while count < 24:
        if count < 12:
            pieces[count] = "X"
        else:
            pieces[count] = "P"

def boardInt():
    for x in range(cols):
        #print(x)
        for y in range(rows):
            if x < 3:
                if x % 2 != 0 and y%2 !=0:
                    board[x][y] = "X"
                if x % 2 == 0 and y%2 ==0:
                    board[x][y] = "X"
            if x > 4:
                if x % 2 != 0 and y%2 !=0:
                    board[x][y] = "P"
                if x % 2 == 0 and y%2 ==0:
                    board[x][y] = "P"
            
def printBoard():
    counter = 0
    print("  0 1 2 3 4 5 6 7 ")
    for rows in board:
        print(counter,*rows,end='')
        counter += 1
        print()
    print()

def selectPiece(xy):
    if xy == '-1' or len(xy) < 2 or len(xy) >= 3:
        return False
    x = int(xy[0])
    y = int(xy[1])
    if (x < 0 or x > 7) and (y < 0 or y > 7):
        print("Selection out of bound")
        return False
    if board[x][y] == "X" or board[x][y] == "P":
        return True
    else:
        print("Invalid Selection")
        return False

def movePiece(xy,selection):
    if xy == '-1' or len(xy) < 2 or len(xy) >= 3:
        return False
    x = int(xy[0])
    y = int(xy[1])
    selectX = int(selection[0])
    selectY = int(selection[1])
    if (x < 0 or x > 7) and (y < 0 or y > 7):
        print("Out of bounds move X:",x,"Y:",y)
        return False
    if x == selectX and y == selectY:
        print("The move is the same as the section X:",x,"Y:",y)
        return False
    if abs(x-selectX) == 1 and abs(y-selectY) == 1:
        if board[x][y] == "X" or board[x][y] == "P":
            print("Unable to move, piece already in place X:",x,"Y:",y)
            return False
        else:
            if board[selectX][selectY] == "X":
                board[selectX][selectY] = 0
                board[x][y] = "X"
                return True
            elif board[selectX][selectY] == "P":
                board[selectX][selectY] = 0
                board[x][y] = "P"
                return True
    else:
        print("Selected piece",selectX,selectY)
        print("Invalid move",x,y)
        return False

<<<<<<< Updated upstream
boardInt()
printBoard()
=======
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
            if pygame.mouse.get_pressed()[0]:
                time.sleep(0.1)
                mouse_x, mouse_y = pygame.mouse.get_pos()
                selection = board.selection(mouse_y,mouse_x)
                if board.valid_selection(mouse_y,mouse_x): 
                    print("selection was valid, inside the while loop")               
                    while not pygame.mouse.get_pressed()[2]:
                        pygame.event.clear()
                        if pygame.mouse.get_pressed()[0]:                            
                            mouse_x, mouse_y = pygame.mouse.get_pos()
                            print("Press right mouse to exit")
                            board.move(mouse_y,mouse_x,selection)
                            break
                    print("Out of loop")
            #print("out of all ifs")

>>>>>>> Stashed changes

while select != '-1':
    select = input("Select your piece: ")
    if selectPiece(select):
        move = input("Enter your move: ")
        while movePiece(move,select) == False:
            move = input("Please enter a valid move: ")
    print()
    printBoard()
