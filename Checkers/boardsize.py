from enum import Enum


class BoardSize(Enum):
    SMALL = 8
    MEDIUM = 10
    LARGE = 12

    def get_size(self) -> int:
        return self.value

    def get_board_size(self):
        return f"{self.get_size()}x{self.get_size()}"
