rows, cols = 8,8
pieces = []
select = ''
move = ''
board = [[0 for x in range(rows)] for y in range(cols)] 

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

boardInt()
printBoard()

while select != '-1':
    select = input("Select your piece: ")
    if selectPiece(select):
        move = input("Enter your move: ")
        while movePiece(move,select) == False:
            move = input("Please enter a valid move: ")
    print()
    printBoard()
