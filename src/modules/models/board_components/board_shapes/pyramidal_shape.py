from modules.models.board_components.board_shapes.board_shape import BoardShape
from modules.models.board_components.boards.simple_board import SimpleBoard

class PyramidalShape(BoardShape):
    
    def __init__(self) -> None:
        super()
        return None
    
    def apply_shape(self, board : SimpleBoard) -> None:

        pyramideSize : int = board.getWidth() // 2

        for line in range(0, pyramideSize):
            
            for column in range(0, pyramideSize - line):
                
                board.setIsCaseBlocked(line, column, True)
                board.setIsCaseBlocked(line, board.getWidth() - column - 1, True)