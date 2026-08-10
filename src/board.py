from .bishop import Bishop
from .king import King
from .knight import Knight
from .pawn import Pawn
from .queen import Queen
from .rook import Rook

# Chess files (verticals a–h); ranks are horizontals 1–8.
FILES = "abcdefgh"


class Board:
    def __init__(self):
        self.figures = {}

        self.figures.setdefault("a", {})[1] = Rook(False)
        self.figures.setdefault("b", {})[1] = Knight(False)
        self.figures.setdefault("c", {})[1] = Bishop(False)
        self.figures.setdefault("d", {})[1] = Queen(False)
        self.figures.setdefault("e", {})[1] = King(False)
        self.figures.setdefault("f", {})[1] = Bishop(False)
        self.figures.setdefault("g", {})[1] = Knight(False)
        self.figures.setdefault("h", {})[1] = Rook(False)

        self.figures.setdefault("a", {})[2] = Pawn(False)
        self.figures.setdefault("b", {})[2] = Pawn(False)
        self.figures.setdefault("c", {})[2] = Pawn(False)
        self.figures.setdefault("d", {})[2] = Pawn(False)
        self.figures.setdefault("e", {})[2] = Pawn(False)
        self.figures.setdefault("f", {})[2] = Pawn(False)
        self.figures.setdefault("g", {})[2] = Pawn(False)
        self.figures.setdefault("h", {})[2] = Pawn(False)

        self.figures.setdefault("a", {})[7] = Pawn(True)
        self.figures.setdefault("b", {})[7] = Pawn(True)
        self.figures.setdefault("c", {})[7] = Pawn(True)
        self.figures.setdefault("d", {})[7] = Pawn(True)
        self.figures.setdefault("e", {})[7] = Pawn(True)
        self.figures.setdefault("f", {})[7] = Pawn(True)
        self.figures.setdefault("g", {})[7] = Pawn(True)
        self.figures.setdefault("h", {})[7] = Pawn(True)

        self.figures.setdefault("a", {})[8] = Rook(True)
        self.figures.setdefault("b", {})[8] = Knight(True)
        self.figures.setdefault("c", {})[8] = Bishop(True)
        self.figures.setdefault("d", {})[8] = Queen(True)
        self.figures.setdefault("e", {})[8] = King(True)
        self.figures.setdefault("f", {})[8] = Bishop(True)
        self.figures.setdefault("g", {})[8] = Knight(True)
        self.figures.setdefault("h", {})[8] = Rook(True)

    def move(self, move):
        import re

        match = re.match(r"^([a-h])(\d)-([a-h])(\d)$", move)
        if not match:
            raise Exception("Incorrect move")

        x_from, y_from, x_to, y_to = match.group(1), int(match.group(2)), match.group(3), int(match.group(4))

        if x_from in self.figures and y_from in self.figures[x_from]:
            self.figures.setdefault(x_to, {})[y_to] = self.figures[x_from][y_from]
            del self.figures[x_from][y_from]

    def dump(self):
        for y in range(8, 0, -1):
            print(f"{y} ", end="")
            for x in FILES:
                if x in self.figures and y in self.figures[x]:
                    print(self.figures[x][y], end="")
                else:
                    print("-", end="")
            print()
        print(f"  {FILES}")
