## Interface

"""
Welcome Page Module

This module provides the implementation of the welcome page for the Tic Tac Toe game using the tkinter library.

Classes:
    Welcome: A class representing the welcome page of the Tic Tac Toe game.

Functions:
    __init__(self, parent: tk.Tk, controller: tk.Tk) -> None:
        Initialize the welcome page with the given parent and controller.
        
    __drawGrid__(self, size: int) -> bool:
        Private method.
        Draw the tic-tac-toe grid with symbols.
        
    __adjustButtonSize__(self, width: int) -> bool:
        Private method.
        Adjust the size of the start button based on the window size.
        
    __onResize__(self, event: tk.Event) -> bool:
        Private method.
        Redraw widgets responsively when the window is resized.
        
    __adjustFontSizes__(self, width: int) -> bool:
        Private method.
        Adjust the font sizes of the title and text labels based on the window size.
        
    __centerCanvas__(self) -> bool:
        Private method.
        Center the canvas when the text label is hidden.
        
    __resetCanvasPosition__(self) -> bool:
        Private method.
        Reset the canvas position when the text label is visible.
        
    start_game(self) -> bool:
        Start the game when the "Start Game" button is pressed.
        
    go_to_settings(self) -> bool:
        Navigate to the settings page.
"""

# ---------------------------------------------------------------------------------------------------- #

## Implementation

# Import #
import tkinter as tk
from tkinter import ttk
from modules.GUI.draft.grid import draw_grid
from modules.utils.decorator import private_method

class Welcome(ttk.Frame):
    ## Initialize the welcome page with the given parent and controller.
    #
    # @param parent The parent widget.
    # @param controller The controller of the application.
    def __init__(self, parent: tk.Frame, controller: tk.Tk) -> None:
        if not isinstance(parent, ttk.Frame):
            raise TypeError("parent must be a tk.Frame instance")
        if not isinstance(controller, tk.Tk):
            raise TypeError("controller must be a tk.Tk instance")

        super().__init__(parent)
        self.controller: tk.Tk = controller

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

        # "Settings" button
        self.settings_button: ttk.Button = ttk.Button(self, text="Settings", command=self.go_to_settings)
        self.settings_button.grid(row=2, column=0, columnspan=2, pady=50, sticky="s")

        # Dynamic resizing
        self.bind("<Configure>", self.__onResize__)

    ## Draw the tic-tac-toe grid with symbols.
    #
    # @param size The size of the grid.
    # @return bool True if the function succeeds, False otherwise.
    @private_method
    def __drawGrid__(self, size: int) -> bool:
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        # Cell size
        cell_size: int = size // 3

        # Example board configuration
        board: list[list[str]] = [
            ['X', 'O', '△'],
            ['⬡', '★', '▢'],
            ['◊', '#', '']
        ]

        # Define player symbols and colors
        player_symbols: list[str] = ['X', 'O', '△', '⬡', '★', '▢', '◊']
        player_colors: list[str] = ['#FF0000', '#00FF00', '#0000FF', '#FFFF00', '#FF00FF', '#00FFFF', '#FFFFFF']

        # Draw the grid with symbols
        if not draw_grid(self.grid_canvas, size, size, cell_size, board, player_symbols=player_symbols, player_colors=player_colors):
            raise RuntimeError("Failed to draw grid")

        return True

    ## Adjust the size of the start button based on the window size.
    #
    # @param width The width of the window.
    # @return bool True if the function succeeds, False otherwise.
    @private_method
    def __adjustButtonSize__(self, width: int) -> bool:
        if not isinstance(width, int):
            raise TypeError("width must be an integer")

        # Calculate new font size for the button
        button_font_size: int = max(18, int(width * 0.01))  # 2% of the window width

        # Update button font size using ttk.Style
        style: ttk.Style = ttk.Style()
        style.configure("TButton", font=("Arial", button_font_size))

        return True

    ## Redraw widgets responsively when the window is resized.
    #
    # @param event The event object.
    # @return bool True if the function succeeds, False otherwise.
    @private_method
    def __onResize__(self, event: tk.Event) -> bool:
        if not isinstance(event, tk.Event):
            raise TypeError("event must be an tk.Event instance")

        # Calculate the size of the square based on the window
        size: int = min(event.width, event.height) * 0.6  # Canvas size (50% of the window)
        size = int(size) - (int(size) % 2)  # Ensure the size is a multiple of 3

        # Update the canvas size
        self.grid_canvas.config(width=size, height=size)

        # Redraw the grid and symbols
        if not self.__drawGrid__(size):
            raise RuntimeError("Failed to draw grid")

        # Adjust font sizes
        if not self.__adjustFontSizes__(event.width):
            raise RuntimeError("Failed to adjust font sizes")

        # Adjust button size
        if not self.__adjustButtonSize__(event.width):
            raise RuntimeError("Failed to adjust button size")

        return True

    ## Adjust the font sizes of the title and text labels based on the window size.
    #
    # @param width The width of the window.
    # @return bool True if the function succeeds, False otherwise.
    @private_method
    def __adjustFontSizes__(self, width: int) -> bool:
        if not isinstance(width, int):
            raise TypeError("width must be an integer")

        # Calculate new font sizes
        title_font_size: int = max(20, int(width * 0.03))  # 3% of the window width
        text_font_size: int = max(12, int(width * 0.015))  # 2% of the window width
        
        # Calculate new wrap length for the text label
        wrap_length: float = width / 2 - 110  # 110 is the sum of the left and right paddings

        # Update font sizes
        self.title_label.config(font=("Arial", title_font_size, "bold"))
        self.text_label.config(font=("Arial", text_font_size), wraplength=wrap_length)

        # Hide text_label if the width is too small
        if width < 900:  # Adjust this threshold as needed
            self.text_label.grid_remove()
            if not self.__centerCanvas__():
                raise RuntimeError("Failed to center canvas")
        else:
            self.text_label.grid()
            if not self.__resetCanvasPosition__():
                raise RuntimeError("Failed to reset canvas position")

        return True

    ## Center the canvas when the text label is hidden.
    #
    # @return bool True if the function succeeds, False otherwise.
    @private_method
    def __centerCanvas__(self) -> bool:
        self.grid_canvas.grid_configure(row=1, column=0, columnspan=2, pady=0, padx=0, sticky="nsew")
        self.grid_canvas.place(relx=0.5, rely=0.5, anchor="center")

        return True

    ## Reset the canvas position when the text label is visible.
    #
    # @return bool True if the function succeeds, False otherwise.
    @private_method
    def __resetCanvasPosition__(self) -> bool:
        self.grid_canvas.grid_configure(row=1, column=1, pady=0, padx=(10, 100), sticky="e")

        return True

    ## Start the game when the "Start Game" button is pressed.
    #
    # @return bool True if the function succeeds, False otherwise.
    def start_game(self) -> bool:
        self.controller.showFrame("Game")
        return True

    ## Navigate to the settings page.
    #
    # @return bool True if the function succeeds, False otherwise.
    def go_to_settings(self) -> bool:
        self.controller.showFrame("Settings")
        return True