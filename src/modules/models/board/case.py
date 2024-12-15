## Interface

"""
Case Module

This module provides a class to represent a case on a board.

Classes:

    Case: Represents a case on a board.
    
    Attributes:
    
        coordinate (Coordinate): The coordinate of the case.
        entity (Entity): The entity on the case.

Methods:

    getCoordinate() -> Coordinate:
    
        Get the coordinate of the case.
        
        Returns:
            Coordinate: The coordinate of the case.
    
    getEntity() -> Entity:
    
        Get the entity on the case.
        
        Returns:
            Entity: The entity on the case.
    
    setEntity(entity: Entity) -> None:
    
        Set the entity on the case.
        
        Args:
            entity (Entity): The entity on the case.
        
        Returns:
            None
"""

# ---------------------------------------------------------------------------------------------------- #

## Implementation

# Import #
from modules.models.coordinate import Coordinate
from modules.models.entities.entity import Entity

# Class #
class Case:
    
    def __init__(self, coordinate : Coordinate, entity : Entity = None, isBlocked = False) -> None:
        """Constructor for the Case class.

        Args:
            coordinate (Coordinate): The coordinate of the case.
            entity (Entity, optional): The entity on the case. Defaults to None.
            isBlocked (boolean, default => False): The blocked state of a case 
            
        Returns:
            None
        """
        
        self.__isBlocked__ = isBlocked
        self.__coordinate__ = coordinate
        self.__entity__ = entity
        
        return None
        
    def getCoordinate(self) -> Coordinate :
        """Get the coordinate of the case.

        Returns:
            int: The coordinate of the case.
        """
        
        return self.__coordinate__
    
    def getEntity(self) -> Entity :
        """Get the entity on the case.

        Returns:
            entity (Entity): The entity on the case.
        """
        
        return self.__entity__
    
    def setEntity(self, entity : Entity) -> None :
        """Set the entity on the case.

        Args:
            entity (Entity): The entity on the case.

        Returns:
            None
        """
        
        self.__entity__ = entity
        
        return None
    
    def isBlocked(self) -> None:
        """Get the blocked state of the case.

        Returns:
            bool: The blocked state of the case
        """
        
        return self.__isBlocked__

    def setIsBlocked(self, isBlocked : bool) -> None:
        """Set the blocked state of the case.

        Args:
            isBlocked (bool): The blocked state.

        Returns:
            None
        """
        self.__isBlocked__ = isBlocked
        
        return None
    
    def isAvaillable(self) -> bool :
  
        isCaseBlocked : bool = self.isBlocked()
        isCaseEmpty : bool = self.getEntity() == None
            
        if(isCaseBlocked or not isCaseEmpty) : return False
        else : return True