from enum import Enum
from modules.models.board_game.components.coordinate import Coordinate
from modules.models.board_game.board.board import Board
from modules.models.board_game.components.move import Move

class SimpleMove(Move) :
    
    def __init__(self, coordinate : Coordinate) -> None :
        
        super().__init__("", coordinate)
        
        return None

    def play(self, board : Board, playerIndex : int) -> bool :

        line : int = self.__coordinate__.getLine()
        column : int = self.__coordinate__.getColumn()

        if(line < 0 or line > board.getHeight()) : 
            #raise ValueError(f"Line is out of range. Should be from 0 to {board.getHeight()} but was <{line}>")
            return False
        if(column < 0 or column > board.getWidth()) : 
            #raise ValueError(f"Column is out of range. Should be from 0 to {board.getWidth()} but was <{column}>")
            return False

        if(not board.isCaseAvaillable(line, column)) : 
            #raise ValueError(f"Can't play at line = {line}, column = {column}. Case is already taken.")
            return False

        board.addPlayerEntityAt(line, column, playerIndex)
        
        return True

    def undo(self, board : Board, playerIndex : int) -> None :

        line : int = self.__coordinate__.getLine()
        column : int = self.__coordinate__.getColumn()

        if(line < 0 or line > board.getHeight()) : raise ValueError(f"Line is out of range. Should be from 0 to {board.getHeight()} but was <{line}>")
        if(column < 0 or column > board.getWidth()) : raise ValueError(f"Column is out of range. Should be from 0 to {board.getWidth()} but was <{column}>")

        if(not board.isEntityAt(line, column)) : raise ValueError(f"Can't cancel move at line = {line}, column = {column}. Case is not taken.")

        board.removeEntityAt(line, column)

    @classmethod
    def canPlay(cls, board : Board, line : int, column : int) -> bool :
        
        if(line < 0 or line > board.getHeight()) : return False
        if(column < 0 or column > board.getWidth()) : return False

        return board.isCaseAvaillable(line, column)

    def __str__(self):
        return super().__str__()