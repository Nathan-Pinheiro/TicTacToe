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

class HardAIPlayer(AIPlayer):
    
    """
    A simple AI player for Tic-Tac-Toe that selects its move based on the scores 
    given by a game analyzer, using the softmax function to calculate probabilities.
    """
    
    def __init__(self, name="Hard AI") -> None:
        
        """
        Initializes the EasyAI player with a name and links to a game analyser.
        
        Args:
            name (str): The name of the player.
        """
        
        super().__init__(name)
        
        self.__strength__ : int = 5
    
    def get_choice(self, gameState: TicTacToeGameState) -> Move:
        
        """
        Selects the best move for the current game state based on the scores 
        calculated by the game analyzer, using the softmax function to convert 
        the scores to probabilities.

        Args:
            gameState (TicTacToeGameState): The current state of the Tic-Tac-Toe game.

        Returns:
            Move: The move that the AI will make.
        """
        
        moveScores : dict[Move, int] = self.__game_analyser__.getMovesScores(gameState)

        if not moveScores : raise ValueError("Can't play as there is no moves to play")

        for _ , score in moveScores.items() : score = score ** self.__strength__

        moveProbabilities = self.__softmax(list(moveScores.values()))
        selectedMove = self.__select_move_based_on_probability(dict(zip(moveScores.keys(), moveProbabilities)))

        return selectedMove

    def __softmax(self, scores: list[int]) -> list[float]:
        
        """
        Applies the softmax function to a list of scores, transforming them into probabilities.
        
        Args:
            scores (list[int]): A list of raw scores (logits).
        
        Returns:
            list[float]: A list of probabilities corresponding to each score.
        """
        
        scores = np.array(scores)
        exp_scores = np.exp(scores - np.max(scores))
        return exp_scores / exp_scores.sum()

    def __select_move_based_on_probability(self, moveProbabilities: dict[Move, float]) -> Move:
        
        """
        Selects a move based on the probabilities of each move being chosen.
        
        Args:
            moveProbabilities (dict[Move, float]): A dictionary mapping moves to their probabilities.
        
        Returns:
            Move: The selected move based on the probabilities.
        """
        
        return random.choices(list(moveProbabilities.keys()), weights = moveProbabilities.values(), k = 1)[0]
