from enum import Enum
from modules.models.board_components.coordinate import Coordinate
from modules.models.board_components.board import Board
from modules.models.board_components.entity import Entity

class Move :
    
    def __init__(self, moveCode : str, coordinate : Coordinate, entity : Entity) -> None :
        
        self.__moveCode__ = moveCode
        self.__coordinate__ = coordinate
        self.__entityToPlay__ = entity
        
        return None
    
    def play(self, board : Board, entity : Entity) -> None :
        pass
    
    @classmethod
    def canPlay(cls, board : Board, line : int, column : int) -> bool:
        pass
