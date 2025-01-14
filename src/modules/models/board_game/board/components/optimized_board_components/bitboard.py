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
    
    def __init__(self, width : int, height : int) -> None:
        
        """
        Constructor for the Board class.

        Args:
            width (int): The width of the board.
            height (int): The height of the board.
            
        Returns:
            None
        """
        
        assert(width * height <= 64)
        
        self.__width__ = width
        self.__height__ = height
    
    @abstractmethod
    def getValue(self) -> int :

        """
        R
        """

        pass
    
    @abstractmethod
    def applyOr(self, value : int) -> None :

        """
        Apply OR bitwise operation to the bitboard with a int mask
        """

        pass
    
    @abstractmethod
    def applyAnd(self, value : int) -> None :

        """
        Apply AND bitwise operation to the bitboard with a int mask
        """

        pass
    
    @abstractmethod
    @privatemethod
    def __hash__(self) -> int:

        """
        Generate a hash of the current board

        Returns:
            int : A hash of the current bit board.
        """

        pass