from modules.models.board.board_shapes.board_shape import BoardShape
from modules.models.board.board import Board

class PyramidalShape(BoardShape):
    
    def __init__(self) -> None:
        super()
        return None
    
    def apply_shape(self, board : Board) -> None:

        pyramideSize : int = board.getWidth() // 2

        for line in range(0, pyramideSize):
            
            for column in range(0, pyramideSize - line):
                
                board.getCase(line, column).setIsBlocked(True)
                board.getCase(line, board.getWidth() - column - 1).setIsBlocked(True)