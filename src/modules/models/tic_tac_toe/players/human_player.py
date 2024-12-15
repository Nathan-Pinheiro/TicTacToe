from modules.models.tic_tac_toe.players.player import Player
from modules.models.board.board import Board
from modules.models.coordinate import Coordinate
from modules.models.board.case import Case
from modules.models.console_displayer import *

class HumanPlayer(Player):
    
    def __init__(self, name : str) -> None:
        super().__init__(name) 
    
    def get_choice(self, board : Board) -> Coordinate:

        clear_screen()
        
        display_centered(f"Tour de : {self.__name__}")
        display_sep()
        display_board(board)
        display_sep()

        chosedCase : Case = None
        isMovePossible : bool = False

        while(not isMovePossible):

            lineChosed : int = ask_for_int("Quelle ligne souhaitez vous jouer ? ")
            columnChosed : int = ask_for_int("Quelle colonne souhaitez vous jouer ? ")

            if(lineChosed and columnChosed) : chosedCase : Case = board.getCase(lineChosed - 1, columnChosed - 1)
            
            isMovePossible = (chosedCase != None and chosedCase.isAvaillable())
            if(not isMovePossible) : display("Ce coup est impossible !")

        return chosedCase.getCoordinate()