from modules.models.board_components.board_shape import BoardShape
from modules.models.board_components.board import Board

class DiamondShape(BoardShape):
    
    def __init__(self) -> None:
        super()
        return None
    
    def apply_shape(self, board: Board) -> None:

        from modules.models.board_components.board_shape import BoardShape
from modules.models.board_components.board import Board

class DiamondShape(BoardShape):
    
    def __init__(self) -> None:
        super()
        return None
    
    def apply_shape(self, board: Board) -> None:
        """
        Applies a diamond shape to the board, blocking cells outside the diamond.
        
        Args:
            board (Board): The board to which the shape will be applied.

        Returns:
            None
        """
        center_x = (board.getWidth() - 1) / 2
        center_y = (board.getHeight() - 1) / 2
        max_distance_x = center_x + 1
        max_distance_y = center_y + 1

        for line in range(board.getHeight()):
            for column in range(board.getWidth()):
                
                scaled_x = abs(column - center_x) / max_distance_x
                scaled_y = abs(line - center_y) / max_distance_y
                if scaled_x + scaled_y >= 1:
                    board.setIsCaseBlocked(line, column, True)

