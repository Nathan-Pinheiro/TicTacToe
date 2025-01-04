## Interface

"""
GUI Render Module

This module provides the main application class for the TicTacToe GUI.

Classes:
    App: Represents the main application window.
    
    Attributes:
        frames (dict[str, ttk.Frame]): A dictionary to hold the frames of the application.

Functions:
    __init__(self, title: str, first_page: str = "Welcome", geometry: Optional[str] = None) -> bool:
        Initialize the welcome page with the given parent and controller.
        
    __closeWindow__(self, event: Optional[tk.Event] = None) -> bool:
        Private method.
        Close the application window.
        
    __createFrames__(self, container: ttk.Frame) -> bool:
        Private method.
        Create the frames for the application.
        
    showFrame(self, page_name: str) -> bool:
        Show a specific frame.
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
    ## Initialize the welcome page with the given parent and controller.
    #
    # @param title The title of the application.
    # @param first_page The first page to display.
    # @param geometry The geometry of the application.
    # @return bool True if the function succeeds, False otherwise.
    def __init__(self, title: str, first_page: str = "Welcome", geometry: Optional[str] = None) -> None:
        if not isinstance(title, str):
            raise TypeError("title must be a string")
        if not isinstance(first_page, str):
            raise TypeError("first_page must be a string")
        if geometry is not None and not isinstance(geometry, str):
            raise TypeError("geometry must be a string or None")

        super().__init__()
        self.title(title)
        if geometry is not None:
            self.geometry(geometry)
        else:
            self.attributes("-fullscreen", True)
            
        self.bind("<Escape>", self.__closeWindow__)
        self.frames: Dict[str, ttk.Frame] = {}

        container: ttk.Frame = ttk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        if not self.__createFrames__(container):
            raise RuntimeError("Failed to create frames")
        self.showFrame(first_page)
        
        sv_ttk.set_theme("dark")
        
        return None
        
    ## Close the application window.
    #
    # @param event The event that triggered the close action.
    # @return bool True if the function succeeds, False otherwise.
    @private_method
    def __closeWindow__(self, event: Optional[tk.Event] = None) -> bool:
        if event is not None and not isinstance(event, tk.Event):
            raise TypeError("event must be a tk.Event instance or None")

        self.destroy()
        
        return True

    ## Create the frames for the application.
    #
    # @param container The container to hold the frames.
    # @return bool True if the function succeeds, False otherwise.
    @private_method
    def __createFrames__(self, container: ttk.Frame) -> bool:
        if not isinstance(container, ttk.Frame):
            raise TypeError("container must be a ttk.Frame instance")

        pages_dir: str = os.path.join(os.path.dirname(__file__), 'pages')
        
        if not os.path.exists(pages_dir):
            print(f"Directory not found: {pages_dir}")
            return False
        
        for filename in os.listdir(pages_dir):
            if filename.endswith('.py') and filename != '__init__.py':
                module_name: str = f"modules.GUI.pages.{filename[:-3]}"
                module = importlib.import_module(module_name)
                for attr in dir(module):
                    cls = getattr(module, attr)
                    if isinstance(cls, type) and issubclass(cls, ttk.Frame):
                        page_name: str = cls.__name__.capitalize()
                        frame: ttk.Frame = cls(parent=container, controller=self)
                        self.frames[page_name] = frame
                        frame.grid(row=0, column=0, sticky="nsew")
                        if page_name == "Settings":
                            frame = cls(parent=container, controller=self)
                            self.frames[page_name] = frame
                            frame.grid(row=0, column=0, sticky="nsew")
            
        return True

    ## Show a specific frame.
    #
    # @param page_name The name of the frame to show.
    # @return bool True if the function succeeds, False otherwise.
    def showFrame(self, page_name: str) -> bool:
        if not isinstance(page_name, str):
            raise TypeError("page_name must be a string")

        frame: ttk.Frame = self.frames.get(page_name)
        if frame is None:
            print(f"Error: No frame found with name '{page_name}'")
            return False
        frame.tkraise()
        
        # Call start_game if the page is Game
        if page_name == "Game":
            frame.start_game()
        elif page_name == "Welcome":
            self.frames["Settings"].reset_settings()
            self.frames["Game"].reset_game()
        
        return True