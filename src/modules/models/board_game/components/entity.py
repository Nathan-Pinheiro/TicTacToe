from __future__ import annotations
from abc import ABC, abstractmethod

# ************************************************
# CLASS Entity
# ************************************************
# ROLE : This class is used to represent an entity
# ************************************************
# VERSION : 1.0
# AUTHOR : Nathan PINHEIRO
# DATE : 13/01/2025
# ************************************************

class Entity:
    
    """
    A class that represents an entity.
    """

    def __init__(self, symbol: str) -> None:
        
        """
        Constructor for the Entity class.

        Parameters:
            symbol (str): The symbol representing the entity.
            
        Raises:
            TypeError: If symbol is not a string.
            ValueError: If symbol is an empty string.

        Returns:
            None
        """
        
        # Check if symbol is a string and not empty
        if not isinstance(symbol, str):
            raise TypeError("symbol must be a string")
        
        if not symbol:
            raise ValueError("symbol must not be an empty string")
        
        # Initialize the symbol attribute
        self.__symbol__ = symbol
        
        return None
        
    def getSymbol(self) -> str:
        
        """
        Get the symbol of the entity.

        Returns:
            str: The symbol of the entity.
        """
        
        return self.__symbol__
    
    def setSymbol(self, symbol: str) -> bool:
        
        """
        Set the symbol of the entity.

        Parameters:
            symbol (str): The symbol representing the entity.
            
        Raises:
            TypeError: If symbol is not a string.
            ValueError: If symbol is an empty string.

        Returns:
            bool: True if the symbol is set successfully.
        """
        
        # Check if symbol is a string and not empty
        if not isinstance(symbol, str):
            raise TypeError("symbol must be a string")
        
        if not symbol:
            raise ValueError("symbol must not be an empty string")
        
        # Set the symbol
        self.__symbol__ = symbol
        
        return True
        
    def __str__(self) -> str:
        
        """
        Return the string value of the entity.
        
        Returns:
            str: The string value of the entity.
        """
        
        return self.__symbol__