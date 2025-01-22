import tkinter as tk
import customtkinter as ctk
from CTkColorPicker import *

from typing import Optional, List, Any

from enum import Enum

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

class Symbols(Enum):
    
    """
    The available symbols.
    """
    
    CROSS = "cross"
    CIRCLE = "circle"
    TRIANGLE = "triangle"
    STAR = "star"
    SQUARE = "square"
    HEXAGON = "hexagon"
    RHOMBUS = "rhombus"

class SymbolSelector(ctk.CTkFrame):
    
    """
    The symbol selector component.
    """

    def __init__(self, parent: ctk.CTkFrame, symbol: Symbols = Symbols.CROSS, disabledSymbols: Optional[List[Symbols]] = None, **kwargs: dict[str, Any]) -> None:
        
        """
        Initializes the symbol selector component.
        
        Parameters:
            parent (ctk.CTkFrame): The parent frame.
            symbol (Symbols): The initial symbol.
            disabledSymbols (Optional[List[Symbols]]): The list of symbols to disable.
            **kwargs (dict): Additional keyword arguments for the frame.
            
        Raises:
            TypeError: If parent is not a ctk.CTkFrame instance.
            ValueError: If symbol is not a valid symbol.

        Returns:
            None
        """
        
        # Check if the parent is a ctk.CTkFrame instance
        if not isinstance(parent, ctk.CTkFrame):
            raise TypeError("parent must be a ctk.CTkFrame instance")
        
        # Call the parent constructor
        super().__init__(parent, **kwargs)
        
        # Check if the symbol is a valid symbol
        self.symbols: List[Symbols] = list(Symbols)
        
        # Check if the symbol is a valid symbol
        if symbol not in self.symbols:
            symbol = self.symbols[0]
            
        # Define the symbol
        self.symbol: Symbols = symbol
        
        # Check if the disabledSymbols are valid symbols
        if disabledSymbols:
            for disabled_symbol in disabledSymbols:
                if disabled_symbol not in self.symbols:
                    raise ValueError(f"Symbol {disabled_symbol} is not a valid symbol")
        
        # Define the disabled symbols
        self.disabledSymbols: List[Symbols] = disabledSymbols if disabledSymbols else []
        
        # Define the onSymbolChange callback
        self.onSymbolChange: Optional[callable] = None
        
        # Create the widgets
        self.__createWidgets__()
        
        return None

    @privatemethod
    def __createWidgets__(self) -> bool:
        
        """
        Creates the widgets for the symbol selector.
        
        Returns:
            bool: True if the widgets are created successfully.
        """
        
        # Create the canvas
        self.canvas: tk.Canvas = tk.Canvas(self, width=132, height=132, bg="#333333", borderwidth=0, highlightthickness=0)
        self.canvas.grid(row=0, column=0, padx=10, pady=10)
        
        # Draw the symbol
        self.__drawSymbol__()
        
        # Create the select button
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
        
        # Clear the canvas
        self.canvas.delete("all")
        
        # Define the size and weight
        canvasWidth: int = int(self.canvas['width'])
        canvasHeight: int = int(self.canvas['height'])
        
        size: int = 100
        
        weight: int = 2
        
        # Define the position
        x: int = (canvasWidth - size) // 2
        y: int = (canvasHeight - size) // 2
        
        # Draw the symbol on the canvas based on the selected symbol
        match self.symbol:
            case Symbols.CROSS:
                drawCross(self.canvas, x, y, size, weight=weight)
            case Symbols.CIRCLE:
                drawCircle(self.canvas, x, y, size, weight=weight)
            case Symbols.TRIANGLE:
                drawTriangle(self.canvas, x, y, size, weight=weight)
            case Symbols.STAR:
                drawStar(self.canvas, x, y, size, weight=weight)
            case Symbols.SQUARE:
                drawSquare(self.canvas, x, y, size, weight=weight)
            case Symbols.HEXAGON:
                drawHexagon(self.canvas, x, y, size, weight=weight)
            case Symbols.RHOMBUS:
                drawRhombus(self.canvas, x, y, size, weight=weight)
            
        return True

    @privatemethod
    def __selectSymbol__(self) -> bool:
        
        """
        Selects the next available symbol.
        
        Returns:
            bool: True if the symbol is selected successfully.
        """
        
        # Get the current index
        currentIndex: int = self.symbols.index(self.symbol)
        nextIndex: int = (currentIndex + 1) % len(self.symbols)
        
        # Get the next available symbol
        while self.symbols[nextIndex] in self.disabledSymbols:
            nextIndex = (nextIndex + 1) % len(self.symbols)
            
        # Set the symbol
        self.symbol = self.symbols[nextIndex]
        
        # Draw the symbol
        self.__drawSymbol__()
        
        # Call the onSymbolChange callback
        if self.onSymbolChange:
            self.onSymbolChange()
            
        return True

    def disableSymbols(self, symbols: List[Symbols]) -> bool:
        
        """
        Disables the specified symbols.
        
        Parameters:
            symbols (List[Symbols]): The list of symbols to disable.
            
        Raises:
            ValueError: If a symbol is not a valid symbol.

        Returns:
            bool: True if the symbols are disabled successfully.
        """
        
        # Check if the symbols are valid symbols
        for symbol in symbols:
            if symbol not in self.symbols:
                raise ValueError(f"Symbol {symbol} is not a valid symbol")
            
        # Disable the symbols
        self.disabledSymbols = symbols
        
        # Select a new symbol if the current symbol is disabled
        if self.symbol in self.disabledSymbols:
            self.__selectSymbol__()
            
        return True

    def setSymbol(self, symbol: Symbols) -> bool:
        
        """
        Sets the symbol of the symbol selector.
        
        Parameters:
            symbol (Symbols): The symbol to set.
            
        Raises:
            ValueError: If symbol is not a valid symbol.
            ValueError: If the symbol is disabled.

        Returns:
            bool: True if the symbol is set successfully.
        """
        
        # Check if the symbol is a valid symbol
        if not isinstance(symbol, Symbols):
            raise ValueError("symbol must be an instance of Symbols")
        
        # Check if the symbol is disabled
        if symbol in self.disabledSymbols:
            raise ValueError(f"Symbol {symbol} is disabled")
        
        # Set the symbol
        self.symbol = symbol
        
        # Draw the symbol
        self.__drawSymbol__()
        
        return True

    def getSymbol(self) -> Symbols:
        
        """
        Gets the selected symbol.
        
        Returns:
            Symbols: The selected symbol.
        """
        
        return self.symbol

    def getAvailableSymbols(self) -> List[Symbols]:
        
        """
        Gets the available symbols.
        
        Returns:
            List[Symbols]: The list of available symbols.
        """
        
        return [symbol for symbol in self.symbols if symbol not in self.disabledSymbols]