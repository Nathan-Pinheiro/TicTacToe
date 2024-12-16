from modules.models.board_components.board import Board
from modules.models.board_components.entity import Entity
from modules.models.tic_tac_toe.win_condition import WinCondition
from modules.models.tic_tac_toe.game_result import GameState, GameStatus
from modules.models.board_components.directions import Directions
from modules.utils.decorator import private_method

MIN_ENTITY_TO_ALIGN = 3

class AlignVictory(WinCondition) :
    
    def __init__(self, entityToAlign : int) -> None:
        
        if(entityToAlign < MIN_ENTITY_TO_ALIGN): raise ValueError(f"Can't create an AlignVictory with {entityToAlign} entity to align. It must be higher or equals than {MIN_ENTITY_TO_ALIGN}")
        
        self.__entityToAlign__ = entityToAlign
        
        return None

    def checkWin(self, board : Board) -> GameState:

        isDraw : bool = True

        for line in range(0, board.getHeight()):
            for column in range(0, board.getWidth()):

                if(board.isCaseAvaillable(line, column)): 
                    isDraw = False
                elif(self.__isCaseWinning__(board, line, column)) : 
                    return GameState(GameStatus.VICTORY, board.getEntityAt(line, column))

        if(isDraw) : return GameState(GameStatus.DRAW)
        else : return GameState(GameStatus.UNFINISHED)

    @private_method
    def __isCaseWinning__(self, board: Board, line : int, column : int) -> bool:
        """
        Check if the given case is part of a winning line.

        Args:
            board (Board): The game board.
            case (Case): The case to check.

        Returns:
            bool: True if the case is part of a winning line, False otherwise.
        """
        
        entity : Entity = board.getEntityAt(line, column)

        if entity is None: return False
        
        return (
            board.isLineConsituedBySameEntity(line, column, self.__entityToAlign__, Directions.HORIZONTAL) or
            board.isLineConsituedBySameEntity(line, column, self.__entityToAlign__, Directions.VERTICAL) or
            board.isLineConsituedBySameEntity(line, column, self.__entityToAlign__, Directions.ASCENDANT_DIAGONAL) or
            board.isLineConsituedBySameEntity(line, column, self.__entityToAlign__, Directions.DESCENDANT_DIAGONAL)
        )