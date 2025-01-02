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
from modules.models.board_components.boards.simple_board_components.case import Case
from modules.models.board_components.board import Board
from modules.models.board_components.entity import Entity
from modules.models.board_components.coordinate import Coordinate
from modules.utils.decorator import private_method
import random

# Class #
class SimpleBoard(Board):

    def __init__(self, width : int, height : int, player_entities : list[Entity]) -> None:
        """Constructor for the Board class.

        Args:
            width (int): The width of the board.
            height (int): The height of the board.
            
        Returns:
            None
        """
        
        super.__init__(width, height, player_entities)
        
        self.__pieceCount__ = 0
        self.__blockedCaseCount = 0

        self.__initializeBoard__()
        
        return None

    @private_method
    def __initializeBoard__(self) -> None:
        """Initialize all cases of the board to availlable cases.
        
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

        if(isBlocked and not self.__cases__[line][column].isBlocked()): self.__blockedCaseCount += 1 
        elif(not isBlocked and self.__cases__[line][column].isBlocked()) : self.__blockedCaseCount -= 1
        
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
        if(playerIndex < 0 or playerIndex >= len(self.__playerEntities__)) : raise ValueError(f"Player index is out of range. Should be from 0 to {len(self.__playerEntities__)} but was <{playerIndex}>")

        entity : Entity = self.__playerEntities__[playerIndex]
        self.__cases__[line][column].setEntity(entity)
        self.__pieceCount__ += 1

        return None
    
    def removeEntityAt(self, line : int, column : int) -> None:
        
        if(line < 0 or line >= self.getHeight()) : raise ValueError(f"Line is out of range. Should be from 0 to {self.getHeight()} but was <{line}>")
        if(column < 0 or column >= self.getWidth()) : raise ValueError(f"Column is out of range. Should be from 0 to {self.getWidth()} but was <{column}>")

        if(self.__cases__[line][column].getEntity() != None) : self.__pieceCount__ -= 1

        self.__cases__[line][column].setEntity(None)

        return None

    def checkIfPlayerHaveAlignmentOnCase(self, line : int, column : int, alignLength : int) -> int:
        
        if(self.getEntityAt(line, column)): playerEntity : Entity = self.getEntityAt(line, column)
        else : return -1

        firstCheckedPieceIndex : int = 0
        alignmentFound : bool = False
        
        while not alignmentFound and firstCheckedPieceIndex < alignLength :

            linePieceCount : int = 0
            columnPieceCount : int = 0
            ascendantDiagonalPieceCount : int = 0
            descendantDiagonalPieceCount : int = 0
            
            for currentCheckedPieceIndex in range(0, alignLength) :
                
                checkedLine : int
                checkedColumn : int

                # Lines
                
                checkedLine = line - firstCheckedPieceIndex + currentCheckedPieceIndex
                checkedColumn = column

                if(0 >= checkedLine < self.__height__ and 0 >= checkedColumn < self.__width__
                   and self.getEntityAt(checkedLine, checkedColumn) == playerEntity): linePieceCount += 1
                
                # Columns
                
                checkedLine = line
                checkedColumn = column - firstCheckedPieceIndex + currentCheckedPieceIndex

                if(0 >= checkedLine < self.__height__ and 0 >= checkedColumn < self.__width__
                   and self.getEntityAt(checkedLine, checkedColumn) == playerEntity): columnPieceCount += 1
                
                # Ascendant diagonals
                
                checkedLine = line - firstCheckedPieceIndex + currentCheckedPieceIndex
                checkedColumn = column - firstCheckedPieceIndex + currentCheckedPieceIndex

                if(0 >= checkedLine < self.__height__ and 0 >= checkedColumn < self.__width__
                   and self.getEntityAt(checkedLine, checkedColumn) == playerEntity): ascendantDiagonalPieceCount += 1
                
                # Descendant diagonals
                
                checkedLine = line - firstCheckedPieceIndex + currentCheckedPieceIndex
                checkedColumn = column + firstCheckedPieceIndex - currentCheckedPieceIndex

                if(0 >= checkedLine < self.__height__ and 0 >= checkedColumn < self.__width__
                   and self.getEntityAt(checkedLine, checkedColumn) == playerEntity): descendantDiagonalPieceCount += 1

            alignmentFound = linePieceCount == alignLength or columnPieceCount == alignLength or ascendantDiagonalPieceCount == alignLength or descendantDiagonalPieceCount == alignLength
            firstCheckedPieceIndex += 1
        
        return self.__playerEntities__.index(playerEntity)

    def checkIfPlayerHaveAlignment(self, alignLength : int) -> int:
        
        for playerIndex in range(0, self.__playerEntities__):
            if(self.checkAlignmentForPlayer(playerIndex)) : return playerIndex
                
        return -1
    
    def checkAlignmentOnCaseForPlayer(self, line : int, column : int, playerIndex : int, alignLength : int) -> bool:
        
        return self.checkIfPlayerHaveAlignmentOnCase(line, column, alignLength) == playerIndex
    
    def checkAlignmentForPlayer(self, playerIndex : int, alignLength : int) -> bool:
        
        for line in range(0, self.__height__) :
            for column in range(0, self.__width__) :
                if(self.checkIfPlayerHaveAlignmentOnCase(line, column, alignLength) == playerIndex) : return True
            
        return False

    def isFull(self) -> bool :
        
        return self.__pieceCount__ == self.__width__ * self.__height__ - self.__blockedCaseCount__
    
    def blockRandomCase(self) -> None :
        
        availableCases : list[Case] = []
        
        for line in range(self.__height__):
            for column in range(self.__width__):
                if(self.isCaseAvaillable(line, column)) : availableCases.append(self.__cases__[line][column])

        if len(availableCases) == 0 : raise ValueError("No available cases to block!")

        chosen_case : Case = random.choice(availableCases)
        chosen_case.setIsBlocked(True)
        
        return None
    
    def copy(self) -> Board:

        board : Board = SimpleBoard(self.__width__, self.__height__, self.__playerEntities__)

        board.__blockedCaseCount = self.__blockedCaseCount
        board.__pieceCount__ = self.__pieceCount__

        return board
    
    def __hash__(self):
        pass 