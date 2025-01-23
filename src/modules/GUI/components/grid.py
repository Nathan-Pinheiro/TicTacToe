import tkinter as tk

from modules.GUI.components.symbols import (
    drawCross, drawCircle, drawTriangle, drawHexagon, drawStar, drawSquare, drawRhombus, drawGrayCase, drawGreenCase
)

from modules.utils.validators import (
    isValidSymbol, isHexColor
)

def drawGrid(canvas: tk.Canvas, width: int, height: int, cellSize: int, board: list[list[str]] = None, lineColor: str = "#FFFFFF", lineWidth: int = 1, playerSymbols: list[str] = ["X", "O"], playerColors: list[str] = ["#FFFFFF", "#FFFFFF"], coord: bool = True, advice: tuple[int | None, int | None] = (None, None)) -> bool:
    
    """
    Draws the game grid on the canvas.
    
    Parameters:
        canvas (tk.Canvas): The canvas to draw on.
        width (int): The width of the grid.
        height (int): The height of the grid.
        cellSize (int): The size of each cell in the grid.
        board (list[list[str]], optional): The game board state.
        lineColor (str): The color of the grid lines.
        lineWidth (int): The width of the grid lines.
        playerSymbols (list[str]): The symbols used by the players.
        playerColors (list[str]): The colors used by the players.
        coord (bool): Whether to draw coordinates on the grid.
        advice (tuple): The coordinates of the advised move.
        
    Raises:
        TypeError: If the canvas is not a tk.Canvas instance.
        TypeError: If width, height, or cellSize is not an integer.
        TypeError: If board is not a 2D list of strings.
        TypeError: If lineColor is not a string.
        TypeError: If lineWidth is not an integer.
        TypeError: If playerSymbols is not a list of strings.
        ValueError: If playerSymbols contains invalid symbols.
        TypeError: If playerColors is not a list of strings.
        ValueError: If playerColors contains invalid colors.
        TypeError: If coord is not a boolean.
        TypeError: If advice is not a tuple of integers.

    Returns:
        bool: True if the function succeeds, False otherwise.
    """
    
    # Check if the canvas is a tk.Canvas instance
    if not isinstance(canvas, tk.Canvas):
        raise TypeError("canvas must be a tk.Canvas instance")
    
    # Check if width, height, and cellSize are integers
    if not isinstance(width, int) or not isinstance(height, int) or not isinstance(cellSize, int):
        raise TypeError("width, height, and cellSize must be integers")
    
    # Check if board is a 2D list of strings
    if board is not None:
        if not isinstance(board, list) or not all(isinstance(row, list) for row in board):
            raise TypeError("board must be a 2D list")
        if not all(isinstance(cell, str) for row in board for cell in row):
            raise TypeError("board must be a 2D list of strings")
        
    # Check if lineColor is a string
    if not isinstance(lineColor, str):
        raise TypeError("lineColor must be a string")
    
    # Check if lineWidth is an integer
    if not isinstance(lineWidth, int):
        raise TypeError("lineWidth must be an integer")
    
    # Check if playerSymbols is a list of strings
    if playerSymbols is not None:
        if not isinstance(playerSymbols, list) or not all(isinstance(symbol, str) for symbol in playerSymbols):
            raise TypeError("playerSymbols must be a list of strings")
        if not all(isValidSymbol(symbol) for symbol in playerSymbols):
            raise ValueError("All playerSymbols must be valid symbols")
        
    # Check if playerColors is a list of strings
    if playerColors is not None:
        if not isinstance(playerColors, list) or not all(isinstance(color, str) for color in playerColors):
            raise TypeError("playerColors must be a list of strings")
        if not all(isHexColor(color) for color in playerColors):
            raise ValueError("All playerColors must be in hexadecimal format")
        
    # Check if coord is a boolean
    if not isinstance(coord, bool):
        raise TypeError("coord must be a boolean")
    
    # Check if advice is a tuple of two integers or None
    if not isinstance(advice, tuple) or len(advice) != 2 or not all(isinstance(coord, int) or coord is None for coord in advice):
            raise TypeError("advice must be a tuple of two integers or None")

    # Clear the canvas
    canvas.delete("all")

    # Draw the background
    canvas.create_rectangle(0, 0, width, height, fill="#4b4b4b", outline="")

    # Draw symbols, gray cases,and green cases on the board
    if board and playerSymbols and playerColors:
        for row in range(len(board)):
            for col in range(len(board[row])):
                x0: int = col * cellSize
                y0: int = row * cellSize
                symbol: str = board[row][col]
                if len(advice) == 2 and [row, col] == [advice[0], advice[1]]:
                    drawGreenCase(canvas, x0, y0, cellSize)
                if symbol == '#':
                    drawGrayCase(canvas, x0, y0, cellSize)
                else:
                    drawSymbol(canvas, x0, y0, cellSize, symbol, playerSymbols, playerColors)

    # Draw the coordinates on the board
    if coord:
        drawCoordinates(canvas, width, height, cellSize)

    # Draw the grid lines
    for indexLine in range(height // cellSize + 1):
        canvas.create_line(0, indexLine * cellSize, width, indexLine * cellSize, fill=lineColor, width=lineWidth)
        
    for indexLine in range(width // cellSize + 1):
        canvas.create_line(indexLine * cellSize, 0, indexLine * cellSize, height, fill=lineColor, width=lineWidth)
        
    canvas.create_line(width-1, 0, width-1, height, fill=lineColor, width=lineWidth)
    canvas.create_line(0, height-1, width, height-1, fill=lineColor, width=lineWidth)

    return True

def drawSymbol(canvas: tk.Canvas, x0: int, y0: int, cellSize: int, symbol: str, playerSymbols: list[str], playerColors: list[str]) -> bool:
    
    """
    Draws a symbol on the canvas.
    
    Parameters:
        canvas (tk.Canvas): The canvas to draw on.
        x0 (int): The x-coordinate of the top-left corner of the cell.
        y0 (int): The y-coordinate of the top-left corner of the cell.
        cellSize (int): The size of the cell.
        symbol (str): The symbol to draw.
        playerSymbols (list[str]): The symbols used by the players.
        playerColors (list[str]): The colors used by the players.
        
    Raises:
        TypeError: If the canvas is not a tk.Canvas instance.
        TypeError: If x0, y0, or cellSize is not an integer.
        TypeError: If symbol is not a string.
        ValueError: If symbol is not a valid symbol.
        TypeError: If playerSymbols is not a list of strings.
        ValueError: If playerSymbols contains invalid symbols.
        TypeError: If playerColors is not a list of strings.
        ValueError: If playerColors contains invalid colors.

    Returns:
        bool: True if the function succeeds, False otherwise.
    """
    
    # Check if the canvas is a tk.Canvas instance
    if not isinstance(canvas, tk.Canvas):
        raise TypeError("canvas must be a tk.Canvas instance")
    
    # Check if x0, y0, and cellSize are integers
    if not isinstance(x0, int) or not isinstance(y0, int) or not isinstance(cellSize, int):
        raise TypeError("x0, y0, and cellSize must be integers")
    
    # Check if symbol is a string
    if not isinstance(symbol, str) or not isValidSymbol(symbol):
        raise TypeError("symbol must be a valid string")
    
    # Check if playerSymbols is a list of strings
    if not isinstance(playerSymbols, list) or not all(isinstance(sym, str) and isValidSymbol(sym) for sym in playerSymbols):
        raise TypeError("playerSymbols must be a list of valid strings")
    
    # Check if playerColors is a list of strings
    if not isinstance(playerColors, list) or not all(isinstance(color, str) for color in playerColors):
        raise TypeError("playerColors must be a list of strings")
    
    # Check if playerColors contains valid hexadecimal colors
    if not all(isHexColor(color) for color in playerColors):
        raise ValueError("All playerColors must be in hexadecimal format")

    # Draw symbols on the canvas
    for indexSymbol, playerSymbol in enumerate(playerSymbols):
        if symbol == playerSymbol:
            color: str = playerColors[indexSymbol]
            match symbol:
                case 'X':
                    drawCross(canvas, x0, y0, cellSize, color)
                case 'O':
                    drawCircle(canvas, x0, y0, cellSize, color)
                case '△':
                    drawTriangle(canvas, x0, y0, cellSize, color)
                case '⬡':
                    drawHexagon(canvas, x0, y0, cellSize, color)
                case '★':
                    drawStar(canvas, x0, y0, cellSize, color)
                case '▢':
                    drawSquare(canvas, x0, y0, cellSize, color)
                case '◊':
                    drawRhombus(canvas, x0, y0, cellSize, color)
                
    return True

def drawCoordinates(canvas: tk.Canvas, width: int, height: int, cellSize: int) -> bool:
    
    """
    Draws the coordinates on the grid.
    
    Parameters:
        canvas (tk.Canvas): The canvas to draw on.
        width (int): The width of the grid.
        height (int): The height of the grid.
        cellSize (int): The size of each cell in the grid.
        
    Raises:
        TypeError: If the canvas is not a tk.Canvas instance.
        TypeError: If width, height, or cellSize is not an integer

    Returns:
        bool: True if the function succeeds, False otherwise.
    """
    
    # Check if the canvas is a tk.Canvas instance
    if not isinstance(canvas, tk.Canvas):
        raise TypeError("canvas must be a tk.Canvas instance")
    
    # Check if width, height, and cellSize are integers
    if not isinstance(width, int) or not isinstance(height, int) or not isinstance(cellSize, int):
        raise TypeError("width, height, and cellSize must be integers")

    # Draw the coordinates on the canvas
    for coordinateCol in range(height // cellSize):
        canvas.create_text(10, coordinateCol * cellSize + cellSize - 14, text=str(coordinateCol + 1), fill="#ffffff")
        
    for coordinateRow in range(width // cellSize):
        letter: str = chr(coordinateRow + 65)
        canvas.create_text(coordinateRow * cellSize + cellSize - 10, 14, text=letter, fill="white")
        
    return True