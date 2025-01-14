from modules.models.tic_tac_toe.tic_tac_toe_game_state import TicTacToeGameState
from modules.models.board_game.components.move import Move
from modules.models.tic_tac_toe.tic_tac_toe_player import Player

# ************************************************
# CLASS AIPlayer
# ************************************************
# ROLE : The goal of this class is to represent an AI player
# ************************************************
# VERSION : 1.0
# AUTHOR : Nathan PINHEIRO / Hugo MERY
# DATE : 10/01/2025
# ************************************************

class AIPlayer(Player):

    def __init__(self, name : str) -> None:
        
        super().__init__(name)
        
        return None

    def get_choice(self, gameState : TicTacToeGameState) -> Move:
        pass