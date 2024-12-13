## Interface

"""
GUI Render Module

This module provides the main application class for the TicTacToe GUI.

Classes:
    App: Represents the main application window.
    
    Attributes:
        frames (dict): A dictionary to hold the frames of the application.

Functions:
    close_window(event: Optional[tk.Event] = None) -> None:
        Close the application window.
        
        Args:
            event (Optional[tk.Event]): The event that triggered the close action.
            
        Returns:
            None

    create_frames(container: ttk.Frame) -> None:
        Create the frames for the application.
        
        Args:
            container (ttk.Frame): The container to hold the frames.
            
        Returns:
            None

    show_frame(page_name: str) -> None:
        Show a specific frame.
        
        Args:
            page_name (str): The name of the frame to show.
            
        Returns:
            None
"""

## Implementation

# Import #
import tkinter as tk
from tkinter import ttk
from typing import Optional

from modules.GUI.pages.welcome import Welcome

# Class #
class App(tk.Tk):
    def __init__(self, title: str, firstPage: str = "Welcome", geometry: Optional[str] = None) -> None:
        """Constructor for the App class.
        
        Args:
            title (str): The title of the application.
            geometry (Optional[str]): The geometry of the application.
            firstPage (str): The first page to display.
            
        Returns:
            None
        """
        
        super().__init__()
        self.title(title)
        if geometry is not None:
            self.geometry(geometry)
        else:
            self.attributes("-fullscreen", False)
            self.state("zoomed")
            
        self.bind("<Escape>", self.close_window)
        self.frames: dict[str, ttk.Frame] = {}

        container = ttk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.create_frames(container)
        self.show_frame(firstPage)
        
        return None
        
    def close_window(self, event: Optional[tk.Event] = None) -> None:
        self.destroy()
        
        return None

    def create_frames(self, container: ttk.Frame) -> None:
        for F in [Welcome]:
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            
        return None

    def show_frame(self, page_name: str) -> None:
        frame: ttk.Frame = self.frames[page_name]
        frame.tkraise()
        
        return None

if __name__ == "__main__":
    app = App("TicTacToe")
    app.mainloop()