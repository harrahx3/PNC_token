import Board

print("hello world")
Board.ConsoleGame()

for i in range(10):
    Board.play(Board.CURRENT_IS_RED, 2)
    Board.ConsoleGame()
    Board.nextPlayer()
    Board.play(Board.CURRENT_IS_RED, 3)
    Board.ConsoleGame()
    Board.nextPlayer()

