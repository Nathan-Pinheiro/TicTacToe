from modules.models.tic_tac_toe.player import Player
from modules.models.tic_tac_toe.game_state import GameState
from modules.models.board_components.coordinate import Coordinate
from modules.models.console_displayer import *
from modules.models.tic_tac_toe.move import Move
from modules.models.tic_tac_toe.moves.simple_move import SimpleMove
from modules.models.tic_tac_toe.moves.bomb_move import BombMove

class HumanPlayer(Player):
    
    def __init__(self, name : str) -> None:
        super().__init__(name)
    
    def get_choice(self, gameState: GameState, line: int, column: int) -> Move:
        move = SimpleMove(Coordinate(line, column))
        return move