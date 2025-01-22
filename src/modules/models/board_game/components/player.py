from modules.models.tic_tac_toe.tic_tac_toe_game_state import TicTacToeGameState
from modules.models.board_game.components.move import Move

from modules.utils.validators import isHexColor

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
            
        Raises:
            TypeError: If name is not a string.
            
        Returns:
            None
        """
        
        # Check if name is a string
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        
        # Initialize the attributes
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
    
    def setName(self, name : str) -> bool:
        
        """
        Set the name of the player.
        
        Parameters:
            name (str): The name of the player.
            
        Returns:
            bool: True if the name has been set.
        """
        
        # Check if name is a string
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        
        # Set the name
        self.__name__ = name
        
        return True
    
    def getColor(self) -> str:
        
        """
        Get the color of the player.

        Returns:
            str: The color of the player.
        """
        
        return self.__color__
    
    def setColor(self, color : str) -> bool:
        
        """
        Set the color of the player.
        
        Parameters:
            color (str): The color of the player.
            
        Raises:
            TypeError: If the color is not a string.
            ValueError: If the color is not a valid hexadecimal color.
            
        Returns:
            bool: True if the color has been set.
        """
        
        # Check if color is a string and a valid hexadecimal color
        if not isinstance(color, str):
            raise TypeError("Color must be a string")
        
        if not isHexColor(color):
            raise ValueError("Color must be a hexadecimal string in the format #RRGGBB")
        
        # Set the color
        self.__color__ = color
        
        return True

    @abstractmethod
    def get_choice(self, gameState : TicTacToeGameState) -> Move:
        
        """
        Get the choice of the player.
        
        Parameters:
            gameState (TicTacToeGameState): The current state of the game.
            
        Raises:
            TypeError: If gameState is not a TicTacToeGameState.
            
        Returns:
            Move: The move chosen by the player.
        """
        
        pass