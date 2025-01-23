import tkinter as tk
import customtkinter as ctk
from CTkColorPicker import *
from PIL import Image, ImageTk

from modules.utils.decorator import privatemethod

from typing import Optional, List, Any, Dict
from enum import Enum

# ************************************************
# CLASS TypeSelector
# ************************************************
# ROLE : This class is used to create a symbol selector
# ************************************************
# VERSION : 1.0
# AUTHOR : Hugo MERY
# DATE : 18/01/2025
# ************************************************

class Types(Enum):
    
    """
    The available types.
    """
    
    HUMAN = "human"
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"
    IMPOSSIBLE = "impossible"

class TypeSelector(ctk.CTkFrame):
    
    """
    The type selector component.
    """

    def __init__(self, parent: ctk.CTkFrame, type: Types = Types.HUMAN, **kwargs: dict[str, Any]) -> None:
        
        """
        Initializes the type selector component.
        
        Parameters:
            parent (ctk.CTkFrame): The parent frame.
            type (Types): The initial type.
            **kwargs: Additional keyword arguments for the frame.
            
        Raises:
            TypeError: If parent is not a ctk.CTkFrame instance.
            TypeError: If type is not an instance of Types.
            ValueError: If type is not a valid type.
            
        Returns:
            None
        """
        
        # Check if the parent is a ctk.CTkFrame instance
        if not isinstance(parent, ctk.CTkFrame):
            raise TypeError("parent must be a ctk.CTkFrame instance")
        
        # Call the parent constructor
        super().__init__(parent, **kwargs)
        
        # Define the types
        self.types: List[Types] = list(Types)
        
        # Check if the type is an instance of Types
        if not isinstance(type, Types):
            raise TypeError("type must be an instance of Types")
        
        # Check if the type is a valid type
        if type not in self.types:
            type = self.types[0]
        
        # Define the type
        self.type: Types = type
        
        # Define the onTypeChange callback
        self.onTypeChange: Optional[callable] = None
        
        # Create the widgets
        self.__createWidgets__()
        
        return None

    @privatemethod
    def __createWidgets__(self) -> bool:
        
        """
        Creates the widgets for the type selector.
        
        Returns:
            bool: True if the widgets are created successfully.
        """

        # Create the canvas
        self.canvas : tk.Canvas = tk.Canvas(self, width=132, height=132, bg="#333333", borderwidth=0, highlightthickness=0)
        self.canvas.grid(row=0, column=0, padx=10, pady=10)
        
        # Load the images
        self.__loadImages__()
        
        # Draw the type
        self.__drawType__()
        
        # Create the select button
        self.selectButton : ctk.CTkButton = ctk.CTkButton(self, text="Select Type", command=self.__selectType__)
        self.selectButton.grid(row=1, column=0, padx=10, pady=10)
        
        return True

    @privatemethod
    def __loadImages__(self) -> bool:
        
        """
        Loads the images for the type selector.
        
        Returns:
            bool: True if the images are loaded successfully.
        """
        
        # Load the images
        self.images : Dict[str, Any] = {
            "human": ImageTk.PhotoImage(Image.open("./assets/Human.png").resize((100, 100))),
            "easy": ImageTk.PhotoImage(Image.open("./assets/Easy.png").resize((100, 100))),
            "medium": ImageTk.PhotoImage(Image.open("./assets/Medium.png").resize((100, 100))),
            "hard": ImageTk.PhotoImage(Image.open("./assets/Hard.png").resize((100, 100))),
            "impossible": ImageTk.PhotoImage(Image.open("./assets/Impossible.png").resize((100, 100)))
        }
        
        return True

    @privatemethod
    def __drawType__(self) -> bool:
        
        """
        Draws the selected type on the canvas.
        
        Returns:
            bool: True if the type is drawn successfully.
        """
        
        # Delete all items on the canvas
        self.canvas.delete("all")
        
        # Draw the image
        self.canvas.create_image(66, 66, image=self.images[self.type.value])
        
        return True

    @privatemethod
    def __selectType__(self) -> bool:
        
        """
        Selects the next type.
        
        Returns:
            bool: True if the type is selected successfully.
        """
        
        # Get the current and next index
        currentIndex : int = self.types.index(self.type)
        nextIndex : int = (currentIndex + 1) % len(self.types)
        
        # Set the type
        self.type = self.types[nextIndex]
        
        # Draw the type
        self.__drawType__()
        
        # Call the onTypeChange callback
        if self.onTypeChange:
            self.onTypeChange()
            return True
        
        return False

    def getType(self) -> Types:
        
        """
        Gets the selected type.
        
        Returns:
            Types: The selected type.
        """
        
        return self.type
    
    def setType(self, type: Types) -> bool:
        
        """
        Sets the type of the type selector.
        
        Parameters:
            type (Types): The type to set.
            
        Returns:
            bool: True if the type is set successfully.
        """
        
        if not isinstance(type, Types):
            raise TypeError("type must be an instance of Types")
        
        # Set the type and draw it
        self.type = type
        self.__drawType__()
        
        return True