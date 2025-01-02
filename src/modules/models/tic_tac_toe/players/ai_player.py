from modules.models.tic_tac_toe.game_state import GameState
from modules.models.tic_tac_toe.move import Move
from modules.models.tic_tac_toe.player import Player

class AIPlayer(Player):

    def __init__(self, name : str) -> None:
        
        super().__init__(name)
        
        return None

    def get_choice(self, gameState : GameState) -> Move:
        pass