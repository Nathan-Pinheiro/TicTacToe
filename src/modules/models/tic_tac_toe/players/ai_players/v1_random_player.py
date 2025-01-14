from modules.models.tic_tac_toe.players.ai_player import AIPlayer
from modules.models.tic_tac_toe.tic_tac_toe_game_state import TicTacToeGameState
from modules.models.utils.console_displayer import *
from modules.models.board_game.components.move import Move
import random

# ************************************************
# CLASS RandomPlayer
# ************************************************
# ROLE : This AI can return a random possible move
# ************************************************
# VERSION : 1.0
# AUTHOR : Nathan PINHEIRO
# DATE : 10/01/2025
# ************************************************

class RandomPlayer(AIPlayer):
    
    """
    RandomPlayer is an AI player that selects a move at random from the list of possible moves.
    Inherits from AIPlayer.
    """
    
    def __init__(self) -> None:
        
        """
        Initializes the RandomPlayer with the name "Random AI".
        """
        super().__init__("Random AI")
    

    def get_choice(self, gameState : TicTacToeGameState) -> Move:
        
        """
        Selects and returns a random move from the list of possible moves.
        
        Args:
            gameState (GameState): The current state of the game.
        
        Returns:
            Move: A randomly chosen move from the available legal moves.
        """
        
        moves : list[Move] = gameState.getPossibleMoves()
        chosenMove: Move = random.choice(moves)
        
        return chosenMove