from typing import Tuple


def decode_position(position: str) -> Tuple[int, int]:
    l = position.removeprefix("(").removesuffix(")").split(",")
    return int(l[0]), int(l[1])


def get_black_checker_color() -> str:
    return "#000000"


def get_white_checker_color() -> str:
    return "#FFFFFF"


def get_square_on_anti_diagonal(from_x, from_y, to_x, to_y):
    if from_x + from_y == to_x + to_y:
        diagonal = []
        if from_x > to_x:
            diagonal = [f"({from_x - i - 1},{from_y + i + 1})" for i in range(from_x - to_x - 1)]
        else:
            diagonal = [f"({from_x + i + 1},{from_y - i - 1})" for i in range(to_x - from_x - 1)]
        return diagonal


def get_square_on_main_diagonal(from_x, from_y, to_x, to_y):
    if from_x - from_y == to_x - to_y:
        diagonal = []
        if from_x > to_x:
            diagonal = [f"({from_x - i - 1},{from_y - i - 1})" for i in range(from_x - to_x - 1)]
        else:
            diagonal = [f"({from_x + i + 1},{from_y + i + 1})" for i in range(to_x - from_x - 1)]
        return diagonal
