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
        self.__name__ = name
        self.__color__ = "#ffffff"
        return None

    def getName(self) -> str :
        return self.__name__
    
    def setName(self, name : str) -> None :
        self.__name__ = name
        return None
    
    def getColor(self) -> str :
        return self.__color__
    
    def setColor(self, color : str) -> None:
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
        pass