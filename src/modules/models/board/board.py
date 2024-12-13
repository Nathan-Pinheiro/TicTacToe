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
from modules.models.board.case import Case
from modules.models.coordinate import Coordinate
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
        
        self.__initializeBoard__()
        
        return None

    @private_method
    def __initializeBoard__(self) -> None:
        """Initialize the board.
        
        Returns:
            None
        """
        
        self.__cases__: list[list[Case]] = [[Case(Coordinate(line, column)) for column in range(self.__width__)] for line in range(self.__height__)]
        
        return None
        
    def getAvaillableCases(self) -> list[Case] :

        availlable_cases = []        

        for line in range(0, self.getHeight()):
            
            for column in range(0, self.getWidth()):

                if(self.getCase(line, column)):
                    
                    case : Case = self.getCase(line, column)
                    
                    isCaseBlocked : bool = case.isBlocked()
                    isCaseEmpty : bool = case.getEntity() == None
                    
                    if(not isCaseBlocked and isCaseEmpty): availlable_cases.append(case)
                    
        return availlable_cases

    def getCase(self, line : int, column : int) -> Case :
        """Get the case at the given line and column.

        Args:
            line (int): The line of the case to get.
            column (int): The column of the case to get.

        Returns:
            Case: The case at the given line and column.
        """
        if(line < 0 or line > self.getHeight()) : return None
        if(column < 0 or column > self.getWidth()) : return None     

        return self.__cases__[line][column]
    
    def getWidth(self) -> int:
        return self.__width__

    def getHeight(self) -> int:
        return self.__height__