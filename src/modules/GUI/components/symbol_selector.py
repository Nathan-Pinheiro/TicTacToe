import tkinter as tk
import customtkinter as ctk
from CTkColorPicker import *
from typing import Optional, List

from modules.utils.decorator import privatemethod

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

        Returns:
            None
        """
        
        super().__init__(parent, **kwargs)
        self.symbols: List[str] = ["cross", "circle", "triangle", "star", "square", "hexagon", "rhombus"]
        if symbol not in self.symbols:
            symbol = self.symbols[0]
        self.symbol: str = symbol
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
        self.__drawSymbol__()
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
        if self.symbol == "cross":
            drawCross(self.canvas, x, y, size, weight=weight)
        elif self.symbol == "circle":
            drawCircle(self.canvas, x, y, size, weight=weight)
        elif self.symbol == "triangle":
            drawTriangle(self.canvas, x, y, size, weight=weight)
        elif self.symbol == "star":
            drawStar(self.canvas, x, y, size, weight=weight)
        elif self.symbol == "square":
            drawSquare(self.canvas, x, y, size, weight=weight)
        elif self.symbol == "hexagon":
            drawHexagon(self.canvas, x, y, size, weight=weight)
        elif self.symbol == "rhombus":
            drawRhombus(self.canvas, x, y, size, weight=weight)
            
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
        self.__drawSymbol__()
        if self.onSymbolChange:
            self.onSymbolChange()
            
        return True

    def disableSymbols(self, symbols: List[str]) -> bool:
        
        """
        Disables the specified symbols.
        
        Parameters:
            symbols (List[str]): The list of symbols to disable.

        Returns:
            bool: True if the symbols are disabled successfully.
        """
        
        self.disabledSymbols = symbols
        if self.symbol in self.disabledSymbols:
            self.selectSymbol()
            
        return True

    def setSymbol(self, symbol: str) -> bool:
        
        """
        Sets the symbol of the symbol selector.
        
        Parameters:
            symbol (str): The symbol to set.

        Returns:
            bool: True if the symbol is set successfully.
        """
        
        self.symbol = symbol
        self.__drawSymbol__()
        
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