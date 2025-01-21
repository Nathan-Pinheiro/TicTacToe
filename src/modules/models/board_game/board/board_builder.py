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
        
        """
        Constructor for the BoardBuilder class.
        
        Parameters:
            playerEntities (list[Entity]): The list of entities that will be on the board.
            width (int, optional): The width of the board. Defaults to 3.
            height (int, optional): The height of the board. Defaults to 3.

        Returns:
            None
        """

        self.__playerEntities__ = playerEntities
        self.__width__ : int = width
        self.__height__ : int = height
        self.__shape__ : BoardShape = None
        self.__randomlyBlockedCases__ : int = 0

        return None
    
    def setWidth(self, width : int) -> BoardBuilder:
        
        """
        Set the width of the board.
        
        Parameters:
            width (int): The width of the board.
            
        Returns:
            BoardBuilder: The current instance of the BoardBuilder class.
        """
        
        self.__width__ = width
        return self
    
    def setHeight(self, height : int) -> BoardBuilder:
        
        """
        Set the height of the board.
        
        Parameters:
            height (int): The height of the board.
            
        Returns:
            BoardBuilder: The current instance of the BoardBuilder class.
        """
        
        self.__height__ = height
        return self

    def setShape(self, shape : BoardShape) -> BoardBuilder:
        
        """
        Set the shape of the board.
        
        Parameters:
            shape (BoardShape): The shape of the board.
            
        Returns:
            BoardBuilder: The current instance of the BoardBuilder class.
        """
        
        self.__shape__ = shape
        return self
    
    def setRandomlyBlockedCaseAmount(self, randomlyBlockedCases : int) -> BoardBuilder:
        
        """
        Set the amount of randomly blocked cases.
        
        Parameters:
            randomlyBlockedCases (bool): The amount of randomly blocked cases.
            
        Returns:
            BoardBuilder: The current instance of the BoardBuilder class.
        """
        
        self.__randomlyBlockedCases__ = randomlyBlockedCases
        return self
    
    def build(self) -> SimpleBoard:
        
        """
        Build a simple board with the given specifications.
        
        Returns:
            SimpleBoard: The generated board.
        """

        if(self.__height__ < MIN_HEIGHT or self.__height__ > MAX_HEIGHT) : raise ValueError(f"Height can't be outside range {MIN_HEIGHT} - {MAX_HEIGHT}")
        if(self.__width__ < MIN_WIDTH or self.__width__ > MAX_WIDTH) : raise ValueError(f"Width can't be outside range {MIN_HEIGHT} - {MAX_HEIGHT}")
        
        board = SimpleBoard(self.__width__, self.__height__, self.__playerEntities__)

        if(self.__shape__) : self.__shape__.applyShape(board)
        
        for _ in range(0, self.__randomlyBlockedCases__): board.blockRandomCase()
                
        return board
    
    def buildOptimizedBoard(self) -> OptimizedBoard:
        
        """
        Build an optimized board with the given specifications.
        
        Returns:
            OptimizedBoard: The generated board.
        """

        if(self.__height__ < MIN_HEIGHT or self.__height__ > MAX_HEIGHT) : raise ValueError(f"Height can't be outside range {MIN_HEIGHT} - {MAX_HEIGHT}")
        if(self.__width__ < MIN_WIDTH or self.__width__ > MAX_WIDTH) : raise ValueError(f"Width can't be outside range {MIN_HEIGHT} - {MAX_HEIGHT}")
        
        board = OptimizedBoard(self.__width__, self.__height__, self.__playerEntities__)

        if(self.__shape__) : self.__shape__.applyShape(board)
        
        for _ in range(0, self.__randomlyBlockedCases__): board.blockRandomCase()
                
        return board