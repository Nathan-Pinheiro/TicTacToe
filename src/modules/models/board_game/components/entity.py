from __future__ import annotations
from abc import ABC, abstractmethod

# ************************************************
# CLASS Entity
# ************************************************
# ROLE : This class is used to represent the entity for a player, that will be drawn on the screen
# ************************************************
# VERSION : 1.0
# AUTHOR : Nathan PINHEIRO
# DATE : 13/01/2025
# ************************************************

class Entity(ABC) :
    
    """
    A class that represent a generic entity
    """

    def __init__(self, name : str, iconPath : str = None) -> None:
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
    
    def __eq__(self, other: object) -> bool:
        """Allow comparing the value of the entity with another objects.
        
        Args:
            the second object to compare with.
        
        Returns: 
            bool : if the two objects have the same content
        """
        if not isinstance(other, Entity): return False
        return self.__name__ == other.__name__ and self.__iconPath__ == other.__iconPath__
    
    def __str__(self):
        """Return the string value of the entity.
        
        Returns:
            str: The string value of the entity
        """
        return self.getName()

    def copy(self) -> Entity:
        """
        Create a copy of the current Entity object.

        Returns:
            Entity: A new instance of Entity with the same attributes.
        """
        return Entity(self.__name__, self.__iconPath__)