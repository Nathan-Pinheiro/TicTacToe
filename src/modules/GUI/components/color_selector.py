import customtkinter as ctk
from CTkColorPicker import AskColor

from typing import Any

from modules.utils.decorator import privatemethod
from modules.utils.validators import isHexColor

# ************************************************
# CLASS ColorSelector
# ************************************************
# ROLE : This class is used to create a color selector
# ************************************************
# VERSION : 1.0
# AUTHOR : Hugo MERY
# DATE : 18/01/2025
# ************************************************

class ColorSelector(ctk.CTkFrame):
    
    """
    The color selector component.
    """
    
    def __init__(self, parent: ctk.CTkFrame, color: str ="#FFFFFF", **kwargs: dict[str, Any]) -> None:
        
        """
        Initializes the color selector component.
        
        Parameters:
            parent (ctk.CTkFrame): The parent frame.
            color (str): The initial color in hexadecimal format.
            **kwargs (dict): Additional keyword arguments for the frame.
            
        Raises:
            TypeError: If the parent is not an instance of ctk.CTkFrame.
            TypeError: If the color is not a string.
            ValueError: If the color is not a valid hexadecimal color.

        Returns:
            None
        """
        
        # Check if the parent is a ctk.CTkFrame instance
        if not isinstance(parent, ctk.CTkFrame):
            raise TypeError("Parent must be an instance of ctk.CTkFrame")
        
        # Call the parent constructor
        super().__init__(parent, **kwargs)
        
        # Check if the color is a string
        if not isinstance(color, str):
            raise TypeError("Color must be a string")
        
        # Check if the color is a valid hexadecimal color
        if not isHexColor(color):
            raise ValueError(f"Color {color} is not a valid hexadecimal color")
        
        # Define the color
        self.color : str = color
        
        # Create the widgets
        self.__createWidgets__()
        
        return None

    @privatemethod
    def __createWidgets__(self) -> bool:
        
        """
        Creates the widgets for the color selector.
        
        Returns:
            bool: True if widgets are created successfully.
        """
        
        # Create the color display
        self.colorDisplay : ctk.CTkLabel = ctk.CTkLabel(self, text="", width=132, height=132, bg_color=self.color)
        self.colorDisplay.grid(row=0, column=0, padx=10, pady=10)

        # Create the select button
        self.selectButton : ctk.CTkButton = ctk.CTkButton(self, text="Select Color", command=lambda : self.__selectColor__())
        self.selectButton.grid(row=1, column=0, padx=10, pady=10)
        
        return True

    @privatemethod
    def __selectColor__(self) -> bool:
        
        """
        Opens a color picker dialog to select a color.
        
        Returns:
            bool: True if a color is selected, False otherwise.
        """
        
        # Open the color picker dialog to select a color and get the color code
        pickColor : AskColor = AskColor(title="Choose color")
        colorCode : str = pickColor.get()
        
        # Set the color if a color is selected
        if colorCode:
            self.color : str = colorCode
            self.colorDisplay.configure(bg_color=self.color)
            return True
        
        return False
    
    def getColor(self) -> str:
        
        """
        Gets the selected color.
        
        Returns:
            str: The selected color in hexadecimal format.
        """
        
        return self.color
    
    def setColor(self, color) -> bool:
        
        """
        Sets the color of the color selector.
        
        Parameters:
            color (str): The color to set in hexadecimal format.
            
        Raises:
            TypeError: If the color is not a string.
            ValueError: If the color is not a valid hexadecimal color.

        Returns:
            bool: True if the color is set successfully.
        """
        
        # Check if the color is a string
        if not isinstance(color, str):
            raise TypeError("Color must be a string")
        
        # Check if the color is a valid hexadecimal color
        if not isHexColor(color):
            raise ValueError(f"Color {color} is not a valid hexadecimal color")
        
        # Set the color and update the display
        self.color = color
        
        self.colorDisplay.configure(bg_color=self.color)
        
        return True