## Interface

"""
Welcome Page Module

This module provides a class to represent the welcome page of the Tic Tac Toe game.

Classes:
    Welcome: Represents the welcome page.
    
    Attributes:
        controller (App): The controller for the application.

Methods:
    __init__(parent: ttk.Frame, controller: App) -> None:
        Constructor for the Welcome class.
        
    on_resize(event: Event) -> None:
        Adjust the font size based on the window size.
"""

# ---------------------------------------------------------------------------------------------------- #

## Implementation

# Import #
import tkinter as tk
from tkinter import ttk
from typing import Any

# Class #
class Welcome(ttk.Frame):
    def __init__(self, parent: ttk.Frame, controller: Any) -> None:
        """Constructor for the Welcome class.

        Args:
            parent (ttk.Frame): The parent frame.
            controller (App): The controller for the application.
            
        Returns:
            None
        """
        
        super().__init__(parent)
        self.controller = controller
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        self.label = ttk.Label(self, text="Tic Tac Toe", font=("Arial", 64))
        self.label.grid(row=0, column=0, pady=100, sticky="n")

        self.button_frame = ttk.Frame(self)
        self.button_frame.grid(row=1, column=0, rowspan=4, sticky="n")

        self.start_button = ttk.Button(self.button_frame, text="Start Game", command=lambda: controller.show_frame("GameScreen"), style="TButton")
        self.start_button.grid(row=0, column=0, pady=15, padx=20, sticky="ew")

        self.settings_button = ttk.Button(self.button_frame, text="Settings", command=lambda: controller.show_frame("Settings"), style="TButton")
        self.settings_button.grid(row=1, column=0, pady=15, padx=20, sticky="ew")
        
        self.quit_button = ttk.Button(self.button_frame, text="Quit", command=controller.close_window, style="TButton")
        self.quit_button.grid(row=2, column=0, pady=15, padx=20, sticky="ew")

        # Apply the font size to the buttons
        self.style = ttk.Style()
        self.style.configure("TButton", font=("Arial", 52))

        # Make the button frame responsive
        self.button_frame.grid_rowconfigure(0, weight=1)
        self.button_frame.grid_rowconfigure(1, weight=1)
        self.button_frame.grid_rowconfigure(2, weight=1)
        self.button_frame.grid_columnconfigure(0, weight=1)

        # Bind the configure event to update fonts
        self.bind("<Configure>", self.on_resize)
        
        return None

    def on_resize(self, event : tk.Event) -> None:
        """Adjust the font size based on the window size.

        Args:
            event (Event): The resize event.
            
        Returns:
            None
        """
        
        new_size = min(event.width // 20, event.height // 20)
        self.label.config(font=("Arial", new_size))
        self.style.configure("TButton", font=("Arial", new_size // 2))
        
        return None