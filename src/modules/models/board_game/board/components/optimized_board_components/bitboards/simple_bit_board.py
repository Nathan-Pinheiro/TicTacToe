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
    
    def __init__(self, width : int, height : int) -> None:
        
        """
        Constructor for the SimpleBitBoard class.

        Args:
            width (int): The width of the board.
            height (int): The height of the board.
            
        Returns:
            None
        """

        super().__init__(width, height)

        self.__value__ : int = 0
        
        self.__generateBoardQuadrantMasks__()
    
    @privatemethod
    def __getBitPosition__(self, line: int, column: int) -> int:
        """Convert (row, col) to a bit index."""
        return line * self.__width__ + column

    @override
    def getValue(self) -> int :
        return self.__value__

    @override
    def applyOr(self, value : int) -> None :
        self.__value__ |= value
    
    @override
    def applyAnd(self, value : int) -> None :
        self.__value__ &= value

    @privatemethod
    @override
    def __hash__(self) -> int:
        return hash(self.__value__)