BOARD_ROWS = 6
BOARD_COLUMS = 7
CURRENT_IS_RED = True

board = [[0 for j in range(BOARD_COLUMS)] for i in range (BOARD_ROWS)]

def clearBoard() :
    board = [[0 for j in range(BOARD_COLUMS)] for i in range (BOARD_ROWS)]

def canPlay(columnIndex) :
    return not board[0][columnIndex]

def play(isRed, columnIndex) :
    if canPlay(columnIndex) :
        row = 0
        while row+1 < BOARD_ROWS and board[row+1][columnIndex] == 0:
            row += 1
        if isRed :
            board[row][columnIndex] = 1
        else :
            board[row][columnIndex] = 2
        return row, columnIndex

def nextPlayer() :
    global CURRENT_IS_RED
    CURRENT_IS_RED = not CURRENT_IS_RED
    return CURRENT_IS_RED

def ConsoleGame() :
    for i in range(BOARD_COLUMS) :
        print(i, end=' ')
    print()
    print()
    for row in board :
        for elmt in row :
            print(elmt, end=' ')
        print()
    print()
    print()

def getBoardStatus() :
    won = False
    if won :
        if CURRENT_IS_RED :
            return "RED_WON"
        else :
            return "YELLOW_WON"
    full = True
    for c in board[0] :
        if c == 0 :
            full = False
    if full :
        return "BOARD_FULL"
    else :
        return "ON_PROGRESS"
