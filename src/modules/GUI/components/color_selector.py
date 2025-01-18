import customtkinter as ctk
from CTkColorPicker import AskColor

from modules.utils.decorator import privatemethod

class ColorSelector(ctk.CTkFrame):
    
    """
    The color selector component.
    """
    
    def __init__(self, parent, color="#FFFFFF", **kwargs) -> None:
        
        """
        Initializes the color selector component.
        
        Parameters:
            parent (ctk.CTkFrame): The parent frame.
            color (str): The initial color in hexadecimal format.
            **kwargs: Additional keyword arguments for the frame.

        Returns:
            None
        """
        
        super().__init__(parent, **kwargs)
        self.color : str = color
        self.__createWidgets__()
        
        return None

    @privatemethod
    def __createWidgets__(self) -> bool:
        
        """
        Creates the widgets for the color selector.
        
        Returns:
            bool: True if widgets are created successfully.
        """
        
        self.colorDisplay : ctk.CTkLabel = ctk.CTkLabel(self, text="", width=132, height=132, bg_color=self.color)
        self.colorDisplay.grid(row=0, column=0, padx=10, pady=10)

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
        
        pickColor : AskColor = AskColor(title="Choose color")
        colorCode : str = pickColor.get()
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

        Returns:
            bool: True if the color is set successfully.
        """
        
        self.color = color
        self.colorDisplay.configure(bg_color=self.color)
        return True