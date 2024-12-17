import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import sv_ttk
from modules.GUI.draft.grid import draw_grid
from modules.utils.decorator import private_method

class Game(ttk.Frame):
    def __init__(self, parent: tk.Tk, controller: tk.Tk, size: int = 100, board: list = [
                ['#', '', '#', '#', ''],
                ['', 'X', 'O', '', ''],
                ['', '', '', '', ''],
                ['#', '', '', '#', ''],
                ['', '', '', '', ''],
                ['', '', '', '', ''],
                ['', '', '', '', '']
            ], button_color: str = "#555") -> None:
        """
        Initialize the game page.

        Args:
            parent (tk.Tk): The parent widget.
            controller (tk.Tk): The controller of the application.
            width (int): The width of the game grid.
            height (int): The height of the game grid.
            board (list): A 2D list representing the game board. 
                          '#' indicates a gray cell, 'X' for a cross, 'O' for a circle, and '' for an empty cell.
            button_color (str): The background color of the buttons.
        """
        super().__init__(parent)
        self.controller = controller
        self.board = board
        self.width = size * len(board[0])
        self.height = size * len(board)
        self.cell_size = size  # Calculate cell size based on width and height

        # Create a frame for the game and the box
        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(fill="both", expand=True)

        # Create a canvas for the game grid
        self.grid_canvas = tk.Canvas(self.main_frame, width=self.width - 3, height=self.height - 3, bg="#333")
        self.grid_canvas.pack(side='left', padx=0, pady=10, anchor='center', expand=True)

        # Create a box on the right
        self.info_box = tk.Canvas(self.main_frame, width=700, bg=button_color, highlightthickness=0)
        self.info_box.pack(side="right", fill="y", padx=0, pady=0)

        # Create a frame for the buttons at the bottom of the info box with a white background
        self.button_frame = ttk.Frame(self.info_box, style="White.TFrame")
        self.button_frame.pack(side="bottom", fill="x", padx=10, pady=10)

        # Customize frame style to have a white background
        style = ttk.Style()
        style.configure("White.TFrame", background="#333")

        # Load images for the buttons using PIL
        self.button_images = [
            self.load_png_image("./static/assets/Bomb.png"),
            self.load_png_image("./static/assets/LeftArrow.png"),
            self.load_png_image("./static/assets/RightArrow.png"),
            self.load_png_image("./static/assets/Bulb.png")
        ]

        # Customize button style to remove focus border
        style = ttk.Style()
        style.configure("Custom.TButton", background=button_color)

        # Add four buttons with images to the button frame
        self.button1 = ttk.Button(self.button_frame, image=self.button_images[0], style="Custom.TButton", command=self.__handleBombClick)
        self.button1.pack(side="left", expand=True, padx=5, pady=5)

        self.button2 = ttk.Button(self.button_frame, image=self.button_images[1], style="Custom.TButton", command=self.__handleLeftArrowClick)
        self.button2.pack(side="left", expand=True, padx=5, pady=5)

        self.button3 = ttk.Button(self.button_frame, image=self.button_images[2], style="Custom.TButton", command=self.__handleRightArrowClick)
        self.button3.pack(side="left", expand=True, padx=5, pady=5)

        self.button4 = ttk.Button(self.button_frame, image=self.button_images[3], style="Custom.TButton", command=self.__handleBulbClick)
        self.button4.pack(side="left", expand=True, padx=5, pady=5)

        # Bind mouse click event to handle cell clicks
        self.grid_canvas.bind("<Button-1>", self.__handle_click)

        # Draw the initial board
        draw_grid(self.grid_canvas, self.width, self.height, self.cell_size, self.board, coord=True)

    def load_png_image(self, file_path: str) -> ImageTk.PhotoImage:
        """Load a PNG image and convert it to a format compatible with Tkinter."""
        image = Image.open(file_path)
        return ImageTk.PhotoImage(image)

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
                draw_grid(self.grid_canvas, self.width, self.height, self.cell_size, self.board, coord=True)
                
    @private_method
    def __handleBombClick(self) -> None:
        """Handle the bomb button click."""
        
        print("Bomb clicked")
        
        return None
    
    @private_method
    def __handleLeftArrowClick(self) -> None:
        """Handle the left arrow button click."""
        
        print("Left arrow clicked")
        
        return None
    
    @private_method
    def __handleRightArrowClick(self) -> None:
        """Handle the right arrow button click."""
        
        print("Right arrow clicked")
        
        return None
    
    @private_method
    def __handleBulbClick(self) -> None:
        """Handle the bulb button click."""
        
        print("Bulb clicked")
        
        return None

    @private_method
    def __get_current_player(self) -> str:
        """Determine the current player based on the board state."""
        # Count Xs and Os to determine the turn
        x_count = sum(row.count('X') for row in self.board)
        o_count = sum(row.count('O') for row in self.board)
        return 'X' if x_count <= o_count else 'O'
