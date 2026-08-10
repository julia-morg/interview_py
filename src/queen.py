from .figure import Figure


class Queen(Figure):
    def __str__(self):
        return "♛" if self.is_black else "♕"
