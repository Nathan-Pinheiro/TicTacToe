from __future__ import annotations

import random

from modules.models.board_components.boards.simple_board import SimpleBoard
from modules.models.board_components.case import Case
from modules.models.board_components.board_shapes.board_shape import BoardShape

from modules.models.console_displayer import *

MIN_HEIGHT = 3
MAX_HEIGHT = 7

MIN_WIDTH = 3
MAX_WIDTH = 7

MAX_BLOCKED_CASE_PERCENTAGE = 50

class BoardBuilder:
    
    def __init__(self, width : int = 3, height : int = 3) -> None:

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
        
        board = SimpleBoard(self.__width__, self.__height__)

        display_board(board)

        if(self.__shape__) : self.__shape__.apply_shape(board)
        
        if(self.__randomlyBlockedCases__ > len(board.getAvaillableCases())) : raise ValueError(f"Cannot block {self.__randomlyBlockedCases__} cases because only {len(board.getAvaillableCases())} can be blocked.")

        if(self.__randomlyBlockedCases__ > 0) :

            for _ in range(0, self.__randomlyBlockedCases__):
                
                availlableCases : list[Case] = board.getAvaillableCases() 
                blockedCaseIndex : int = random.randint(0, len(availlableCases) - 1)
                availlableCases[blockedCaseIndex].setIsBlocked(True)
                
        return board