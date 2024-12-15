from enum import Enum
from typing import Optional
from modules.models.entities.entity import Entity

class GameStatus(Enum):
    
    UNFINISHED = 0
    DRAW = 1
    VICTORY = 2

class GameState:
    
    def __init__(self, state: GameStatus, winner: Optional[Entity] = None):
        """
        Represents the result of a game.
        
        :param state: The current state of the game (UNFINISHED, DRAW, or VICTORY).
        :param winner: The ID of the winning player if applicable. None for UNFINISHED or DRAW.
        """
        
        self.__state__ = state
        self.__winner__ = winner

from enum import Enum
from typing import Optional
from modules.models.entities.entity import Entity

class GameStatus(Enum):
    UNFINISHED = 0
    DRAW = 1
    VICTORY = 2

class GameState:
    
    def __init__(self, state: GameStatus, winner: Optional[Entity] = None):
        """
        Represents the result of a game.
        
        :param state: The current state of the game (UNFINISHED, DRAW, or VICTORY).
        :param winner: The ID of the winning player if applicable. None for UNFINISHED or DRAW.
        """
        
        self.__state__ = state
        self.__winner__ = winner

    def getGameStatus(self) -> GameStatus:
        """Get the current state of the game."""
        return self.__state__

    def getWinner(self) -> Optional[Entity]:
        """Get the winner of the game, if applicable."""
        return self.__winner__

    def __str__(self):

        match self.__state__ :
            case GameStatus.UNFINISHED : return "Game is still ongoing."
            case GameStatus.DRAW : return "The game ended in a draw."
            case GameStatus.VICTORY : return f"Player {self.__winner__} won the game!"