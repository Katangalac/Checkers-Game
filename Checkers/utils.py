from typing import Tuple


def decode_position(position: str) -> Tuple[int, int]:
    l = position.removeprefix("(").removesuffix(")").split(",")
    return int(l[0]), int(l[1])


def get_black_checker_color() -> str:
    return "#000000"


def get_white_checker_color() -> str:
    return "#FFFFFF"
