## Interface

"""
Grid Drawing Module

This module provides functions to draw a tic-tac-toe grid on a graphical canvas.

Functions:
    drawGrid(canvas: tk.Canvas, width: int, height: int, cellSize: int, board: list[list[str]] = None, lineColor: str = "white", lineWidth: int = 1, playerSymbols: list[str] = None, playerColors: list[str] = None, coord: bool = False) -> bool:
        Draw a tic-tac-toe grid on the given canvas.
        
    drawSymbol(canvas: tk.Canvas, x0: int, y0: int, cellSize: int, symbol: str, playerSymbols: list[str], playerColors: list[str]) -> bool:
        Draw a symbol on the canvas.
        
    drawCoordinates(canvas: tk.Canvas, width: int, height: int, cellSize: int) -> bool:
        Draw coordinates around the grid.
"""

# ---------------------------------------------------------------------------------------------------- #

## Implementation

# Import
import tkinter as tk
from modules.GUI.draft.symbols import drawCross, drawCircle, drawTriangle, drawHexagon, drawStar, drawSquare, drawRhombus, drawGrayCase
from modules.utils.validators import isValidSymbol, isHexColor

## Draw a tic-tac-toe grid on the given canvas.
#
# @param canvas The canvas on which to draw the grid.
# @param width The width of the grid.
# @param height The height of the grid.
# @param cellSize The size of each cell in the grid.
# @param board A 2D list representing the game board. 
#              '#' indicates a gray cell, 'X' for a cross, 'O' for a circle, and '' for an empty cell.
# @param lineColor The color of the grid lines.
# @param lineWidth The width of the grid lines.
# @param playerSymbols A list of symbols representing the players.
# @param playerColors A list of colors corresponding to the player symbols.
# @param coord Whether to draw coordinates around the grid.
# @return bool True if the function succeeds, False otherwise.
def drawGrid(canvas: tk.Canvas, width: int, height: int, cellSize: int, board: list[list[str]] = None, lineColor: str = "white", lineWidth: int = 1, playerSymbols: list[str] = None, playerColors: list[str] = None, coord: bool = False) -> bool:
    # Validate parameters
    if not isinstance(canvas, tk.Canvas):
        raise TypeError("canvas must be a tk.Canvas instance")
    if not isinstance(width, int) or not isinstance(height, int) or not isinstance(cellSize, int):
        raise TypeError("width, height, and cellSize must be integers")
    if board is not None and not isinstance(board, list) or not all(isinstance(row, list) for row in board):
        raise TypeError("board must be a 2D list")
    if not isinstance(lineColor, str):
        raise TypeError("lineColor must be a string")
    if not isinstance(lineWidth, int):
        raise TypeError("lineWidth must be an integer")
    if playerSymbols is not None:
        if not isinstance(playerSymbols, list) or not all(isinstance(symbol, str) for symbol in playerSymbols):
            raise TypeError("playerSymbols must be a list of strings")
        if not all(isValidSymbol(symbol) for symbol in playerSymbols):
            raise ValueError("All playerSymbols must be valid symbols")
    if playerColors is not None:
        if not isinstance(playerColors, list) or not all(isinstance(color, str) for color in playerColors):
            raise TypeError("playerColors must be a list of strings")
        if not all(isHexColor(color) for color in playerColors):
            raise ValueError("All playerColors must be in hexadecimal format")
    if not isinstance(coord, bool):
        raise TypeError("coord must be a boolean")

    # Clear the canvas
    canvas.delete("all")

    # Draw the gray square (background)
    canvas.create_rectangle(0, 0, height, width, fill="#333", outline="")

    # Draw white lines (horizontal and vertical)
    for i in range(1, height // cellSize):
        canvas.create_line(0, i * cellSize, width, i * cellSize, fill=lineColor, width=lineWidth)
    for i in range(1, width // cellSize):
        canvas.create_line(i * cellSize, 0, i * cellSize, height, fill=lineColor, width=lineWidth)

    # Draw symbols if a board is provided
    if board and playerSymbols and playerColors:
        for row in range(len(board)):
            for col in range(len(board[row])):
                x0: int = col * cellSize
                y0: int = row * cellSize
                symbol: str = board[row][col]
                if symbol == '#':
                    if not drawGrayCase(canvas, x0, y0, cellSize):
                        raise RuntimeError("Failed to draw gray case")
                else:
                    if not drawSymbol(canvas, x0, y0, cellSize, symbol, playerSymbols, playerColors):
                        raise RuntimeError("Failed to draw symbol")

    # Draw coordinates if coord is True
    if coord:
        if not drawCoordinates(canvas, width, height, cellSize):
            raise RuntimeError("Failed to draw coordinates")

    return True

## Draw a symbol on the canvas.
#
# @param canvas The canvas on which to draw the symbol.
# @param x0 The x-coordinate of the top-left corner of the cell.
# @param y0 The y-coordinate of the top-left corner of the cell.
# @param cellSize The size of the cell.
# @param symbol The symbol to draw.
# @param playerSymbols A list of symbols representing the players.
# @param playerColors A list of colors corresponding to the player symbols.
# @return bool True if the function succeeds, False otherwise.
def drawSymbol(canvas: tk.Canvas, x0: int, y0: int, cellSize: int, symbol: str, playerSymbols: list[str], playerColors: list[str]) -> bool:
    # Validate parameters
    if not isinstance(canvas, tk.Canvas):
        raise TypeError("canvas must be a tk.Canvas instance")
    if not isinstance(x0, int) or not isinstance(y0, int) or not isinstance(cellSize, int):
        raise TypeError("x0, y0, and cellSize must be integers")
    if not isinstance(symbol, str) or not isValidSymbol(symbol):
        raise TypeError("symbol must be a valid string")
    if not isinstance(playerSymbols, list) or not all(isinstance(sym, str) and isValidSymbol(sym) for sym in playerSymbols):
        raise TypeError("playerSymbols must be a list of valid strings")
    if not isinstance(playerColors, list) or not all(isinstance(color, str) for color in playerColors):
        raise TypeError("playerColors must be a list of strings")
    if not all(isHexColor(color) for color in playerColors):
        raise ValueError("All playerColors must be in hexadecimal format")

    for i, playerSymbol in enumerate(playerSymbols):
        if symbol == playerSymbol:
            color: str = playerColors[i]
            if symbol == 'X':
                if not drawCross(canvas, x0, y0, cellSize, color):
                    raise RuntimeError("Failed to draw cross")
            elif symbol == 'O':
                if not drawCircle(canvas, x0, y0, cellSize, color):
                    raise RuntimeError("Failed to draw circle")
            elif symbol == '△':
                if not drawTriangle(canvas, x0, y0, cellSize, color):
                    raise RuntimeError("Failed to draw triangle")
            elif symbol == '⬡':
                if not drawHexagon(canvas, x0, y0, cellSize, color):
                    raise RuntimeError("Failed to draw hexagon")
            elif symbol == '★':
                if not drawStar(canvas, x0, y0, cellSize, color):
                    raise RuntimeError("Failed to draw star")
            elif symbol == '▢':
                if not drawSquare(canvas, x0, y0, cellSize, color):
                    raise RuntimeError("Failed to draw square")
            elif symbol == '◊':
                if not drawRhombus(canvas, x0, y0, cellSize, color):
                    raise RuntimeError("Failed to draw rhombus")
    return True

## Draw coordinates around the grid.
#
# @param canvas The canvas on which to draw the coordinates.
# @param width The width of the grid.
# @param height The height of the grid.
# @param cellSize The size of each cell in the grid.
# @return bool True if the function succeeds, False otherwise.
def drawCoordinates(canvas: tk.Canvas, width: int, height: int, cellSize: int) -> bool:
    # Validate parameters
    if not isinstance(canvas, tk.Canvas):
        raise TypeError("canvas must be a tk.Canvas instance")
    if not isinstance(width, int) or not isinstance(height, int) or not isinstance(cellSize, int):
        raise TypeError("width, height, and cellSize must be integers")

    for i in range(height // cellSize):
        canvas.create_text(10, i * cellSize + cellSize - 14, text=str(i + 1), fill="#ffffff")
    for i in range(width // cellSize):
        letter: str = chr(i + 65)
        canvas.create_text(i * cellSize + cellSize - 10, 14, text=letter, fill="white")
    return True