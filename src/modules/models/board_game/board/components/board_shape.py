from modules.models.board_game.board.board import Board
from abc import ABC, abstractmethod

# ************************************************
# Class BoardShape
# ************************************************
# ROLE : This module representing a generic shape
# ************************************************
# VERSION : 1.0
# AUTHOR : Nathan PINHEIRO
# DATE : 13/01/2025
# ************************************************

class BoardShape(ABC):
    
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

    @abstractmethod
    def applyShape(self, board: Board) -> None:
        """
        Apply a specific shape to the given board.

        Args:
            board (Board): The board to which the shape will be applied.

        Returns:
            None
        """
        pass
