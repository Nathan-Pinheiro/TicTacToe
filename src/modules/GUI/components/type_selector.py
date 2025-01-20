import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
from CTkColorPicker import *
from typing import Optional, List, Any, Dict

# ************************************************
# CLASS TypeSelector
# ************************************************
# ROLE : This class is used to create a symbol selector
# ************************************************
# VERSION : 1.0
# AUTHOR : Hugo MERY
# DATE : 18/01/2025
# ************************************************

class TypeSelector(ctk.CTkFrame):
    
    """
    The type selector component.
    """

    def __init__(self, parent, type="human", **kwargs) -> None:
        
        """
        Initializes the type selector component.
        
        Parameters:
            parent (ctk.CTkFrame): The parent frame.
            type (str): The initial type.
            **kwargs: Additional keyword arguments for the frame.
            
        Returns:
            None
        """
        
        super().__init__(parent, **kwargs)
        self.types : List[str] = ["human", "easy", "medium", "hard"]
        if type not in self.types:
            type = self.types[0]
        self.type : str = type
        self.onTypeChange: Optional[callable] = None
        self.__createWidgets__()
        
        return None

    def __createWidgets__(self) -> bool:
        
        """
        Creates the widgets for the type selector.
        
        Returns:
            bool: True if the widgets are created successfully.
        """
        
        self.canvas : tk.Canvas = tk.Canvas(self, width=132, height=132, bg="#333333", borderwidth=0, highlightthickness=0)
        self.canvas.grid(row=0, column=0, padx=10, pady=10)
        self.__loadImages__()
        self.__drawType__()
        self.selectButton : ctk.CTkButton = ctk.CTkButton(self, text="Select Type", command=self.__selectType__)
        self.selectButton.grid(row=1, column=0, padx=10, pady=10)
        
        return True

    def __loadImages__(self) -> bool:
        
        """
        Loads the images for the type selector.
        
        Returns:
            bool: True if the images are loaded successfully.
        """
        
        self.images : Dict[str, Any] = {
            "human": ImageTk.PhotoImage(Image.open("./assets/Human.png").resize((100, 100))),
            "easy": ImageTk.PhotoImage(Image.open("./assets/Easy.png").resize((100, 100))),
            "medium": ImageTk.PhotoImage(Image.open("./assets/Medium.png").resize((100, 100))),
            "hard": ImageTk.PhotoImage(Image.open("./assets/Hard.png").resize((100, 100)))
        }
        
        return True

    def __drawType__(self) -> bool:
        
        """
        Draws the selected type on the canvas.
        
        Returns:
            bool: True if the type is drawn successfully.
        """
        
        self.canvas.delete("all")
        self.canvas.create_image(66, 66, image=self.images[self.type])
        
        return True

    def __selectType__(self) -> bool:
        
        """
        Selects the next type.
        
        Returns:
            bool: True if the type is selected successfully.
        """
        
        currentIndex : int = self.types.index(self.type)
        nextIndex : int = (currentIndex + 1) % len(self.types)
        self.type : str = self.types[nextIndex]
        self.__drawType__()
        if self.onTypeChange:
            self.onTypeChange()
            return True
        return False

    def getType(self) -> str:
        
        """
        Gets the selected type.
        
        Returns:
            str: The selected type.
        """
        
        return self.type
    
    def setType(self, type) -> bool:
        
        """
        Sets the type of the type selector.
        
        Parameters:
            type (str): The type to set.
            
        Returns:
            bool: True if the type is set successfully.
        """
        
        self.type : Any | str = type
        self.__drawType__()