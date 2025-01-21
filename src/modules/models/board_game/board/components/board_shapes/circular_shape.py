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
    
    def __init__(self) -> None:
        super()
        return None
    
    def applyShape(self, board : Board) -> None:

        center_x = (board.getWidth() - 1) / 2
        center_y = (board.getHeight() - 1) / 2
        radius_x = (board.getWidth() - 0.9) / 2
        radius_y = (board.getWidth() - 0.9) / 2

        for line in range(board.getHeight()):
            for column in range(board.getWidth()):
                
                normalized_x = (column - center_x) / radius_x
                normalized_y = (line - center_y) / radius_y
                distance = math.sqrt(normalized_x ** 2 + normalized_y ** 2)
                if distance > 1: board.setIsCaseBlocked(line, column, True)