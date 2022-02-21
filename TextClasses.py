from Color import Color

class Letter:

    character = ""
    color = Color.GRAY

    def __init__(self, char) -> None:
        self.character = char

    def __repr__(self) -> str:
        return self.character

    def __str__(self) -> str:
        return self.character + " (" + self.color.name + ")" 

    def markColor(self, word, pos, count = 1):
        if self.character in word:
            if self.character == word[pos]:
                self.color = Color.GREEN
            elif word.count(self.character) >= count:
                self.color = Color.YELLOW


class Word:

    WORDS = set(open("words_alpha.txt").read().split())
    length = 5
    letters = []
    validWords = {""}

    def __init__(self, word) -> None:
        self.letters = [Letter(i) for i in word]
        self.length = len(word)

    def getRandomWord(length) -> str:
        if len(Word.validWords) < 2:
            Word.validWords = {w for w in Word.WORDS if len(w) == length}
        return Word.validWords.pop()

    def isWord(guess) -> bool:
        return guess in Word.WORDS

    
