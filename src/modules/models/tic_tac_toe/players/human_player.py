from modules.models.tic_tac_toe.tic_tac_toe_player import Player
from modules.models.tic_tac_toe.tic_tac_toe_game_state import TicTacToeGameState
from modules.models.board_components.coordinate import Coordinate
from modules.models.console_displayer import *
from modules.models.board_game.move import Move
from modules.models.tic_tac_toe.moves.simple_move import SimpleMove
from modules.models.tic_tac_toe.moves.bomb_move import BombMove

class HumanPlayer(Player):
    
    def __init__(self, name : str) -> None:
        super().__init__(name)
    
    def get_choice(self, gameState: TicTacToeGameState, line: int, column: int) -> Move:
        move = SimpleMove(Coordinate(line, column))
        return move