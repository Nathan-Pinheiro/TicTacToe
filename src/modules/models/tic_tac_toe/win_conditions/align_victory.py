from modules.models.board_components.board import Board
from modules.models.tic_tac_toe.win_condition import WinCondition
from modules.models.tic_tac_toe.game_outcome import GameOutcome, GameOutcomeStatus
from modules.models.tic_tac_toe.game_state import GameState
from modules.utils.decorator import privatemethod

MIN_ENTITY_TO_ALIGN = 3

class AlignVictory(WinCondition) :
    
    def __init__(self, alignLength : int) -> None:
        
        if(alignLength < MIN_ENTITY_TO_ALIGN): raise ValueError(f"Can't create an AlignVictory with {alignLength} entity to align. It must be higher or equals than {MIN_ENTITY_TO_ALIGN}")
        
        self.__alignLength__ = alignLength
        
        return None

    def checkWin(self, board : Board) -> GameOutcome:

        winnerIndex : int = board.checkIfPlayerHaveAlignment(self.__alignLength__)

        if(winnerIndex != -1) : return GameOutcome(GameOutcomeStatus.VICTORY, winnerIndex)
        elif(board.isFull()) : return GameOutcome(GameOutcomeStatus.DRAW)
        else : return GameOutcome(GameOutcomeStatus.UNFINISHED)
    
    def checkWinForPlayer(self, playerIndex : int, board : Board) -> GameOutcome:

        if(board.checkAlignmentForPlayer(playerIndex, self.__alignLength__)) : return GameOutcome(GameOutcomeStatus.VICTORY, playerIndex)
        elif(board.isFull()) : return GameOutcome(GameOutcomeStatus.DRAW)
        else : return GameOutcome(GameOutcomeStatus.UNFINISHED)

    def evaluateForPlayer(self, playerToEvaluateIndex : int, board : Board) -> int:
        
        playerAlignStrength : int = 0
        oponentsAlignStrength : int = 0

        for alignLength in range(2, self.__alignLength__) :
            for playerIndex in range(0, len(board.getPlayerEntities())):
                if(playerIndex == playerToEvaluateIndex): playerAlignStrength += 2**alignLength * board.checkAlignmentForPlayer(playerIndex, alignLength)
                else : oponentsAlignStrength += 2**alignLength * board.checkAlignmentForPlayer(playerIndex, alignLength)

        totalStrength = playerAlignStrength + oponentsAlignStrength
        
        if totalStrength == 0: return 0.0
        else : return (playerAlignStrength - oponentsAlignStrength) / totalStrength