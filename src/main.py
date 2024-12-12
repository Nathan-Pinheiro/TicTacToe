from modules.models.board import Board
from modules.models.coordinate_encoder import *
from modules.models.case import Case
from modules.models.coordinate import *

if(__name__ == "__main__"):
    
    width : int = 5
    height : int = 5

    board = Board(width, height)
   
    for line in range(height):
        for column in range(width):
            case : Case = board.getCase(line, column)
            print(encode(case.getCoordinate()))