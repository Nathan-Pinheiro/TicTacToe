from modules.utils.decorator import privatemethod
from abc import ABC, abstractmethod

# ************************************************
# Class BitBoard
# ************************************************
# ROLE : This module is representing bitboard
# ************************************************
# VERSION : 1.0
# AUTHOR : Nathan PINHEIRO
# DATE : 13/01/2025
# ************************************************

class BitBoard(ABC) :
    
    """
    Represents a bitboard
    """
    
    def __init__(self, width : int, height : int) -> None:
        
        """
        Initializes a new instance of the BitBoard class.

        Parameters:
            width (int): The width of the board.
            height (int): The height of the board.
            
        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than or equal to 0.
        
        Returns:
            None
        """
        
        if not isinstance(width, int) or not isinstance(height, int):
            raise TypeError("width and height must be integers")
        
        if width <= 0 or height <= 0:
            raise ValueError("width and height must be greater than 0")
        
        if (width * height) > 64:
            raise ValueError("width * height must be less than or equal to 64")
        
        self.__width__ = width
        self.__height__ = height
        
        return None
    
    @abstractmethod
    def getValue(self) -> int:
        
        """
        Get the value of the bitboard.

        Returns:
            value (int): The value of the bitboard.
        """

        pass
    
    @abstractmethod
    def applyOr(self, value : int) -> bool:

        """
        Apply a bitwise OR operation to the bitboard.
        
        Parameters:
            value (int): The value to apply the OR operation with.
            
        Raises:
            TypeError: If value is not an integer.

        Returns:
            bool: True if the operation is applied successfully.
        """

        pass
    
    @abstractmethod
    def applyXor(self, value : int) -> bool:

        """
        Apply a bitwise XOR operation to the bitboard.
        
        Parameters:
            value (int): The value to apply the XOR operation with.
            
        Raises:
            TypeError: If value is not an integer.

        Returns:
            bool: True if the operation is applied successfully.
        """

        pass

    @abstractmethod
    def applyAnd(self, value : int) -> bool:

        """
        Apply a bitwise AND operation to the bitboard.
        
        Parameters:
            value (int): The value to apply the AND operation with.
            
        Raises:
            TypeError: If value is not an integer.

        Returns:
            bool: True if the operation is applied successfully.
        """

        pass
    
    @abstractmethod
    @privatemethod
    def __hash__(self) -> int:

        """
        Get the hash of the bitboard.
        
        Returns:
            hash (int): The hash of the bitboard.
        """

        pass