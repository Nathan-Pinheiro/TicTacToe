## Interface

"""
GUI Render Module

This module provides the main application class for the TicTacToe GUI.

Classes:
    App: Represents the main application window.
    
    Attributes:
        frames (dict[str, Page]): A dictionary to hold the frames of the application.

Functions:
    __init__(self, title: str, firstPage: PageName, geometry: Optional[str] = None) -> bool:
        Initialize the application with the given title, first page, and geometry.
        
    __closeWindow__(self, event: Optional[tk.Event] = None) -> bool:
        Private method.
        Close the application window.
        
    __createFrames__(self, container: ttk.Frame) -> bool:
        Private method.
        Create the frames for the application.
        
    showFrame(self, pageName: PageName) -> bool:
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
from enum import Enum

from modules.utils.decorator import privatemethod
from modules.GUI.pages.page import Page

class PageName(Enum):
    WELCOME = "Welcome"
    SETTINGS = "SettingsPage"
    GAME = "Game"

# Class #
class App(tk.Tk):
    ## Initialize the application with the given title, first page, and geometry.
    #
    # @param title The title of the application.
    # @param firstPage The first page to display.
    # @param geometry The geometry of the application.
    # @return bool True if the function succeeds, False otherwise.
    def __init__(self, title: str, firstPage: PageName = PageName.WELCOME, geometry: Optional[str] = None) -> None:
        if not isinstance(title, str):
            raise TypeError("title must be a string")
        if not isinstance(firstPage, PageName):
            raise TypeError("firstPage must be a PageName")
        if geometry is not None and not isinstance(geometry, str):
            raise TypeError("geometry must be a string or None")

        super().__init__()
        self.title(title)
        if geometry is not None:
            self.geometry(geometry)
        else:
            self.attributes("-fullscreen", True)
            
        self.bind("<Escape>", self.__closeWindow__)
        self.frames: Dict[str, Page] = {}

        container: ttk.Frame = ttk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        if not self.__createFrames__(container):
            raise RuntimeError("Failed to create frames")
        if not self.showFrame(firstPage):
            raise RuntimeError("Failed to show frame")
        
        sv_ttk.set_theme("dark")
        
        return None
        
    ## Close the application window.
    #
    # @param event The event that triggered the close action.
    # @return bool True if the function succeeds, False otherwise.
    @privatemethod
    def __closeWindow__(self, event: Optional[tk.Event] = None) -> bool:
        if event is not None and not isinstance(event, tk.Event):
            raise TypeError("event must be a tk.Event instance or None")

        self.destroy()
        
        return True

    ## Create the frames for the application.
    #
    # @param container The container to hold the frames.
    # @return bool True if the function succeeds, False otherwise.
    @privatemethod
    def __createFrames__(self, container: ttk.Frame) -> bool:
        if not isinstance(container, ttk.Frame):
            raise TypeError("container must be a ttk.Frame instance")

        pagesDir: str = os.path.join(os.path.dirname(__file__), 'pages')
        
        if not os.path.exists(pagesDir):
            print(f"Directory not found: {pagesDir}")
            return False
        
        for filename in os.listdir(pagesDir):
            if filename.endswith('.py') and filename != '__init__.py':
                moduleName: str = f"modules.GUI.pages.{filename[:-3]}"
                module = importlib.import_module(moduleName)
                for attr in dir(module):
                    cls = getattr(module, attr)
                    if isinstance(cls, type) and issubclass(cls, Page) and cls is not Page:
                        pageName: str = cls.__name__
                        frame: Page = cls(parent=container, controller=self)
                        self.frames[pageName] = frame
                        frame.grid(row=0, column=0, sticky="nsew")
            
        return True

    ## Show a specific frame.
    #
    # @param pageName The name of the frame to show.
    # @return bool True if the function succeeds, False otherwise.
    def showFrame(self, pageName: PageName) -> bool:
        if not isinstance(pageName, PageName):
            raise TypeError("pageName must be a PageName")

        frame: Page = self.frames.get(pageName.value)
        if frame is None:
            print(f"Error: No frame found with name '{pageName.value}'")
            return False
        frame.tkraise()
        
        # Call startGame if the page is Game
        if pageName == PageName.GAME:
            if not frame.startGame():
                return False
        elif pageName == PageName.WELCOME:
            if not self.frames[PageName.SETTINGS.value].resetSettings():
                return False
            if not self.frames[PageName.GAME.value].resetGame():
                return False
        
        return True