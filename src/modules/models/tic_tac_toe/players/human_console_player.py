from modules.models.tic_tac_toe.tic_tac_toe_player import Player
from modules.models.tic_tac_toe.tic_tac_toe_game_state import TicTacToeGameState
from modules.models.board_game.components.coordinate import Coordinate
from modules.models.displayer.console_displayer import *
from modules.models.board_game.components.move import Move
from modules.models.tic_tac_toe.moves.simple_move import SimpleMove

class HumanConsolePlayer(Player):
    
    """
    A class that represents a human console player.
    """
    
    def __init__(self, name : str) -> None:
        
        """
        Constructor for the HumanConsolePlayer class.
        
        Parameters:
            name (str): The name.
            
        Returns:
            None
        """
        
        super().__init__(name)
        
        return None
    
    def get_choice(self, gameState : TicTacToeGameState) -> Move:
        
        """
        Gets the choice of the player.
        
        Parameters:
            gameState (TicTacToeGameState): The current state of the Tic-Tac-Toe game.
            
        Returns:
            Move: The move that the player will make.
        """

        clear_screen()
        
        display_centered(f"Tour de : {self.__name__}")
        display_sep()
        display_board(gameState.getBoard())
        display_sep()

        move : Move = SimpleMove

        isMovePossible : bool = False

        while(not isMovePossible):

            lineChosed : int = ask_for_int("Quelle ligne souhaitez vous jouer ? ")
            columnChosed : int = ask_for_int("Quelle colonne souhaitez vous jouer ? ")

            isLineValid = lineChosed and 0 <= lineChosed - 1 < gameState.getBoard().getHeight()
            isColumnValid = columnChosed and 0 <= columnChosed - 1 < gameState.getBoard().getWidth()

            if(isLineValid and isColumnValid) : 

                isMovePossible = move.canPlay(gameState.getBoard(), lineChosed - 1, columnChosed - 1)
                if(not isMovePossible) : display("La case n'est pas disponible ...")

            else : display("Ce coup est impossible !")

        return move(Coordinate(lineChosed - 1, columnChosed - 1))