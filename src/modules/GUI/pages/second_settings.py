import customtkinter as ctk
import tkinter as tk
from typing import Optional

from modules.GUI.page import Page
from modules.GUI.render import PageName
from modules.GUI.components.int_selector import IntSelector

from modules.utils.decorator import override, privatemethod

# ************************************************
# CLASS SecondSettings
# ************************************************
# ROLE : The goal of this class is to represent the second settings page
# ************************************************
# VERSION : 1.0
# AUTHOR : Hugo MERY
# DATE : 18/01/2025
# ************************************************

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
            
        Raises:
            TypeError: If the parent is not an instance of ctk.CTkFrame.
            TypeError: If the controller is not an instance of ctk.CTk.

        Returns:
            None
        """
        
        # Check if the parent is a ctk.CTkFrame instance
        if not isinstance(parent, ctk.CTkFrame):
            raise TypeError("Parent must be an instance of ctk.CTkFrame")
        
        # Check if the controller is a ctk.CTk instance
        if not isinstance(controller, ctk.CTk):
            raise TypeError("Controller must be an instance of ctk.CTk")
        
        # Call the parent constructor
        super().__init__(parent, controller)
        
        # Initialize the settings
        self.settings: Optional[dict] = None
        
        # Initialize the grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.grid_columnconfigure(4, weight=1)
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        
        # Create the widgets
        self.__createWidgets__()
        
        return None
    
    @override
    def redirect(self, pageName: PageName) -> bool:
        
        """
        Redirects to the specified page with the selected settings.
        
        Parameters:
            pageName (PageName): The name of the page to redirect to.
            
        Raises:
            TypeError: If pageName is not an instance of PageName.

        Returns:
            bool: True if the function succeeds, False otherwise.
        """
        
        # Check if pageName is an instance of PageName
        if not isinstance(pageName, PageName):
            raise TypeError("pageName must be an instance of PageName")
        
        # On ajoute aux settings les valeurs des champs
        settings: dict = self.settings
        
        settings["board"] = {
            "width": self.widthSelector.getValue(),
            "height": self.heightSelector.getValue(),
            "shape": self.shapeVar.get(),
            "blockedCases": self.blockSelector.getValue()
        }
        
        settings["game"] = {
            "nbSymbols": self.nbSymbolsSelector.getValue(),
            "alignToWin": self.alignToWinVar.get(),
            "startingPlayer": self.startingPlayerVar.get(),
            "gamemode": self.gamemodeVar.get()
        }
        
        # On affiche la page suivante
        self.controller.showFrame(pageName=pageName, settings=settings)
        
        return True

    def setValues(self, settings: dict) -> bool:
        
        """
        Sets the values for the game settings.
        
        Parameters:
            settings (dict): The game settings.
            
        Raises:
            TypeError: If settings is not a dictionary.

        Returns:
            bool: True if the function succeeds, False otherwise.
        """
        
        # Check if settings is a dictionary
        if not isinstance(settings, dict):
            raise TypeError("settings must be a dictionary")
        
        # Set the settings
        self.settings = settings
        
        # Set the values of the settings in the widgets
        self.startingPlayerOptionMenu.configure(values=[settings["player1"]["name"], settings["player2"]["name"], "Random"])
        
        self.startingPlayerVar.set("Random")
        
        return True
    
    @override
    def __createWidgets__(self) -> bool:
        
        """
        Creates the widgets for the second settings page.
        
        Returns:
            bool: True if the function succeeds, False otherwise
        """
        
        # Get the screen ratio
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
        
        # OptionMenu for shape
        ctk.CTkLabel(self, text="Shape :", font=("Arial", int(32 * heightRatio), "bold"), text_color="#FFFFFF").grid(row=1, column=0, pady=(int(380 * heightRatio),0), sticky="en")
        self.shapeVar: ctk.StringVar = ctk.StringVar(value="No special shape")
        self.shapeOptionMenu: ctk.CTkOptionMenu = ctk.CTkOptionMenu(self, values=["No special shape", "Pyramidal", "Circular", "Diamond", 'Random shape', 'Random block'], variable=self.shapeVar, command=self.__handleShapeChange__)
        self.shapeOptionMenu.grid(row=1, column=1, padx=(int(20 * widthRatio), 0), pady=(int(387 * heightRatio),0), sticky="wn")
        self.shapeVar.set("No special shape")
        
        # Block selector
        self.blockLabel: ctk.CTkLabel = ctk.CTkLabel(self, text="Blocked cases :", font=("Arial", int(32 * heightRatio), "bold"), text_color="#FFFFFF")
        self.blockSelector: IntSelector = IntSelector(self, minValue=1, maxValue=9, initialValue=1, width=int(50 * widthRatio), height=int(50 * heightRatio))
        
        # Symbols to align selector
        ctk.CTkLabel(self, text="Symbols to align :", font=("Arial", int(32 * heightRatio), "bold"), text_color="#FFFFFF").grid(row=1, column=3, pady=(int(180 * heightRatio),0), sticky="n")
        self.nbSymbolsSelector: IntSelector = IntSelector(self, minValue=3, maxValue=3, initialValue=3, width=int(50 * widthRatio), height=int(50 * heightRatio))
        self.nbSymbolsSelector.grid(row=1, column=4, pady=(int(160 * heightRatio),0), sticky="n")
        
        # Checkbox for align to win condition
        self.alignToWinVar: ctk.BooleanVar = ctk.BooleanVar(value=True)
        ctk.CTkLabel(self, text="Align to win :", font=("Arial", int(32 * heightRatio), "bold"), text_color="#FFFFFF").grid(row=1, column=3, pady=(int(260 * heightRatio),0), sticky="en")
        self.alignToWinSelector: ctk.CTkCheckBox = ctk.CTkCheckBox(self, text="", variable=self.alignToWinVar, onvalue=True, offvalue=False)
        self.alignToWinSelector.grid(row=1, column=4, pady=(int(267 * heightRatio),0), padx=(int(20 * widthRatio), 0), sticky="wn")
        
        # OptionMenu for starting player, values will be initialized in setValues
        ctk.CTkLabel(self, text="Starting player :", font=("Arial", int(32 * heightRatio), "bold"), text_color="#FFFFFF").grid(row=1, column=3, pady=(int(460 * heightRatio),0), sticky="en")
        self.startingPlayerVar: ctk.StringVar = ctk.StringVar(value="Nan")
        self.startingPlayerOptionMenu: ctk.CTkOptionMenu = ctk.CTkOptionMenu(self, values=["Nan"], variable=self.startingPlayerVar)
        self.startingPlayerOptionMenu.grid(row=1, column=4, padx=(int(20 * widthRatio), 0), pady=(int(467 * heightRatio),0), sticky="wn")
        self.startingPlayerVar.set("Nan")
        
        # OptionMenu for gamemode
        ctk.CTkLabel(self, text="Gamemode :", font=("Arial", int(32 * heightRatio), "bold"), text_color="#FFFFFF").grid(row=1, column=3, pady=(int(520 * heightRatio),0), sticky="en")
        self.gamemodeVar: ctk.StringVar = ctk.StringVar(value="No mod")
        ctk.CTkOptionMenu(self, values=["No mod", "Bomb mod"], variable=self.gamemodeVar).grid(row=1, column=4, padx=(int(20 * widthRatio), 0), pady=(int(527 * heightRatio),0), sticky="wn")
        self.gamemodeVar.set("No mod")
        
        # Line
        ctk.CTkLabel(self, text="", bg_color="#FFFFFF").grid(row=1, column=2, sticky="ns")
        
        # Back button
        ctk.CTkButton(self, text="Back", font=("Arial", int(32 * heightRatio)), command=lambda: self.redirect(pageName=PageName.FIRSTSETTINGS)).grid(row=2, column=0, columnspan=2, pady=(int(100 * heightRatio),0), sticky="e")
        
        # Next button
        ctk.CTkButton(self, text="Next", font=("Arial", int(32 * heightRatio)), command=lambda: self.redirect(pageName=PageName.GAME)).grid(row=2, column=3, columnspan=2, pady=(int(100 * heightRatio),0), sticky="w")
        
        # Set click event on the size selectors
        self.widthSelector.decrementButton.bind("<Button-1>", self.__handleClick__)
        self.widthSelector.incrementButton.bind("<Button-1>", self.__handleClick__)
        self.heightSelector.decrementButton.bind("<Button-1>", self.__handleClick__)
        self.heightSelector.incrementButton.bind("<Button-1>", self.__handleClick__)
        
        return True
    
    @privatemethod
    def __handleClick__(self, event: tk.Event) -> bool:
        
        """
        Handles the click event on the size selectors.
        
        Parameters:
            event (tk.Event): The event object.
            
        Raises:
            TypeError: If event is not an instance of tk.Event.
            
        Returns:
            bool: True if the function succeeds.
        """
        
        # Check if event is an instance of tk.Event
        if not isinstance(event, tk.Event):
            raise TypeError("event must be an instance of tk.Event")
        
        # Update the values of the selectors
        self.__updateValues__()
        
        return True
        
    @privatemethod
    def __updateValues__(self) -> bool:
        
        """
        Updates the values of the selectors.
        
        Returns:
            bool: True if the function succeeds.
        """
        
        self.nbSymbolsSelector.setMaxValue(max(self.widthSelector.getValue(), self.heightSelector.getValue()))
        self.nbSymbolsSelector.updateButtons()
        self.blockSelector.setMaxValue(self.widthSelector.getValue() * self.heightSelector.getValue() - max(self.widthSelector.getValue(), self.heightSelector.getValue()))
        self.blockSelector.updateButtons()
        
        return True
        
    @privatemethod
    def __handleShapeChange__(self, value: str) -> bool:
        
        """
        Handles the change of shape.
        
        Parameters:
            value (str): The new value of the shape.
            
        Raises:
            TypeError: If value is not a string.
        
        Returns:
            bool: True if the function succeeds.
        """
        
        # Check if value is a string 
        if not isinstance(value, str):
            raise TypeError("value must be a string")
        
        # If the value is not "Random shape", we hide the block selector
        if value == "Random block":
            
            # Get the screen ratio
            widthRatio: float
            heightRatio: float
            widthRatio, heightRatio = self.getScreenRatio()
        
            # Set the block selector and label visible
            self.blockLabel.grid(row=1, column=0, pady=(int(480 * heightRatio),0), sticky="en")
            self.blockSelector.grid(row=1, column=1, padx=(int(20 * widthRatio), 0), pady=(int(470 * heightRatio),0), sticky="wn")
            
        else:
            
            # Set the block selector and label invisible
            self.blockLabel.grid_forget()
            self.blockSelector.grid_forget()
            
        return True

    def resetSettings(self) -> bool:
        
        """
        Resets the game settings to default values.
        
        Returns:
            bool: True if the function succeeds, False otherwise.
        """
        
        # Reset the settings
        self.widthSelector.setValue(3)
        self.heightSelector.setValue(3)
        self.shapeVar.set("No special shape")
        self.blockSelector.setValue(1)
        
        self.nbSymbolsSelector.setValue(3)
        self.__updateValues__()
        
        self.alignToWinVar.set(True)
        
        self.startingPlayerOptionMenu.configure(values=["Nan"])
        self.startingPlayerVar.set("Nan")
        
        self.__handleShapeChange__("No special shape")
        
        self.gamemodeVar.set("No mod")
        
        return True