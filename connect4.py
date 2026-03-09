def drawBoard(board):
    for row in board:
        print(row)
    print("")


def switchPlayer(player):
    if player == "X":
        return "O"
    else:
        return "X"


def dropPiece(board, player, column):
    for row in range(5, -1, -1):
        if board[row][column] == 0:
            board[row][column] = player
            return True
    return False


def checkWinner(board, player):

    
    for r in range(6):
        for c in range(4):
            if board[r][c] == player:
                if board[r][c+1] == player:
                    if board[r][c+2] == player:
                        if board[r][c+3] == player:
                            return True

    
    for r in range(3):
        for c in range(7):
            if board[r][c] == player:
                if board[r+1][c] == player:
                    if board[r+2][c] == player:
                        if board[r+3][c] == player:
                            return True

    
    for r in range(3):
        for c in range(4):
            if board[r][c] == player:
                if board[r+1][c+1] == player:
                    if board[r+2][c+2] == player:
                        if board[r+3][c+3] == player:
                            return True

    
    for r in range(3, 6):
        for c in range(4):
            if board[r][c] == player:
                if board[r-1][c+1] == player:
                    if board[r-2][c+2] == player:
                        if board[r-3][c+3] == player:
                            return True

    return False
 

def main():
    board = [
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0]
    ]

    player = "X"

    while True:
        drawBoard(board)

        col = int(input("Choose column (0-6): "))

        if dropPiece(board, player, col) == False:
            print("Column full. Try again.")
            continue

        if checkWinner(board, player):
            drawBoard(board)
            print(player, "wins!")
            break

        player = switchPlayer(player)


main()