from enum import Enum


def get_board_size_from(size):
    if BoardSize.SMALL.get_size() == size:
        return BoardSize.SMALL.get_checker_number()
    elif BoardSize.MEDIUM.get_size() == size:
        return BoardSize.MEDIUM.get_checker_number()
    elif BoardSize.LARGE.get_size() == size:
        return BoardSize.LARGE.get_checker_number()


class BoardSize(Enum):
    SMALL = 8
    MEDIUM = 10
    LARGE = 12

    def get_size(self) -> int:
        return self.value

    def get_board_size(self):
        return f"{self.get_size()}x{self.get_size()}"

    def get_checker_number(self) -> int | None:
        if self == BoardSize.SMALL:
            return 12
        elif self == BoardSize.MEDIUM:
            return 20
        elif self == BoardSize.LARGE:
            return 30
        else:
            return None
