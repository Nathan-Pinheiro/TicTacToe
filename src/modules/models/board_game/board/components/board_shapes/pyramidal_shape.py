from modules.models.board_game.board.components.board_shape import BoardShape
from modules.models.board_game.board.board import Board

# ************************************************
# Class PyramidalShape
# ************************************************
# ROLE : This class represent a pyramidal shape
# ************************************************
# VERSION : 1.0
# AUTHOR : Nathan PINHEIRO
# DATE : 13/01/2025
# ************************************************

class PyramidalShape(BoardShape):
    
    """
    Represents a pyramidal shape
    """
    
    def __init__(self) -> None:
        
        """
        Constructor of the class PyramidalShape

        Returns:
            None
        """
        
        # Call the parent constructor
        super()
        
        return None
    
    def applyShape(self, board: Board) -> bool:
        
        """
        Applies a pyramidal shape to the board, blocking cells outside the pyramid.
        
        Parameters:
            board (Board): The board to which the shape will be applied.
            
        Raises:
            TypeError: If board is not an instance of Board.
            
        Returns:
            bool: True if the pyramidal shape is applied.
        """
        
        # Check if the board is an instance of Board
        if not isinstance(board, Board):
            raise TypeError("board must be an instance of Board")

        # Define the center and the maximum distance from the center
        width : int = board.getWidth()
        height : int = board.getHeight()
        center_x : int = (width - 1) // 2

        # Block cells outside the pyramid
        for line in range(height):
            
            pyramid_width : int = line * ((width + 1) // 2) // height

            for column in range(width):
                
                if column < center_x - pyramid_width or column > center_x + pyramid_width + (1 if width % 2 == 0 else 0):
                    board.setIsCaseBlocked(line, column, True)
                    
        return True
