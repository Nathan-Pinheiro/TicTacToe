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
from modules.models.board_components.directions import Directions
from modules.models.board_components.entity import Entity

import numpy as np
import random

MINIMAL_ALIGNMENT_LENGTH : int = 2

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
        
        self.__player_boards__ = np.zeros(len(playerEntities), dtype=np.uint64)
        self.__blocked_cells__ : int = 0

        self.__generateMasks__()

        return None

    def __get_bit_position(self, line: int, column: int) -> int:
        
        """Convert (row, col) to a bit index."""
        
        return line * self.__width__ + column

    def __generateMasks__(self) -> int :
        
        # This method allow initializing masks foreach possible line lenght, that allow then finding correctly 
        # if there is alignments in any positions, for any given line length

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
                
    def checkIfAlignmentOnCaseForPlayer(self, line : int, column : int, playerIndex : int, alignLength : int) -> bool:
        
        """Check for alignments for a given player"""        

        return self.checkAlignmentForPlayer(playerIndex, alignLength)
    
    def checkAlignmentForPlayer(self, playerIndex : int, alignLength : int) -> bool:
        
        """Check for alignments for a given player"""        

        playerPieces : int = self.__player_boards__[playerIndex]

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
        
        """Check for alignments for all players. If one have alignments, it returns the player index, else return -1"""        

        for playerIndex in range(0, len(self.__player_boards__)):
            if(self.checkAlignmentForPlayer(playerIndex, alignLength)) : return playerIndex
        
        return -1

    def isFull(self) -> bool:
        
        """Check if the board is full."""
        
        current_taken_cases = 0
        for player_board in self.__player_boards__: current_taken_cases |= player_board

        full_board = (1 << (self.__width__ * self.__height__)) - 1

        return current_taken_cases == full_board
    
    def isCaseAvaillable(self, line : int, column : int) -> bool :
        
        if(line < 0 or line >= self.getHeight()) : raise ValueError(f"Line is out of range. Should be from 0 to {self.getHeight()} but was <{line}>")
        if(column < 0 or column >= self.getWidth()) : raise ValueError(f"Column is out of range. Should be from 0 to {self.getWidth()} but was <{column}>")

        bit_position = self.__get_bit_position(line, column)

        takenCases = 0
        for player_board in self.__player_boards__: takenCases |= player_board
        takenCases |= self.__blocked_cells__

        return (takenCases & (1 << bit_position)) == 0
    
    def isCaseBlocked(self, line : int, column : int) -> bool :
        
        if(line < 0 or line >= self.getHeight()) : raise ValueError(f"Line is out of range. Should be from 0 to {self.getHeight()} but was <{line}>")
        if(column < 0 or column >= self.getWidth()) : raise ValueError(f"Column is out of range. Should be from 0 to {self.getWidth()} but was <{column}>")

        bit_position = self.__get_bit_position(line, column)

        return (self.__blocked_cells__ & (1 << bit_position)) != 0
    
    def setIsCaseBlocked(self, line : int, column : int, isBlocked : bool) -> None :
        
        if(line < 0 or line >= self.getHeight()) : raise ValueError(f"Line is out of range. Should be from 0 to {self.getHeight()} but was <{line}>")
        if(column < 0 or column >= self.getWidth()) : raise ValueError(f"Column is out of range. Should be from 0 to {self.getWidth()} but was <{column}>")

        bit_position = self.__get_bit_position(line, column)
        
        self.__blocked_cells__ |= (1 << bit_position)

        return None

    def getEntityAt(self, line : int, column : int) -> Entity :
        
        if(line < 0 or line >= self.getHeight()) : raise ValueError(f"Line is out of range. Should be from 0 to {self.getHeight()} but was <{line}>")
        if(column < 0 or column >= self.getWidth()) : raise ValueError(f"Column is out of range. Should be from 0 to {self.getWidth()} but was <{column}>")

        bit_position = self.__get_bit_position(line, column)

        for playerIndex in range(0, len(self.__player_boards__)) : 
            if((self.__player_boards__[playerIndex] & (1 << bit_position)) != 0) : return self.__player_entities__[playerIndex]

        return None
    
    def isEntityAt(self, line : int, column : int) -> bool :
        
        if(line < 0 or line >= self.getHeight()) : raise ValueError(f"Line is out of range. Should be from 0 to {self.getHeight()} but was <{line}>")
        if(column < 0 or column >= self.getWidth()) : raise ValueError(f"Column is out of range. Should be from 0 to {self.getWidth()} but was <{column}>")

        bit_position = self.__get_bit_position(line, column)

        for playerIndex in range(0, len(self.__player_boards__)) : 
            if((self.__player_boards__[playerIndex] & (1 << bit_position)) != 0) : return True

        return False

    def addPlayerEntityAt(self, line : int, column : int, playerIndex : int) -> None:
        
        if(line < 0 or line >= self.getHeight()) : raise ValueError(f"Line is out of range. Should be from 0 to {self.getHeight()} but was <{line}>")
        if(column < 0 or column >= self.getWidth()) : raise ValueError(f"Column is out of range. Should be from 0 to {self.getWidth()} but was <{column}>")

        bit_position = self.__get_bit_position(line, column)
        
        self.__player_boards__[playerIndex] |= (1 << bit_position)

        return None
    
    def removeEntityAt(self, line : int, column : int) -> None:
        
        if(line < 0 or line >= self.getHeight()) : raise ValueError(f"Line is out of range. Should be from 0 to {self.getHeight()} but was <{line}>")
        if(column < 0 or column >= self.getWidth()) : raise ValueError(f"Column is out of range. Should be from 0 to {self.getWidth()} but was <{column}>")

        bit_position = self.__get_bit_position(line, column)

        for playerIndex in range(0, len(self.__player_boards__)) : 
            
            # This mask allows making the bit to remove be considered as unsigned int by python interpreter
            
            mask = (1 << 64) - 1
            bitToRemove =  ~(1 << bit_position) & mask

            self.__player_boards__[playerIndex] &= bitToRemove

        return None
    
    def blockRandomCase(self) -> None:
        
        """Block a random available case."""
        
        takenCases = 0
        for player_board in self.__player_boards__: takenCases |= player_board
        takenCases |= self.__blocked_cells__

        available_cases = []
        
        for line in range(self.__height__):
            for column in range(self.__width__):
                
                bit_position = self.__get_bit_position(line, column)
                
                if (takenCases & (1 << bit_position)) == 0: available_cases.append(bit_position)

        if len(available_cases) == 0 : raise ValueError("No available cases to block!")

        chosen_case = random.choice(available_cases)

        self.__blocked_cells__ |= (1 << chosen_case)
        
        return None
        
    def copy(self) -> Board:

        board : Board = OptimizedBoard(self.__width__, self.__height__, self.__player_entities__)

        board.__blocked_cells__ = self.__blocked_cells__
        board.__player_boards__ = self.__player_boards__

        return board