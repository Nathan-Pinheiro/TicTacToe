from abc import ABC, abstractmethod

import customtkinter as ctk

from modules.utils.decorator import privatemethod

# ************************************************
# CLASS Page
# ************************************************
# ROLE : The goal of this class is to represent an abstract page
# ************************************************
# VERSION : 1.0
# AUTHOR : Hugo MERY
# DATE : 18/01/2025
# ************************************************

class Page(ctk.CTkFrame, ABC):
    
    """
    The abstract class for a page.
    """
    
    def __init__(self, parent: ctk.CTkFrame, controller: ctk.CTk) -> None:
        
        """
        Initializes a page.
        
        Parameters:
            parent (ctk.CTkFrame): The parent frame.
            controller (ctk.CTk): The main controller.

        Returns:
            None
        """
        
        super().__init__(parent, border_width=0)
        self.controller = controller
        return None
    
    @abstractmethod
    def redirect(self) -> bool:
        
        """
        Redirects to another page.
        
        Returns:
            bool: True if the function succeeds, False otherwise.
        """
        
        pass
    
    @privatemethod
    def __createWidgets__(self) -> bool:
        
        """
        Creates the widgets for the page.
        
        Returns:
            bool: True if the function succeeds, False otherwise.
        """
        
        pass
    
    def getScreenRatio(self) -> tuple:
        
        """
        Returns the screen ratio.
        
        Returns:
            tuple: The screen ratio.
        """
        
        return (self.controller.winfo_screenwidth() / 1920, self.controller.winfo_screenheight() / 1080)