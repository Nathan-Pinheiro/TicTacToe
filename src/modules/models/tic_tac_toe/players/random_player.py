from modules.models.tic_tac_toe.players.player import Player
from modules.models.board_components.boards.simple_board import SimpleBoard
from modules.models.board_components.coordinate import Coordinate
from modules.models.board_components.case import Case
from modules.models.console_displayer import *

class HumanPlayer(Player):
    
    def __init__(self, name : str) -> None:
        super(name)
    
    def get_choice(self, board : SimpleBoard) -> Coordinate:

        chosedCase : Case = None
        isChoicePossible : bool = False

        while(not isChoicePossible):
        
            clear_screen()
            display_board(board)

            display("Dans quelle case voulez-vous placer votre pion ?")

            lineChosed : int = ask_for_int("Quelle ligne souhaitez vous jouer ? ")
            columnChosed : int = ask_for_int("Quelle colonne souhaitez vous jouer ? ")

            if(lineChosed and columnChosed):

                chosedCase : Case = board.getCase(lineChosed, columnChosed)
                if(chosedCase != None) : isChoicePossible = True

        return chosedCase.getCoordinate()