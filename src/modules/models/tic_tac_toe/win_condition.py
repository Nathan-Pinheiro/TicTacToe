from modules.models.board_components.board import Board
from modules.models.tic_tac_toe.game_outcome import GameOutcome

class WinCondition :
    
    def __init__(self) -> None:
        return None
    
    def checkWin(self, board : Board) -> GameOutcome :
        pass
    
    def checkWinForPlayer(self, playerIndex : int, board : Board) -> GameOutcome:
        pass
    
    def evaluateForPlayer(self, playerIndex : int, board : Board) -> int:
        pass