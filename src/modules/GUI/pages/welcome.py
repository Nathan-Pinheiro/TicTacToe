import customtkinter as ctk
from PIL import Image

from modules.GUI.page import Page
from modules.GUI.render import PageName
from modules.utils.decorator import privatemethod

# ************************************************
# CLASS Welcome
# ************************************************
# ROLE : The goal of this class is to represent the welcome page
# ************************************************
# VERSION : 1.0
# AUTHOR : Hugo MERY
# DATE : 18/01/2025
# ************************************************

class Welcome(Page):
    
    """
    The welcome page.
    """
    
    def __init__(self, parent: ctk.CTkFrame, controller: ctk.CTk) -> None:
        
        """
        Initializes the welcome page.
        
        Parameters:
            parent (ctk.CTkFrame): The parent frame.
            controller (ctk.CTk): The main controller.

        Returns:
            None
        """
        
        super().__init__(parent, controller)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.__createWidgets__()
        return None
    
    def redirect(self) -> bool:
        
        """
        Redirects to the first settings page.
        
        Returns:
            bool: True if the function succeeds, False otherwise.
        """
        
        self.controller.showFrame(PageName.FIRSTSETTINGS)
        return True
    
    @privatemethod
    def __createWidgets__(self) -> bool:
        
        """
        Creates the widgets for the welcome page.
        
        Returns:
            bool: True if the function succeeds, False otherwise.
        """
        
        widthRatio: float
        heightRatio: float
        widthRatio, heightRatio = self.getScreenRatio()
        
        # Title
        ctk.CTkLabel(self, text="Tic Tac Toe", font=("Inter", int(72 * heightRatio), "bold"), text_color="#FFFFFF").grid(row=0, columnspan=2, pady=(int(20 * heightRatio),0))
        
        # Left text
        text: str = "Ready to take on the challenge?"
        ctk.CTkLabel(self, text=text, font=("Arial", int(36 * heightRatio), "bold"), wraplength=int(600 * widthRatio)).grid(row=1, column=0, pady=(int(210 * heightRatio),0), sticky="n")
        text = "Challenge your friends or test your skills against the computer in thrilling games of Tic-Tac-Toe! Simple yet strategic, every move can change the course of the game. Choose your symbol, place it, and be the first to align three symbols (or not) to win!"
        ctk.CTkLabel(self, text=text, font=("Arial", int(32 * heightRatio)), wraplength=int(675 * widthRatio)).grid(row=1, column=0, pady=(int(210 * heightRatio),0))
        
        # Right image
        image: ctk.CTkImage = ctk.CTkImage(   
                            light_image=Image.open("./assets/Board.png"),
                            dark_image=Image.open("./assets/Board.png"),
                            size=(int(600 * widthRatio), int(600 * heightRatio))
                                )          
        ctk.CTkLabel(self, image=image, text="").grid(row=1, column=1, pady=(int(80 * heightRatio),0))
        
        # Play button
        ctk.CTkButton(self, text="Play", font=("Arial", int(32 * heightRatio)), command=lambda: self.redirect()).grid(row=2, columnspan=2, pady=(int(100 * heightRatio),0))
        
        return True