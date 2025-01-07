import tkinter as tk
from tkinter import *
import os

from PIL import Image, ImageTk
from src.drawer.squareDrawer import *
from src.drawer.checkerDrawer import *
from src.base.checkersboard import CheckersBoard
from src.base.utils import *


class BoardDrawer:
    def __init__(self, canvas, square_size=70):
        self.canvas = canvas
        self.square_size = square_size
        self.checkerBoard = CheckersBoard()

    def draw_board(self):
        for row in range(10):
            for col in range(10):
                x1, y1 = col * self.square_size, row * self.square_size
                x2, y2 = x1 + self.square_size, y1 + self.square_size
                square_drawer = SquareDrawer(canvas=self.canvas, color="#9e5902", size=self.square_size)
                if (row + col) % 2 == 0:
                    square_drawer = SquareDrawer(canvas=self.canvas, color="#fbd39f", size=self.square_size)
                square_drawer.draw(x1, y1, x2, y2)

    def draw_pieces(self):
        white_pieces_position = self.checkerBoard.get_white_starting_positions()
        black_pieces_position = self.checkerBoard.get_black_starting_positions()
        padding = 6

        for position_list in white_pieces_position:
            for position in position_list:
                y, x = position
                x1, y1 = x * self.square_size, y * self.square_size
                x2, y2 = x1 + self.square_size, y1 + self.square_size
                checker_drawer = CheckerDrawer(self.canvas, "white")
                checker_drawer.draw(x1 + padding, y1 + padding, x2 - padding, y2 - padding)

        for position_list in black_pieces_position:
            for position in position_list:
                y, x = position
                x1, y1 = x * self.square_size, y * self.square_size
                x2, y2 = x1 + self.square_size, y1 + self.square_size
                checker_drawer = CheckerDrawer(self.canvas, "black")
                checker_drawer.draw(x1 + padding, y1 + padding, x2 - padding, y2 - padding)

    def draw(self):
        self.draw_board()
        self.draw_pieces()
