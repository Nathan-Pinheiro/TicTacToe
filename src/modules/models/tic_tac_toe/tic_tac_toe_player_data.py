from modules.models.board_game.components.player_data import PlayerData
from modules.models.tic_tac_toe.moves.power_up_move import PowerUpMove
from typing import Type

class TicTacToePlayerData(PlayerData) :
    
    """
    A class that represents the data of a Tic-Tac-Toe player.
    """
    
    def __init__(self, powerUpsMoves : list[Type[PowerUpMove]]) :
        
        """
        Constructor for the TicTacToePlayerData class.
        
        Parameters:
            powerUpsMoves (list[Type[PowerUpMove]]): The power up moves.
        
        Returns:
            None
        """
        
        # Initialize the power up moves
        self.__powerUpsMoves__ : list[Type[PowerUpMove]] = powerUpsMoves
        
        return None
    
    def getPowerUpMoves(self) -> list[Type[PowerUpMove]]:
        
        """
        Gets the power up moves.

        Returns:
            list[Type[PowerUpMove]]: The power up moves.
        """
        
        return self.__powerUpsMoves__
    