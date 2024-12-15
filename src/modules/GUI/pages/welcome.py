## Interface

"""
Welcome Page Module

This module provides the implementation of the welcome page for the Tic Tac Toe game using the tkinter library.

Classes:
    Welcome: A class representing the welcome page of the Tic Tac Toe game.
    
Methods:
    __init__(self, parent: Any, controller: Any) -> None:
        Initialize the welcome page with the given parent and controller.
    
    __drawGrid__(self, size: int) -> None:
        Private method.
        Draw the tic-tac-toe grid with symbols.
    
    __onResize__(self, event: Any) -> None:
        Private method.
        Redraw widgets responsively when the window is resized.
    
    __adjustFontSizes__(self, width: int) -> None:
        Private method.
        Adjust the font sizes of the title and text labels based on the window size.
    
    __centerCanvas__(self) -> None:
        Private method.
        Center the canvas when the text label is hidden.
    
    __resetCanvasPosition__(self) -> None:
        Private method.
        Reset the canvas position when the text label is visible.
    
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

from modules.GUI.draft.symbols import *

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
        self.grid_columnconfigure(1, weight=2)  # Increase the space for the grid

        # Title "Tic Tac Toe"
        self.title_label: ttk.Label = ttk.Label(self, text="Tic Tac Toe", font=("Arial", 48, "bold"))
        self.title_label.grid(row=0, column=0, columnspan=2, pady=(50, 0), padx=0, sticky="n")

        # Lorem Ipsum text
        self.text_label: ttk.Label = ttk.Label(self, 
                                    text=("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent rutrum tellus "
                                          "non ante euismod, id blandit massa auctor. Quisque urna tellus, sodales at ante nec," 
                                          " pharetra tincidunt ante."), 
                                    wraplength=600, 
                                    justify="left",
                                    font=("Arial", 20))
        self.text_label.grid(row=1, column=0, pady=(5, 5), padx=(100, 10), sticky="w")  # Reduce paddings

        # Unique canvas for the grid and symbols
        self.grid_canvas: tk.Canvas = tk.Canvas(self, bg="#333", highlightthickness=0)
        self.grid_canvas.grid(row=1, column=1, pady=0, padx=(10, 100), sticky="e")  # Reduce padding gap

        # "Start Game" button
        self.start_button: ttk.Button = ttk.Button(self, text="Start Game", command=self.start_game)
        self.start_button.grid(row=2, column=0, columnspan=2, pady=50, sticky="s")

        # Dynamic resizing
        self.bind("<Configure>", self.__onResize__)

        # Dark theme
        sv_ttk.set_theme("dark")
        
        return None

    @private_method
    def __drawGrid__(self, size: int) -> None:
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
        drawCross(self, 0, 0, cell_size)
        drawCircle(self, cell_size, 0, cell_size)
        drawTriangle(self, 2 * cell_size, 0, cell_size)
        drawHexagon(self, 0, cell_size, cell_size)
        drawStar(self, cell_size, cell_size, cell_size)
        drawSquare(self, 2 * cell_size, cell_size, cell_size)
        drawRhombus(self, 0, 2 * cell_size, cell_size)
        drawGrayCase(self, cell_size, 2 * cell_size, cell_size)
        
        return None

    @private_method
    def __adjustButtonSize__(self, width: int) -> None:
        """Adjust the size of the start button based on the window size.

        Args:
            width (int): The width of the window.

        Returns:
            None
        """
        # Calculate new font size for the button
        button_font_size = max(14, int(width * 0.01))  # 2% of the window width

        # Update button font size using ttk.Style
        style = ttk.Style()
        style.configure("TButton", font=("Arial", button_font_size))

        return None

    @private_method
    def __onResize__(self, event: Any) -> None:
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
        self.__drawGrid__(size)

        # Adjust font sizes
        self.__adjustFontSizes__(event.width)

        # Adjust button size
        self.__adjustButtonSize__(event.width)

        return None


    @private_method
    def __adjustFontSizes__(self, width: int) -> None:
        """Adjust the font sizes of the title and text labels based on the window size.

        Args:
            width (int): The width of the window.

        Returns:
            None
        """
        # Calculate new font sizes
        title_font_size = max(20, int(width * 0.03))  # 3% of the window width
        text_font_size = max(12, int(width * 0.015))  # 2% of the window width
        
        # Calculate new wrap length for the text label
        wrap_length = width/2 - 110 # 110 is the sum of the left and right paddings

        # Update font sizes
        self.title_label.config(font=("Arial", title_font_size, "bold"))
        self.text_label.config(font=("Arial", text_font_size), wraplength=wrap_length)

        # Hide text_label if the width is too small
        if width < 900:  # Adjust this threshold as needed
            self.text_label.grid_remove()
            self.__centerCanvas__()
        else:
            self.text_label.grid()
            self.__resetCanvasPosition__()

        return None

    @private_method
    def __centerCanvas__(self) -> None:
        """Center the canvas when the text label is hidden.

        Returns:
            None
        """
        self.grid_canvas.grid_configure(row=1, column=0, columnspan=2, pady=0, padx=0, sticky="nsew")
        # Il faut que le canvas prenne seulement la taille de la grille
        # Il faut que le canvas soit centré dans la fenêtre
        self.grid_canvas.place(relx=0.5, rely=0.5, anchor="center")

        return None

    @private_method
    def __resetCanvasPosition__(self) -> None:
        """Reset the canvas position when the text label is visible.

        Returns:
            None
        """
        self.grid_canvas.grid_configure(row=1, column=1, pady=0, padx=(10, 100), sticky="e")

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