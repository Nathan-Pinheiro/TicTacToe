from modules.models.tic_tac_toe.players.ai_player import AIPlayer
from modules.models.tic_tac_toe.tic_tac_toe_game_state import TicTacToeGameState
from modules.models.board_game.components.move import Move

import numpy as np
import random

# ************************************************
# CLASS HardAIPlayer
# ************************************************
# ROLE : The goal of this class is to represent an AI player that as an hard level
# ************************************************
# VERSION : 1.0
# AUTHOR : Nathan PINHEIRO
# DATE : 10/01/2025
# ************************************************

class ImpossibleAIPlayer(AIPlayer):
    
    """
    A simple AI player for Tic-Tac-Toe that selects its move based on the scores 
    given by a game analyzer, using the softmax function to calculate probabilities.
    """
    
    def __init__(self, name="Hard AI") -> None:
        
        """
        Initializes the EasyAI player with a name and links to a game analyser.
        
        Parameters:
            name (str): The name of the player.
            
        Raises:
            ValueError: If the name is not a string.
            
        Returns:
            None
        """
        
        # Check if the name is a string
        if not isinstance(name, str):
            raise ValueError("The name must be a string.")
        
        # Call the parent constructor
        super().__init__(name)
        
        return None
    
    def getChoice(self, gameState: TicTacToeGameState) -> Move:
        
        """
        Selects the best move for the current game state based on the scores 
        calculated by the game analyzer, using the softmax function to convert 
        the scores to probabilities.

        Parameters:
            gameState (TicTacToeGameState): The current state of the Tic-Tac-Toe game.
            
        Raises:
            ValueError: If the game state is not a TicTacToeGameState object.

        Returns:
            Move: The move that the AI will make.
        """
        
        # Check if the game state is a TicTacToeGameState instance
        if not isinstance(gameState, TicTacToeGameState):
            raise ValueError("The game state must be a TicTacToeGameState instance.")

        return self.__gameAnalyser__.getBestMove(gameState)