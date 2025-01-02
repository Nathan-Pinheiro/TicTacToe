import tkinter as tk
from modules.GUI.draft.symbols import drawCross, drawCircle, drawTriangle, drawHexagon, drawStar, drawSquare, drawRhombus, drawGrayCase

def draw_grid(canvas: tk.Canvas, width: int, height: int, cell_size: int, board: list = None, line_color: str = "white", line_width: int = 1, color: str = "#ffffff", coord: bool = False) -> None:
    """Draw a tic-tac-toe grid on the given canvas.

    Args:
        canvas (tk.Canvas): The canvas on which to draw the grid.
        size (int): The size of the grid (width and height).
        cell_size (int): The size of each cell in the grid.
        board (list): A 2D list representing the game board. 
                      '#' indicates a gray cell, 'X' for a cross, 'O' for a circle, and '' for an empty cell.
        line_color (str): The color of the grid lines.
        line_width (int): The width of the grid lines.
        coord (bool): Whether to draw coordinates around the grid.

    Returns:
        None
    """
    # Clear the canvas
    canvas.delete("all")

    # Draw the gray square (background)
    canvas.create_rectangle(0, 0, height, width, fill="#333", outline="")

    # Draw white lines (horizontal and vertical)
    for i in range(1, height // cell_size):
        # Horizontal lines
        canvas.create_line(0, i * cell_size, width, i * cell_size, fill=line_color, width=line_width)
    
    for i in range(1, width // cell_size):
        # Vertical lines
        canvas.create_line(i * cell_size, 0, i * cell_size, height, fill=line_color, width=line_width)

    # Draw symbols if a board is provided
    if board:
        for row in range(len(board)):
            for col in range(len(board[row])):
                x0 = col * cell_size
                y0 = row * cell_size

                # Draw gray cases for '#'
                if board[row][col] == '#':
                    drawGrayCase(canvas, x0, y0, cell_size)
                # Draw 'X'
                elif board[row][col] == 'X':
                    drawCross(canvas, x0, y0, cell_size, color)
                # Draw 'O'
                elif board[row][col] == 'O':
                    drawCircle(canvas, x0, y0, cell_size, color)
                # Draw other symbols if needed
                elif board[row][col] == '△':
                    drawTriangle(canvas, x0, y0, cell_size, color)
                elif board[row][col] == '⬡':
                    drawHexagon(canvas, x0, y0, cell_size, color)
                elif board[row][col] == 'S':
                    drawStar(canvas, x0, y0, cell_size, color)
                elif board[row][col] == 'Q':
                    drawSquare(canvas, x0, y0, cell_size, color)
                elif board[row][col] == 'R':
                    drawRhombus(canvas, x0, y0, cell_size, color)
                    
    # Draw coordinates if coord is True
    if coord:
        for i in range(height // cell_size):
            # Draw row coordinates
            canvas.create_text(10, i * cell_size + cell_size - 14, text=str(i + 1), fill="#ffffff")
        for i in range(width // cell_size):
            # Draw column coordinates
            letter = chr(i + 65)
            canvas.create_text(i * cell_size + cell_size - 10, 14, text=letter, fill="white")

    return None