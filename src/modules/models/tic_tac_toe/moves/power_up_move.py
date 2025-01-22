from modules.models.board_game.components.move import Move
from modules.models.board_game.components.coordinate import Coordinate
from modules.models.board_game.board.board import Board
from abc import abstractmethod

class PowerUpMove(Move):
    
    """
    A class that represents a power up move.
    """
    
    def __init__(self, moveCode : str, coordinate : Coordinate) -> None:
        
        """
        Constructor for the PowerUpMove class.
        
        Parameters:
            moveCode (str): The move code.
            coordinate (Coordinate): The coordinate.
            
        Raises:
            ValueError: If the coordinate is not an instance of the Coordinate class.
            ValueError: If the move code is not a string.

        Returns:
            None
        """
        
        # Check if the coordinate is an instance of the Coordinate class
        if not isinstance(coordinate, Coordinate):
            raise ValueError("The coordinate must be an instance of the Coordinate class.")
        
        # Check if the move code is a string
        if not isinstance(moveCode, str):
            raise ValueError("The move code must be a string.")
        
        # Call the parent constructor
        super().__init__(moveCode, coordinate)

        return None
    
    @abstractmethod
    def play(self, board : Board, playerIndex : int) -> int :
        
        """
        Plays the move.
        
        Parameters:
            board (Board): The board.
            playerIndex (int): The player index.
            
        Raises:
            ValueError: If the player index is not an integer.
            ValueError: If the player index is not a valid index.
            TypeError: If the board is not a Board object.
            
        Returns:
            bool: True if the move was played, False otherwise.
        """
        
        pass
        
    @abstractmethod
    def undo(self, board : Board, playerIndex : int) -> bool :
        
        """
        Undoes the move.
        
        Parameters:
            board (Board): The board.
            playerIndex (int): The player index.
            
        Raises:
            ValueError: If the player index is not an integer.
            ValueError: If the player index is not a valid index.
            TypeError: If the board is not a Board object.
            
        Returns:
            bool: True if the move was undone, False otherwise.
        """
        
        pass

    @classmethod
    @abstractmethod
    def canPlay(cls, board : Board, line : int, column : int) -> bool:
        
        """
        Checks if a move can be played.
        
        Parameters:
            board (Board): The board.
            line (int): The line.
            column (int): The column.
            
        Raises:
            TypeError : If the board is not a Board object.
            TypeError : If the line and column are not integers. 
            
        Returns:
            bool: True if the move can be played, False otherwise.
        """
        
        pass
    
    def __str__(self) -> str:
        
        """
        Returns the string representation of the move.
        
        Returns:
            str: The string representation of the move.
        """
        
        return super().__str__()