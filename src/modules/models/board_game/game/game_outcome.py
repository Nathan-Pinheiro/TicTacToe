from enum import Enum
from typing import Optional

# ************************************************
# CLASS GameOutcome and GameOutcomeStatus
# ************************************************
# ROLE : Those two classes are used to define a game outcome.
# ************************************************
# VERSION : 1.0
# AUTHOR : Nathan PINHEIRO
# DATE : 13/01/2025
# ************************************************

class GameOutcomeStatus(Enum):
    
    """
    An enumeration that describe the outcome status
    """

    UNFINISHED = 0
    DRAW = 1
    VICTORY = 2

class GameOutcome:
    
    """
    An enumeration that describe the game outcome
    """

    def __init__(self, state: GameOutcomeStatus, winner: Optional[int] = None):
        
        """
        Represents the result of a game.
        
        Parameters :        
            - state (GameState) : The current state of the game (UNFINISHED, DRAW, or VICTORY).
            - winner (int) : The ID of the winning player if applicable. None for UNFINISHED or DRAW.
        """
        
        self.__state__ = state
        self.__winner__ = winner

    def getGameStatus(self) -> GameOutcomeStatus:
        
        """
        Get the current state of the game.
        
        Returns :
            - GameOutcomeStatus : the outcome status of a game
        """
        
        return self.__state__

    def getWinner(self) -> Optional[int]:
        
        """
        Get the winner of the game, if applicable.
        
        Returns :
            - int (Optional) : the winner player index
        """
        
        return self.__winner__

    def __str__(self):

        """Returns the game outcome as a sentence"""

        match self.__state__ :
            case GameOutcomeStatus.UNFINISHED : return "Game is still ongoing."
            case GameOutcomeStatus.DRAW : return "The game ended in a draw."
            case GameOutcomeStatus.VICTORY : return f"Player {self.__winner__} won the game!"