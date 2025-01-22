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

class NumpyBitBoard(BitBoard):
    
    """
    Represents a bitboard using numpy
    """

    def __init__(self, width: int, height: int) -> None:
        
        """
        Constructor for the NumpyBitBoard class.

        Parameters:
            width (int): The width of the board.
            height (int): The height of the board.
            
        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than or equal to 0.
            
        Returns:
            None
        """
        
        # Check if width and height are integers and greater than 0
        if not isinstance(width, int) or not isinstance(height, int):
            raise TypeError("width and height must be integers")
        
        if width <= 0 or height <= 0:
            raise ValueError("width and height must be greater than 0")

        # Call the parent constructor
        super().__init__(width, height)

        # Define the bits array
        self.__bits__: np.ndarray = np.zeros((height, width), dtype=int)
        
        # Generate the board quadrant masks
        self.__generateBoardQuadrantMasks__()
        
        return None
    
    @privatemethod
    def __getBitPosition__(self, line: int, column: int) -> int:
        
        """
        Convert (row, col) to a bit index.
        
        Parameters:
            line (int): The line of the bit.
            column (int): The column of the bit.
            
        Raises:
            TypeError: If line or column is not an integer.
            ValueError: If line or column is out of range.
            
        Returns:
            position (int): the position index of the bit
        """
        
        # Check if line and column are integers and within the board dimensions
        if not isinstance(line, int) or not isinstance(column, int):
            raise TypeError("line and column must be integers")
        
        if line < 0 or line >= self.__height__:
            raise ValueError(f"line must be between 0 and {self.__height__ - 1}")
        
        if column < 0 or column >= self.__width__:
            raise ValueError(f"column must be between 0 and {self.__width__ - 1}")
        
        return line * self.__width__ + column
    
    @privatemethod
    def __generateBoardQuadrantMasks__(self) -> bool:
        
        """
        This method allow initializing masks foreach part of board. (upper left, upper right, lower left, lower right).
        This will then be useful to hash the BitBoard, having a hash code that have the same hash for symmetrical boards.
        
        Returns:
            bool: True if the masks are generated successfully.
        """
        
        # Initialize the masks
        self.__upperLeftMask__: np.ndarray = np.zeros((self.__height__, self.__width__), dtype=int)
        self.__upperRightMask__: np.ndarray = np.zeros((self.__height__, self.__width__), dtype=int)
        self.__lowerLeftMask__: np.ndarray = np.zeros((self.__height__, self.__width__), dtype=int)
        self.__lowerRightMask__: np.ndarray = np.zeros((self.__height__, self.__width__), dtype=int)
        
        # Define the center of the board
        centerLine: float = (self.__height__ - 1) / 2
        centerColumn: float = (self.__width__ - 1) / 2

        # Generate the masks
        for line in range(0, self.__height__):
            for column in range(0, self.__width__):
                if line <= centerLine and column <= centerColumn:
                    self.__upperLeftMask__[line][column] = 1
                if line <= centerLine and column >= centerColumn:
                    self.__upperRightMask__[line][column] = 1
                if line >= centerLine and column <= centerColumn:
                    self.__lowerLeftMask__[line][column] = 1
                if line >= centerLine and column >= centerColumn:
                    self.__lowerRightMask__[line][column] = 1
                
        return True

    @privatemethod
    def __convertBitArrayToInt__(self, bitBoard: np.ndarray) -> int:
        
        """
        Convert a bit array to an integer.
        
        Parameters:
            bitBoard (np.ndarray): The bit array to convert.
            
        Raises:
            TypeError: If bitBoard is not a numpy ndarray.

        Returns:
            bitboard_int (int): The integer representation of the bit array.
        """
        
        # Check if bitBoard is a numpy ndarray
        if not isinstance(bitBoard, np.ndarray):
            raise TypeError("bitBoard must be a numpy ndarray")
        
        # Flatten the bit array and convert it to an integer
        flat_bitboard = bitBoard.ravel()
        bitboard_int = np.dot(flat_bitboard, 1 << np.arange(flat_bitboard.size))
        
        return bitboard_int
    
    @privatemethod
    def __convertIntToBitArray__(self, bitboard_int: int) -> np.ndarray:
        
        """
        Convert an integer to a bit array.
        
        Parameters:
            bitboard_int (int): The integer to convert.
            
        Raises:
            TypeError: If bitboard_int is not an integer.

        Returns:
            bitboard (np.ndarray): The bit array representation of the integer.
        """
        
        # Check if bitboard_int is an integer
        if not isinstance(bitboard_int, int):
            raise TypeError("bitboard_int must be an integer")
        
        # Create a bit array from the integer
        bitboard = np.zeros((self.__height__, self.__width__), dtype=int)
        
        for line in range(self.__height__):
            for column in range(self.__width__):
                bitboard[line][column] = 1 if 1 << line * self.__width__ + column & bitboard_int else 0
    
        return bitboard
    
    @privatemethod
    def __getRotatedBitBoardBy90Degree__(self, mask: np.ndarray = None, numberRotate: int = 1) -> np.ndarray:
        
        """
        Return the rotated the given bitboard value & the given mask by 90 degrees. Do this n times.
        
        Parameters:
            mask (np.ndarray): The mask.
            numberRotate (int): The amount of time it has to rotate by 90 degrees.
            
        Raises:
            TypeError: If mask is not a numpy ndarray or numberRotate is not an integer.

        Returns:
            bitboard (np.ndarray): The rotated bitboard.
        """
        
        # Check if mask is a numpy ndarray and numberRotate is an integer
        if mask is not None and not isinstance(mask, np.ndarray):
            raise TypeError("mask must be a numpy ndarray")
        
        if not isinstance(numberRotate, int):
            raise TypeError("numberRotate must be an integer")

        # Rotate the bitboard by 90 degrees n times
        bits: np.ndarray
        if mask is not None:
            bits = self.__bits__ & mask
        else:
            bits = self.__bits__

        return np.rot90(bits, k=numberRotate)

    @override
    def getValue(self) -> int:
        
        """
        Get the value of the bitboard.

        Returns:
            value (int): The value of the bitboard.
        """
        
        return self.__convertBitArrayToInt__(self.__bits__)
    
    @override
    def applyOr(self, value: int) -> bool:
        
        """
        Apply a bitwise OR operation to the bitboard.
        
        Parameters:
            value (int): The value to apply the OR operation with.
            
        Raises:
            TypeError: If value is not an integer.

        Returns:
            bool: True if the operation is applied successfully.
        """
        
        # Check if value is an integer
        if not isinstance(value, int):
            raise TypeError("value must be an integer")
        
        # Apply the OR operation
        self.__bits__ |= self.__convertIntToBitArray__(value)
        
        return True
        
    @override
    def applyXor(self, value: int) -> bool:
        
        """
        Apply a bitwise XOR operation to the bitboard.
        
        Parameters:
            value (int): The value to apply the XOR operation with.
            
        Raises:
            TypeError: If value is not an integer.

        Returns:
            bool: True if the operation is applied successfully.
        """
        
        # Check if value is an integer
        if not isinstance(value, int):
            raise TypeError("value must be an integer")
        
        # Apply the XOR operation
        self.__bits__ ^= self.__convertIntToBitArray__(value)
        
        return True
    
    @override
    def applyAnd(self, value: int) -> bool:
        
        """
        Apply a bitwise AND operation to the bitboard.
        
        Parameters:
            value (int): The value to apply the AND operation with.
            
        Raises:
            TypeError: If value is not an integer.

        Returns:
            bool: True if the operation is applied successfully.
        """
        
        # Check if value is an integer
        if not isinstance(value, int):
            raise TypeError("value must be an integer")
        
        # Apply the AND operation
        self.__bits__ &= self.__convertIntToBitArray__(value)
        
        return True

    @override
    @privatemethod
    def __hash__(self) -> int:
        
        """
        Hash the bitboard.
        
        Returns:
            hash (int): The hash of the bitboard.
        """

        # Get the hash of the bitboard and its symmetrical boards
        normalHash: int = hash(self.__bits__.tobytes())
        rotated90Hash: int = hash(self.__getRotatedBitBoardBy90Degree__(1).tobytes())
        rotated180Hash: int = hash(self.__getRotatedBitBoardBy90Degree__(2).tobytes())
        rotated270Hash: int = hash(self.__getRotatedBitBoardBy90Degree__(3).tobytes())
        
        # Get the hash of the vertically and horizontally flipped boards
        verticallyFlippedHash: int = hash(np.fliplr(self.__bits__).tobytes())
        horizontallyFlippedHash: int = hash(np.flipud(self.__bits__).tobytes())
        
        return normalHash + rotated90Hash + rotated180Hash + rotated270Hash + verticallyFlippedHash + horizontallyFlippedHash
