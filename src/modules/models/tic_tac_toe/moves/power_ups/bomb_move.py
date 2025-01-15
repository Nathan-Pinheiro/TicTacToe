from modules.models.tic_tac_toe.moves.power_up_move import PowerUpMove
from modules.models.board_game.components.coordinate import Coordinate
from modules.models.board_game.components.entity import Entity
from modules.models.board_game.board.board import Board
from modules.models.utils.console_displayer import *

class BombMove(PowerUpMove):
    
    def __init__(self, coordinate : Coordinate) -> None:
        
        super().__init__("b", coordinate)
        
        self.__deletedEntities__ : list[tuple[Entity, bool]] = []
    
    def play(self, board : Board, playerIndex : int) -> None :
        
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

    def undo(self, board : Board, playerIndex : int) -> None:
        
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
        
    @classmethod
    def canPlay(cls, board : Board, line : int, column : int) -> bool:
        
        if(line < 0 or line > board.getHeight()) : return False
        if(column < 0 or column > board.getWidth()) : return False
        
        return True
    
    def __str__(self):
        return super().__str__()