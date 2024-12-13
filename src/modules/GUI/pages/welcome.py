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
        
    debounce_resize(event: Event) -> None:
        Debounce the resize event to improve performance.
        
    on_resize(event: Event) -> None:
        Adjust the font size based on the window size.
"""

# ---------------------------------------------------------------------------------------------------- #

## Implementation

# Import #
import tkinter as tk
from tkinter import ttk
import sv_ttk

# Class #
class Welcome(ttk.Frame):
    def __init__(self, parent: ttk.Frame, controller: 'App') -> None:
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
        self.grid_columnconfigure(1, weight=1)
        
        self.label = ttk.Label(self, text="Tic Tac Toe", font=("Arial", 64))
        self.label.grid(row=0, column=0, columnspan=2, pady=100, sticky="n")

        self.button_frame = ttk.Frame(self)
        self.button_frame.grid(row=1, column=0, rowspan=4, sticky="nsew")

        self.start_button = ttk.Button(self.button_frame, text="Start Game", command=lambda: controller.show_frame("GameScreen"), style="TButton")
        self.start_button.grid(row=0, column=0, pady=15, padx=20, sticky="ew")

        self.settings_button = ttk.Button(self.button_frame, text="Settings", command=lambda: controller.show_frame("Settings"), style="TButton")
        self.settings_button.grid(row=1, column=0, pady=15, padx=20, sticky="ew")
        
        self.quit_button = ttk.Button(self.button_frame, text="Quit", command=controller.close_window, style="TButton")
        self.quit_button.grid(row=2, column=0, pady=15, padx=20, sticky="ew")

        # Apply the font size to the buttons
        self.style = ttk.Style()
        self.style.configure("TButton", font=("Arial", 20))

        # Make the button frame responsive
        self.button_frame.grid_rowconfigure(0, weight=1)
        self.button_frame.grid_rowconfigure(1, weight=1)
        self.button_frame.grid_rowconfigure(2, weight=1)
        self.button_frame.grid_columnconfigure(0, weight=1)
        
        sv_ttk.set_theme("dark")

        # Bind the configure event to update fonts
        self.bind("<Configure>", self.debounce_resize)
        
        self._resize_id = None
        
        return None

    def debounce_resize(self, event):
        """Debounce the resize event to improve performance."""
        if self._resize_id is not None:
            self.after_cancel(self._resize_id)
        self._resize_id = self.after(300, self.on_resize, event)

    def on_resize(self, event):
        """Adjust the layout based on the window size.

        Args:
            event (Event): The resize event.
            
        Returns:
            None
        """
        if event.width < 600:
            self.button_frame.grid(row=1, column=0, columnspan=2, sticky="nsew")
        else:
            self.button_frame.grid(row=1, column=0, rowspan=4, sticky="nsew")
        
        return None
