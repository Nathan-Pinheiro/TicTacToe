from modules.models.board.board import Board
from modules.models.board.case import Case
from modules.models.entities.entity import Entity
from modules.models.tic_tac_toe.win_conditions.win_condition import WinCondition
from modules.models.tic_tac_toe.win_conditions.game_result import GameState, GameStatus
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
                
                case : Case = board.getCase(line, column)

                if(case.isAvaillable()):
                    
                    isDraw = False
                    if(self.__isCaseWinning__(board, case)) : return GameState(GameStatus.VICTORY, case.getEntity())


        if(isDraw) : return GameState(GameStatus.DRAW)
        else : return GameState(GameStatus.UNFINISHED)

    @private_method
    def __isCaseWinning__(self, board: Board, case: Case) -> bool:
        """
        Check if the given case is part of a winning line.

        Args:
            board (Board): The game board.
            case (Case): The case to check.

        Returns:
            bool: True if the case is part of a winning line, False otherwise.
        """
        
        if case.getEntity() is None: return False

        entity : Entity = case.getEntity()
        line : int = case.getCoordinate().getLine() 
        column : int = case.getCoordinate().getColumn()
        
        return (
            self.__checkAlignInDirection__(board, entity, line, column, 1, 0) or  # Horizontal
            self.__checkAlignInDirection__(board, entity, line, column, 0, 1) or  # Vertical
            self.__checkAlignInDirection__(board, entity, line, column, 1, 1) or  # Diagonal (top-left to bottom-right)
            self.__checkAlignInDirection__(board, entity, line, column, 1, -1)    # Diagonal (top-right to bottom-left)
        )

    @private_method
    def __checkAlignInDirection__(self, board: Board, entity, startLine: int, startColumn: int, lineDirection: int, columnDirection: int) -> bool:
        """
        Check if a specific direction contains a winning line.

        Args:
            board (Board): The game board.
            entity (Entity): The entity to check for.
            startLine (int): Starting line.
            startColumn (int): Starting column.
            lineDirection (int): Direction increment for line.
            columnDirection (int): Direction increment for column.

        Returns:
            bool: True if there is a winning line in the direction, False otherwise.
        """
        count = 0

        for line in range(startLine, startLine + self.__entityToAlign__, lineDirection):
            for column in range(startColumn, startColumn + self.__entityToAlign__, columnDirection):
                
                if line < 0 or line >= board.getHeight() : return False
                if column < 0 or column >= board.getWidth() : return False
                    
                case = board.getCase(line, column)
                if case and case.getEntity() == entity: count += 1
                    
        if count == self.__entityToAlign__: return True
        return False
        
        