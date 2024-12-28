from modules.models.tic_tac_toe.move import Move
from modules.models.board_components.coordinate import Coordinate
from modules.models.board_components.board import Board
from modules.models.tic_tac_toe.move import Move
from modules.models.tic_tac_toe.power_up import PowerUp
from modules.models.board_components.entity import Entity

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