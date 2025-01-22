import customtkinter as ctk

from modules.GUI.page import Page
from modules.GUI.render import PageName

from modules.GUI.components.color_selector import ColorSelector
from modules.GUI.components.symbol_selector import SymbolSelector, Symbols
from modules.GUI.components.type_selector import TypeSelector, Types

from modules.utils.decorator import privatemethod, override

# ************************************************
# CLASS FirstSettings
# ************************************************
# ROLE : The goal of this class is to represent the first settings page
# ************************************************
# VERSION : 1.0
# AUTHOR : Hugo MERY
# DATE : 18/01/2025
# ************************************************

class FirstSettings(Page):
    
    """
    The first settings page.
    """
    
    def __init__(self, parent: ctk.CTkFrame, controller: ctk.CTk) -> None:
        
        """
        Initializes the first settings page.
        
        Parameters:
            parent (ctk.CTkFrame): The parent frame.
            controller (ctk.CTk): The main controller.
            
        Raises:
            TypeError: If parent is not a ctk.CTkFrame instance.
            TypeError: If controller is not a ctk.CTk instance.

        Returns:
            None
        """
        
        # Check if the parent is a ctk.CTkFrame instance
        if not isinstance(parent, ctk.CTkFrame):
            raise TypeError("parent must be a ctk.CTkFrame instance")
        
        # Check if the controller is a ctk.CTk instance
        if not isinstance(controller, ctk.CTk):
            raise TypeError("controller must be a ctk.CTk instance")
        
        # Call the parent constructor
        super().__init__(parent, controller)
        
        # Configure the grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.grid_columnconfigure(4, weight=1)
        self.grid_columnconfigure(5, weight=1)
        self.grid_columnconfigure(6, weight=1)
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        
        # Create the widgets
        self.__createWidgets__()
        
        return None
    
    @override
    def redirect(self, pageName: PageName) -> bool:
        
        """
        Redirects to the second settings page after validating player names.
        
        Parameters:
            pageName (PageName): The name of the page to redirect to.
            
        Raises:
            TypeError: If pageName is not a PageName instance.
        
        Returns:
            bool: True if the function succeeds, False otherwise.
        """
        
        # Check if the pageName is a PageName instance
        if not isinstance(pageName, PageName):
            raise TypeError("pageName must be a PageName instance")
        
        # Get the player names
        names: list[str] = [self.nameP1.get(), self.nameP2.get()]
        
        # Check if the names are valid
        if names[0] == "" or names[0] == "Random":
            self.nameP1.focus_set()
            self.nameP1.configure(border_color="red")
            return False
        
        if names[1] == "" or names[0] == names[1] or names[1] == "Random":
            self.nameP2.focus_set()
            self.nameP2.configure(border_color="red")
            return False
        
        # Get the settings
        settings: dict = {
            "player1": {
                "name": self.nameP1.get(),
                "color": self.colorSelectorP1.getColor(),
                "symbol": self.symbolSelectorP1.getSymbol().value,
                "type": self.typeSelectorP1.getType().value
            },
            "player2": {
                "name": self.nameP2.get(),
                "color": self.colorSelectorP2.getColor(),
                "symbol": self.symbolSelectorP2.getSymbol().value,
                "type": self.typeSelectorP2.getType().value
            }
        }
        
        # Save the settings
        self.controller.showFrame(pageName=pageName, settings=settings)
        
        return True
    
    @override
    def __createWidgets__(self) -> bool:
        
        """
        Creates the widgets for the first settings page.
        
        Returns:
            bool: True if the widgets are created successfully.
        """
        
        # Screen ratio
        widthRatio: float
        heightRatio: float
        widthRatio, heightRatio = self.getScreenRatio()
        
        # Title
        ctk.CTkLabel(self, text="Players settings", font=("Inter", int(72 * heightRatio), "bold"), text_color="#FFFFFF").grid(row=0, columnspan=7, pady=(int(20 * heightRatio),0))
        
        # Left text
        text: str = "Player 1"
        ctk.CTkLabel(self, text=text, font=("Arial", int(48 * heightRatio), "bold"), text_color="#FFFFFF", wraplength=int(600 * widthRatio)).grid(row=1, column=0, columnspan=3, pady=(int(50 * heightRatio),0), sticky="n")
        
        # Left entry
        self.nameP1: ctk.CTkEntry = ctk.CTkEntry(self, placeholder_text="Name...", font=("Arial", int(32 * heightRatio)), width=int(400 * widthRatio), height=int(50 * heightRatio))
        self.nameP1.grid(row=1, column=0, columnspan=3, pady=(int(140 * heightRatio), 0), sticky="n")
        self.nameP1.bind("<Key>", lambda event: self.nameP1.configure(border_color="#565b5e"))
        
        # Left color selector
        self.colorSelectorP1: ColorSelector = ColorSelector(self)
        self.colorSelectorP1.grid(row=1, column=0, pady=(int(250 * heightRatio), 0), sticky="n")
        
        # Left symbol selector
        self.symbolSelectorP1: SymbolSelector = SymbolSelector(self, disabledSymbols=[Symbols.CIRCLE])
        self.symbolSelectorP1.grid(row=1, column=1, pady=(int(250 * heightRatio), 0), sticky="n")
        self.symbolSelectorP1.on_symbol_change = self.__updateSymbolsP1__

        # Left type selector
        self.typeSelectorP1: TypeSelector = TypeSelector(self)
        self.typeSelectorP1.grid(row=1, column=2, pady=(int(250 * heightRatio), 0), sticky="n")
       
        # Right text
        text = "Player 2"
        ctk.CTkLabel(self, text=text, font=("Arial", int(48 * heightRatio), "bold"), text_color="#FFFFFF", wraplength=int(600 * widthRatio)).grid(row=1, column=4, columnspan=3, pady=(int(50 * heightRatio),0), sticky="n")
        
        # Right entry
        self.nameP2: ctk.CTkEntry = ctk.CTkEntry(self, placeholder_text="Name...", font=("Arial", int(32 * heightRatio)), width=int(400 * widthRatio), height=int(50 * heightRatio))
        self.nameP2.grid(row=1, column=4, columnspan=3, pady=(int(140 * heightRatio), 0), sticky="n")
        self.nameP2.bind("<Key>", lambda event: self.nameP2.configure(border_color="#565b5e"))
        
        # Right color selector
        self.colorSelectorP2: ColorSelector = ColorSelector(self)
        self.colorSelectorP2.grid(row=1, column=4, pady=(int(250 * heightRatio), 0), sticky="n")
        
        # Right symbol selector
        self.symbolSelectorP2: SymbolSelector = SymbolSelector(self, symbol="circle", disabledSymbols=[Symbols.CROSS])
        self.symbolSelectorP2.grid(row=1, column=5, pady=(int(250 * heightRatio), 0), sticky="n")
        self.symbolSelectorP2.on_symbol_change = self.__updateSymbolsP2__

        # Right type selector
        self.typeSelectorP2: TypeSelector = TypeSelector(self)
        self.typeSelectorP2.grid(row=1, column=6, pady=(int(250 * heightRatio), 0), sticky="n")
        
        # Line
        ctk.CTkLabel(self, text="", bg_color="#FFFFFF").grid(row=1, column=3, sticky="ns")
        
        # Back button
        ctk.CTkButton(self, text="Back", font=("Arial", int(32 * heightRatio)), command=lambda: self.redirect(PageName.WELCOME)).grid(row=2, column=0, columnspan=3, pady=(0, int(50 * heightRatio)), sticky="es")
        # Next button
        ctk.CTkButton(self, text="Next", font=("Arial", int(32 * heightRatio)), command=lambda: self.redirect(PageName.SECONDSETTINGS)).grid(row=2, column=4, columnspan=3, pady=(0, int(50 * heightRatio)), sticky="ws")
        
        return True

    @privatemethod
    def __updateSymbolsP1__(self) -> bool:
        
        """
        Updates the symbols for player 2 based on player 1's selection.
        
        Returns:
            bool: True if the function succeeds.
        """
        
        # Disable the symbol selected by player 1 for player 2
        self.symbolSelectorP2.disableSymbols([self.symbolSelectorP1.getSymbol()])
        
        return True

    @privatemethod
    def __updateSymbolsP2__(self) -> bool:
        
        """
        Updates the symbols for player 1 based on player 2's selection.
        
        Returns:
            bool: True if the function succeeds.
        """
        
        # Disable the symbol selected by player 2 for player 1
        self.symbolSelectorP1.disableSymbols([self.symbolSelectorP2.getSymbol()])
        
        return True

    def resetSettings(self) -> bool:
        
        """
        Resets the settings for both players to default values.
        
        Returns:
            bool: True if the function succeeds.
        """
        
        # Reset the settings for player 1
        if self.nameP1.get() != "":
            self.nameP1.delete(0, "end")
        self.colorSelectorP1.setColor("#FFFFFF")
        self.symbolSelectorP1.disableSymbols([Symbols.CIRCLE])
        self.symbolSelectorP1.setSymbol(Symbols.CROSS)
        self.__updateSymbolsP2__()
        self.typeSelectorP1.setType(Types.HUMAN)
        
        # Reset the settings for player 2
        if self.nameP2.get() != "":
            self.nameP2.delete(0, "end")
        self.colorSelectorP2.setColor("#FFFFFF")
        self.symbolSelectorP2.disableSymbols([Symbols.CROSS])
        self.symbolSelectorP2.setSymbol(Symbols.CIRCLE)
        self.__updateSymbolsP1__()
        self.typeSelectorP2.setType(Types.EASY)
        
        return True