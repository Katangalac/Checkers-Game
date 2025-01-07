from src.base.square import Square
import pygame
import sys

import tkinter as tk
from tkinter import *
import os

from PIL import Image, ImageTk
from src.base.utils import *


class SquareDrawer:
    def __init__(self, canvas, color, size=70):
        self.canvas = canvas
        self.size = size
        self.color = color
        self.is_selected = False
        self.is_regularMove = False
        self.is_captureMove = False

    def draw(self, x1, y1, x2, y2):
        self.canvas.create_rectangle(x1, y1, x2, y2, outline='black', fill=self.color)

    def set_is_selected(self, selected):
        self.is_selected = selected

    def set_is_regular_move(self, is_regular_move):
        self.is_regularMove = is_regular_move

    def set_is_capture_move(self, is_capture_move):
        self.is_captureMove = is_capture_move
