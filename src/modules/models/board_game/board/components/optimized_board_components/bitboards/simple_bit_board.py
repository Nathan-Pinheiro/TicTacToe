from modules.utils.decorator import privatemethod, override
from modules.models.board_game.board.components.optimized_board_components.bitboard import BitBoard

# ************************************************
# Class SimpleBitBoard
# ************************************************
# ROLE : This module is representing bitboard
# ************************************************
# VERSION : 1.0
# AUTHOR : Nathan PINHEIRO
# DATE : 13/01/2025
# ************************************************

class SimpleBitBoard(BitBoard) :
    
    """
    Represents a simple bitboard
    """
    
    def __init__(self, width : int, height : int) -> None:
        
        """
        Constructor for the SimpleBitBoard class.

        Parameters:
            width (int): The width of the board.
            height (int): The height of the board.
            
        Returns:
            None
        """

        super().__init__(width, height)

        self.__value__ : int = 0
        
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

    @override
    def getValue(self) -> int :
        
        """
        Get the value of the bitboard
        
        Returns:
            value (int): The value of the bitboard
        """
        
        return self.__value__

    @override
    def applyOr(self, value : int) -> None :
        
        """
        Apply a bitwise OR operation to the bitboard
        
        Parameters:
            value (int): The value to apply the OR operation with
            
        Returns:
            None
        """
        
        self.__value__ |= value
        
        return None
    
    @override
    def applyAnd(self, value : int) -> None :
        
        """
        Apply a bitwise AND operation to the bitboard
        
        Parameters:
            value (int): The value to apply the AND operation with
            
        Returns:
            None
        """
        
        self.__value__ &= value
        
        return None 

    @privatemethod
    @override
    def __hash__(self) -> int:
        
        """
        Get the hash of the bitboard
        
        Returns:
            hash (int): The hash of the bitboard
        """
        
        return hash(self.__value__)