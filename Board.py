from TextClasses import *

class Board:

    def __init__(self, length, rows) -> None:
        self.length = length
        self.board = [["" for i in range(length)] for j in range(rows)]

    def fillBoard(self, guess):
        pass