from modules.models.tic_tac_toe.game_state import GameState
from modules.models.tic_tac_toe.move import Move

class Player:

    def __init__(self, name : str) -> None:
        self.__name__ = name
        return None

    def getName(self) -> str :
        return self.__name__
    
    def setName(self, name : str) -> None :
        self.__name__ = name
        return None

    def get_choice(self, gameState : GameState) -> Move:
        pass