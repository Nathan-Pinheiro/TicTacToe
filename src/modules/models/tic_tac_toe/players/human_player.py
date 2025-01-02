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
    
    def get_choice_2(self, gameState : GameState) -> Move:

        clear_screen()
        
        display_centered(f"Tour de : {self.__name__}")
        display_sep()
        display_board(gameState.getBoard())
        display_sep()

        move : Move = SimpleMove

        isMovePossible : bool = False

        # while(not isMovePossible):
            
        #     display("Types de coups :")
        #     display(" 1 - Normal Moove")
        #     display(" 2 - BOMB !!!")

        #     rep : int = ask_for_int("Quel type de coup voulez-vous jouer ? ")
            
        #     if(rep == 1) :
        #         isMovePossible = True
        #         move = SimpleMove
                
        #     elif(rep == 2) :
        #         isMovePossible = BombMove in gameState.getPlayerData(gameState.getPlayerToPlayIndex()).getPowerUpMoves()
        #         if(isMovePossible): move = BombMove
                
        #     if(not isMovePossible) : display("Ce coup est impossible !")

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
    
    def get_choice(self, gameState: GameState, line: int, column: int) -> Move:
        move = SimpleMove(Coordinate(line, column))
        return move