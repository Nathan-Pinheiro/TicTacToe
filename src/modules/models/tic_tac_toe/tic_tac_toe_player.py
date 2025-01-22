from abc import abstractmethod
from modules.models.tic_tac_toe.tic_tac_toe_game_state import TicTacToeGameState
from modules.models.board_game.components.move import Move

from modules.utils.validators import isHexColor

class Player:
    
    """
    A class that represents a player.
    """

    def __init__(self, name : str, color: str = "#FFFFFF") -> None:
        
        """
        Constructor for the Player class.
        
        Parameters:
            name (str): The name.
            
        Raises:
            ValueError: If the name is not a string.
            ValueError: If the color is not a hexadecimal string in the format #RRGGBB.
            
        Returns:
            None
        """
        
        # Check if the name is a string
        if not isinstance(name, str):
            raise ValueError("The name must be a string.")
        
        # Check if the color is a hexadecimal string in the format #RRGGBB
        if not isinstance(color, str) or not color.startswith('#') or len(color) != 7 or not isHexColor(color):
            raise ValueError("The color must be a hexadecimal string in the format #RRGGBB.")
        
        # Initialize the name and color
        self.__name__ = name
        self.__color__ = color
        
        return None

    def getName(self) -> str :
        
        """
        Gets the name.
        
        Returns:
            str: The name.
        """
        
        return self.__name__
    
    def setName(self, name : str) -> bool :
        
        """
        Sets the name.
        
        Parameters:
            name (str): The name.
            
        Raises:
            ValueError: If the name is not a string.
            
        Returns:
            bool: True if the name was set, False otherwise.
        """
        
        # Check if the name is a string
        if not isinstance(name, str):
            raise ValueError("The name must be a string.")
        
        # Set the name
        self.__name__ = name
        
        return True
    
    def getColor(self) -> str :
        
        """
        Gets the color.
        
        Returns:
            str: The color.
        """
        
        return self.__color__
    
    def setColor(self, color : str) -> bool:
        
        """
        Sets the color.
        
        Parameters:
            color (str): The color.
            
        Raises:
            ValueError: If the color is not a hexadecimal string in the format #RRGGBB.
            
        Returns:
            bool: True if the color was set.
        """
        
        # Check if the color is a hexadecimal string in the format #RRGGBB
        if not isinstance(color, str) or not color.startswith('#') or len(color) != 7 or not isHexColor(color):
            raise ValueError("The color must be a hexadecimal string in the format #RRGGBB.")
        
        # Set the color
        self.__color__ = color
        
        return True

    @abstractmethod
    def getChoice(self, gameState : TicTacToeGameState) -> Move:
        
        """
        Gets the choice of the player.
        
        Parameters:
            gameState (TicTacToeGameState): The current state of the Tic-Tac-Toe game.
            
        Returns:
            Move: The move that the player will make.
        """
        
        pass