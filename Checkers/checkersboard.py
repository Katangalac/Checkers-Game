from boardsize import BoardSize
from typing import List

from checker import Checker
from square import Square


class CheckersBoard:
    def __init__(self, board_size: BoardSize):
        self.size = board_size.get_size()
        self.squares: List[List[Square]] | None = None
        self.initialize_squares()

    def initialize_squares(self) -> None:
        self.squares = [[Square(x, y) for x in range(self.size)] for y in range(self.size)]

    def get_size(self):
        return self.size

    def get_squares(self) -> List[List[Square]] | None:
        return self.squares

    def get_board_size(self):
        return f"{self.size}x{self.size}"

    def get_square_at(self, row: int, col: int) -> Square:
        if self.is_in_bounds(row, col):
            return self.squares[row][col]

    def get_checker_at(self, row: int, col: int) -> Checker:
        if self.is_in_bounds(row, col):
            return self.get_square_at(row, col).get_checker()

    def set_size(self, new_size: int) -> None:
        self.size = new_size
        self.initialize_squares()

    def set_checker_at(self, row: int, col: int, checker: Checker):
        if self.is_in_bounds(row, col):
            self.get_square_at(row, col).set_checker(checker)

    def put_checker_at(self, row: int, col: int):
        if self.is_in_bounds(row, col):
            self.get_square_at(row, col).set_checker(Checker(row, col))

    def move_checker(self, from_x: int, from_y: int, to_x: int, to_y: int):
        if self.is_in_bounds(from_x, from_y) and self.is_in_bounds(to_x, to_y):
            if self.get_square_at(from_x, from_y).get_checker() is not None and self.is_empty(to_x, to_y):
                self.set_checker_at(to_x, to_y, self.get_checker_at(from_x, from_y))
                self.remove_checker_at(from_x, from_y)

    def remove_checker_at(self, row: int, col: int):
        if self.is_in_bounds(row, col):
            self.get_square_at(row, col).remove_checker()

    def is_empty(self, row: int, col: int) -> bool:
        if self.is_in_bounds(row, col):
            return self.get_square_at(row, col).is_empty()

    def is_in_bounds(self, x: int, y: int) -> bool:
        return 0 <= x < self.size and 0 <= y < self.size

    def print_board(self):
        for square_list in self.squares:
            for square in square_list:
                print(str(square), end=' ')
            print()
