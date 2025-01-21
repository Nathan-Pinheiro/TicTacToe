import tkinter as tk
import customtkinter as ctk
from CTkColorPicker import *
from typing import Optional, List

from modules.utils.decorator import privatemethod
from modules.utils.validators import isValidSymbol

from modules.GUI.components.symbols import (
    drawCross, drawCircle, drawTriangle, drawStar, drawSquare, drawHexagon, drawRhombus
)

# ************************************************
# CLASS SymbolSelector
# ************************************************
# ROLE : This class is used to create a symbol selector
# ************************************************
# VERSION : 1.0
# AUTHOR : Hugo MERY
# DATE : 18/01/2025
# ************************************************

class SymbolSelector(ctk.CTkFrame):
    
    """
    The symbol selector component.
    """

    def __init__(self, parent: ctk.CTkFrame, symbol: str = "cross", disabledSymbols: Optional[List[str]] = None, **kwargs) -> None:
        
        """
        Initializes the symbol selector component.
        
        Parameters:
            parent (ctk.CTkFrame): The parent frame.
            symbol (str): The initial symbol.
            disabledSymbols (Optional[List[str]]): The list of symbols to disable.
            **kwargs: Additional keyword arguments.
            
        Raises:
            TypeError: If parent is not a ctk.CTkFrame instance.
            ValueError: If symbol is not a valid symbol.

        Returns:
            None
        """
        
        if not isinstance(parent, ctk.CTkFrame):
            raise TypeError("parent must be a ctk.CTkFrame instance")
        
        super().__init__(parent, **kwargs)
        
        self.symbols: List[str] = ["cross", "circle", "triangle", "star", "square", "hexagon", "rhombus"]
        
        if symbol not in self.symbols:
            symbol = self.symbols[0]
            
        self.symbol: str = symbol
        
        for disabled_symbol in disabledSymbols:
            if disabled_symbol not in self.symbols:
                raise ValueError(f"Symbol {disabled_symbol} is not a valid symbol")
        
        self.disabledSymbols: List[str] = disabledSymbols if disabledSymbols else []
        
        self.onSymbolChange: Optional[callable] = None
        
        self.__createWidgets__()
        
        return None

    @privatemethod
    def __createWidgets__(self) -> bool:
        
        """
        Creates the widgets for the symbol selector.
        
        Returns:
            bool: True if the widgets are created successfully.
        """
        
        self.canvas: tk.Canvas = tk.Canvas(self, width=132, height=132, bg="#333333", borderwidth=0, highlightthickness=0)
        self.canvas.grid(row=0, column=0, padx=10, pady=10)
        
        if not self.__drawSymbol__():
            return False
        
        self.selectButton: ctk.CTkButton = ctk.CTkButton(self, text="Select Symbol", command=self.__selectSymbol__)
        self.selectButton.grid(row=1, column=0, padx=10, pady=10)
        
        return True

    @privatemethod
    def __drawSymbol__(self) -> bool:
        
        """
        Draws the selected symbol on the canvas.
        
        Returns:
            bool: True if the symbol is drawn successfully.
        """
        
        self.canvas.delete("all")
        
        canvas_width: int = int(self.canvas['width'])
        canvas_height: int = int(self.canvas['height'])
        
        size: int = 100
        
        weight: int = 2
        
        x: int = (canvas_width - size) // 2
        y: int = (canvas_height - size) // 2
        
        match self.symbol:
            case "cross":
                if not drawCross(self.canvas, x, y, size, weight=weight):
                    return False
            case "circle":
                if not drawCircle(self.canvas, x, y, size, weight=weight):
                    return False
            case "triangle":
                if not drawTriangle(self.canvas, x, y, size, weight=weight):
                    return False
            case "star":
                if not drawStar(self.canvas, x, y, size, weight=weight):
                    return False
            case "square":
                if not drawSquare(self.canvas, x, y, size, weight=weight):
                    return False
            case "hexagon":
                if not drawHexagon(self.canvas, x, y, size, weight=weight):
                    return False
            case "rhombus":
                if not drawRhombus(self.canvas, x, y, size, weight=weight):
                    return False  
            
        return True

    @privatemethod
    def __selectSymbol__(self) -> bool:
        
        """
        Selects the next available symbol.
        
        Returns:
            bool: True if the symbol is selected successfully.
        """
        
        current_index: int = self.symbols.index(self.symbol)
        next_index: int = (current_index + 1) % len(self.symbols)
        
        while self.symbols[next_index] in self.disabledSymbols:
            next_index = (next_index + 1) % len(self.symbols)
            
        self.symbol = self.symbols[next_index]
        
        if not self.__drawSymbol__():
            return False
        
        if self.onSymbolChange:
            self.onSymbolChange()
            
        return True

    def disableSymbols(self, symbols: List[str]) -> bool:
        
        """
        Disables the specified symbols.
        
        Parameters:
            symbols (List[str]): The list of symbols to disable.
            
        Raises:
            ValueError: If a symbol is not a valid symbol.

        Returns:
            bool: True if the symbols are disabled successfully.
        """
        for symbol in symbols:
            if symbol not in self.symbols:
                raise ValueError(f"Symbol {symbol} is not a valid symbol")
            
        self.disabledSymbols = symbols
        
        if self.symbol in self.disabledSymbols:
            if not self.__selectSymbol__():
                return False
            
        return True

    def setSymbol(self, symbol: str) -> bool:
        
        """
        Sets the symbol of the symbol selector.
        
        Parameters:
            symbol (str): The symbol to set.
            
        Raises:
            ValueError: If the symbol is not a valid symbol.
            ValueError: If the symbol is disabled.

        Returns:
            bool: True if the symbol is set successfully.
        """
        
        if not isValidSymbol(symbol):
            raise ValueError(f"Symbol {symbol} is not a valid symbol")
        
        if symbol in self.disabledSymbols:
            raise ValueError(f"Symbol {symbol} is disabled")
        
        self.symbol = symbol
        
        if not self.__drawSymbol__():
            return False
        
        return True

    def getSymbol(self) -> str:
        
        """
        Gets the selected symbol.
        
        Returns:
            str: The selected symbol.
        """
        
        return self.symbol

    def getAvailableSymbols(self) -> List[str]:
        
        """
        Gets the available symbols.
        
        Returns:
            List[str]: The list of available symbols.
        """
        
        return [symbol for symbol in self.symbols if symbol not in self.disabledSymbols]