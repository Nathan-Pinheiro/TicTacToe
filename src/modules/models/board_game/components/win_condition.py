from modules.models.board_game.board.board import Board
from modules.models.board_game.game.game_outcome import GameOutcome
from abc import ABC, abstractmethod

# ************************************************
# CLASS WinCondition
# ************************************************
# ROLE : This abstract class is used to represent a win condition
# ************************************************
# VERSION : 1.0
# AUTHOR : Nathan PINHEIRO
# DATE : 13/01/2025
# ************************************************

class WinCondition(ABC) :
    
    """
    A class that represent a generic win condition
    """

    def __init__(self) -> None:
        return None
    
    @abstractmethod
    def checkWin(self, board : Board) -> GameOutcome :
        pass
    
    @abstractmethod
    def checkWinForPlayer(self, playerIndex : int, board : Board) -> GameOutcome:
        pass
    
    @abstractmethod
    def evaluateForPlayer(self, playerIndex : int, board : Board) -> int:
        pass