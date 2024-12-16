from modules.models.board_components.boards.simple_board import SimpleBoard
from modules.models.board_components.coordinate import Coordinate

class Player:

    def __init__(self, name : str) -> None:
        self.__name__ = name
        return None

    def getName(self) -> str :
        return self.__name__
    
    def setName(self, name : str) -> None :
        self.__name__ = name
        return None

    def get_choice(self, board : SimpleBoard) -> Coordinate:
        pass