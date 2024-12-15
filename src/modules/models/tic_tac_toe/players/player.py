from modules.models.board.board import Board
from modules.models.coordinate import Coordinate

class Player:

    def __init__(self, name : str) -> None:
        self.__name__ = name
        return None

    def getName(self) -> str :
        return self.__name__
    
    def setName(self, name : str) -> None :
        self.__name__ = name
        return None

    def get_choice(self, board : Board) -> Coordinate:
        pass