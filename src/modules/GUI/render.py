from typing import Optional, Dict
from enum import Enum
import os
import importlib

import customtkinter as ctk
import tkinter as tk
from tkinter import ttk

from modules.utils.decorator import privatemethod
from modules.GUI.page import Page

# ************************************************
# CLASS App
# ************************************************
# ROLE : Used to create the main application
# ************************************************
# VERSION : 1.0
# AUTHOR : Hugo MERY
# DATE : 18/01/2025
# ************************************************

class PageName(Enum):
    WELCOME = "Welcome"
    FIRSTSETTINGS = "FirstSettings"
    SECONDSETTINGS = "SecondSettings"
    GAME = "Game"

class App(ctk.CTk):
    
    """
    The main application.
    """
    
    def __init__(self, title: str, firstPage: PageName = PageName.WELCOME, geometry: Optional[str] = None) -> None:
        
        """
        Initializes the application.
        
        Parameters:
            title (str): The title of the application.
            firstPage (PageName): The first page to display.
            geometry (Optional[str]): The geometry of the application window.

        Returns:
            None
        """
        
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
            self.attributes("-fullscreen", False)
            
        self.bind("<Escape>", self.__closeWindow__)
        self.frames: Dict[str, Page] = {}

        container: ttk.Frame = ttk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        if not self.__createFrames__(container):
            raise RuntimeError("Failed to create frames")
        if not self.showFrame(firstPage):
            print(f"Error: Failed to show frame '{firstPage.value}'")
            raise RuntimeError("Failed to show frame")
        
        return None

    @privatemethod
    def __closeWindow__(self, event: Optional[tk.Event] = None) -> bool:
        
        """
        Closes the application window.
        
        Parameters:
            event (Optional[tk.Event]): The event that triggered the close action.

        Returns:
            bool: True if the function succeeds, False otherwise.
        """
        
        if event is not None and not isinstance(event, tk.Event):
            raise TypeError("event must be a tk.Event instance or None")

        self.destroy()
        
        return True

    @privatemethod
    def __createFrames__(self, container: ttk.Frame) -> bool:
        
        """
        Creates the frames for the application.
        
        Parameters:
            container (ttk.Frame): The container to hold the frames.

        Returns:
            bool: True if the function succeeds, False otherwise.
        """
        
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

    def showFrame(self, pageName: PageName, **kwargs) -> bool:
        
        """
        Shows a specific frame.
        
        Parameters:
            pageName (PageName): The name of the frame to show.

        Returns:
            bool: True if the function succeeds, False otherwise.
        """
        
        if not isinstance(pageName, PageName):
            raise TypeError("pageName must be a PageName")

        frame: Page = self.frames.get(pageName.value)
        if frame is None:
            print(f"Error: No frame found with name '{pageName.value}'")
            return False
        frame.tkraise()
        
        # Call startGame if the page is Game
        if pageName == PageName.GAME:
            if not frame.startGame(**kwargs):
                print("Error: Failed to start game")
                return False
        elif pageName == PageName.SECONDSETTINGS:
            if not frame.setValues(**kwargs):
                print("Error: Failed to set values for SecondSettings")
                return False
        elif pageName == PageName.WELCOME:
            if not self.frames[PageName.FIRSTSETTINGS.value].resetSettings():
                print("Error: Failed to reset settings for FirstSettings")
                return False
            if not self.frames[PageName.GAME.value].resetGame():
                print("Error: Failed to reset game for Game")
                return False
            if not self.frames[PageName.SECONDSETTINGS.value].resetSettings():
                print("Error: Failed to reset settings for FirstSettings")
                return False            
        
        return True