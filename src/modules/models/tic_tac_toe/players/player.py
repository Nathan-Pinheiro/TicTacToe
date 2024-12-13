from modules.models.board import Board

class Player:

    def __init__(self, name : str) -> None:
        self.__name__ = name
        return None

    def getName(self) -> str :
        return self.__name__
    
    def setName(self, name : str) -> None :
        self.__name__ = name
        return None

    def get_choice(self, board : Board) -> int:
        pass