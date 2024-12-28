from modules.models.tic_tac_toe.move import Move 
from modules.models.board_components.board import Board

class GameHistory:
    
    def __init__(self) -> None:
        
        self.__moves__ : list[Move] = []
        
        return None

    def getMoveCount(self) -> Move:
        return len(self.__moves__)

    def getMove(self, moveIndex : int) -> Move:
        return self.__moves__[moveIndex]
    
    def getLastMove(self) -> Move:
        return self.__moves__[len(self.__moves__) - 1]
    
    def addMove(self, move : Move) -> None:
        self.__moves__.append(move)
    
    def removeLastMove(self) -> None:
        del self.__moves__[len(self.__moves__) - 1]
        return None
    
    def removeMove(self, moveIndex : int) -> None:
        del self.__moves__[moveIndex]
        return None