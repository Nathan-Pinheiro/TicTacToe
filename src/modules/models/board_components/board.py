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
from modules.models.board_components.case import Case
from modules.models.board_components.entity import Entity
from modules.models.board_components.directions import Directions
from modules.utils.decorator import private_method

# Class #
class Board:

    def __init__(self, width : int, height : int) -> None:
        """Constructor for the Board class.

        Args:
            width (int): The width of the board.
            height (int): The height of the board.
            
        Returns:
            None
        """
        
        self.__width__ : int = width
        self.__height__ : int = height
        
        return None
        
    def isCaseAvaillable(self, line : int, column : int) -> bool :
        pass 
    
    def getAvaillableCases(self) -> list[Case] :
        pass

    def isCaseBlocked(self, line : int, column : int) -> bool :
        pass
    
    def setIsCaseBlocked(self, line : int, column : int, isBlocked : bool) -> None :
        pass

    def getEntityAt(self, line : int, column : int) -> Entity:
        pass

    def setEntityAt(self, line : int, column : int, entity : Entity) -> None:
        pass
    
    def isLineConsituedBySameEntity(self, startLine : int, startColumn : int, lineLength : int, direction : Directions) -> bool:
        """
        Check if a specific line contains a the same entity.

        Args:
            startLine (int): Starting line.
            startColumn (int): Starting column.
            lineLength (int): The length of the line.
            direction (int): The direction the line is going.

        Returns:
            bool: True if there the described line is constituted by the same entity, False otherwise.
        """
        pass
    
    def getWidth(self) -> int:
        return self.__width__

    def getHeight(self) -> int:
        return self.__height__