from modules.models.board_game.components.move import Move
from modules.models.board_game.components.coordinate import Coordinate
from modules.models.board_game.board.board import Board

class PowerUpMove(Move):
    
    def __init__(self, moveCode : str, coordinate : Coordinate) -> None:
        
        super().__init__(moveCode, coordinate)

        return None
    
    def play(self, board : Board, playerIndex : int) -> None :
        pass
        
    @classmethod
    def canPlay(cls, board : Board, line : int, column : int) -> bool:
        pass
    
    def __str__(self):
        return super().__str__()