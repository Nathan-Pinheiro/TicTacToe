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
        
        return None
    
    def getChoice(self, gameState: TicTacToeGameState, line: int, column: int, bomb: bool) -> Move:
        
        """
        Gets the choice of the player.
        
        Parameters:
            gameState (TicTacToeGameState): The current state of the Tic-Tac-Toe game.
            line (int): The line.
            column (int): The column.
            bomb (bool): True if bomb, False otherwise.
            
        Raises:
            ValueError: If the game state is not a TicTacToeGameState object.
            ValueError: If the line or the column is not an integer.
            ValueError: If the line or the column is not a valid index.
            TypeError: If the bomb is not a boolean.
            
        Returns:
            Move: The move that the player will make.
        """
        
        # Check if the game state is a TicTacToeGameState object
        if not isinstance(gameState, TicTacToeGameState):
            raise ValueError("The game state must be a TicTacToeGameState object.")
        
        # Check if the line and the column are integers and valid indexes
        if not isinstance(line, int) or not isinstance(column, int):
            raise ValueError("The line and the column must be integers.")
        
        if line < 0 or line >= gameState.getBoard().getHeight() or column < 0 or column >= gameState.getBoard().getWidth():
            raise ValueError("The line and the column must be valid indexes.")
        
        # Check if the bomb is a boolean
        if not isinstance(bomb, bool):
            raise TypeError("The bomb must be a boolean.")
        
        # Check if the move is a bomb or a simple move and return it
        if bomb:
            return BombMove(Coordinate(line, column))
        else:
           return SimpleMove(Coordinate(line, column))