from modules.models.tic_tac_toe.tic_tac_toe_player import Player
from modules.models.tic_tac_toe.tic_tac_toe_game_state import TicTacToeGameState
from modules.models.board_game.components.coordinate import Coordinate
from modules.models.displayer.console_displayer import *
from modules.models.board_game.components.move import Move
from modules.models.tic_tac_toe.moves.simple_move import SimpleMove
from modules.models.tic_tac_toe.moves.power_ups.bomb_move import BombMove

class HumanGUIPlayer(Player):
    
    """
    A class that represents a human player.
    """
    
    def __init__(self, name : str) -> None:
        
        """
        Constructor for the HumanPlayer class.
        
        Parameters:
            name (str): The name.
            
        Returns:
            None
        """
        
        super().__init__(name)
    
    def get_choice(self, gameState: TicTacToeGameState, line: int, column: int, bomb: bool) -> Move:
        
        """
        Gets the choice of the player.
        
        Parameters:
            gameState (TicTacToeGameState): The current state of the Tic-Tac-Toe game.
            line (int): The line.
            column (int): The column.
            bomb (bool): True if bomb, False otherwise.
            
        Returns:
            Move: The move that the player will make.
        """
        
        if bomb:
            return BombMove(Coordinate(line, column))
        else:
           return SimpleMove(Coordinate(line, column))