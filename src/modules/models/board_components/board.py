## Interface

"""
Board Module

This module provides a class to represent a board.

Classes:
    Board: Represents a board.
    
    Attributes:
        width (int): The width of the board.
        height (int): The height of the board.

Methods:
    initializeBoard() -> None:
        Private method.
        Initialize the board.
        
        Returns:
            None

    getCase(line: int, column: int) -> Case:
        Get the case at the given line and column.
        
        Args:
            line (int): The line of the case to get.
            column (int): The column of the case to get.
        
        Returns:
            Case: The case at the given line and column.
"""

# ---------------------------------------------------------------------------------------------------- #

## Implementation

# Import #
from __future__ import annotations

from modules.models.board_components.case import Case
from modules.models.board_components.entity import Entity
from modules.models.board_components.directions import Directions
from modules.utils.decorator import private_method

# Class #
class Board:

    def __init__(self, width : int, height : int, player_entities : list[Entity]) -> None:
        """Constructor for the Board class.

        Args:
            width (int): The width of the board.
            height (int): The height of the board.
            
        Returns:
            None
        """

        self.__width__ : int = width
        self.__height__ : int = height
        self.__player_entities__ : list[Entity] = player_entities
        
        return None
        
    def isCaseAvaillable(self, line : int, column : int) -> bool :
        pass

    def isCaseBlocked(self, line : int, column : int) -> bool :
        pass
    
    def setIsCaseBlocked(self, line : int, column : int, isBlocked : bool) -> None :
        pass
    
    def blockRandomCase(self) -> None :
        pass
    
    def isEntityAt(self, line : int, column : int) -> bool :
        pass

    def getEntityAt(self, line : int, column : int) -> Entity :
        pass

    def addPlayerEntityAt(self, line : int, column : int, playerIndex : int) -> None:
        pass
    
    def removeEntityAt(self, line : int, column : int) -> None:
        pass

    def checkIfAlignmentOnCaseForPlayer(self, line : int, column : int, playerIndex : int, alignLength : int) -> bool:
        
        """
        Check if there a given player have his entities aligned
        """

        pass
    
    def checkAlignmentForPlayer(self, playerIndex : int, alignLength : int) -> bool:
        pass

    def checkIfPlayerHaveAlignment(self, alignLength : int) -> int:

        """
        Check for alignments for all players with a given length. 
        
        Return the player with aligned pieces index, -1 if there is no alignments. 
        """        

        pass
    
    def isFull(self) -> bool :
        pass

    def getWidth(self) -> int:
        return self.__width__

    def getHeight(self) -> int:
        return self.__height__
    
    def getPlayerEntities(self) -> list[int]:
        return self.__player_entities__
    
    def copy(self) -> Board:
        pass