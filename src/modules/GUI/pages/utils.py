## Interface

"""
GUI Utility Module

This module provides utility functions for the GUI, such as navigation and resizing.

Functions:
    goTo(app, frame: str) -> None:
        Show the frame specified.
        
        Args:
            frame (str): The frame to show.
            
        Returns:
            None

    onResize(app, event: tk.Event) -> None:
        Adjust the font size based on the window size.
        
        Args:
            event (Event): The resize event.
            
        Returns:
            None
"""

## Implementation

# Import #
import tkinter as tk

# Functions #
def goTo(app: tk.Tk, frame: str) -> None:
        """Show the frame specified.

        Args:
            frame (str): The frame to show.
            
        Returns:
            None
        """
        
        app.controller.show_frame(frame)
        
        return None
    
def onResize(app: tk.Tk, event: tk.Event) -> None:
        """Adjust the font size based on the window size.

        Args:
            event (Event): The resize event.
            
        Returns:
            None
        """
        
        new_size = min(event.width // 20, event.height // 20)
        app.label.config(font=("Arial", new_size))
        app.style.configure("TButton", font=("Arial", new_size // 2))
        
        return None