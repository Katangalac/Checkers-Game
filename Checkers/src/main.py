# This is a sample Python script.
# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import tkinter as tk

from src.base.checkersboard import CheckersBoard
from src.base.boardsize import *
from src.drawer.squareDrawer import SquareDrawer
from src.drawer.boardDrawer import BoardDrawer
from src.base.utils import *


def print_hi(name):
    board = CheckersBoard(BoardSize.MEDIUM)
    board.print_board()
    # board.print_white_starting_position()
    # board.print_black_starting_position()
    # board.set_checker_at(5,6, Checker(5,6,get_black_checker_color(), True))
    # print(board.get_legal_moves(6,5))
    # print(board.can_be_promoted(board.get_checker_at(3,4)))
    # print(board.can_capture(board.get_checker_at(6,5)))
    # print(get_square_on_main_diagonal(5,4,9,8))


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Checkers Game")

    frame = tk.Frame(root, padx=68, pady=68)
    frame.pack(fill=tk.BOTH, expand=True)

    canvas = tk.Canvas(frame, width=800, height=800)
    canvas.pack(fill=tk.BOTH, expand=True)

    board_drawer = BoardDrawer(canvas, 80, '../../resources/images/darkWood5.jpg',
                               '../../resources/images/lightWood.jpg')
    board_drawer.draw()

    root.mainloop()
