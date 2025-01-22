from enum import Enum
from modules.models.board_game.components.coordinate import Coordinate
from modules.models.board_game.board.board import Board
from modules.models.board_game.components.move import Move

class SimpleMove(Move) :
    
    """
    A class that represents a simple move.
    """
    
    def __init__(self, coordinate : Coordinate) -> None :
        
        """
        Constructor for the SimpleMove class.
        
        Parameters:
            coordinate (Coordinate): The coordinate.
            
        Raises:
            ValueError: If the coordinate is not a Coordinate object.
            
        Returns:
            None
        """
        
        # Check if the coordinate is a Coordinate object
        if not isinstance(coordinate, Coordinate): 
            raise ValueError("The coordinate must be a Coordinate object.")
        
        # Call the parent constructor
        super().__init__("", coordinate)
        
        return None

    def play(self, board : Board, playerIndex : int) -> bool :
        
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
            bool : True if the move was played, False otherwise.
        """
        
        # Check if the board is a Board object
        if not isinstance(board, Board):
            raise TypeError("The board must be a Board object.")
        
        # Check if the player index is an integer
        if not isinstance(playerIndex, int):
            raise ValueError("The player index must be an integer.")
        
        # Check if the player index is a valid index
        if playerIndex < 0 or playerIndex >= board.getPlayerCount():
            raise ValueError("The player index must be a valid index.")

        # Get the line and column
        line : int = self.__coordinate__.getLine()
        column : int = self.__coordinate__.getColumn()

        # Check if the line and column are in the board
        if(line < 0 or line > board.getHeight()) : 
            raise ValueError(f"Line is out of range. Should be from 0 to {board.getHeight()} but was <{line}>")
        
        if(column < 0 or column > board.getWidth()) : 
            raise ValueError(f"Column is out of range. Should be from 0 to {board.getWidth()} but was <{column}>")

        # Check if the case is availlable
        if(not board.isCaseAvaillable(line, column)) : 
            raise ValueError(f"Can't play at line = {line}, column = {column}. Case is already taken.")

        # Add the player entity at the line and column
        board.addPlayerEntityAt(line, column, playerIndex)
        
        return True

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
            bool: True if the move was undone.
        """
        
        # Check if the board is a Board object
        if not isinstance(board, Board):
            raise TypeError("The board must be a Board object.")
        
        # Check if the player index is an integer
        if not isinstance(playerIndex, int):
            raise ValueError("The player index must be an integer.")
        
        # Check if the player index is a valid index
        if playerIndex < 0 or playerIndex >= board.getPlayerCount():
            raise ValueError("The player index must be a valid index.")
        
        # Get the line and column
        line : int = self.__coordinate__.getLine()
        column : int = self.__coordinate__.getColumn()

        # Check if the line and column are in the board
        if(line < 0 or line > board.getHeight()):
            raise ValueError(f"Line is out of range. Should be from 0 to {board.getHeight()} but was <{line}>")
        
        if(column < 0 or column > board.getWidth()): 
            raise ValueError(f"Column is out of range. Should be from 0 to {board.getWidth()} but was <{column}>")

        # Check if the case is taken
        if(not board.isEntityAt(line, column)) : raise ValueError(f"Can't cancel move at line = {line}, column = {column}. Case is not taken.")

        # Remove the entity at the line and column
        board.removeEntityAt(line, column)
        
        return True

    @classmethod
    def canPlay(cls, board : Board, line : int, column : int) -> bool :
        
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
        
        # Check if the board is a Board object
        if not isinstance(board, Board):
            raise TypeError("The board must be a Board object.")
        
        # Check if the line and column are integers
        if not isinstance(line, int) or not isinstance(column, int):
            raise TypeError("The line and column must be integers.")
        
        if(line < 0 or line > board.getHeight()) : return False
        if(column < 0 or column > board.getWidth()) : return False

        return board.isCaseAvaillable(line, column)

    def __str__(self) -> str:
        
        """
        Returns the string representation of the move.
        
        Returns:
            str: The string representation of the move.
        """
        
        return super().__str__()