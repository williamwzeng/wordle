from TextClasses import *
from Board import *

class Game:


    def __init__(self, length, limit) -> None:
        self.attempts = 0
        self.length = length
        self.limit = limit
        self.board = Board(length, limit)
        self.guess = ""
        self.word = ""
        self.colorHistory = ""

    def play():
        pass

    def generateWord(self):
        self.word = Word.getRandomWord(self.length)

    def acceptGuess(self):
        guess = input("Enter your guess:")
        while not Word.isWord(guess) or len(guess) != self.length:
            guess = input("Please enter a valid English word of length " + self.length)
        self.guess = guess

    def checkGuess(self):
        self.board.fillBoard(self.guess)
        pass

    def getPerformance():
        pass
