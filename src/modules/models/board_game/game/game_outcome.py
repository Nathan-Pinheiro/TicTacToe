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
    
    Values:
        UNFINISHED (int): The game is still ongoing. (0)
        DRAW (int): The game ended in a draw. (1)
        VICTORY (int): A player has won the game. (2)
    """

    UNFINISHED = 0
    DRAW = 1
    VICTORY = 2

class GameOutcome:
    
    """
    Represents the result of a game.
    """

    def __init__(self, state: GameOutcomeStatus, winner: Optional[int] = None):
        
        """
        Constructor for the GameOutcome class.
        
        Parameters :        
            state (GameState) : The current state of the game (UNFINISHED, DRAW, or VICTORY).
            winner (int) : The ID of the winning player if applicable. None for UNFINISHED or DRAW.
            
        Raises :
            ValueError : If state is not a GameOutcomeStatus enum value.
            ValueError : If winner is not an integer value.
            
        Returns :
            None
        """
        
        # Check if state is a GameOutcomeStatus enum value
        if not isinstance(state, GameOutcomeStatus): 
            raise ValueError("state must be a GameOutcomeStatus enum value")
        
        # Check if winner is an integer value
        if winner is not None and not isinstance(winner, int):
            raise ValueError("winner must be an integer value")
        
        # Define the state and winner attributes
        self.__state__ = state
        self.__winner__ = winner
        
        return None

    def getGameStatus(self) -> GameOutcomeStatus:
        
        """
        Get the current state of the game.
        
        Returns :
            GameOutcomeStatus : the outcome status of a game
        """
        
        return self.__state__

    def getWinner(self) -> Optional[int]:
        
        """
        Get the winner of the game, if applicable.
        
        Returns :
            int (Optional) : the winner player index
        """
        
        return self.__winner__

    def __str__(self) -> str:

        """
        Returns the game outcome as a sentence
        
        Returns :
            str : The game outcome as a sentence
        """

        match self.__state__ :
            case GameOutcomeStatus.UNFINISHED : return "Game is still ongoing."
            case GameOutcomeStatus.DRAW : return "The game ended in a draw."
            case GameOutcomeStatus.VICTORY : return f"Player {self.__winner__} won the game!"