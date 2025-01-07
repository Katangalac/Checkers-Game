from typing import List
from src.base.utils import *

from src.base.checker import Checker
from src.base.square import Square


class CheckersBoard:
    def __init__(self):
        self.size = 10
        self.squares: List[List[Square]] = []
        self.checkers: List[Checker] = []
        self.checker_number = 20
        self.initialize_squares()
        self.initialize_starting_checkers()

    def initialize_squares(self) -> None:
        self.squares = [[Square(j, i) for i in range(self.size)] for j in range(self.size)]

    def initialize_starting_checkers(self) -> None:

        for position_list in self.get_black_starting_positions():
            for position in position_list:
                x, y = position
                checker = Checker(x, y, get_black_checker_color())
                self.set_checker_at(x, y, checker)
                self.checkers.append(checker)

        for position_list in self.get_white_starting_positions():
            for position in position_list:
                x, y = position
                checker = Checker(x, y, get_white_checker_color())
                self.set_checker_at(x, y, checker)
                self.checkers.append(checker)

    def get_size(self):
        return self.size

    def get_squares(self) -> List[List[Square]]:
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

    def get_checker_moves(self, row: int, col: int):
        moves = {}
        checker = self.get_checker_at(row, col)

        if not checker.is_king:
            if checker.get_color() == get_white_checker_color():
                possible_directions = [(-1, -1), (-1, 1)]
            else:
                possible_directions = [(1, -1), (1, 1)]

            for i, j in possible_directions:
                new_row = row + i
                new_col = col + j

                if self.is_in_bounds(new_row, new_col):
                    if self.is_empty(new_row, new_col):
                        moves[(new_row, new_col)] = False
                    elif self.are_opponents(row, col, new_row, new_col):
                        if self.is_in_bounds(new_row + i, new_col + j) and self.is_empty(new_row + i, new_col + j):
                            moves[(new_row + i, new_col + j)] = True
        else:
            possible_directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

            for i, j in possible_directions:
                new_row = row
                new_col = col

                while self.is_in_bounds(new_row + i, new_col + j):
                    new_row += i
                    new_col += j
                    if self.is_empty(new_row, new_col):
                        moves[(new_row, new_col)] = False
                    elif self.are_opponents(row, col, new_row, new_col):
                        if self.is_in_bounds(new_row + i, new_col + j) and self.is_empty(new_row + i, new_col + j):
                            moves[(new_row + i, new_col + j)] = True

        return moves

    def get_black_starting_positions(self):
        max_line = self.checker_number / (self.size / 2)
        positions = [[(j, i) for i in range(self.size) if j < max_line and (i + j) % 2 != 0] for j in
                     range(self.size)]

        return positions

    def get_white_starting_positions(self):
        max_line = self.checker_number / (self.size / 2)
        positions = [[(self.size - j - 1, i) for i in range(self.size) if j < max_line and (i + j) % 2 == 0] for j
                     in
                     range(self.size)]

        return positions

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

    def are_opponents(self, row1: int, col1: int, row2: int, col2: int) -> bool:
        if self.is_in_bounds(row1, col1) and self.is_in_bounds(row2, col2):
            if not (self.is_empty(row1, col1) and self.is_empty(row2, col2)):
                return self.get_checker_at(row1, col1).get_color() != self.get_checker_at(row2, col2).get_color()

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
        moves = self.get_checker_moves(checker.row, checker.get_col())
        return any(is_capture for is_capture in moves.values())

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
        moves = self.get_checker_moves(row, col)
        for move in moves:
            print(move, end=' ')
