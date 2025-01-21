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

        Returns:
            None
        """
        
        super().__init__(moveCode, coordinate)

        return None
    
    @abstractmethod
    def play(self, board : Board, playerIndex : int) -> None :
        
        """
        Plays the move.
        
        Parameters:
            board (Board): The board.
            playerIndex (int): The player index.
            
        Returns:
            None
        """
        
        pass
        
    @abstractmethod
    def undo(self, board : Board, playerIndex : int) -> None :
        
        """
        Undoes the move.
        
        Parameters:
            board (Board): The board.
            playerIndex (int): The player index.
            
        Returns:
            None
        """
        
        pass

    @classmethod
    def canPlay(cls, board : Board, line : int, column : int) -> bool:
        
        """
        Checks if a move can be played.
        
        Parameters:
            board (Board): The board.
            line (int): The line.
            column (int): The column.
            
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