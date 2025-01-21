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
            
        Returns:
            None
        """
        
        super().__init__("b", coordinate)
        
        self.__deletedEntities__ : list[tuple[Entity, bool]] = []
        
        return None
    
    def play(self, board : Board, playerIndex : int) -> None :
        
        """
        Plays the bomb move.
        
        Parameters:
            board (Board) : The board to play the move on.
            playerIndex (int) : The index of the player playing the move.

        Returns:
            None
        """
        
        line : int = self.__coordinate__.getLine()
        column : int = self.__coordinate__.getColumn()

        if(line < 0 or line > board.getHeight()) : return False
        if(column < 0 or column > board.getWidth()) : return False
        
        for currentLine in range(line - 1, line + 2):
            for currentColumn in range(column - 1, column + 2):
                
                if(0 <= currentLine < board.getHeight() and 0 <= currentColumn < board.getWidth()):

                    self.__deletedEntities__.append((board.getEntityAt(currentLine, currentColumn), board.isCaseBlocked(currentLine, currentColumn)))

                    board.removeEntityAt(currentLine, currentColumn)
                    board.setIsCaseBlocked(currentLine, currentColumn, False)

        self.__isMoveDone__ = True
        
        return None

    def undo(self, board : Board, playerIndex : int) -> None:
        
        """
        Undoes the bomb move.
        
        Parameters:
            board (Board) : The board to undo the move on.
            playerIndex (int) : The index of the player playing the move.
            
        Returns:
            None
        """
        
        line : int = self.__coordinate__.getLine()
        column : int = self.__coordinate__.getColumn()

        if(line < 0 or line > board.getHeight()) : return False
        if(column < 0 or column > board.getWidth()) : return False

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

        self.__deletedEntities__ = []
        self.__isMoveDone__ = False
        
        return None
        
    @classmethod
    def canPlay(cls, board : Board, line : int, column : int) -> bool:
        
        """
        Checks if a bomb move can be played.
        
        Parameters:
            board (Board) : The board to check the move on.
            line (int) : The line of the move.
            column (int) : The column of the move.
            
        Returns:
            bool : True if the move can be played, False otherwise.
        """
        
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