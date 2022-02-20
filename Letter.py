import Color

class Letter:

    character = ""
    color = Color.GRAY

    def __init__(self, char) -> None:
        self.character = char

    def __repr__(self) -> str:
        return self.character

    def __str__(self) -> str:
        pass    

