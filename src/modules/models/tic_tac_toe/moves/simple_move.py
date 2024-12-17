from enum import Enum
from modules.models.board_components.coordinate import Coordinate
from modules.models.board_components.board import Board
from modules.models.tic_tac_toe.move import Move
from modules.models.board_components.entity import Entity

class SimpleMove(Move) :
    
    def __init__(self, coordinate : Coordinate, entity : Entity) -> None :
        
        super().__init__("", coordinate, entity)
        
        return None

    def play(self, board : Board) -> None :
        
        line : int = self.__coordinate__.getLine()
        column : int = self.__coordinate__.getColumn()

        if(line < 0 or line > board.getHeight()) : raise ValueError(f"Line is out of range. Should be from 0 to {board.getHeight()} but was <{line}>")
        if(column < 0 or column > board.getWidth()) : raise ValueError(f"Column is out of range. Should be from 0 to {board.getWidth()} but was <{column}>")

        if(not board.isCaseAvaillable(line, column)) : raise ValueError(f"Can't play at line = {line}, column = {column}. Case is already taken.")

        board.setEntityAt(line, column, self.__entityToPlay__)
        
        return None

    @classmethod
    def canPlay(cls, board : Board, line : int, column : int) -> bool :
        
        if(line < 0 or line > board.getHeight()) : return False
        if(column < 0 or column > board.getWidth()) : return False

        return board.isCaseAvaillable(line, column)
