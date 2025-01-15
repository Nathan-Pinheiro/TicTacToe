from modules.models.board_game.board.components.optimized_board_components.bitboard import BitBoard
from modules.utils.decorator import privatemethod, override

import numpy as np

# ************************************************
# Class NumpyBitBoard
# ************************************************
# ROLE : This module is representing bitboard
# ************************************************
# VERSION : 1.0
# AUTHOR : Nathan PINHEIRO
# DATE : 13/01/2025
# ************************************************

class NumpyBitBoard(BitBoard) :
    


    def __init__(self, width : int, height : int) -> None:
        
        """
        Constructor for the NumpyBitBoard class.

        Args:
            width (int): The width of the board.
            height (int): The height of the board.
            
        Returns:
            None
        """

        super().__init__(width, height)

        self.__bits__ : np.ndarray = np.zeros((height, width), dtype=int)
        
        self.__generateBoardQuadrantMasks__()
    
    @privatemethod
    def __getBitPosition__(self, line: int, column: int) -> int:
        
        """
        Convert (row, col) to a bit index.
        
        Args:
            line (int): The line of the bit.
            column (int): The column of the bit.
            
        Returns:
            position (int): the position index of the bit
        """
        
        return line * self.__width__ + column

    @privatemethod
    def __generateBoardQuadrantMasks__(self) -> None :
        
        """
        This method allow initializing masks foreach part of board. (upper left, upper right, lower left, lower right).
        This will then be usefull to hash the BitBoard, having a hash code that have the same hash for symetrical boards.
        """
        
        self.__upperLeftMask__ : np.ndarray = np.zeros((self.__height__, self.__width__), dtype=int)
        self.__upperRighMask__ : np.ndarray = np.zeros((self.__height__, self.__width__), dtype=int)
        self.__lowerLeftMask__ : np.ndarray = np.zeros((self.__height__, self.__width__), dtype=int)
        self.__lowerRightMask__ : np.ndarray = np.zeros((self.__height__, self.__width__), dtype=int)
        
        centerLine : float = (self.__height__ - 1) / 2
        centerColumn : float = (self.__width__ - 1) / 2

        for line in range(0, self.__height__) :
            for column in range(0, self.__width__) :
                
                bitIndex = self.__getBitPosition__(line, column)
                if(line <= centerLine and column <= centerColumn) : self.__upperLeftMask__[line][column] = 1
                if(line <= centerLine and column >= centerColumn) : self.__upperRighMask__[line][column] = 1
                if(line >= centerLine and column <= centerColumn) : self.__lowerLeftMask__[line][column] = 1
                if(line >= centerLine and column >= centerColumn) : self.__lowerRightMask__[line][column] = 1

    @privatemethod
    def __convertBitArrayToInt__(self, bitBoard : np.ndarray) -> int :
        
        flat_bitboard = bitBoard.ravel() 
        bitboard_int = np.dot(flat_bitboard, 1 << np.arange(flat_bitboard.size))
        
        return bitboard_int
    
    @privatemethod
    def __convertIntToBitArray__(self, bitboard_int: int) -> np.ndarray:
        
        bitboard = np.zeros((self.__height__, self.__width__), dtype=int)
        
        for line in range(self.__height__): 
            for column in range(self.__width__):
                bitboard[line][column] = 1 if 1 << line * self.__width__ + column & bitboard_int else 0
    
        return bitboard
    
    @privatemethod
    def __getRotatedBitBoardBy90Degree__(self, mask: np.ndarray = None, n : int = 1) -> np.ndarray:
        
        """
        Return the rotated the given bitboard value & the given mask by 90 degrees. Do this n times.
        
        Parameters :
            - mask (np.ndarray) : The mask
            - n (int) : the amount of time it has to rotate by 90 degrees
            
        Returns:
            bitboard (np.ndarray): the rotated bitboard
        """

        bits : np.ndarray
        if(mask is not None) : bits = self.__bits__ & mask
        else : bits = self.__bits__

        return np.rot90(bits, k=n)

    @override
    def getValue(self) -> int :
        return self.__convertBitArrayToInt__(self.__bits__)
    
    @override
    def applyOr(self, value : int) -> None :
        self.__bits__ |= self.__convertIntToBitArray__(value)
        
    @override
    def applyXor(self, value : int) -> None :
        self.__bits__ ^= self.__convertIntToBitArray__(value)
    
    @override
    def applyAnd(self, value : int) -> None :
        self.__bits__ &= self.__convertIntToBitArray__(value)

    @override
    @privatemethod
    def __hash__(self) -> int:

        normalHash : int = hash(self.__bits__.tobytes())
        rotated90Hash : int = hash(self.__getRotatedBitBoardBy90Degree__(1).tobytes())
        rotated180Hash : int = hash(self.__getRotatedBitBoardBy90Degree__(2).tobytes())
        rotated270Hash : int = hash(self.__getRotatedBitBoardBy90Degree__(3).tobytes())
        
        verticalyFlippedHash : int = hash(np.fliplr(self.__bits__).tobytes())
        horizontallyFlippedHash : int = hash(np.flipud(self.__bits__).tobytes())
        
        return normalHash + rotated90Hash + rotated180Hash + rotated270Hash + verticalyFlippedHash + horizontallyFlippedHash
