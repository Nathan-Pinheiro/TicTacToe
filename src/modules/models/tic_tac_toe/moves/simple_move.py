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
            
        Returns:
            None
        """
        
        super().__init__("", coordinate)
        
        return None

    def play(self, board : Board, playerIndex : int) -> bool :
        
        """
        Plays the move.

        Parameters:
            board (Board): The board.
            playerIndex (int): The player index.

        Returns:
            bool : True if the move was played, False otherwise.
        """

        line : int = self.__coordinate__.getLine()
        column : int = self.__coordinate__.getColumn()

        if(line < 0 or line > board.getHeight()) : 
            raise ValueError(f"Line is out of range. Should be from 0 to {board.getHeight()} but was <{line}>")
            return False
        if(column < 0 or column > board.getWidth()) : 
            raise ValueError(f"Column is out of range. Should be from 0 to {board.getWidth()} but was <{column}>")
            return False

        if(not board.isCaseAvaillable(line, column)) : 
            raise ValueError(f"Can't play at line = {line}, column = {column}. Case is already taken.")
            return False

        board.addPlayerEntityAt(line, column, playerIndex)
        
        return True

    def undo(self, board : Board, playerIndex : int) -> None :
        
        """
        Undoes the move.

        Parameters:
            board (Board): The board.
            playerIndex (int): The player index.
            
        Returns:
            None
        """

        line : int = self.__coordinate__.getLine()
        column : int = self.__coordinate__.getColumn()

        if(line < 0 or line > board.getHeight()) : raise ValueError(f"Line is out of range. Should be from 0 to {board.getHeight()} but was <{line}>")
        if(column < 0 or column > board.getWidth()) : raise ValueError(f"Column is out of range. Should be from 0 to {board.getWidth()} but was <{column}>")

        if(not board.isEntityAt(line, column)) : raise ValueError(f"Can't cancel move at line = {line}, column = {column}. Case is not taken.")

        board.removeEntityAt(line, column)
        
        return None

    @classmethod
    def canPlay(cls, board : Board, line : int, column : int) -> bool :
        
        """
        Checks if a move can be played.
        
        Parameters:
            board (Board): The board.
            line (int): The line.
            column (int): The column.
            
        Returns:
            bool: True if the move can be played, False otherwise.
        """
        
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