import Board

def ConsoleGame() :
    for i in range(Board.BOARD_COLUMS) :
        print(i, end=' ')
    print()
    print()
    for row in Board.board :
        for elmt in row :
            print(elmt, end=' ')
        print()
    print()
    print()

print("hello world")
ConsoleGame()

while Board.getBoardStatus() == "ON_PROGRESS":
    if Board.CURRENT_IS_RED :
        player = "red"
    else :
        player = "yellow"
    columnToPlay = -1
    while not Board.canPlay(columnToPlay) :
        columnToPlay = int(input("Joueur " + player + " : "))
    Board.play(Board.CURRENT_IS_RED, columnToPlay)
    ConsoleGame()
    Board.nextPlayer()

