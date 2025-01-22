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

class SimpleBitBoard(BitBoard):
    
    """
    Represents a simple bitboard
    """
    
    def __init__(self, width: int, height: int) -> None:
        
        """
        Constructor for the SimpleBitBoard class.

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

        # Initialize the bitboard value
        self.__value__: int = 0
        
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

    @override
    def getValue(self) -> int:
        
        """
        Get the value of the bitboard
        
        Returns:
            value (int): The value of the bitboard
        """
        
        return self.__value__

    @override
    def applyOr(self, value: int) -> bool:
        
        """
        Apply a bitwise OR operation to the bitboard
        
        Parameters:
            value (int): The value to apply the OR operation with
            
        Raises:
            TypeError: If value is not an integer.
            
        Returns:
            bool: True if the operation is applied successfully.
        """
        
        # Check if value is an integer
        if not isinstance(value, int):
            raise TypeError("value must be an integer")
        
        # Apply the OR operation
        self.__value__ |= value
        
        return True
    
    @override
    def applyAnd(self, value: int) -> bool:
        
        """
        Apply a bitwise AND operation to the bitboard
        
        Parameters:
            value (int): The value to apply the AND operation with
            
        Raises:
            TypeError: If value is not an integer.
            
        Returns:
            bool: True if the operation is applied successfully.
        """
        
        # Check if value is an integer
        if not isinstance(value, int):
            raise TypeError("value must be an integer")
        
        # Apply the AND operation
        self.__value__ &= value
        
        return True 

    @override
    @privatemethod
    def __hash__(self) -> int:
        
        """
        Get the hash of the bitboard
        
        Returns:
            hash (int): The hash of the bitboard
        """
        
        return hash(self.__value__)