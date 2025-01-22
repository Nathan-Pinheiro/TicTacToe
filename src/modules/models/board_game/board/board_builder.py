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

    def __init__(self, playerEntities: list[Entity], width: int = 3, height: int = 3) -> None:
        
        """
        Constructor for the BoardBuilder class.
        
        Parameters:
            playerEntities (list[Entity]): The list of entities that will be on the board.
            width (int, optional): The width of the board. Defaults to 3.
            height (int, optional): The height of the board. Defaults to 3.
            
        Raises:
            TypeError: If playerEntities is not a list of Entity instances.
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than or equal to 0.

        Returns:
            None
        """
        
        # Check if playerEntities is a list of Entity instances
        if not isinstance(playerEntities, list) or not all(isinstance(entity, Entity) for entity in playerEntities):
            raise TypeError("playerEntities must be a list of Entity instances")
        
        # Check if width and height are integers and greater than 0
        if not isinstance(width, int) or not isinstance(height, int):
            raise TypeError("width and height must be integers")
        
        if width <= 0 or height <= 0:
            raise ValueError("width and height must be greater than 0")

        # Initialize the attributes
        self.__playerEntities__ = playerEntities
        self.__width__: int = width
        self.__height__: int = height
        self.__shape__: BoardShape = None
        self.__randomlyBlockedCases__: int = 0

        return None
    
    def setWidth(self, width: int) -> BoardBuilder:
        
        """
        Set the width of the board.
        
        Parameters:
            width (int): The width of the board.
            
        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than or equal to 0.

        Returns:
            BoardBuilder: The current instance of the BoardBuilder class.
        """
        
        # Check if width is an integer and greater than 0
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        
        if width <= 0:
            raise ValueError("width must be greater than 0")
        
        # Set the width
        self.__width__ = width
        
        return self
    
    def setHeight(self, height: int) -> BoardBuilder:
        
        """
        Set the height of the board.
        
        Parameters:
            height (int): The height of the board.
            
        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than or equal to 0.

        Returns:
            BoardBuilder: The current instance of the BoardBuilder class.
        """
        
        # Check if height is an integer and greater than 0
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        
        if height <= 0:
            raise ValueError("height must be greater than 0")
        
        # Set the height
        self.__height__ = height
        
        return self

    def setShape(self, shape: BoardShape) -> BoardBuilder:
        
        """
        Set the shape of the board.
        
        Parameters:
            shape (BoardShape): The shape of the board.
            
        Raises:
            TypeError: If shape is not an instance of BoardShape.

        Returns:
            BoardBuilder: The current instance of the BoardBuilder class.
        """
        
        # Check if shape is an instance of BoardShape
        if not isinstance(shape, BoardShape):
            raise TypeError("shape must be an instance of BoardShape")
        
        # Set the shape
        self.__shape__ = shape
        
        return self
    
    def setRandomlyBlockedCaseAmount(self, randomlyBlockedCases: int) -> BoardBuilder:
        
        """
        Set the amount of randomly blocked cases.
        
        Parameters:
            randomlyBlockedCases (int): The amount of randomly blocked cases.
            
        Raises:
            TypeError: If randomlyBlockedCases is not an integer.
            ValueError: If randomlyBlockedCases is less than 0.

        Returns:
            BoardBuilder: The current instance of the BoardBuilder class.
        """
        
        # Check if randomlyBlockedCases is an integer and greater than or equal to 0
        if not isinstance(randomlyBlockedCases, int):
            raise TypeError("randomlyBlockedCases must be an integer")
        
        if randomlyBlockedCases < 0:
            raise ValueError("randomlyBlockedCases must be greater than or equal to 0")
        
        # Set the amount of randomly blocked cases
        self.__randomlyBlockedCases__ = randomlyBlockedCases
        
        return self
    
    def build(self) -> SimpleBoard:
        
        """
        Build a simple board with the given specifications.
        
        Raises:
            ValueError: If width or height is outside the allowed range.
            
        Returns:
            SimpleBoard: The generated board.
        """
        
        # Check if width and height are within the allowed range
        if self.__height__ < MIN_HEIGHT or self.__height__ > MAX_HEIGHT:
            raise ValueError(f"Height can't be outside range {MIN_HEIGHT} - {MAX_HEIGHT}")
        
        if self.__width__ < MIN_WIDTH or self.__width__ > MAX_WIDTH:
            raise ValueError(f"Width can't be outside range {MIN_WIDTH} - {MAX_WIDTH}")
        
        # Create a simple board
        board = SimpleBoard(self.__width__, self.__height__, self.__playerEntities__)

        # Apply the shape if specified
        if self.__shape__:
            self.__shape__.applyShape(board)
        
        # Block random cases if specified
        for _ in range(0, self.__randomlyBlockedCases__):
            board.blockRandomCase()
                
        return board
    
    def buildOptimizedBoard(self) -> OptimizedBoard:
        
        """
        Build an optimized board with the given specifications.
        
        Raises:
            ValueError: If width or height is outside the allowed range.
            
        Returns:
            OptimizedBoard: The generated board.
        """
        
        # Check if width and height are within the allowed range
        if self.__height__ < MIN_HEIGHT or self.__height__ > MAX_HEIGHT:
            raise ValueError(f"Height can't be outside range {MIN_HEIGHT} - {MAX_HEIGHT}")
        
        if self.__width__ < MIN_WIDTH or self.__width__ > MAX_WIDTH:
            raise ValueError(f"Width can't be outside range {MIN_WIDTH} - {MAX_WIDTH}")
        
        # Create an optimized board
        board = OptimizedBoard(self.__width__, self.__height__, self.__playerEntities__)

        # Apply the shape if specified
        if self.__shape__:
            self.__shape__.applyShape(board)
        
        # Block random cases if specified
        for _ in range(0, self.__randomlyBlockedCases__):
            board.blockRandomCase()
                
        return board