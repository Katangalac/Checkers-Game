class Checker:
    def __init__(self, row: int, col: int, color: str = None, is_king: bool = False):
        self.row = row
        self.col = col
        self.color = color
        self.is_king = is_king

    def __repr__(self):
        return f"Checker({self.row},{self.col}, {self.color}, {self.is_king})"

    def __str__(self):
        return f"({self.row},{self.col})"

    def get_row(self) -> int:
        return self.row

    def get_col(self) -> int:
        return self.col

    def get_color(self):
        return self.color

    def set_row(self, new_row: int) -> None:
        self.row = new_row

    def set_col(self, new_col: int) -> None:
        self.col = new_col

    def set_position(self, new_row: int, new_col: int) -> None:
        self.row = new_row
        self.col = new_col

    def set_color(self, new_color) -> None:
        self.color = new_color

    def set_is_king(self, is_king) -> None:
        self.is_king = is_king

    def print_checker(self) -> None:
        print(str(self), end=' ')