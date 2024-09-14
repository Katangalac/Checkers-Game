from src.base.checker import Checker


class Square:
    def __init__(self, row: int, col: int, checker: Checker = None):
        self.row = row
        self.col = col
        self.checker = checker

    def __str__(self):
        return f"[{self.row},{self.col}]"

    def __repr__(self):
        return f"Square[{self.row},{self.col}, {repr(self.checker)}]"

    def get_row(self) -> int:
        return self.row

    def get_col(self) -> int:
        return self.col

    def get_checker(self) -> Checker:
        return self.checker

    def set_checker(self, new_checker: Checker) -> None:
        self.checker = new_checker
        self.checker.set_row(self.row)
        self.checker.set_col(self.col)

    def remove_checker(self) -> None:
        self.checker = None

    def is_empty(self) -> bool:
        return self.checker is None

    def print_square(self) -> None:
        print(str(self), end=' ')
