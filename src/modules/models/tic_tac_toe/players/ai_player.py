from modules.models.tic_tac_toe.tic_tac_toe_game_state import TicTacToeGameState
from modules.models.board_game.components.move import Move
from modules.models.tic_tac_toe.tic_tac_toe_player import Player
from modules.models.board_game.game.game_analyser import GameAnalyser
from modules.models.board_game.game.game_analysers.minmax_alpha_beta_pruning_analyser import AlphaBetaPruningAnalyser

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
        
        # Initialize the game analyser
        self.__gameAnalyser__ : GameAnalyser = AlphaBetaPruningAnalyser(3)
        
        return None

    def getChoice(self, gameState : TicTacToeGameState) -> Move:
        
        """
        Selects the best move for the current game state based on the scores
        
        Parameters:
            gameState (TicTacToeGameState): The current state of the Tic-Tac-Toe game.
            
        Raises:
            ValueError: If the game state is not a TicTacToeGameState object.
            ValueError: Can't play as there is no moves to play
            
        Returns:
            Move: The move that the AI will make.
        """
        
        pass