import tkinter as tk

import Board

COLUMNS_WIDTH = 50
SPAN = 5

def clickOnColumn(event) :
    print("clicked at", event.x, event.y)
    row = event.y // COLUMNS_WIDTH
    columClicked = event.x // COLUMNS_WIDTH
    print("correpond to", row, columClicked)
    if Board.canPlay(columClicked) :
        rowPlayed, columnPlayed = Board.play(Board.CURRENT_IS_RED, columClicked)
        if Board.CURRENT_IS_RED:
            playerColor = 'red'
        else :
            playerColor = 'yellow'
        canvas.itemconfig(ovals[rowPlayed][columnPlayed], fill=playerColor)
        Board.nextPlayer()

root = tk.Tk()
root.geometry("600x200")
frame = tk.Frame()
frame.master.title("4 in a row")

canvas = tk.Canvas(frame)

canvas.create_rectangle(0, 0, Board.BOARD_COLUMS*COLUMNS_WIDTH, Board.BOARD_ROWS*COLUMNS_WIDTH, fill='blue', tags="board")
ovals = [[canvas.create_oval(j*COLUMNS_WIDTH + SPAN, i*COLUMNS_WIDTH + SPAN, (j+1)*COLUMNS_WIDTH - SPAN, (i+1)*COLUMNS_WIDTH - SPAN, fill="white", tags='board') for j in range(Board.BOARD_COLUMS)] for i in range(Board.BOARD_ROWS)]
# for i, row in enumerate(Board.board) :
#     for j, elmt in enumerate(row) :
#         canvas.create_oval(j*COLUMNS_WIDTH + SPAN, i*COLUMNS_WIDTH + SPAN, (j+1)*COLUMNS_WIDTH - SPAN, (i+1)*COLUMNS_WIDTH - SPAN, fill="white")


canvas.tag_bind('board', '<Button-1>', clickOnColumn)

canvas.pack(expand=True, fill='both')
frame.pack(expand=True, fill= 'both')

root.mainloop()



 
