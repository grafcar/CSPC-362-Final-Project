board = [[0, 1, 0, 1, 0, 1, 0, 1],
         [1, 0, 1, 0, 1, 0, 1, 0],
         [0, 1, 0, 1, 0, 1, 0, 1],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [2, 0, 2, 0, 2, 0, 2, 0],
         [0, 2, 0, 2, 0, 2, 0, 2],
         [2, 0, 2, 0, 2, 0, 2, 0]]

def print_board(board):
    print("  0 1 2 3 4 5 6 7 ")
    for i, row in enumerate(board):
        print(i, " ".join([str(x) for x in row]))

def get_move(player, board):
    print("Player", player)
    while True:
        start = input("Enter the starting position (row col): ")
        start = start.split()
        start_row = int(start[0])
        start_col = int(start[1])

        end = input("Enter the ending position (row col): ")
        end = end.split()
        end_row = int(end[0])
        end_col = int(end[1])

        if board[start_row][start_col] == player and board[end_row][end_col] == 0:
            board[start_row][start_col] = 0
            board[end_row][end_col] = player
            return board
        else:
            print("Invalid move, try again.")

player = 1
while True:
    print_board(board)
    board = get_move(player, board)
    if player == 1:
        player = 2
    else:
        player = 1
