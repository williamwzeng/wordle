from TextClasses import *

class Board:

    def __init__(self, length, rows) -> None:
        self.length = length
        self.board = [["" for i in range(length)] for j in range(rows)]
        self.nextRow = 0

    def fillBoard(self, guess):
        self.board[self.nextRow] = [Letter(i) for i in guess]
        self.nextRow += 1