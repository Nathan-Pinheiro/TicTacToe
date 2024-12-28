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
from modules.models.board_components.board import Board
from modules.models.board_components.entity import Entity
from modules.utils.decorator import private_method

import numpy as np
import random

# Class #
class OptimizedBoard(Board):

    def __init__(self, width : int, height : int, playerEntities : list[Entity]) -> None:
        """Constructor for the Board class.

        Args:
            width (int): The width of the board.
            height (int): The height of the board.
            
        Returns:
            None
        """
        
        super().__init__(width, height, playerEntities)

        assert(width * height <= 64)
        
        self.__playerBoards__ = np.zeros(len(playerEntities), dtype=np.uint64)
        self.__blockedCases__ : int = 0
        self.__blockedCaseCount__ : int = 0
        self.__pieceCount__ : int = 0

        self.__generateMasks__()

        return None

    @private_method
    def __get_bit_position(self, line: int, column: int) -> int:
        
        """Convert (row, col) to a bit index."""
        
        return line * self.__width__ + column

    @private_method
    def __generateMasks__(self) -> int :
        """
        This method allow initializing masks foreach possible line lenght, that allow then finding correctly 
        if there is alignments in any positions, for any given line length
        """

        self.__lineMasks__ : list[int] = []
        self.__columnMasks__ : list[int] = []
        self.__ascendantDiagonalMasks__ : list[int] = []
        self.__descendantDiagonalMasks__ : list[int] = []

        for alinmentLength in range(0, max(self.__width__, self.__height__) + 1):

            self.__lineMasks__.append(0)
            self.__columnMasks__.append(0)
            self.__ascendantDiagonalMasks__.append(0)
            self.__descendantDiagonalMasks__.append(0)

            for lineIndex in range(0, self.__height__) :
                for columnIndex in range(0, self.__width__) :

                    if(lineIndex <= self.__height__ - alinmentLength) : 
                        self.__columnMasks__[alinmentLength] += (1 << (lineIndex * self.__width__ + columnIndex))
                        
                    if(columnIndex <= self.__width__ - alinmentLength) : 
                        self.__lineMasks__[alinmentLength] += (1 << (lineIndex * self.__width__ + columnIndex))
                        
                    if(lineIndex <= self.__height__ - alinmentLength and columnIndex <= self.__width__ - alinmentLength) : 
                        self.__descendantDiagonalMasks__[alinmentLength] += (1 << (lineIndex * self.__width__ + columnIndex))
                        
                    if(lineIndex <= self.__height__ - alinmentLength and columnIndex >= alinmentLength - 1) : 
                        self.__ascendantDiagonalMasks__[alinmentLength] += (1 << (lineIndex * self.__width__ + columnIndex))
    
    def isCaseAvaillable(self, line : int, column : int) -> bool :
        
        if(line < 0 or line >= self.getHeight()) : raise ValueError(f"Line is out of range. Should be from 0 to {self.getHeight()} but was <{line}>")
        if(column < 0 or column >= self.getWidth()) : raise ValueError(f"Column is out of range. Should be from 0 to {self.getWidth()} but was <{column}>")

        bit_position = self.__get_bit_position(line, column)

        takenCases = 0
        for player_board in self.__playerBoards__: takenCases |= player_board
        takenCases |= self.__blockedCases__

        return (takenCases & (1 << bit_position)) == 0
    
    def isCaseBlocked(self, line : int, column : int) -> bool :
        
        if(line < 0 or line >= self.getHeight()) : raise ValueError(f"Line is out of range. Should be from 0 to {self.getHeight()} but was <{line}>")
        if(column < 0 or column >= self.getWidth()) : raise ValueError(f"Column is out of range. Should be from 0 to {self.getWidth()} but was <{column}>")

        bit_position = self.__get_bit_position(line, column)

        return (self.__blockedCases__ & (1 << bit_position)) != 0
    
    def setIsCaseBlocked(self, line : int, column : int, isBlocked : bool) -> None :
        
        if(line < 0 or line >= self.getHeight()) : raise ValueError(f"Line is out of range. Should be from 0 to {self.getHeight()} but was <{line}>")
        if(column < 0 or column >= self.getWidth()) : raise ValueError(f"Column is out of range. Should be from 0 to {self.getWidth()} but was <{column}>")

        bit_position = self.__get_bit_position(line, column)
        
        if(self.__blockedCases__ & (1 << bit_position) == 0 and isBlocked) : self.__blockedCaseCount__ += 1
        elif(self.__blockedCases__ & (1 << bit_position) == 1 and not isBlocked) : self.__blockedCaseCount__ -= 1
        
        self.__blockedCases__ |= (1 << bit_position)

        return None

    def getEntityAt(self, line : int, column : int) -> Entity :
        
        if(line < 0 or line >= self.getHeight()) : raise ValueError(f"Line is out of range. Should be from 0 to {self.getHeight()} but was <{line}>")
        if(column < 0 or column >= self.getWidth()) : raise ValueError(f"Column is out of range. Should be from 0 to {self.getWidth()} but was <{column}>")

        bit_position = self.__get_bit_position(line, column)

        for playerIndex in range(0, len(self.__playerBoards__)) : 
            if((self.__playerBoards__[playerIndex] & (1 << bit_position)) != 0) : return self.__playerEntities__[playerIndex]

        return None
    
    def isEntityAt(self, line : int, column : int) -> bool :
        
        if(line < 0 or line >= self.getHeight()) : raise ValueError(f"Line is out of range. Should be from 0 to {self.getHeight()} but was <{line}>")
        if(column < 0 or column >= self.getWidth()) : raise ValueError(f"Column is out of range. Should be from 0 to {self.getWidth()} but was <{column}>")

        bit_position = self.__get_bit_position(line, column)

        for playerIndex in range(0, len(self.__playerBoards__)) : 
            if((self.__playerBoards__[playerIndex] & (1 << bit_position)) != 0) : return True

        return False

    def addPlayerEntityAt(self, line : int, column : int, playerIndex : int) -> None:
        
        if(line < 0 or line >= self.getHeight()) : raise ValueError(f"Line is out of range. Should be from 0 to {self.getHeight()} but was <{line}>")
        if(column < 0 or column >= self.getWidth()) : raise ValueError(f"Column is out of range. Should be from 0 to {self.getWidth()} but was <{column}>")

        bit_position = self.__get_bit_position(line, column)
        
        self.__playerBoards__[playerIndex] |= (1 << bit_position)
        self.__pieceCount__ += 1

        return None
    
    def removeEntityAt(self, line : int, column : int) -> None:
        
        if(line < 0 or line >= self.getHeight()) : raise ValueError(f"Line is out of range. Should be from 0 to {self.getHeight()} but was <{line}>")
        if(column < 0 or column >= self.getWidth()) : raise ValueError(f"Column is out of range. Should be from 0 to {self.getWidth()} but was <{column}>")

        bit_position = self.__get_bit_position(line, column)

        for playerIndex in range(0, len(self.__playerBoards__)) : 
            
            # This mask allows making the bit to remove be considered as unsigned int by python interpreter
            
            mask = (1 << 64) - 1
            bitToRemove =  ~(1 << bit_position) & mask

            self.__playerBoards__[playerIndex] &= bitToRemove

        self.__pieceCount__ -= 1

        return None

    def checkAlignmentOnCaseForPlayer(self, line : int, column : int, playerIndex : int, alignLength : int) -> bool:
        
        return self.checkAlignmentForPlayer(playerIndex, alignLength)
    
    def checkAlignmentForPlayer(self, playerIndex : int, alignLength : int) -> bool:
        
        # The idea there is to use the less loops as possible, and replace this by binary computations, finding pairs with a 
        # given shift between them and doing it as much times as the length of the alignment is. Then by using a mask, 
        # we can avoid having wrong results as for exemple bits that are together but that are not on the same line.
        # As those masks are computed one time only at the initialization of the object, it do not slow down the computation.

        playerPieces : int = self.__playerBoards__[playerIndex]

        # Lines
        
        shift : int = 1
        casesWithNeibours : int = playerPieces
        for _ in range(alignLength - 1) : casesWithNeibours &= (casesWithNeibours >> shift)
        if(casesWithNeibours & self.__lineMasks__[alignLength] != 0) : return True
        
        # Columns
        
        shift : int = self.__width__
        casesWithNeibours : int = playerPieces
        for _ in range(alignLength - 1): casesWithNeibours &= (casesWithNeibours >> shift)
        if(casesWithNeibours & self.__columnMasks__[alignLength] != 0) : return True
        
        # Ascendant diagonals
        
        shift : int = self.__width__ - 1
        casesWithNeibours : int = playerPieces
        for _ in range(alignLength - 1): casesWithNeibours &= (casesWithNeibours >> shift)
        if(casesWithNeibours & self.__ascendantDiagonalMasks__[alignLength] != 0) : return True
        
        # Descendant diagonals
        
        shift : int = self.__width__ + 1
        casesWithNeibours : int = playerPieces
        for _ in range(alignLength - 1): casesWithNeibours &= (casesWithNeibours >> shift)
        if(casesWithNeibours & self.__descendantDiagonalMasks__[alignLength] != 0) : return True

        return False
    
    def checkIfPlayerHaveAlignment(self, alignLength : int) -> int:
        
        for playerIndex in range(0, len(self.__playerBoards__)):
            if(self.checkAlignmentForPlayer(playerIndex, alignLength)) : return playerIndex
        
        return -1

    def checkIfPlayerHaveAlignmentOnCase(self, alignLength: int) -> int:
        
        for playerIndex in range(0, len(self.__playerBoards__)):
            if(self.checkAlignmentOnCaseForPlayer(playerIndex, alignLength)) : return playerIndex
        
        return -1

    def isFull(self) -> bool:
        
        return self.__pieceCount__ == self.__width__ * self.__height__ - self.__blockedCaseCount__

    def blockRandomCase(self) -> None:
        
        takenCases = 0
        for player_board in self.__playerBoards__: takenCases |= player_board
        takenCases |= self.__blockedCases__

        available_cases = []
        
        for line in range(self.__height__):
            for column in range(self.__width__):
                bit_position = self.__get_bit_position(line, column)
                if (takenCases & (1 << bit_position)) == 0: available_cases.append(bit_position)

        if len(available_cases) == 0 : raise ValueError("No available cases to block!")

        chosen_case = random.choice(available_cases)
        self.__blockedCases__ |= (1 << chosen_case)
        
        return None
        
    def copy(self) -> Board:

        board : Board = OptimizedBoard(self.__width__, self.__height__, self.__playerEntities__)

        board.__playerBoards__ = self.__playerBoards__
        board.__blockedCases__ = self.__blockedCases__
        board.__pieceCount__ = self.__pieceCount__

        return board