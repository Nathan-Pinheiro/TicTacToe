## Interface

"""
GUI Render Module

This module provides the main application class for the TicTacToe GUI.

Classes:
    App: Represents the main application window.
    
    Attributes:
        frames (dict[str, ttk.Frame]): A dictionary to hold the frames of the application.

Methods:
    __init__(self, title: str, first_page: str = "Welcome", geometry: Optional[str] = None) -> None:
        Private method.
        Constructor for the App class.
        
        Args:
            title (str): The title of the application.
            geometry (Optional[str]): The geometry of the application.
            first_page (str): The first page to display.
        
    __closeWindow__(self, event: Optional[tk.Event] = None) -> None:
        Private method.
        Close the application window.
        
        Args:
            event (Optional[tk.Event]): The event that triggered the close action.
        
    __createFrames__(self, container: ttk.Frame) -> None:
        Private method.
        Create the frames for the application.
        
        Args:
            container (ttk.Frame): The container to hold the frames.
        
    showFrame(self, page_name: str) -> None:
        Show a specific frame.
        
        Args:
            page_name (str): The name of the frame to show.
"""

## Implementation

# Import #
import tkinter as tk
from tkinter import ttk
from typing import Optional, Dict
import sv_ttk
import os
import importlib

from modules.utils.decorator import private_method

# Class #
class App(tk.Tk):
    def __init__(self, title: str, first_page: str = "Welcome", geometry: Optional[str] = None) -> None:
        """Constructor for the App class.
        
        Args:
            title (str): The title of the application.
            geometry (Optional[str]): The geometry of the application.
            first_page (str): The first page to display.
            
        Returns:
            None
        """
        
        super().__init__()
        self.title(title)
        if geometry is not None:
            self.geometry(geometry)
        else:
            self.attributes("-fullscreen", True)
            
        self.bind("<Escape>", self.__closeWindow__)
        self.frames: Dict[str, ttk.Frame] = {}

        container = ttk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.__createFrames__(container)
        self.showFrame(first_page)
        
        sv_ttk.set_theme("dark")
        
        return None
        
    @private_method
    def __closeWindow__(self, event: Optional[tk.Event] = None) -> None:
        """Close the application window.
        
        Args:
            event (Optional[tk.Event]): The event that triggered the close action.
            
        Returns:
            None
        """
        self.destroy()
        
        return None

    @private_method
    def __createFrames__(self, container: ttk.Frame) -> None:
        """Create the frames for the application.
        
        Args:
            container (ttk.Frame): The container to hold the frames.
            
        Returns:
            None
        """

        pages_dir = os.path.join(os.path.dirname(__file__), 'pages')
        
        if not os.path.exists(pages_dir):
            print(f"Répertoire introuvable : {pages_dir}")
            return None
        
        for filename in os.listdir(pages_dir):
            if filename.endswith('.py') and filename != '__init__.py':
                module_name = f"modules.GUI.pages.{filename[:-3]}"
                module = importlib.import_module(module_name)
                for attr in dir(module):
                    cls = getattr(module, attr)
                    if isinstance(cls, type) and issubclass(cls, ttk.Frame):
                        page_name = cls.__name__.capitalize()
                        frame = cls(parent=container, controller=self)
                        self.frames[page_name] = frame
                        frame.grid(row=0, column=0, sticky="nsew")
            
        return None

    def showFrame(self, page_name: str) -> None:
        """Show a specific frame.
        
        Args:
            page_name (str): The name of the frame to show.
            
        Returns:
            None
        """
        frame: ttk.Frame = self.frames[page_name]
        if frame is None:
            print(f"Error: No frame found with name '{page_name}'")
            return None
        frame.tkraise()
        
        # Appeler start_game si la page est Game
        if page_name == "Game":
            frame.start_game()
        
        return None

if __name__ == "__main__":
    app = App("TicTacToe")
    app.mainloop()