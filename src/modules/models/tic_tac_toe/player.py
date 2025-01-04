from modules.models.tic_tac_toe.game_state import GameState
from modules.models.tic_tac_toe.move import Move

class Player:

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

    def get_choice(self, gameState : GameState) -> Move:
        pass