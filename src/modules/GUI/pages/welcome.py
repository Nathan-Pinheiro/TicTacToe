## Interface

"""
Welcome Page Module

This module provides the implementation of the welcome page for the Tic Tac Toe game using the tkinter library.

Classes:
    Welcome: A class representing the welcome page of the Tic Tac Toe game.
    
Methods:
    __init__(self, parent: Any, controller: Any) -> None:
        Initialize the welcome page with the given parent and controller.
    
    __draw_grid(self, size: int) -> None:
        Private method.
        Draw the tic-tac-toe grid with symbols.
    
    __draw_x(self, x: int, y: int, size: int) -> None:
        Private method.
        Draw an X symbol centered in a cell.
    
    __draw_o(self, x: int, y: int, size: int) -> None:
        Private method.
        Draw an O symbol centered in a cell.
    
    __draw_triangle(self, x: int, y: int, size: int) -> None:
        Private method.
        Draw a triangle symbol centered in a cell.
    
    __on_resize(self, event: Any) -> None:
        Private method.
        Redraw the tic-tac-toe grid responsively when the window is resized.
    
    start_game(self) -> None:
        Start the game when the "Start Game" button is pressed.
"""

# ---------------------------------------------------------------------------------------------------- #

## Implementation

# Import #
import tkinter as tk
from tkinter import ttk
import sv_ttk
from typing import Any

from modules.utils.decorator import private_method

class Welcome(ttk.Frame):
    def __init__(self, parent: Any, controller: Any) -> None:
        """Initialize the welcome page with the given parent and controller.

        Args:
            parent (Any): The parent widget.
            controller (Any): The controller of the application.

        Returns:
            None
        """
        super().__init__(parent)
        self.controller: Any = controller

        # Main grid configuration
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=2)  # Increase the space for the text
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)  # Decrease the space for column 1

        # Title "Tic Tac Toe"
        self.title_label: ttk.Label = ttk.Label(self, text="Tic Tac Toe", font=("Arial", 48, "bold"))
        self.title_label.grid(row=0, column=0, columnspan=2, pady=(10, 0), sticky="n")

        # Lorem Ipsum text
        self.text_label: ttk.Label = ttk.Label(self, 
                                    text=("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent rutrum tellus "
                                          "non ante euismod, id blandit massa auctor. Quisque urna tellus, sodales at ante nec," 
                                          " pharetra tincidunt ante."), 
                                    wraplength=400, 
                                    justify="left",
                                    font=("Arial", 12))
        self.text_label.grid(row=1, column=0, pady=(5, 5), padx=100, sticky="w")  # Reduce paddings

        # Unique canvas for the grid and symbols
        self.grid_canvas: tk.Canvas = tk.Canvas(self, bg="#333", highlightthickness=0)
        self.grid_canvas.grid(row=1, column=1, pady=0, padx=100, sticky="e")  # Reduce padding gap

        # "Start Game" button
        self.start_button: ttk.Button = ttk.Button(self, text="Start Game", command=self.start_game)
        self.start_button.grid(row=2, column=0, columnspan=2, pady=50, sticky="s")

        # Dynamic resizing
        self.bind("<Configure>", self.__on_resize)

        # Dark theme
        sv_ttk.set_theme("dark")
        
        return None

    @private_method
    def __draw_grid(self, size: int) -> None:
        """Draw the tic-tac-toe grid with symbols.

        Args:
            size (int): The size of the grid.

        Returns:
            None
        """
        self.grid_canvas.delete("all")  # Clear the canvas

        # Cell size
        cell_size: int = size // 3

        # Draw the gray square (background)
        self.grid_canvas.create_rectangle(0, 0, size, size, fill="#333", outline="")
        
        # Set the canvas to the same size as the grid
        self.grid_canvas.config(width=size, height=size)

        # Draw white lines (horizontal and vertical)
        for i in range(1, 3):
            # Horizontal lines
            self.grid_canvas.create_line(0, i * cell_size, size, i * cell_size, fill="white", width=3)
            # Vertical lines
            self.grid_canvas.create_line(i * cell_size, 0, i * cell_size, size, fill="white", width=3)

        # Draw symbols (here X, O, Triangle in the cells of the first row)
        self.__draw_x(0, 0, cell_size)
        self.__draw_o(cell_size, 0, cell_size)
        self.__draw_triangle(2 * cell_size, 0, cell_size)
        
        return None

    @private_method
    def __draw_x(self, x: int, y: int, size: int) -> None:
        """Draw an X centered in a cell.

        Args:
            x (int): The x-coordinate of the cell.
            y (int): The y-coordinate of the cell.
            size (int): The size of the cell.

        Returns:
            None
        """
        margin: float = size * 0.2
        self.grid_canvas.create_line(x + margin, y + margin, x + size - margin, y + size - margin, fill="white", width=4)
        self.grid_canvas.create_line(x + margin, y + size - margin, x + size - margin, y + margin, fill="white", width=4)
        
        return None

    @private_method
    def __draw_o(self, x: int, y: int, size: int) -> None:
        """Draw an O centered in a cell.

        Args:
            x (int): The x-coordinate of the cell.
            y (int): The y-coordinate of the cell.
            size (int): The size of the cell.

        Returns:
            None
        """
        margin: float = size * 0.2
        self.grid_canvas.create_oval(x + margin, y + margin, x + size - margin, y + size - margin, outline="white", width=4)
        
        return None

    @private_method
    def __draw_triangle(self, x: int, y: int, size: int) -> None:
        """Draw a triangle centered in a cell.

        Args:
            x (int): The x-coordinate of the cell.
            y (int): The y-coordinate of the cell.
            size (int): The size of the cell.

        Returns:
            None
        """
        half: int = size // 2
        margin: float = size * 0.2
        self.grid_canvas.create_polygon(
            x + half, y + margin,
            x + margin, y + size - margin,
            x + size - margin, y + size - margin,
            outline="white", width=4, fill="")
        
        return None

    @private_method
    def __on_resize(self, event: Any) -> None:
        """Redraw widgets responsively when the window is resized.

        Args:
            event (Any): The event object.

        Returns:
            None
        """
        # Calculate the size of the square based on the window
        size: int = min(event.width, event.height) * 0.5  # Canvas size (50% of the window)
        size = int(size) - (int(size) % 3)  # Ensure the size is a multiple of 3

        # Update the canvas size
        self.grid_canvas.config(width=size, height=size)

        # Redraw the grid and symbols
        self.__draw_grid(size)
        
        return None

    def start_game(self) -> None:
        """Start the game when the "Start Game" button is pressed.

        Returns:
            None
        """
        print("Starting the game...")
        
        return None

# Launch the application
if __name__ == "__main__":
    class App(tk.Tk):
        def __init__(self) -> None:
            super().__init__()
            self.title("Tic Tac Toe - Welcome")
            self.geometry("800x600")
            self.frame: Welcome = Welcome(self, self)
            self.frame.pack(fill="both", expand=True)

    app: App = App()
    app.mainloop()