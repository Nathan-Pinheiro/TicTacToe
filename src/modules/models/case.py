## Interface

"""
Case Module

This module provides a class to represent a case on a board.

Classes:
    Case: Represents a case on a board.
    
    Attributes:
        coordinate (Coordinate): The coordinate of the case.
        pawn (Pawn): The pawn on the case.

Methods:
    getCoordinate() -> Coordinate:
        Get the coordinate of the case.
        
        Returns:
            Coordinate: The coordinate of the case.
    
    getPawn() -> Pawn:
        Get the pawn on the case.
        
        Returns:
            Pawn: The pawn on the case.
    
    setPawn(pawn: Pawn) -> None:
        Set the pawn on the case.
        
        Args:
            pawn (Pawn): The pawn on the case.
        
        Returns:
            None
"""

# ---------------------------------------------------------------------------------------------------- #

## Implementation

# Import #
from modules.models.coordinate import Coordinate
from modules.models.pawn import Pawn

# Class #
class Case:
    
    def __init__(self, coordinate : Coordinate, pawn : Pawn = None, isBlocked = False) -> None:
        """Constructor for the Case class.

        Args:
            coordinate (Coordinate): The coordinate of the case.
            pawn (Pawn, optional): The pawn on the case. Defaults to None.
            isBlocked (boolean, default => False): The blocked state of a case 
            
        Returns:
            None
        """
        
        self.__isBlocked__ = isBlocked
        self.__coordinate__ = coordinate
        self.__pawn__ = pawn
        
        return None
        
    def getCoordinate(self) -> Coordinate :
        """Get the coordinate of the case.

        Returns:
            int: The coordinate of the case.
        """
        
        return self.__coordinate__
    
    def getPawn(self) -> Pawn :
        """Get the pawn on the case.

        Returns:
            int: The pawn on the case.
        """
        
        return self.__pawn__
    
    def setPawn(self, pawn : Pawn) -> None :
        """Set the pawn on the case.

        Args:
            column (int): The pawn on the case.

        Returns:
            None
        """
        
        self.__pawn__ = pawn
        
        return None
    
    def isBlocked(self, isBlocked : bool) -> None:
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