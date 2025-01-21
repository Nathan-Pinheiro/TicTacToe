from modules.models.tic_tac_toe.tic_tac_toe_player import Player
from modules.models.tic_tac_toe.tic_tac_toe_game_state import TicTacToeGameState
from modules.models.board_game.components.coordinate import Coordinate
from modules.models.utils.console_displayer import *
from modules.models.board_game.components.move import Move
from modules.models.tic_tac_toe.moves.simple_move import SimpleMove
from modules.models.tic_tac_toe.moves.power_ups.bomb_move import BombMove

class HumanGUIPlayer(Player):
    
    def __init__(self, name : str) -> None:
        super().__init__(name)
    
    def get_choice(self, gameState: TicTacToeGameState, line: int, column: int, bomb: bool) -> Move:
        if bomb:
            return BombMove(Coordinate(line, column))
        else:
           return SimpleMove(Coordinate(line, column))