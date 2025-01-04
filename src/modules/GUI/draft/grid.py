## Interface

"""
Grid Drawing Module

This module provides functions to draw a tic-tac-toe grid on a graphical canvas.

Functions:
    draw_grid(canvas: tk.Canvas, width: int, height: int, cell_size: int, board: list[list[str]] = None, line_color: str = "white", line_width: int = 1, player_symbols: list[str] = None, player_colors: list[str] = None, coord: bool = False) -> bool:
        Draw a tic-tac-toe grid on the given canvas.
        
    draw_symbol(canvas: tk.Canvas, x0: int, y0: int, cell_size: int, symbol: str, player_symbols: list[str], player_colors: list[str]) -> bool:
        Draw a symbol on the canvas.
        
    draw_coordinates(canvas: tk.Canvas, width: int, height: int, cell_size: int) -> bool:
        Draw coordinates around the grid.
"""

# ---------------------------------------------------------------------------------------------------- #

## Implementation

# Import
import tkinter as tk
from modules.GUI.draft.symbols import drawCross, drawCircle, drawTriangle, drawHexagon, drawStar, drawSquare, drawRhombus, drawGrayCase
from modules.utils.validators import is_valid_symbol, is_hex_color

## Draw a tic-tac-toe grid on the given canvas.
#
# @param canvas The canvas on which to draw the grid.
# @param width The width of the grid.
# @param height The height of the grid.
# @param cell_size The size of each cell in the grid.
# @param board A 2D list representing the game board. 
#              '#' indicates a gray cell, 'X' for a cross, 'O' for a circle, and '' for an empty cell.
# @param line_color The color of the grid lines.
# @param line_width The width of the grid lines.
# @param player_symbols A list of symbols representing the players.
# @param player_colors A list of colors corresponding to the player symbols.
# @param coord Whether to draw coordinates around the grid.
# @return bool True if the function succeeds, False otherwise.
def draw_grid(canvas: tk.Canvas, width: int, height: int, cell_size: int, board: list[list[str]] = None, line_color: str = "white", line_width: int = 1, player_symbols: list[str] = None, player_colors: list[str] = None, coord: bool = False) -> bool:
    # Validate parameters
    if not isinstance(canvas, tk.Canvas):
        raise TypeError("canvas must be a tk.Canvas instance")
    if not isinstance(width, int) or not isinstance(height, int) or not isinstance(cell_size, int):
        raise TypeError("width, height, and cell_size must be integers")
    if board is not None and not isinstance(board, list) or not all(isinstance(row, list) for row in board):
        raise TypeError("board must be a 2D list")
    if not isinstance(line_color, str):
        raise TypeError("line_color must be a string")
    if not isinstance(line_width, int):
        raise TypeError("line_width must be an integer")
    if player_symbols is not None:
        if not isinstance(player_symbols, list) or not all(isinstance(symbol, str) for symbol in player_symbols):
            raise TypeError("player_symbols must be a list of strings")
        if not all(is_valid_symbol(symbol) for symbol in player_symbols):
            raise ValueError("All player_symbols must be valid symbols")
    if player_colors is not None:
        if not isinstance(player_colors, list) or not all(isinstance(color, str) for color in player_colors):
            raise TypeError("player_colors must be a list of strings")
        if not all(is_hex_color(color) for color in player_colors):
            raise ValueError("All player_colors must be in hexadecimal format")
    if not isinstance(coord, bool):
        raise TypeError("coord must be a boolean")

    # Clear the canvas
    canvas.delete("all")

    # Draw the gray square (background)
    canvas.create_rectangle(0, 0, height, width, fill="#333", outline="")

    # Draw white lines (horizontal and vertical)
    for i in range(1, height // cell_size):
        canvas.create_line(0, i * cell_size, width, i * cell_size, fill=line_color, width=line_width)
    for i in range(1, width // cell_size):
        canvas.create_line(i * cell_size, 0, i * cell_size, height, fill=line_color, width=line_width)

    # Draw symbols if a board is provided
    if board and player_symbols and player_colors:
        for row in range(len(board)):
            for col in range(len(board[row])):
                x0: int = col * cell_size
                y0: int = row * cell_size
                symbol: str = board[row][col]
                if symbol == '#':
                    if not drawGrayCase(canvas, x0, y0, cell_size):
                        raise RuntimeError("Failed to draw gray case")
                else:
                    if not draw_symbol(canvas, x0, y0, cell_size, symbol, player_symbols, player_colors):
                        raise RuntimeError("Failed to draw symbol")

    # Draw coordinates if coord is True
    if coord:
        if not draw_coordinates(canvas, width, height, cell_size):
            raise RuntimeError("Failed to draw coordinates")

    return True

## Draw a symbol on the canvas.
#
# @param canvas The canvas on which to draw the symbol.
# @param x0 The x-coordinate of the top-left corner of the cell.
# @param y0 The y-coordinate of the top-left corner of the cell.
# @param cell_size The size of the cell.
# @param symbol The symbol to draw.
# @param player_symbols A list of symbols representing the players.
# @param player_colors A list of colors corresponding to the player symbols.
# @return bool True if the function succeeds, False otherwise.
def draw_symbol(canvas: tk.Canvas, x0: int, y0: int, cell_size: int, symbol: str, player_symbols: list[str], player_colors: list[str]) -> bool:
    # Validate parameters
    if not isinstance(canvas, tk.Canvas):
        raise TypeError("canvas must be a tk.Canvas instance")
    if not isinstance(x0, int) or not isinstance(y0, int) or not isinstance(cell_size, int):
        raise TypeError("x0, y0, and cell_size must be integers")
    if not isinstance(symbol, str) or not is_valid_symbol(symbol):
        raise TypeError("symbol must be a valid string")
    if not isinstance(player_symbols, list) or not all(isinstance(sym, str) and is_valid_symbol(sym) for sym in player_symbols):
        raise TypeError("player_symbols must be a list of valid strings")
    if not isinstance(player_colors, list) or not all(isinstance(color, str) for color in player_colors):
        raise TypeError("player_colors must be a list of strings")
    if not all(is_hex_color(color) for color in player_colors):
        raise ValueError("All player_colors must be in hexadecimal format")

    for i, player_symbol in enumerate(player_symbols):
        if symbol == player_symbol:
            color: str = player_colors[i]
            if symbol == 'X':
                if not drawCross(canvas, x0, y0, cell_size, color):
                    raise RuntimeError("Failed to draw cross")
            elif symbol == 'O':
                if not drawCircle(canvas, x0, y0, cell_size, color):
                    raise RuntimeError("Failed to draw circle")
            elif symbol == '△':
                if not drawTriangle(canvas, x0, y0, cell_size, color):
                    raise RuntimeError("Failed to draw triangle")
            elif symbol == '⬡':
                if not drawHexagon(canvas, x0, y0, cell_size, color):
                    raise RuntimeError("Failed to draw hexagon")
            elif symbol == '★':
                if not drawStar(canvas, x0, y0, cell_size, color):
                    raise RuntimeError("Failed to draw star")
            elif symbol == '▢':
                if not drawSquare(canvas, x0, y0, cell_size, color):
                    raise RuntimeError("Failed to draw square")
            elif symbol == '◊':
                if not drawRhombus(canvas, x0, y0, cell_size, color):
                    raise RuntimeError("Failed to draw rhombus")
    return True

## Draw coordinates around the grid.
#
# @param canvas The canvas on which to draw the coordinates.
# @param width The width of the grid.
# @param height The height of the grid.
# @param cell_size The size of each cell in the grid.
# @return bool True if the function succeeds, False otherwise.
def draw_coordinates(canvas: tk.Canvas, width: int, height: int, cell_size: int) -> bool:
    # Validate parameters
    if not isinstance(canvas, tk.Canvas):
        raise TypeError("canvas must be a tk.Canvas instance")
    if not isinstance(width, int) or not isinstance(height, int) or not isinstance(cell_size, int):
        raise TypeError("width, height, and cell_size must be integers")

    for i in range(height // cell_size):
        canvas.create_text(10, i * cell_size + cell_size - 14, text=str(i + 1), fill="#ffffff")
    for i in range(width // cell_size):
        letter: str = chr(i + 65)
        canvas.create_text(i * cell_size + cell_size - 10, 14, text=letter, fill="white")
    return True