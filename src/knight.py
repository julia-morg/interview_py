from .figure import Figure


class Knight(Figure):
    def __str__(self):
        return "♞" if self.is_black else "♘"
