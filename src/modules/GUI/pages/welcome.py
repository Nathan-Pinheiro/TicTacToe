import customtkinter as ctk
from modules.GUI.page import Page
from modules.GUI.render import PageName
from PIL import Image

class Welcome(Page):
    
    def __init__(self, parent: ctk.CTkFrame, controller: ctk.CTk) -> None:
        super().__init__(parent, controller)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.__createWidgets__()
        return None
    
    def redirect(self) -> bool:
        self.controller.showFrame(PageName.FIRSTSETTINGS)
        return True
    
    def __createWidgets__(self) -> None:
        width_ratio, height_ratio = self.getScreenRatio()
        
        # Title
        ctk.CTkLabel(self, text="Tic Tac Toe", font=("Inter", int(72 * height_ratio), "bold"), text_color="#FFFFFF").grid(row=0, columnspan=2, pady=(int(20 * height_ratio),0))
        
        # Left text
        text = "Ready to take on the challenge?"
        ctk.CTkLabel(self, text=text, font=("Arial", int(36 * height_ratio), "bold"), wraplength=int(600 * width_ratio)).grid(row=1, column=0, pady=(int(210 * height_ratio),0), sticky="n")
        text = "Challenge your friends or test your skills against the computer in thrilling games of Tic-Tac-Toe! Simple yet strategic, every move can change the course of the game. Choose your symbol, place it, and be the first to align three symbols (or not) to win!"
        ctk.CTkLabel(self, text=text, font=("Arial", int(32 * height_ratio)), wraplength=int(675 * width_ratio)).grid(row=1, column=0, pady=(int(210 * height_ratio),0))
        
        # Right image
        image = ctk.CTkImage(   
                            light_image=Image.open("./src/assets/Board.png"),
                            dark_image=Image.open("./src/assets/Board.png"),
                            size=(int(600 * width_ratio), int(600 * height_ratio))
                                )          
        ctk.CTkLabel(self, image=image, text="").grid(row=1, column=1, pady=(int(80 * height_ratio),0))
        
        # Play button
        ctk.CTkButton(self, text="Play", font=("Arial", int(32 * height_ratio)), command=lambda: self.redirect()).grid(row=2, columnspan=2, pady=(int(100 * height_ratio),0))
        
        return None