from modules.models.tic_tac_toe.tic_tac_toe_game_state import TicTacToeGameState
from modules.models.board_game.components.move import Move

class Player:
    
    """
    A class that represents a player.
    """

    def __init__(self, name : str) -> None:
        
        """
        Constructor for the Player class.
        
        Parameters:
            name (str): The name.
            
        Returns:
            None
        """
        
        self.__name__ = name
        self.__color__ = "#ffffff"
        return None

    def getName(self) -> str :
        
        """
        Gets the name.
        
        Returns:
            str: The name.
        """
        
        return self.__name__
    
    def setName(self, name : str) -> None :
        
        """
        Sets the name.
        
        Parameters:
            name (str): The name.
            
        Returns:
            None
        """
        
        self.__name__ = name
        return None
    
    def getColor(self) -> str :
        
        """
        Gets the color.
        
        Returns:
            str: The color.
        """
        
        return self.__color__
    
    def setColor(self, color : str) -> None:
        
        """
        Sets the color.
        
        Parameters:
            color (str): The color.
            
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

    def get_choice(self, gameState : TicTacToeGameState) -> Move:
        
        """
        Gets the choice of the player.
        
        Parameters:
            gameState (TicTacToeGameState): The current state of the Tic-Tac-Toe game.
            
        Returns:
            Move: The move that the player will make.
        """
        
        pass