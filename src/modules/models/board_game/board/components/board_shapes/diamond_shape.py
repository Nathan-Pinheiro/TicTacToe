from modules.models.board_game.board.components.board_shape import BoardShape
from modules.models.board_game.board.board import Board

# ************************************************
# Class PyramidalShape
# ************************************************
# ROLE : This class represent a diamond shape
# ************************************************
# VERSION : 1.0
# AUTHOR : Nathan PINHEIRO
# DATE : 13/01/2025
# ************************************************

class DiamondShape(BoardShape):
    
    """
    Represents a diamond shape
    """
    
    def __init__(self) -> None:
        
        """
        Constructor of the class DiamondShape
        
        Returns:
            None
        """
        
        # Call the parent constructor
        super()
        
        return None
    
    def applyShape(self, board: Board) -> bool:
        
        """
        Applies a diamond shape to the board, blocking cells outside the diamond.
        
        Parameters:
            board (Board): The board to which the shape will be applied.
            
        Raises:
            TypeError: If board is not an instance of Board.

        Returns:
            bool: True if the diamond shape is applied.
        """
        
        # Check if the board is an instance of Board
        if not isinstance(board, Board):
            raise TypeError("board must be an instance of Board")
        
        # Define the center and the maximum distance from the center
        center_x = (board.getWidth() - 1) / 2
        center_y = (board.getHeight() - 1) / 2
        max_distance_x = center_x + 1
        max_distance_y = center_y + 1

        # Block cells outside the diamond
        for line in range(board.getHeight()):
            for column in range(board.getWidth()):
                
                scaled_x = abs(column - center_x) / max_distance_x
                scaled_y = abs(line - center_y) / max_distance_y
                if scaled_x + scaled_y >= 1:
                    board.setIsCaseBlocked(line, column, True)
                    
        return True

