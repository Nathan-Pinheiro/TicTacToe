from typing import Any, Optional, Dict
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
    
    """
    The available pages.
    """
    
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
            
        Raises:
            TypeError: If title is not a string.
            TypeError: If firstPage is not a PageName.
            TypeError: If geometry is not a string or None.

        Returns:
            None
        """
        
        # Check if the title is a string
        if not isinstance(title, str):
            raise TypeError("title must be a string")
        
        # Check if firstPage is a PageName
        if not isinstance(firstPage, PageName):
            raise TypeError("firstPage must be a PageName")
        
        # Check if geometry is a string or None
        if geometry is not None and not isinstance(geometry, str):
            raise TypeError("geometry must be a string or None")

        # Call the parent constructor
        super().__init__()
        
        # Configure the window
        self.title(title)
        
        if geometry is not None:
            self.geometry(geometry)
            
        else:
            self.attributes("-fullscreen", False)
            
        # Bind the escape key to close the window
        self.bind("<Escape>", self.__closeWindow__)
        
        # Initialize the frames
        self.frames: Dict[str, Page] = {}

        # Create the container and configure it
        container: ctk.CTkFrame = ctk.CTkFrame(self)
        container.pack(side="top", fill="both", expand=True)
        
        container.grid_rowconfigure(0, weight=1)
        
        container.grid_columnconfigure(0, weight=1)

        # Show the container and display the first page 
        self.__createFrames__(container)
        
        self.showFrame(firstPage)
        
        return None

    @privatemethod
    def __closeWindow__(self, event: Optional[tk.Event] = None) -> bool:
        
        """
        Closes the application window.
        
        Parameters:
            event (Optional[tk.Event]): The event that triggered the close action.
            
        Raises:
            TypeError: If event is not a tk.Event instance or None.

        Returns:
            bool: True if the function succeeds, False otherwise.
        """
        
        # Check if event is a tk.Event instance or None
        if event is not None and not isinstance(event, tk.Event):
            raise TypeError("event must be a tk.Event instance or None")

        # Destroy the window
        self.destroy()
        
        return True

    @privatemethod
    def __createFrames__(self, container: ctk.CTkFrame) -> bool:
        
        """
        Creates the frames for the application.
        
        Parameters:
            container (ctk.CTkFrame): The container to hold the frames.
            
        Raises:
            TypeError: If the container is not a ctk.CTkFrame instance.
            FileNotFoundError: If the pages directory is not found.

        Returns:
            bool: True if the function succeeds, False otherwise.
        """
        
        # Check if the container is a ctk.CTkFrame instance
        if not isinstance(container, ctk.CTkFrame):
            raise TypeError("container must be a ctk.Frame instance")

        # Get the path to the pages directory
        pagesDir: str = os.path.join(os.path.dirname(__file__), 'pages')
        
        # Check if the pages directory exists
        if not os.path.exists(pagesDir):
            raise FileNotFoundError(f"Directory {pagesDir} not found")
        
        # Load the pages
        for filename in os.listdir(pagesDir):
            
            # Check if the file is a Python file and not the init file
            if filename.endswith('.py') and filename != '__init__.py':
                
                # Import dynamically the module
                moduleName: str = f"modules.GUI.pages.{filename[:-3]}"
                module = importlib.import_module(moduleName)
                
                # Get the classes in the module
                for attr in dir(module):
                    
                    cls = getattr(module, attr)
                    
                    # Check if the class is a subclass of Page and not Page itself
                    if isinstance(cls, type) and issubclass(cls, Page) and cls is not Page:
                        
                        # Create the frame and add it to the frames dictionary with the class name as key
                        pageName: str = cls.__name__
                        frame: Page = cls(parent=container, controller=self)
                        self.frames[pageName] = frame
                        frame.grid(row=0, column=0, sticky="nsew")
            
        return True

    def showFrame(self, pageName: PageName, **kwargs: dict[str, Any]) -> bool:
        
        """
        Shows a specific frame.
        
        Parameters:
            pageName (PageName): The name of the frame to show.
            **kwargs: Additional keyword arguments for the frame.

        Raises:
            TypeError: If pageName is not a PageName.
            TypeError: If kwargs is not a dictionary.
            ValueError: If the page is not found.
        
        Returns:
            bool: True if the function succeeds, False otherwise.
        """
        
        # Check if pageName is a PageName
        if not isinstance(pageName, PageName):
            raise TypeError("pageName must be a PageName")
        
        # Check if kwargs is a dictionary
        if not isinstance(kwargs, dict):
            raise TypeError("kwargs must be a dictionary")

        # Get the frame with the specified name
        frame: Page = self.frames.get(pageName.value)
        
        # Raise an error if the frame is not found
        if frame is None:
            raise ValueError(f"Page {pageName.value} not found")
        
        # Raise the frame
        frame.tkraise()
        
        # Call startGame if the page is Game
        if pageName == PageName.GAME:
            frame.startGame(**kwargs)
        
        # Set values if the page is FirstSettings or SecondSettings
        elif pageName == PageName.SECONDSETTINGS:
            frame.setValues(**kwargs)
            
        # Reset settings and game if the page is Welcome
        elif pageName == PageName.WELCOME:
            
            self.frames[PageName.FIRSTSETTINGS.value].resetSettings()
            
            self.frames[PageName.SECONDSETTINGS.value].resetSettings()    
            
            self.frames[PageName.GAME.value].resetGame()     
        
        return True