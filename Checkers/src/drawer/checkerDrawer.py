from tkinter import *


class CheckerDrawer:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.color = color
        self.is_selected = False

    def draw(self, x1, y1, x2, y2):
        self.canvas.create_oval(x1, y1, x2, y2, outline='black', fill=self.color)

    def set_is_selected(self, selected):
        self.is_selected = selected

