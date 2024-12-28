"""
Board Shape Module

This module provides a class to define and apply shapes to a game board.

Classes:
    BoardShape: Represents a shape that can be applied to a board.
    
    Methods:
        apply_shape(board: Board) -> None:
            Apply a specific shape to the given board.

            Args:
                board (Board): The board to which the shape will be applied.
            
            Returns:
                None
"""
# ---------------------------------------------------------------------------------------------------- #

## Implementation

# ---------------------------------------------------------------------------------------------------- #

# Imports #

from modules.models.board_components.board import Board

# ---------------------------------------------------------------------------------------------------- #

# Class #

class BoardShape:
    """
    Represents a shape that can be applied to a game board.
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the BoardShape class.
        
        Returns:
            None
        """
        return None

    def apply_shape(self, board: Board) -> None:
        """
        Apply a specific shape to the given board.

        Args:
            board (Board): The board to which the shape will be applied.

        Returns:
            None
        """
        pass
