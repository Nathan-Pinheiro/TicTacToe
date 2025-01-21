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
            
        Returns:
            None
        """
        
        super().__init__(name)
        
        return None
    
    def get_choice(self, gameState: TicTacToeGameState) -> Move:
        
        """
        Selects the best move for the current game state based on the scores 
        calculated by the game analyzer, using the softmax function to convert 
        the scores to probabilities.

        Parameters:
            gameState (TicTacToeGameState): The current state of the Tic-Tac-Toe game.

        Returns:
            Move: The move that the AI will make.
        """

        return self.__game_analyser__.getBestMove(gameState)