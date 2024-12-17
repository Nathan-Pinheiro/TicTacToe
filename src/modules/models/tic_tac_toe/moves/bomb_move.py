from modules.models.tic_tac_toe.move import Move
from modules.models.board_components.coordinate import Coordinate
from modules.models.board_components.board import Board
from modules.models.tic_tac_toe.moves.power_up_move import PowerUpMove
from modules.models.board_components.entity import Entity
import os

class BombMove(PowerUpMove):
    
    def __init__(self, coordinate : Coordinate, entity : Entity) -> None:
        
        super().__init__("b", coordinate, entity)

        return None
    
    def play(self, board : Board) -> None :
        
        line : int = self.__coordinate__.getLine()
        column : int = self.__coordinate__.getColumn()

        if(line < 0 or line > board.getHeight()) : return False
        if(column < 0 or column > board.getWidth()) : return False

        for currentLine in range(line - 1, line + 2):
            for currentColumn in range(column - 1, column + 2):
                if(0 <= currentLine < board.getHeight() and 0 <= currentColumn < board.getWidth()):
                    board.setEntityAt(currentLine, currentColumn, None)
                    board.setIsCaseBlocked(currentLine, currentColumn, False)

        return None
        
    @classmethod
    def canPlay(cls, board : Board, line : int, column : int) -> bool:
        
        if(line < 0 or line > board.getHeight()) : return False
        if(column < 0 or column > board.getWidth()) : return False
        
        return True