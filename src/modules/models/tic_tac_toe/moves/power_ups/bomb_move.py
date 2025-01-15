from modules.models.tic_tac_toe.moves.power_up_move import PowerUpMove
from modules.models.board_game.components.coordinate import Coordinate
from modules.models.board_game.board.board import Board

class BombMove(PowerUpMove):
    
    def __init__(self, coordinate : Coordinate) -> None:
        super().__init__("b", coordinate)
    
    def play(self, board : Board, playerIndex : int) -> None :
        
        line : int = self.__coordinate__.getLine()
        column : int = self.__coordinate__.getColumn()

        if(line < 0 or line > board.getHeight()) : return False
        if(column < 0 or column > board.getWidth()) : return False

        for currentLine in range(line - 1, line + 2):
            for currentColumn in range(column - 1, column + 2):
                if(0 <= currentLine < board.getHeight() and 0 <= currentColumn < board.getWidth()):
                    
                    board.removeEntityAt(currentLine, currentColumn)
                    board.setIsCaseBlocked(currentLine, currentColumn, False)

    def undo(self, board : Board, playerIndex : int) -> None:
        return
        
    @classmethod
    def canPlay(cls, board : Board, line : int, column : int) -> bool:
        
        if(line < 0 or line > board.getHeight()) : return False
        if(column < 0 or column > board.getWidth()) : return False
        
        return True
    
    def __str__(self):
        return super().__str__()