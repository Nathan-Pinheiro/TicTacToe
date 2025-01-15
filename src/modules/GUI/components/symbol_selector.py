import customtkinter as ctk
from CTkColorPicker import *
import tkinter as tk
from modules.GUI.components.symbols import drawCross, drawCircle, drawTriangle, drawStar, drawSquare, drawHexagon, drawRhombus

class SymbolSelector(ctk.CTkFrame):

    def __init__(self, parent, symbol="cross", disabled_symbols=[], **kwargs):
        super().__init__(parent, **kwargs)
        self.symbols = ["cross", "circle", "triangle", "star", "square", "hexagon", "rhombus"]
        if symbol not in self.symbols:
            symbol = self.symbols[0]
        self.symbol = symbol
        self.disabled_symbols = disabled_symbols
        self.on_symbol_change = None
        self.__createWidgets__()

    def __createWidgets__(self):
        self.canvas = tk.Canvas(self, width=132, height=132, bg="#333333", borderwidth=0, highlightthickness=0)
        self.canvas.grid(row=0, column=0, padx=10, pady=10)
        self.draw_symbol()
        self.select_button = ctk.CTkButton(self, text="Select Symbol", command=self.select_symbol)
        self.select_button.grid(row=1, column=0, padx=10, pady=10)

    def draw_symbol(self):
        self.canvas.delete("all")
        canvas_width = int(self.canvas['width'])
        canvas_height = int(self.canvas['height'])
        size = 100
        weight = 2
        x = (canvas_width - size) // 2
        y = (canvas_height - size) // 2
        if self.symbol == "cross":
            drawCross(self.canvas, x, y, size, weight=weight)
        elif self.symbol == "circle":
            drawCircle(self.canvas, x, y, size, weight=weight)
        elif self.symbol == "triangle":
            drawTriangle(self.canvas, x, y, size, weight=weight)
        elif self.symbol == "star":
            drawStar(self.canvas, x, y, size, weight=weight)
        elif self.symbol == "square":
            drawSquare(self.canvas, x, y, size, weight=weight)
        elif self.symbol == "hexagon":
            drawHexagon(self.canvas, x, y, size, weight=weight)
        elif self.symbol == "rhombus":
            drawRhombus(self.canvas, x, y, size, weight=weight)

    def select_symbol(self):
        current_index = self.symbols.index(self.symbol)
        next_index = (current_index + 1) % len(self.symbols)
        while self.symbols[next_index] in self.disabled_symbols:
            next_index = (next_index + 1) % len(self.symbols)
        self.symbol = self.symbols[next_index]
        self.draw_symbol()
        if self.on_symbol_change:
            self.on_symbol_change()

    def disable_symbols(self, symbols):
        self.disabled_symbols = symbols
        if self.symbol in self.disabled_symbols:
            self.select_symbol()

    def set_symbol(self, symbol):
        self.symbol = symbol
        self.draw_symbol()

    def get_symbol(self):
        return self.symbol

    def get_available_symbols(self):
        return [symbol for symbol in self.symbols if symbol not in self.disabled_symbols]