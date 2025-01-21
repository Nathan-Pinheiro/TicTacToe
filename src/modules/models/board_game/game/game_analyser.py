from modules.models.board_game.components.move import Move
from modules.models.board_game.game.game_state import GameState
from abc import ABC, abstractmethod

# ************************************************
# CLASS GameAnalyser
# ************************************************
# ROLE : Define a generic analyser class
# ************************************************
# VERSION : 1.0
# AUTHOR : Nathan PINHEIRO
# DATE : 10/01/2025
# ************************************************

class GameAnalyser(ABC):

    """
    A generic abstract class for analyzing game states and moves. 
    Subclasses are expected to provide specific implementations 
    for analyzing moves and determining the best move for a particular game.
    """    

    def __init__(self, depth : int, isDebugOn : bool = False):
        
        """
        Initializes a new GameAnalyser instance.
        
        Parameters:
            depth (int): The depth of analysis (e.g., search depth).
            isDebugOn (bool): Optional flag to enable debugging output (default is False).
            
        Returns:
            None
        """

        self.__depth__ : bool = depth
        self.__isDebugOn__ : bool = isDebugOn
        
        return None
        
    @abstractmethod
    def getMovesScores(self, gameState : GameState) -> dict[Move, int] :
        
        """
        Abstract method to get a dictionary of moves and their respective scores.
        
        Parameters:
            gameState (GameState): The current state of the game.

        Returns:
            dict[Move, int]: A dictionary where keys are Move objects and values are their corresponding evaluation scores.
        """

        pass
    
    @abstractmethod
    def getBestMove(self, gameState : GameState) -> Move :
        
        """
        Abstract method to get the best move based on the analysis.
        
        Parameters:
            gameState (GameState): The current state of the game.

        Returns:
            Move: The best move according to the evaluation.
        """

        pass
