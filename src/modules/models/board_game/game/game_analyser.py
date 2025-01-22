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

    def __init__(self, depth : int, isDebugOn : bool = False) -> None:
        
        """
        Initializes a new GameAnalyser instance.
        
        Parameters:
            depth (int): The depth of analysis (e.g., search depth).
            isDebugOn (bool): Optional flag to enable debugging output (default is False).
            
        Raises:
            ValueError: If depth is not a non-negative integer.
            ValueError: If isDebugOn is not a boolean value.
            
        Returns:
            None
        """
        
        # Check if depth is a positive integer
        if not isinstance(depth, int) or depth < 0:
            raise ValueError("depth must be a non-negative integer")
        
        # Check if isDebugOn is a boolean value
        if not isinstance(isDebugOn, bool):
            raise ValueError("isDebugOn must be a boolean value")

        # Define the depth and isDebugOn attributes
        self.__depth__ : bool = depth
        self.__isDebugOn__ : bool = isDebugOn
        
        return None
        
    @abstractmethod
    def getMovesScores(self, gameState : GameState) -> dict[Move, int] :
        
        """
        Abstract method to get a dictionary of moves and their respective scores.
        
        Parameters:
            gameState (GameState): The current state of the game.
            
        Raises:
            TypeError: If gameState is not a GameState instance.

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
            
        Raises:
            TypeError: If gameState is not a GameState instance.

        Returns:
            Move: The best move according to the evaluation.
        """

        pass
