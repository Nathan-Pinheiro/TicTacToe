from __future__ import annotations

from modules.models.board_game.board.boards.simple_board import SimpleBoard
from modules.models.board_game.board.boards.optimized_board import OptimizedBoard
from modules.models.board_game.board.components.board_shape import BoardShape
from modules.models.board_game.components.entity import Entity

# ************************************************
# Class BoardBuilder
# ************************************************
# ROLE : This module allows encoding and decoding coordinates
# ************************************************
# VERSION : 1.0
# AUTHOR : Nathan PINHEIRO
# DATE : 13/01/2025
# ************************************************

MIN_HEIGHT = 3
MAX_HEIGHT = 7

MIN_WIDTH = 3
MAX_WIDTH = 7

MAX_BLOCKED_CASE_PERCENTAGE = 50

class BoardBuilder:
    
    """
    A class that allow generating a Board object with given specifications
    """

    def __init__(self, playerEntities : list[Entity], width : int = 3, height : int = 3) -> None:

        self.__playerEntities__ = playerEntities
        self.__width__ : int = width
        self.__height__ : int = height
        self.__shape__ : BoardShape = None
        self.__randomlyBlockedCases__ : int = 0

        return None
    
    def setWidth(self, width : int) -> BoardBuilder:
        
        self.__width__ = width
        return self
    
    def setHeight(self, height : int) -> BoardBuilder:
        
        self.__height__ = height
        return self

    def setShape(self, shape : BoardShape) -> BoardBuilder:
        
        self.__shape__ = shape
        return self
    
    def setRandomlyBlockedCaseAmount(self, randomlyBlockedCases : bool) -> BoardBuilder:
        
        self.__randomlyBlockedCases__ = randomlyBlockedCases
        return self
    
    def build(self) -> SimpleBoard:

        if(self.__height__ < MIN_HEIGHT or self.__height__ > MAX_HEIGHT) : raise ValueError(f"Height can't be outside range {MIN_HEIGHT} - {MAX_HEIGHT}")
        if(self.__width__ < MIN_WIDTH or self.__width__ > MAX_WIDTH) : raise ValueError(f"Width can't be outside range {MIN_HEIGHT} - {MAX_HEIGHT}")
        
        board = SimpleBoard(self.__width__, self.__height__, self.__playerEntities__)

        if(self.__shape__) : self.__shape__.apply_shape(board)
        
        for _ in range(0, self.__randomlyBlockedCases__): board.blockRandomCase()
                
        return board
    
    def buildOptimizedBoard(self) -> OptimizedBoard:

        if(self.__height__ < MIN_HEIGHT or self.__height__ > MAX_HEIGHT) : raise ValueError(f"Height can't be outside range {MIN_HEIGHT} - {MAX_HEIGHT}")
        if(self.__width__ < MIN_WIDTH or self.__width__ > MAX_WIDTH) : raise ValueError(f"Width can't be outside range {MIN_HEIGHT} - {MAX_HEIGHT}")
        
        board = OptimizedBoard(self.__width__, self.__height__, self.__playerEntities__)

        if(self.__shape__) : self.__shape__.apply_shape(board)
        
        # if(self.__randomlyBlockedCases__ > len(board.getAvaillableCases())) : raise ValueError(f"Cannot block {self.__randomlyBlockedCases__} cases because only {len(board.getAvaillableCases())} can be blocked.")

        for _ in range(0, self.__randomlyBlockedCases__): board.blockRandomCase()
                
        return board