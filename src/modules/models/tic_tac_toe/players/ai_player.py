from modules.models.tic_tac_toe.tic_tac_toe_game_state import TicTacToeGameState
from modules.models.board_game.components.move import Move
from modules.models.tic_tac_toe.tic_tac_toe_player import Player
from modules.models.board_game.game.game_analyser import GameAnalyser
from modules.models.board_game.game.game_analysers.minimax_alpha_beta_pruning_analyser import AlphaBetaPruningAnalyser

# ************************************************
# CLASS AIPlayer
# ************************************************
# ROLE : The goal of this class is to represent an AI player
# ************************************************
# VERSION : 1.0
# AUTHOR : Nathan PINHEIRO
# DATE : 10/01/2025
# ************************************************

class AIPlayer(Player):
    
    """
    A simple AI player for Tic-Tac-Toe that selects its move based on the scores
    """

    def __init__(self, name : str) -> None:
        
        """
        Initializes the AI player with a name and links to a game analyser.
        
        Parameters:
            name (str): The name of the player.
            
        Returns:
            None
        """
        
        super().__init__(name)
        
        self.__game_analyser__ : GameAnalyser = AlphaBetaPruningAnalyser(3)

    def get_choice(self, gameState : TicTacToeGameState) -> Move:
        
        """
        Selects the best move for the current game state based on the scores
        
        Parameters:
            gameState (TicTacToeGameState): The current state of the Tic-Tac-Toe game.
            
        Returns:
            Move: The move that the AI will make.
        """
        
        pass