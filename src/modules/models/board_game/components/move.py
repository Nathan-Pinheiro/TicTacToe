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
        
        """
        Constructor for the Move class.
        
        Parameters:
            moveCode (str): The code of the move.
            coordinate (Coordinate): The coordinate of the move.
            
        Raises:
            TypeError: If moveCode is not a string or if coordinate is not a Coordinate object.
            
        Returns:
            None
        """
        
        # Check if moveCode is a string
        if not isinstance(moveCode, str):
            raise TypeError("moveCode must be a string")
        
        # Check if coordinate is a Coordinate object
        if not isinstance(coordinate, Coordinate):
            raise TypeError("coordinate must be a Coordinate object")
        
        # Initialize the attributes        
        self.__moveCode__ : str = moveCode
        self.__coordinate__ : Coordinate = coordinate
        self.__isMoveDone__ : bool = False
        
        return None
    
    @abstractmethod
    def play(self, board : Board, playerIndex : int) -> bool:
        
        """
        Play the move on the board.
        
        Parameters:
            board (Board): The board on which the move will be played.
            playerIndex (int): The index of the player who plays the move.
            
        Raises:
            TypeError: If board is not a Board object.
            TypeError: If playerIndex is not an integer.
            ValueError: If playerIndex is less than 0 or greater than the number of players.
            
        Returns:
            bool: True if the move has been played.
        """
        
        pass
    
    @abstractmethod
    def undo(self, board : Board, playerIndex : int) -> bool:
        
        """
        Undo the move on the board.
        
        Parameters:
            board (Board): The board on which the move will be played.
            playerIndex (int): The index of the player who plays the move.
            
        Raises:
            TypeError: If board is not a Board object.
            TypeError: If playerIndex is not an integer.
            ValueError: If playerIndex is less than 0 or greater than the number of players.
            
        Returns:
            bool: True if the move has been undone.
        """
        
        pass
    
    @classmethod
    @abstractmethod
    def canPlay(cls, board : Board, line : int, column : int) -> bool:
        
        """
        Checks if the move can be played on the board.
        
        Parameters:
            board (Board): The board on which the move will be played.
            line (int): The line of the move.
            column (int): The column of the move.
            
        Raises:
            TypeError: If board is not a Board object.
            TypeError: If line is not an integer.
            TypeError: If column is not an integer.
            ValueError: If line is less than 0 or greater than the height of the board.
            ValueError: If column is less than 0 or greater than the width of the board.
            
        Returns:
            bool : True if the move can be played, False otherwise.
        """
        
        pass
    
    def getCoordinate(self) -> Coordinate:
        
        """
        Get the coordinate of the move.
        
        Returns:
            Coordinate: The coordinate of the move.
        """
        
        return self.__coordinate__
    
    def getMoveCode(self) -> str:
        
        """
        Get the code of the move.
        
        Returns:
            str: The code of the move.
        """
        
        return self.__moveCode__
    
    def isMoveDone(self) -> bool:
        
        """
        Get the state of the move.
        
        Returns:
            bool: The state of the move.
        """
        
        return self.__isMoveDone__

    def __str__(self) -> str:
        
        """
        Get the string representation of the move.
        
        Returns:
            str: The string representation of the move.
        """
        
        return self.__moveCode__ + encode(self.__coordinate__)
    
    def __repr__(self) -> str:
        
        """
        Get the string representation of the move.
        
        Returns:
            str: The string representation of the move.
        """
        
        return self.__str__()
