from modules.models.tic_tac_toe.players.player import Player
from modules.models.board_components.boards.simple_board import SimpleBoard
from modules.models.board_components.coordinate import Coordinate
from modules.models.board_components.case import Case
from modules.models.console_displayer import *

class HumanPlayer(Player):
    
    def __init__(self, name : str) -> None:
        super().__init__(name) 
    
    def get_choice(self, board : SimpleBoard) -> Coordinate:

        clear_screen()
        
        display_centered(f"Tour de : {self.__name__}")
        display_sep()
        display_board(board)
        display_sep()

        isMovePossible : bool = False

        while(not isMovePossible):

            lineChosed : int = ask_for_int("Quelle ligne souhaitez vous jouer ? ")
            columnChosed : int = ask_for_int("Quelle colonne souhaitez vous jouer ? ")

            isLineValid = lineChosed and 0 <= lineChosed - 1 < board.getHeight()
            isColumnValid = columnChosed and 0 <= columnChosed - 1 < board.getWidth()

            if(isLineValid and isColumnValid) : 

                isMovePossible = board.isCaseAvaillable(lineChosed - 1, columnChosed - 1)
                if(not isMovePossible) : display("La case n'est pas disponible ...")

            else : display("Ce coup est impossible !")

        return Coordinate(lineChosed - 1, columnChosed - 1)