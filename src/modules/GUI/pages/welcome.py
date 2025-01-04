## Interface

"""
Welcome Page Module

This module provides the implementation of the welcome page for the Tic Tac Toe game using the tkinter library.

Classes:
    Welcome: Represents the welcome page of the Tic Tac Toe game.

Functions:
    __init__(self, parent: tk.Frame, controller: tk.Tk) -> bool:
        Initialize the welcome page with the given parent and controller.
        
    show(self) -> bool:
        Show the welcome page.
        
    hide(self) -> bool:
        Hide the welcome page.
        
    startGame(self) -> bool:
        Start the game when the "Start Game" button is pressed.
    
    __drawGrid__(self, size: int) -> bool:
        private method
        Draw the grid on the canvas.
        
    __adjustButtonSize__(self, width: int) -> bool:
        private method
        Adjust the button size based on the window width.
    
    __onResize__(self, event: tk.Event) -> bool:
        private method
        Resize the elements on the page based on the window size.
        
    __adjustFontSizes__(self, width: int) -> bool:
        private method
        Adjust the font sizes based on the window width.
        
    __centerCanvas__(self) -> bool:
        private method
        Center the canvas on the page.
        
    __resetCanvasPosition__(self) -> bool:
        private method
        Reset the canvas position on the page.
        
    goToSettings(self) -> bool:
        Navigate to the settings page.
"""

# ---------------------------------------------------------------------------------------------------- #

## Implementation

# Import #
import tkinter as tk
from tkinter import ttk
from modules.GUI.draft.grid import drawGrid
from modules.utils.decorator import privatemethod
from modules.GUI.pages.page import Page
from modules.GUI.render import PageName

class Welcome(Page):
    ## Initialize the welcome page with the given parent and controller.
    #
    # @param parent The parent frame.
    # @param controller The controller for the page.
    # @return bool True if the function succeeds, False otherwise.
    def __init__(self, parent: tk.Frame, controller: tk.Tk) -> None:
        super().__init__(parent, controller)

        # Main grid configuration
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=2)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)

        # Title "Tic Tac Toe"
        self.titleLabel = ttk.Label(self, text="Tic Tac Toe", font=("Arial", 48, "bold"))
        self.titleLabel.grid(row=0, column=0, columnspan=2, pady=(50, 0), padx=0, sticky="n")

        # Lorem Ipsum text
        self.textLabel = ttk.Label(self, 
                                    text=("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent rutrum tellus "
                                          "non ante euismod, id blandit massa auctor. Quisque urna tellus, sodales at ante nec," 
                                          " pharetra tincidunt ante."), 
                                    wraplength=600, 
                                    justify="left",
                                    font=("Arial", 20))
        self.textLabel.grid(row=1, column=0, pady=(5, 5), padx=(100, 10), sticky="w")

        # Unique canvas for the grid and symbols
        self.gridCanvas = tk.Canvas(self, bg="#333", highlightthickness=0)
        self.gridCanvas.grid(row=1, column=1, pady=0, padx=(10, 100), sticky="e")

        # "Settings" button
        self.settingsButton = ttk.Button(self, text="Settings", command=self.goToSettings)
        self.settingsButton.grid(row=2, column=0, columnspan=2, pady=50, sticky="s")

        # Dynamic resizing
        self.bind("<Configure>", self.__onResize__)

        return None

    ## Show the welcome page.
    #
    # @return bool True if the function succeeds, False otherwise.
    def show(self) -> bool:
        self.grid()
        return True

    ## Hide the welcome page.
    #
    # @return bool True if the function succeeds, False otherwise.
    def hide(self) -> bool:
        self.gridRemove()
        return True

    @privatemethod
    def __drawGrid__(self, size: int) -> bool:
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        cellSize = size // 3

        board = [
            ['X', 'O', '△'],
            ['⬡', '★', '▢'],
            ['◊', '#', '']
        ]

        playerSymbols = ['X', 'O', '△', '⬡', '★', '▢', '◊']
        playerColors = ['#FF0000', '#00FF00', '#0000FF', '#FFFF00', '#FF00FF', '#00FFFF', '#FFFFFF']

        if not drawGrid(self.gridCanvas, size, size, cellSize, board, playerSymbols=playerSymbols, playerColors=playerColors):
            raise RuntimeError("Failed to draw grid")

        return True

    @privatemethod
    def __adjustButtonSize__(self, width: int) -> bool:
        if not isinstance(width, int):
            raise TypeError("width must be an integer")

        buttonFontSize = max(18, int(width * 0.01))

        style = ttk.Style()
        style.configure("TButton", font=("Arial", buttonFontSize))

        return True

    @privatemethod
    def __onResize__(self, event: tk.Event) -> bool:
        if not isinstance(event, tk.Event):
            raise TypeError("event must be an tk.Event instance")

        size = min(event.width, event.height) * 0.6
        size = int(size) - (int(size) % 2)

        self.gridCanvas.config(width=size, height=size)

        if not self.__drawGrid__(size):
            raise RuntimeError("Failed to draw grid")

        if not self.__adjustFontSizes__(event.width):
            raise RuntimeError("Failed to adjust font sizes")

        if not self.__adjustButtonSize__(event.width):
            raise RuntimeError("Failed to adjust button size")

        return True

    @privatemethod
    def __adjustFontSizes__(self, width: int) -> bool:
        if not isinstance(width, int):
            raise TypeError("width must be an integer")

        titleFontSize = max(20, int(width * 0.03))
        textFontSize = max(12, int(width * 0.015))
        
        wrapLength = width / 2 - 110

        self.titleLabel.config(font=("Arial", titleFontSize, "bold"))
        self.textLabel.config(font=("Arial", textFontSize), wraplength=wrapLength)

        if width < 900:
            self.textLabel.gridRemove()
            if not self.__centerCanvas__():
                raise RuntimeError("Failed to center canvas")
        else:
            self.textLabel.grid()
            if not self.__resetCanvasPosition__():
                raise RuntimeError("Failed to reset canvas position")

        return True

    @privatemethod
    def __centerCanvas__(self) -> bool:
        self.gridCanvas.grid_configure(row=1, column=0, columnspan=2, pady=0, padx=0, sticky="nsew")
        self.gridCanvas.place(relx=0.5, rely=0.5, anchor="center")

        return True

    @privatemethod
    def __resetCanvasPosition__(self) -> bool:
        self.gridCanvas.grid_configure(row=1, column=1, pady=0, padx=(10, 100), sticky="e")

        return True

    ## Start the game when the "Start Game" button is pressed.
    #
    # @return bool True if the function succeeds, False otherwise.
    def startGame(self) -> bool:
        return self.controller.showFrame(PageName.GAME)

    ## Navigate to the settings page.
    #
    # @return bool True if the function succeeds, False otherwise.
    def goToSettings(self) -> bool:
        return self.controller.showFrame(PageName.SETTINGS)