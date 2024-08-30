# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from checkersboard import CheckersBoard
from boardsize import *
from utils import *


def print_hi(name):
    board = CheckersBoard(BoardSize.MEDIUM)
    board.print_board()
    #print(decode_position("(1,2)"))
    #board.print_white_starting_position()
    #board.print_black_starting_position()
    #print(board.get_legal_moves(6,5))
    #print(board.can_be_promoted(board.get_checker_at(3,4)))


if __name__ == '__main__':
    print_hi('PyCharm')
