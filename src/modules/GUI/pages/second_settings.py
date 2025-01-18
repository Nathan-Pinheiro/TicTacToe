import customtkinter as ctk
from typing import Optional

from modules.GUI.page import Page
from modules.GUI.render import PageName
from modules.GUI.components.int_selector import IntSelector

class SecondSettings(Page):
    
    """
    The second settings page.
    """
    
    def __init__(self, parent: ctk.CTkFrame, controller: ctk.CTk) -> None:
        
        """
        Initializes the second settings page.
        
        Parameters:
            parent (ctk.CTkFrame): The parent frame.
            controller (ctk.CTk): The main controller.

        Returns:
            None
        """
        
        super().__init__(parent, controller)
        self.settings: Optional[dict] = None
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.grid_columnconfigure(4, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.__createWidgets__()
        return None
    
    def redirect(self, pageName: Optional[PageName] = None) -> bool:
        
        """
        Redirects to the specified page with the selected settings.
        
        Parameters:
            pageName (Optional[PageName]): The name of the page to redirect to.

        Returns:
            bool: True if the function succeeds, False otherwise.
        """
        
        # On ajoute aux settings les valeurs des champs
        settings: dict = self.settings
        settings["board"] = {
            "width": self.widthSelector.getValue(),
            "height": self.heightSelector.getValue(),
            "shape": self.shapeVar.get()
        }
        settings["game"] = {
            "nbSymbols": self.nbSymbolsSelector.getValue(),
            "alignToWin": self.alignToWinVar.get(),
            "startingPlayer": self.startingPlayerVar.get(),
            "gamemode": self.gamemodeVar.get()
        }
        self.controller.showFrame(pageName=pageName, settings=settings)
        return True

    def setValues(self, settings: dict) -> bool:
        
        """
        Sets the values for the game settings.
        
        Parameters:
            settings (dict): The game settings.

        Returns:
            bool: True if the function succeeds, False otherwise.
        """
        
        self.settings = settings
        self.startingPlayerCombobox.configure(values=[settings["player1"]["name"], settings["player2"]["name"], "Random"])
        self.startingPlayerVar.set(settings["player1"]["name"])
        return True
    
    def __createWidgets__(self) -> bool:
        """
        Creates the widgets for the second settings page.
        
        Returns:
            bool: True if the function succeeds, False otherwise
        """
        widthRatio: float
        heightRatio: float
        widthRatio, heightRatio = self.getScreenRatio()
        
        # Title
        ctk.CTkLabel(self, text="Game settings", font=("Inter", int(72 * heightRatio), "bold"), text_color="#FFFFFF").grid(row=0, columnspan=5, pady=(int(20 * heightRatio),0))
        
        # Left text
        text: str = "Board options"
        ctk.CTkLabel(self, text=text, font=("Arial", int(48 * heightRatio), "bold"), text_color="#FFFFFF", wraplength=int(600 * widthRatio), width=int(600 * widthRatio)).grid(row=1, column=0, columnspan=2, pady=(int(50 * heightRatio),0), sticky="n")
       
        # Right text
        text: str = "Miscellaneous options"
        ctk.CTkLabel(self, text=text, font=("Arial", int(48 * heightRatio), "bold"), text_color="#FFFFFF", wraplength=int(600 * widthRatio), width=int(600 * widthRatio)).grid(row=1, column=3, columnspan=2, pady=(int(50 * heightRatio),0), sticky="n")
        
        # Width size selector
        ctk.CTkLabel(self, text="Width :", font=("Arial", int(32 * heightRatio), "bold"), text_color="#FFFFFF").grid(row=1, column=0, pady=(int(180 * heightRatio),0), sticky="n")
        self.widthSelector: IntSelector = IntSelector(self, minValue=3, maxValue=7, initialValue=3, width=int(50 * widthRatio), height=int(50 * heightRatio))
        self.widthSelector.grid(row=1, column=1, pady=(int(160 * heightRatio),0), sticky="n")
        
        # Height size selector
        ctk.CTkLabel(self, text="Height :", font=("Arial", int(32 * heightRatio), "bold"), text_color="#FFFFFF").grid(row=1, column=0, pady=(int(280 * heightRatio),0), sticky="n")
        self.heightSelector: IntSelector = IntSelector(self, minValue=3, maxValue=7, initialValue=3, width=int(50 * widthRatio), height=int(50 * heightRatio))
        self.heightSelector.grid(row=1, column=1, pady=(int(260 * heightRatio),0), sticky="n")
        
        # Combobox for shape
        ctk.CTkLabel(self, text="Shape :", font=("Arial", int(32 * heightRatio), "bold"), text_color="#FFFFFF").grid(row=1, column=0, pady=(int(380 * heightRatio),0), sticky="en")
        self.shapeVar: ctk.StringVar = ctk.StringVar(value="No special shape")
        ctk.CTkComboBox(self, values=["No special shape", "Pyramidal", "Circular", "Diamond", 'Random'], variable=self.shapeVar).grid(row=1, column=1, padx=(int(20 * widthRatio), 0), pady=(int(387 * heightRatio),0), sticky="wn")
        self.shapeVar.set("No special shape")
        
        # Symbols to align selector
        ctk.CTkLabel(self, text="Symbols to align :", font=("Arial", int(32 * heightRatio), "bold"), text_color="#FFFFFF").grid(row=1, column=3, pady=(int(180 * heightRatio),0), sticky="n")
        self.nbSymbolsSelector: IntSelector = IntSelector(self, minValue=3, maxValue=7, initialValue=3, width=int(50 * widthRatio), height=int(50 * heightRatio))
        self.nbSymbolsSelector.grid(row=1, column=4, pady=(int(160 * heightRatio),0), sticky="n")
        
        # Checkbox for align to win condition
        self.alignToWinVar: ctk.BooleanVar = ctk.BooleanVar(value=True)
        ctk.CTkLabel(self, text="Align to win :", font=("Arial", int(32 * heightRatio), "bold"), text_color="#FFFFFF").grid(row=1, column=3, columnspan=2, pady=(int(10 * heightRatio),0), padx=(int(300 * widthRatio),0), sticky="w")
        self.alignToWinSelector: ctk.CTkCheckBox = ctk.CTkCheckBox(self, text="", variable=self.alignToWinVar, onvalue=True, offvalue=False)
        self.alignToWinSelector.grid(row=1, column=3, columnspan=2, pady=(int(10 * heightRatio),0), padx=(0, int(250 * widthRatio)), sticky="e")
        
        # Combobox for starting player, values will be initialized in setValues
        ctk.CTkLabel(self, text="Starting player :", font=("Arial", int(32 * heightRatio), "bold"), text_color="#FFFFFF").grid(row=1, column=3, pady=(int(460 * heightRatio),0), sticky="en")
        self.startingPlayerVar: ctk.StringVar = ctk.StringVar(value="Nan")
        self.startingPlayerCombobox: ctk.CTkComboBox = ctk.CTkComboBox(self, values=["Nan"], variable=self.startingPlayerVar)
        self.startingPlayerCombobox.grid(row=1, column=4, padx=(int(20 * widthRatio), 0), pady=(int(467 * heightRatio),0), sticky="wn")
        self.startingPlayerVar.set("Nan")
        
        # Combobox for gamemode
        ctk.CTkLabel(self, text="Gamemode :", font=("Arial", int(32 * heightRatio), "bold"), text_color="#FFFFFF").grid(row=1, column=3, pady=(int(520 * heightRatio),0), sticky="en")
        self.gamemodeVar: ctk.StringVar = ctk.StringVar(value="No mod")
        ctk.CTkComboBox(self, values=["No mod", "Bomb mod"], variable=self.gamemodeVar).grid(row=1, column=4, padx=(int(20 * widthRatio), 0), pady=(int(527 * heightRatio),0), sticky="wn")
        self.gamemodeVar.set("No mod")
        
        # Line
        ctk.CTkLabel(self, text="", bg_color="#FFFFFF").grid(row=1, column=2, sticky="ns")
        
        # Back button
        ctk.CTkButton(self, text="Back", font=("Arial", int(32 * heightRatio)), command=lambda: self.redirect(pageName=PageName.FIRSTSETTINGS)).grid(row=2, column=0, columnspan=2, pady=(int(100 * heightRatio),0), sticky="e")
        
        # Next button
        ctk.CTkButton(self, text="Next", font=("Arial", int(32 * heightRatio)), command=lambda: self.redirect(pageName=PageName.GAME)).grid(row=2, column=3, columnspan=2, pady=(int(100 * heightRatio),0), sticky="w")
        
        return True
    
    def resetSettings(self) -> bool:
        
        """
        Resets the game settings to default values.
        
        Returns:
            bool: True if the function succeeds, False otherwise.
        """
        
        self.widthSelector.setValue(3)
        self.heightSelector.setValue(3)
        self.shapeVar.set("No special shape")
        self.nbSymbolsSelector.setValue(3)
        self.alignToWinVar.set(True)
        self.startingPlayerCombobox.configure(values=["Nan"])
        self.startingPlayerVar.set("Nan")
        self.gamemodeVar.set("No mod")
        return True