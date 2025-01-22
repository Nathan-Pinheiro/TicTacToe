from modules.models.tic_tac_toe.moves.power_up_move import PowerUpMove
from modules.models.board_game.components.coordinate import Coordinate
from modules.models.board_game.components.entity import Entity
from modules.models.board_game.board.board import Board
from modules.models.displayer.console_displayer import *

class BombMove(PowerUpMove):
    
    """
    Represents a bomb move.
    """
    
    def __init__(self, coordinate : Coordinate) -> None:
        
        """
        Constructor for the BombMove class.
        
        Parameters:
            coordinate (Coordinate) : The coordinate of the bomb.
            
        Raises:
            TypeError : If the coordinate is not a Coordinate object.
            
        Returns:
            None
        """
        
        # Check if the coordinate is a Coordinate object
        if not isinstance(coordinate, Coordinate): 
            raise TypeError("The coordinate must be a Coordinate object.")
        
        # Call the parent constructor
        super().__init__("b", coordinate)
        
        # The list of deleted entities
        self.__deletedEntities__ : list[tuple[Entity, bool]] = []
        
        return None
    
    def play(self, board : Board, playerIndex : int) -> bool:
        
        """
        Plays the bomb move.
        
        Parameters:
            board (Board) : The board to play the move on.
            playerIndex (int) : The index of the player playing the move.
            
        Raises:
            TypeError : If the board is not a Board object.
            ValueError : If the player index is not an integer.
            ValueError : If the player index is not a valid index.

        Returns:
            bool: True if the move was played, False otherwise.
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
        
        # Get the line and column of the bomb
        line : int = self.__coordinate__.getLine()
        column : int = self.__coordinate__.getColumn()

        # Check if the line and column are valid
        if(line < 0 or line > board.getHeight()) : return False
        if(column < 0 or column > board.getWidth()) : return False
        
        # Delete the entities around the bomb
        for currentLine in range(line - 1, line + 2):
            for currentColumn in range(column - 1, column + 2):
                
                if(0 <= currentLine < board.getHeight() and 0 <= currentColumn < board.getWidth()):

                    self.__deletedEntities__.append((board.getEntityAt(currentLine, currentColumn), board.isCaseBlocked(currentLine, currentColumn)))

                    board.setIsCaseBlocked(currentLine, currentColumn, False)
                    board.removeEntityAt(currentLine, currentColumn)

        # The move is done
        self.__isMoveDone__ = True
        
        return True

    def undo(self, board : Board, playerIndex : int) -> bool:
        
        """
        Undoes the bomb move.
        
        Parameters:
            board (Board) : The board to undo the move on.
            playerIndex (int) : The index of the player playing the move.
            
        Raises:
            TypeError : If the board is not a Board object.
            ValueError : If the player index is not an integer.
            ValueError : If the player index is not a valid index.
            
        Returns:
            bool: True if the move was undone, False otherwise.
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
        
        # Get the line and column of the bomb
        line : int = self.__coordinate__.getLine()
        column : int = self.__coordinate__.getColumn()

        # Check if the line and column are valid
        if(line < 0 or line > board.getHeight()) : return False
        if(column < 0 or column > board.getWidth()) : return False

        # Add the entities around the bomb
        deletedEntityIndex : int = 0

        for currentLine in range(line - 1, line + 2):
            for currentColumn in range(column - 1, column + 2):

                if(0 <= currentLine < board.getHeight() and 0 <= currentColumn < board.getWidth()):

                    deletedEntityData : tuple[Entity, bool] = self.__deletedEntities__[deletedEntityIndex]
                    
                    entity : Entity = deletedEntityData[0]
                    wasCaseBlocked : bool = deletedEntityData[1]

                    if(entity != None) : board.addEntityAt(currentLine, currentColumn, entity)
                    board.setIsCaseBlocked(currentLine, currentColumn, wasCaseBlocked)
                    
                    deletedEntityIndex += 1

        # The move is undone
        self.__deletedEntities__ = []
        self.__isMoveDone__ = False
        
        return True
        
    @classmethod
    def canPlay(cls, board : Board, line : int, column : int) -> bool:
        
        """
        Checks if a bomb move can be played.
        
        Parameters:
            board (Board) : The board to check the move on.
            line (int) : The line of the move.
            column (int) : The column of the move.
            
        Raises:
            TypeError : If the board is not a Board object.
            TypeError : If the line and column are not integers.
            
        Returns:
            bool : True if the move can be played, False otherwise.
        """
        
        # Check if board is a Board object
        if not isinstance(board, Board):
            raise TypeError("The board must be a Board object.")
        
        # Check if the line and column are valid
        if not isinstance(line, int) or not isinstance(column, int):
            raise TypeError("The line and column must be integers.")
        
        if(line < 0 or line > board.getHeight()) : return False
        if(column < 0 or column > board.getWidth()) : return False
        
        return True
    
    def __str__(self) -> str:
        
        """
        Returns the string representation of the bomb move.
        
        Returns:
            str : The string representation of the bomb move.
        """
        
        return super().__str__()