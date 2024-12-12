## Interface

"""
Entity Module

This module provides a class to represent an entity.

Classes:
    Entity: Represents a entity.
    
    Attributes:
        name (str): The name of the pawn.

Methods:            

    getName() -> str:
        Get the name of the pawn.
        
        Returns:
            str: The name of the pawn.
            
    setName(name: str) -> None:
        Set the name of the pawn.
        
        Args:
            name (str): The name of the pawn.
        
        Returns:
            None
            
    getIconPath(self):
        Get the icon path of the entity.

        Args:
            iconPath (str): The icon path of the entity.
        
        Returns: None
        
    setIconPath(self, iconPath : str) -> None:
        Set the icon path of the entity to a given value.

        Args:
            iconPath (str): The icon path of the entity.
        
        Returns: None
"""

# ---------------------------------------------------------------------------------------------------- #

## Implementation

# Class #
class Entity:
    
    def __init__(self, name : str, iconPath : str = None):
        """Constructor for the Pawn class.

        Args:
            name (str): The name of the pawn.
            iconPath (str): The path of the pawn.
        """

        self.__name__ : str = name
        self.__iconPath__ : str = iconPath
        
    def getName(self):
        """Get the name of the entity.
        
        Returns:
            str: The line of the coordinate.
        """
        
        return self.__name__
    
    def setName(self, name : str) -> None: 
        """Get the name of the entity.

        Args:
            name (str): The name of the entity.
        
        Returns: None
        """
        self.__name__ = name
        return None
    
    def getIconPath(self):
        """Get the icon path of the entity.
        
        Returns:
            str: The icon path of the coordinate.
        """
        
        return self.__name__

    def setIconPath(self, iconPath : str) -> None: 
        """Set the icon path of the entity to a given value.

        Args:
            iconPath (str): The icon path of the entity.
        
        Returns: None
        """
        self.__name__ = iconPath
        return None