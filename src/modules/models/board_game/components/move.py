from modules.models.board_game.board.board import Board
from modules.models.board_game.components.coordinate import Coordinate
from modules.models.board_game.components.coordinate_encoder import encode
from abc import ABC, abstractmethod

# ************************************************
# CLASS Move
# ************************************************
# ROLE : This class is used to represent a generic move
# ************************************************
# VERSION : 1.0
# AUTHOR : Nathan PINHEIRO
# DATE : 13/01/2025
# ************************************************

class Move(ABC) :
    
    """
    A class that represent a generic move
    """

    def __init__(self, moveCode : str, coordinate : Coordinate) -> None :
        
        self.__moveCode__ = moveCode
        self.__coordinate__ = coordinate
        
        return None
    
    @abstractmethod
    def play(self, board : Board, playerIndex : int) -> None :
        pass
    
    @abstractmethod
    def undo(self, board : Board, playerIndex : int) -> None :
        pass
    
    @classmethod
    @abstractmethod
    def canPlay(cls, board : Board, line : int, column : int) -> bool:
        pass
    
    def getCoordinate(self) -> Coordinate :
        return self.__coordinate__

    def __str__(self):
        return self.__moveCode__ + encode(self.__coordinate__)
    
    def __repr__(self):
        return self.__str__()
