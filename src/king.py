from .figure import Figure


class King(Figure):
    def __str__(self):
        return "♚" if self.is_black else "♔"
