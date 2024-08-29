class Checker:
    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col

    def __repr__(self):
        return f"Checker({self.row}, {self.col})"

    def __str__(self):
        return f"({self.row}, {self.col})"

    def get_row(self) -> int:
        return self.row

    def get_col(self) -> int:
        return self.col

    def set_row(self, new_row: int) -> None:
        self.row = new_row

    def set_col(self, new_col: int) -> None:
        self.col = new_col
