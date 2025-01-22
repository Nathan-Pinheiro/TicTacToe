from modules.models.board_game.board.components.board_shape import BoardShape
from modules.models.board_game.board.board import Board

import math

# ************************************************
# Class CircularShape
# ************************************************
# ROLE : This class represent a circular shape
# ************************************************
# VERSION : 1.0
# AUTHOR : Nathan PINHEIRO
# DATE : 13/01/2025
# ************************************************

class CircularShape(BoardShape):
    
    """
    Represents a circular shape
    """
    
    def __init__(self) -> None:
        
        """
        Constructor of the class CircularShape

        Returns:
            None
        """
        
        # Call the parent constructor
        super()
        
        return None
    
    def applyShape(self, board : Board) -> bool:
        
        """
        Apply the circular shape to the board
        
        Parameters:
            board (Board): The board to apply the shape to
            
        Raises:
            TypeError: If board is not an instance of Board
        
        Returns:
            bool: True if the circular shape is applied.
        """
        
        # Check if the board is an instance of Board
        if not isinstance(board, Board):
            raise TypeError("board must be an instance of Board")

        # Define the center and the radius of the circle
        center_x = (board.getWidth() - 1) / 2
        center_y = (board.getHeight() - 1) / 2
        radius_x = (board.getWidth() - 0.9) / 2
        radius_y = (board.getWidth() - 0.9) / 2

        # Block cells outside the circle
        for line in range(board.getHeight()):
            for column in range(board.getWidth()):
                
                normalized_x = (column - center_x) / radius_x
                normalized_y = (line - center_y) / radius_y
                distance = math.sqrt(normalized_x ** 2 + normalized_y ** 2)
                if distance > 1: board.setIsCaseBlocked(line, column, True)
                
        return True