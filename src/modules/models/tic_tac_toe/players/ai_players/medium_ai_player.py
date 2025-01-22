from modules.models.tic_tac_toe.players.ai_player import AIPlayer
from modules.models.tic_tac_toe.tic_tac_toe_game_state import TicTacToeGameState
from modules.models.board_game.components.move import Move

from modules.utils.decorator import override

import numpy as np
import random

# ************************************************
# CLASS EasyAI
# ************************************************
# ROLE : The goal of this class is to represent an AI player that as an medium level
# ************************************************
# VERSION : 1.0
# AUTHOR : Nathan PINHEIRO
# DATE : 10/01/2025
# ************************************************

class MediumAIPlayer(AIPlayer):
    
    """
    A simple AI player for Tic-Tac-Toe that selects its move based on the scores 
    given by a game analyzer, using the softmax function to calculate probabilities.
    """
    
    def __init__(self, name="Medium AI") -> None:
        
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
        
        # Initialize the strength of the AI
        self.__strength__ : int = 2
        
        return None
    
    @override
    def getChoice(self, gameState: TicTacToeGameState) -> Move:
        
        """
        Selects the best move for the current game state based on the scores 
        calculated by the game analyzer, using the softmax function to convert 
        the scores to probabilities.

        Parameters:
            gameState (TicTacToeGameState): The current state of the Tic-Tac-Toe game.
            
        Raises:
            ValueError: If the game state is not a TicTacToeGameState object.
            ValueError: Can't play as there is no moves to play

        Returns:
            Move: The move that the AI will make.
        """
        
        # Check if the game state is a TicTacToeGameState instance
        if not isinstance(gameState, TicTacToeGameState):
            raise TypeError("The game state must be a TicTacToeGameState instance.")

        # Get the scores of the moves
        moveScores : dict[Move, int] = self.__gameAnalyser__.getMovesScores(gameState)

        # Check if there are moves to play
        if not moveScores : raise ValueError("Can't play as there is no moves to play")

        # Strengthen the scores
        for move, score in moveScores.items(): moveScores[move] = score ** self.__strength__

        # Get the probabilities of each move
        moveProbabilities = self.__softmax__(list(moveScores.values()))

        # Select the move based on the probabilities
        selectedMove = self.__selectMoveBasedOnProbability__(dict(zip(moveScores.keys(), moveProbabilities)))

        return selectedMove

    def __softmax__(self, scores: list[int | float]) -> list[float]:
        
        """
        Applies the softmax function to a list of scores, transforming them into probabilities.
        
        Parameters:
            scores (list[int]): A list of raw scores (logits).
            
        Raises:
            ValueError: If the scores are not a list of integers or floats.
        
        Returns:
            list[float]: A list of probabilities corresponding to each score.
        """
        
        # Check if the scores are a list of integers
        if not all(isinstance(score, (int, float)) for score in scores):
            raise ValueError("The scores must be a list of integers.")
        
        # Set the scores as a numpy array
        scores = np.array(scores, dtype=float)
        
        # Get the exponential of the scores
        exp_scores = np.exp(scores - np.max(scores))
        
        return exp_scores / exp_scores.sum()

    def __selectMoveBasedOnProbability__(self, moveProbabilities: dict[Move, float]) -> Move:
        
        """
        Selects a move based on the probabilities of each move being chosen.
        
        Args:
            moveProbabilities (dict[Move, float]): A dictionary mapping moves to their probabilities.
        
        Returns:
            Move: The selected move based on the probabilities.
        """
        
        # Check if the moveProbabilities is a dictionary
        if not isinstance(moveProbabilities, dict):
            raise ValueError("The moveProbabilities must be a dictionary.")
        
        # Ensure all probabilities are finite
        finiteProbabilities = {move: prob for move, prob in moveProbabilities.items() if np.isfinite(prob)}
        
        # Select a move based on the probabilities
        if not finiteProbabilities:
            return random.choice(list(moveProbabilities.keys()))
        
        return random.choices(list(finiteProbabilities.keys()), weights=finiteProbabilities.values(), k=1)[0]
