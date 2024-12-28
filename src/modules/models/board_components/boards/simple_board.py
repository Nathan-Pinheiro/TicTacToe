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

    def __init__(self, width : int, height : int, player_entities : list[Entity]) -> None:
        """Constructor for the Board class.
s
        Args:
            width (int): The width of the board.
            height (int): The height of the board.
            
        Returns:
            None
        """
        
        super.__init__(width, height, player_entities)
        
        self.__piecesOnBoard__ = 0
        self.__caseBlocked__ = 0

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

    def isCaseBlocked(self, line : int, column : int) -> bool :
        
        if(line < 0 or line > self.getHeight()) : raise ValueError(f"Line is out of range. Should be from 0 to {self.getHeight()} but was <{line}>")
        if(column < 0 or column > self.getWidth()) : raise ValueError(f"Column is out of range. Should be from 0 to {self.getWidth()} but was <{column}>")

        return self.__cases__[line][column].isBlocked()

    def setIsCaseBlocked(self, line : int, column : int, isBlocked : bool) -> None :

        if(isBlocked and not self.__cases__[line][column].isBlocked()): self.__caseBlocked__ += 1 
        elif(not isBlocked and self.__cases__[line][column].isBlocked()) : self.__caseBlocked__ -= 1
        
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
    
    def addPlayerEntityAt(self, line : int, column : int, playerIndex : int) -> None:
        
        if(line < 0 or line >= self.getHeight()) : raise ValueError(f"Line is out of range. Should be from 0 to {self.getHeight()} but was <{line}>")
        if(column < 0 or column >= self.getWidth()) : raise ValueError(f"Column is out of range. Should be from 0 to {self.getWidth()} but was <{column}>")
        if(playerIndex < 0 or playerIndex >= len(self.__player_entities__)) : raise ValueError(f"Player index is out of range. Should be from 0 to {len(self.__player_entities__)} but was <{playerIndex}>")

        entity : Entity = self.__player_entities__[playerIndex]
        self.__cases__[line][column].setEntity(entity)
        self.__piecesOnBoard__ += 1

        return None
    
    def removeEntityAt(self, line : int, column : int) -> None:
        
        if(line < 0 or line >= self.getHeight()) : raise ValueError(f"Line is out of range. Should be from 0 to {self.getHeight()} but was <{line}>")
        if(column < 0 or column >= self.getWidth()) : raise ValueError(f"Column is out of range. Should be from 0 to {self.getWidth()} but was <{column}>")

        if(self.__cases__[line][column].getEntity() != None) : self.__piecesOnBoard__ -= 1

        self.__cases__[line][column].setEntity(None)

        return None

    def checkIfAlignmentOnCaseForPlayer(self, line : int, column : int, playerIndex : int, align_length : int) -> bool:
        
        """
        Check if there a given player have his entities aligned
        """

        pass
    
    def checkAlignmentForPlayer(self, playerIndex : int, alignLength : int) -> bool:
        pass

    def checkIfPlayerHaveAlignment(self, alignLength : int) -> int:
        pass
    
    def getEntityAligned(self, align_length : int) -> Entity:
        """
        Check if there is an Alignment of a given length and return the entity aligned
        """
        
        raise NotImplementedError("not develloped for the moment")

        pass
    
    def isFull(self) -> bool :
        
        raise NotImplementedError("not develloped for the moment")

        pass
    
    def blockRandomCase(self) -> None :
        pass
    
    def copy(self) -> Board:
        pass