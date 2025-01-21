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
    
    def __init__(self) -> None:
        super()
        return None
    
    def applyShape(self, board: Board) -> None:

        width : int = board.getWidth()
        height : int = board.getHeight()
        center_x : int = (width - 1) // 2

        for line in range(height):
            
            pyramid_width : int = line * ((width + 1) // 2) // height

            for column in range(width):
                
                if column < center_x - pyramid_width or column > center_x + pyramid_width + (1 if width % 2 == 0 else 0):
                    board.setIsCaseBlocked(line, column, True)
