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
    
    """
    Represents a bitboard using numpy
    """

    def __init__(self, width : int, height : int) -> None:
        
        """
        Constructor for the NumpyBitBoard class.

        Parameters:
            width (int): The width of the board.
            height (int): The height of the board.
            
        Returns:
            None
        """

        super().__init__(width, height)

        self.__bits__ : np.ndarray = np.zeros((height, width), dtype=int)
        
        self.__generateBoardQuadrantMasks__()
        
        return None
    
    @privatemethod
    def __getBitPosition__(self, line: int, column: int) -> int:
        
        """
        Convert (row, col) to a bit index.
        
        Parameters:
            line (int): The line of the bit.
            column (int): The column of the bit.
            
        Returns:
            position (int): the position index of the bit
        """
        
        return line * self.__width__ + column

    @privatemethod
    def __convertBitArrayToInt__(self, bitBoard : np.ndarray) -> int :
        
        """
        Convert a bit array to an integer.
        
        Parameters:
            bitBoard (np.ndarray): The bit array to convert.

        Returns:
            bitboard_int (int): The integer representation of the bit array.
        """
        
        flat_bitboard = bitBoard.ravel() 
        bitboard_int = np.dot(flat_bitboard, 1 << np.arange(flat_bitboard.size))
        
        return bitboard_int
    
    @privatemethod
    def __convertIntToBitArray__(self, bitboard_int: int) -> np.ndarray:
        
        """
        Convert an integer to a bit array.
        
        Parameters:
            bitboard_int (int): The integer to convert.

        Returns:
            bitboard (np.ndarray): The bit array representation of the integer.
        """
        
        bitboard = np.zeros((self.__height__, self.__width__), dtype=int)
        
        for line in range(self.__height__): 
            for column in range(self.__width__):
                bitboard[line][column] = 1 if 1 << line * self.__width__ + column & bitboard_int else 0
    
        return bitboard
    
    @privatemethod
    def __getRotatedBitBoardBy90Degree__(self, mask: np.ndarray = None, n : int = 1) -> np.ndarray:
        
        """
        Return the rotated the given bitboard value & the given mask by 90 degrees. Do this n times.
        
        Parameters:
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
        
        """
        Get the value of the bitboard.

        Returns:
            value (int): The value of the bitboard.
        """
        
        return self.__convertBitArrayToInt__(self.__bits__)
    
    @override
    def applyOr(self, value : int) -> None :
        
        """
        Apply a bitwise OR operation to the bitboard.
        
        Parameters:
            value (int): The value to apply the OR operation with.
            
        Returns:
            None
        """
        
        self.__bits__ |= self.__convertIntToBitArray__(value)
        
        return None
        
    @override
    def applyXor(self, value : int) -> None :
        
        """
        Apply a bitwise XOR operation to the bitboard.
        
        Parameters:
            value (int): The value to apply the XOR operation with.
            
        Returns:
            None
        """
        
        self.__bits__ ^= self.__convertIntToBitArray__(value)
        
        return None
    
    @override
    def applyAnd(self, value : int) -> None :
        
        """
        Apply a bitwise AND operation to the bitboard.
        
        Parameters:
            value (int): The value to apply the AND operation with.
            
        Returns:
            None
        """
        
        self.__bits__ &= self.__convertIntToBitArray__(value)
        
        return None

    @override
    @privatemethod
    def __hash__(self) -> int:
        
        """
        Hash the bitboard.
        
        Returns:
            hash (int): The hash of the bitboard.
        """

        normalHash : int = hash(self.__bits__.tobytes())
        rotated90Hash : int = hash(self.__getRotatedBitBoardBy90Degree__(1).tobytes())
        rotated180Hash : int = hash(self.__getRotatedBitBoardBy90Degree__(2).tobytes())
        rotated270Hash : int = hash(self.__getRotatedBitBoardBy90Degree__(3).tobytes())
        
        verticalyFlippedHash : int = hash(np.fliplr(self.__bits__).tobytes())
        horizontallyFlippedHash : int = hash(np.flipud(self.__bits__).tobytes())
        
        return normalHash + rotated90Hash + rotated180Hash + rotated270Hash + verticalyFlippedHash + horizontallyFlippedHash
