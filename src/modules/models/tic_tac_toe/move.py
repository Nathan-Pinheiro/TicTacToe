from enum import Enum
from modules.models.board_components.coordinate import Coordinate
from modules.models.board_components.board import Board
from modules.models.coordinate_encoder import encode

class Move :
    
    def __init__(self, moveCode : str, coordinate : Coordinate) -> None :
        
        self.__moveCode__ = moveCode
        self.__coordinate__ = coordinate
        
        return None
    
    def play(self, board : Board, playerIndex : int) -> None :
        pass
    
    def undo(self, board : Board, playerIndex : int) -> None :
        pass
    
    @classmethod
    def canPlay(cls, board : Board, line : int, column : int) -> bool:
        pass
    
    def __str__(self):
        return self.__moveCode__ + encode(self.__coordinate__)
    
    def __repr__(self):
        return self.__str__()
