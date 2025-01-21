from modules.models.tic_tac_toe.tic_tac_toe_game_state import TicTacToeGameState
from modules.models.board_game.components.move import Move
from abc import ABC, abstractmethod

# ************************************************
# CLASS Player
# ************************************************
# ROLE : This abstract class is used to store player informations
# ************************************************
# VERSION : 1.0
# AUTHOR : Nathan PINHEIRO
# DATE : 13/01/2025
# ************************************************

class Player(ABC):

    """
    A class that represent a generic player
    """

    def __init__(self, name : str) -> None:
        
        """
        Constructor for the Player class.
        
        Parameters:
            name (str): The name of the player.
            
        Returns:
            None
        """
        
        self.__name__ = name
        self.__color__ = "#ffffff"
        return None

    def getName(self) -> str :
        
        """
        Get the name of the player.

        Returns:
            str: The name of the player.
        """
        
        return self.__name__
    
    def setName(self, name : str) -> None :
        
        """
        Set the name of the player.
        
        Parameters:
            name (str): The name of the player.
            
        Returns:
            None
        """
        
        self.__name__ = name
        return None
    
    def getColor(self) -> str :
        
        """
        Get the color of the player.

        Returns:
            str: The color of the player.
        """
        
        return self.__color__
    
    def setColor(self, color : str) -> None:
        
        """
        Set the color of the player.
        
        Parameters:
            color (str): The color of the player.
            
        Returns:
            None
        """
        
        if not isinstance(color, str) or not color.startswith('#') or len(color) != 7:
            raise ValueError("Color must be a hexadecimal string in the format #RRGGBB")
        try:
            int(color[1:], 16)
        except ValueError:
            raise ValueError("Color must be a hexadecimal string in the format #RRGGBB")
        self.__color__ = color
        return None

    @abstractmethod
    def get_choice(self, gameState : TicTacToeGameState) -> Move:
        
        """
        Get the choice of the player.
        
        Parameters:
            gameState (TicTacToeGameState): The current state of the game.
            
        Returns:
            Move: The move chosen by the player.
        """
        
        pass