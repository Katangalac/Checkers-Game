from boardsize import *
from typing import List
from utils import *

from checker import Checker
from square import Square


class CheckersBoard:
    def __init__(self, board_size: BoardSize):
        self.size = board_size.get_size()
        self.squares: List[List[Square]] | None = []
        self.checkers: List[Checker] | None = []
        self.checker_number = board_size.get_checker_number()
        self.initialize_squares()
        self.initialize_starting_checkers()

    def initialize_squares(self) -> None:
        self.squares = [[Square(j, i) for i in range(self.size)] for j in range(self.size)]

    def initialize_starting_checkers(self) -> None:

        for position_list in self.get_black_starting_positions():
            for position in position_list:
                x, y = decode_position(position)
                checker = Checker(x, y, get_black_checker_color())
                self.set_checker_at(x, y, checker)
                self.checkers.append(checker)

        for position_list in self.get_white_starting_positions():
            for position in position_list:
                x, y = decode_position(position)
                checker = Checker(x, y, get_white_checker_color())
                self.set_checker_at(x, y, checker)
                self.checkers.append(checker)

    def get_size(self):
        return self.size

    def get_squares(self) -> List[List[Square]] | None:
        return self.squares

    def get_checkers(self) -> List[Checker]:
        return self.checkers

    def get_board_size(self):
        return f"{self.size}x{self.size}"

    def get_square_at(self, row: int, col: int) -> Square:
        if self.is_in_bounds(row, col):
            return self.squares[row][col]

    def get_checker_at(self, row: int, col: int) -> Checker:
        if self.is_in_bounds(row, col):
            return self.get_square_at(row, col).get_checker()

    def get_legal_moves(self, row: int, col: int):
        moves = []
        checker = self.get_checker_at(row, col)
        print(checker)

        if checker is not None:
            if not checker.is_king:
                if checker.get_color() == get_black_checker_color():
                    self.add_if_valid(moves, checker.get_row() + 1, checker.get_col() + 1)
                    self.add_if_valid(moves, checker.get_row() + 1, checker.get_col() - 1)
                elif checker.get_color() == get_white_checker_color():
                    self.add_if_valid(moves, checker.get_row() - 1, checker.get_col() - 1)
                    self.add_if_valid(moves, checker.get_row() - 1, checker.get_col() + 1)
            else:
                for i in range(self.size):
                    self.add_if_valid(moves, checker.get_row() - i, checker.get_col() - i)
                    self.add_if_valid(moves, checker.get_row() - i, checker.get_col() + i)
                    self.add_if_valid(moves, checker.get_row() + i, checker.get_col() - i)
                    self.add_if_valid(moves, checker.get_row() + i, checker.get_col() + i)

        return moves

    def get_black_starting_positions(self):
        max_line = self.checker_number / (self.size / 2)
        positions = [[f"({j},{i})" for i in range(self.size) if j < max_line and (i + j) % 2 != 0] for j in
                     range(self.size)]

        return positions

    def get_white_starting_positions(self):
        max_line = self.checker_number / (self.size / 2)
        positions = [[f"({self.size - j - 1},{i})" for i in range(self.size) if j < max_line and (i + j) % 2 == 0] for j in
                     range(self.size)]

        return positions

    def add_if_valid(self, moves: List[str], row: int, col: int):
        if self.is_in_bounds(row, col) and self.is_empty(row, col):
            moves.append(f"({row},{col})")

    def set_size(self, new_size: int) -> None:
        self.size = new_size
        self.checker_number = get_board_size_from(new_size)
        self.initialize_squares()
        self.initialize_starting_checkers()

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

    def can_be_promoted(self, checker: Checker) -> bool:
        if checker.get_color() == get_black_checker_color():
            promote_line = [f"({self.size - 1},{i})" for i in range(self.size)]
            print(promote_line)
            if str(checker) in promote_line:
                return True
            else:
                return False
        elif checker.get_color() == get_white_checker_color():
            promote_line = [f"(0,{i})" for i in range(self.size)]
            print(promote_line)
            if str(checker) in promote_line:
                return True
            else:
                return False

    def can_capture(self, checker: Checker) -> bool:
        # TODO : Must be implemented
        pass

    def get_capture_paths(self, checker: Checker):
        # TODO : Must be implemented
        pass
    def print_board(self):
        for square_list in self.squares:
            for square in square_list:
                square.print_square()
            print()

    def print_black_starting_position(self):
        for square_list in self.get_black_starting_positions():
            for square in square_list:
                print(square, end=' ')
            print()

    def print_white_starting_position(self):
        for square_list in self.get_white_starting_positions():
            for square in square_list:
                print(square, end=' ')
            print()

    def print_legal_moves(self, row: int, col: int):
        moves = self.get_legal_moves(row, col)
        for move in moves:
            print(move, end=' ')
