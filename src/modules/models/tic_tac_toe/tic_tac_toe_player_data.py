from modules.models.board_game.components.player_data import PlayerData
from modules.models.tic_tac_toe.moves.power_up_move import PowerUpMove
from typing import Type

class TicTacToePlayerData(PlayerData) :
    
    def __init__(self, powerUpsMoves : list[Type[PowerUpMove]]) :
        
        self.__powerUpsMoves__ : list[Type[PowerUpMove]] = powerUpsMoves
    
    def getPowerUpMoves(self) -> list[Type[PowerUpMove]]:
        
        return self.__powerUpsMoves__
    