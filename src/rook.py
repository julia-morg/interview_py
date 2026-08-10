from .figure import Figure


class Rook(Figure):
    def __str__(self):
        return "♜" if self.is_black else "♖"
