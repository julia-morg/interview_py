from .figure import Figure


class Pawn(Figure):
    def __str__(self):
        return "♟" if self.is_black else "♙"
