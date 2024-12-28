from modules.models.tic_tac_toe.player import Player
from modules.models.tic_tac_toe.game_state import GameState
from modules.models.board_components.coordinate import Coordinate
from modules.models.board_components.case import Case
from modules.models.console_displayer import *
from modules.models.tic_tac_toe.move import Move
import random

class RandomPlayer(Player):
    
    def __init__(self) -> None:
        super().__init__("Random AI")
    
    def get_choice(self, gameState : GameState) -> Move:

        moves : list[Move] = gameState.getPossibleMoves()
        chosenMove: Move = random.choice(moves)
        
        return chosenMove