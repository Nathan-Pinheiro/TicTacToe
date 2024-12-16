import tkinter as tk
from tkinter import ttk
import sv_ttk
from modules.GUI.draft.grid import draw_grid
from modules.utils.decorator import private_method

class Game(ttk.Frame):
    def __init__(self, parent: tk.Tk, controller: tk.Tk, width: int = 600, height: int = 600, board: list = [
                ['#', '', '#', '#', ''],
                ['', 'X', 'O', '', ''],
                ['', '', '', '', ''],
                ['#', '', '', '#', ''],
                ['', 'O', 'X', '', '']
            ]) -> None:
        """
        Initialize the game page.

        Args:
            parent (tk.Tk): The parent widget.
            controller (tk.Tk): The controller of the application.
            width (int): The width of the game grid.
            height (int): The height of the game grid.
            board (list): A 2D list representing the game board. 
                          '#' indicates a gray cell, 'X' for a cross, 'O' for a circle, and '' for an empty cell.
        """
        super().__init__(parent)
        self.controller = controller
        self.board = board
        self.width = width
        self.height = height
        self.cell_size = min(width // len(board[0]), height // len(board))  # Calculate cell size based on width and height

        # Create a frame for the game and the box
        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(fill="both", expand=True)

        # Create a canvas for the game grid
        self.grid_canvas = tk.Canvas(self.main_frame, width=self.width - 1, height=self.height - 1, bg="#333")
        self.grid_canvas.pack(side="left", padx=(100, 0), pady=10)

        # Create a box on the right
        self.info_box = tk.Canvas(self.main_frame, width=700, bg="#555")
        self.info_box.pack(side="right", fill="y", padx=0, pady=0)

        # Bind mouse click event to handle cell clicks
        self.grid_canvas.bind("<Button-1>", self.__handle_click)

        # Draw the initial board
        draw_grid(self.grid_canvas, self.width, self.cell_size, self.board)

    @private_method
    def __handle_click(self, event: tk.Tk) -> None:
        """Handle mouse click events on the canvas."""
        col = event.x // self.cell_size
        row = event.y // self.cell_size

        # Ensure the click is within bounds and the cell is playable
        if 0 <= row < len(self.board) and 0 <= col < len(self.board[0]):
            if self.board[row][col] == '':
                # Alternate between 'X' and 'O' based on turn
                self.board[row][col] = 'X' if self.__get_current_player() == 'X' else 'O'

                # Redraw the updated board
                draw_grid(self.grid_canvas, self.width, self.cell_size, self.board)

    @private_method
    def __get_current_player(self) -> str:
        """Determine the current player based on the board state."""
        # Count Xs and Os to determine the turn
        x_count = sum(row.count('X') for row in self.board)
        o_count = sum(row.count('O') for row in self.board)
        return 'X' if x_count <= o_count else 'O'