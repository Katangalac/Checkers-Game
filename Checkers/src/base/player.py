
class Player:
    def __init__(self, name: str, color: str):
        self.name = name
        self.color = color
        self.checker_number = 20

    def get_name(self) -> str:
        return self.name

    def get_color(self) -> str:
        return self.color

    def get_checker_number(self) -> int:
        return self.checker_number

    def set_checker_number(self, new_checker_number: int) -> None:
        self.checker_number = new_checker_number
