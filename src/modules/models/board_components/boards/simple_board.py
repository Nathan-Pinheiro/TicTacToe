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
from modules.models.board_components.board import Board
from modules.models.board_components.entity import Entity
from modules.models.board_components.directions import Directions
from modules.models.board_components.coordinate import Coordinate
from modules.utils.decorator import private_method

# Class #
class SimpleBoard(Board):

    def __init__(self, width : int, height : int) -> None:
        """Constructor for the Board class.
s
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

                case : Case = self.__cases__[line][column]

                if(self.__cases__[line][column]):
                    
                    if(case.isAvaillable()): availlable_cases.append(case)
                    
        return availlable_cases

    def isCaseBlocked(self, line : int, column : int) -> bool :
        
        if(line < 0 or line > self.getHeight()) : raise ValueError(f"Line is out of range. Should be from 0 to {self.getHeight()} but was <{line}>")
        if(column < 0 or column > self.getWidth()) : raise ValueError(f"Column is out of range. Should be from 0 to {self.getWidth()} but was <{column}>")

        return self.__cases__[line][column].isBlocked()

    def setIsCaseBlocked(self, line : int, column : int, isBlocked : bool) -> None :
        self.__cases__[line][column].setIsBlocked(isBlocked)
        return None

    def isCaseAvaillable(self, line : int, column : int) -> bool :
        
        if(line < 0 or line > self.getHeight()) : raise ValueError(f"Line is out of range. Should be from 0 to {self.getHeight()} but was <{line}>")
        if(column < 0 or column > self.getWidth()) : raise ValueError(f"Column is out of range. Should be from 0 to {self.getWidth()} but was <{column}>")
        
        return self.__cases__[line][column].isAvaillable()

    def getEntityAt(self, line : int, column : int) -> Entity :
        
        if(line < 0 or line > self.getHeight()) : raise ValueError(f"Line is out of range. Should be from 0 to {self.getHeight()} but was <{line}>")
        if(column < 0 or column > self.getWidth()) : raise ValueError(f"Column is out of range. Should be from 0 to {self.getWidth()} but was <{column}>")

        return self.__cases__[line][column].getEntity()
    
    def setEntityAt(self, line : int, column : int, entity : Entity) :
        
        if(line < 0 or line > self.getHeight()) : raise ValueError(f"Line is out of range. Should be from 0 to {self.getHeight()} but was <{line}>")
        if(column < 0 or column > self.getWidth()) : raise ValueError(f"Column is out of range. Should be from 0 to {self.getWidth()} but was <{column}>")

        return self.__cases__[line][column].setEntity(entity)
    
    def isLineConsituedBySameEntity(self, startLine : int, startColumn : int, lineLength : int, direction : Directions) -> bool:

        if(lineLength < 1) : return False
          
        if startLine < 0 or startLine >= self.getHeight() : return False
        if startColumn < 0 or startColumn >= self.getWidth() : return False

        if(direction == None) : return False        

        lineDirection, columnDirection = direction.value
        
        if startLine + lineLength * lineDirection < 0 or startLine + lineLength * lineDirection >= self.getHeight() : return False
        if startColumn + lineLength * columnDirection < 0 or startColumn + lineLength * columnDirection >= self.getWidth() : return False
        
        entity = self.getEntityAt(startLine, startColumn)
        
        for step in range(1, lineLength):
            
            currentLine = startLine + step * lineDirection
            currentColumn = startColumn + step * columnDirection
                
            if self.getEntityAt(currentLine, currentColumn) != entity: return False
                    
        return True