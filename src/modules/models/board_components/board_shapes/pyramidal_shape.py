from modules.models.board_components.board_shape import BoardShape
from modules.models.board_components.board import Board

class PyramidalShape(BoardShape):
    
    def __init__(self) -> None:
        super()
        return None
    
    def apply_shape(self, board: Board) -> None:

        width = board.getWidth()
        height = board.getHeight()
        center_x = (width - 1) // 2

        for line in range(height):
            
            pyramid_width = line * ((width + 1) // 2) // height

            for column in range(width):
                
                if column < center_x - pyramid_width or column > center_x + pyramid_width + (1 if width % 2 == 0 else 0):
                    board.setIsCaseBlocked(line, column, True)
