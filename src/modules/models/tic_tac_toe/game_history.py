from modules.models.tic_tac_toe.move import Move 
from modules.models.board_components.board import Board

class GameHistory:
    
    def __init__(self, initialBoard : Board) -> None:
        
        self.__initialBoard__ = initialBoard
        self.__moves__ : list[Move] = []
        
        return None

    def getMoveCount(self) -> Move:
        return len(self.__moves__)

    def getMove(self, moveIndex : int) -> Move:
        return self.__moves__[moveIndex]
    
    def addMove(self, moveIndex : int) -> None:
        return self.__moves__[moveIndex]
    
    def removeLastMove(self) -> None:
        del self.__moves__[len(self.__moves__) - 1]
        return None