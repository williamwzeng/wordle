from mimetypes import init
from tokenize import String
from Color import Color

class Letter:

    character = ""
    color = Color.GRAY

    def __init__(self, char) -> None:
        self.character = char

    def __repr__(self) -> str:
        return self.character

    def __str__(self) -> str:
        pass    

    def markColor(self, word, pos, count = 1):
        if self.character in word:
            if self.character == word[pos]:
                self.color = Color.GREEN
            elif word.count(self.character) >= count:
                self.color = Color.YELLOW


class Word:

    WORDS = set(open("words_alpha.txt").read().split())
    

    def __init__(self) -> None:
        pass


    def getRandomWord(self):
        result = Word.WORDS.pop()
        Word.WORDS.add(result)
        return result

