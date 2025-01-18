from modules.models.board_game.board.board import Board
from modules.models.board_game.components.win_condition import WinCondition
from modules.models.board_game.game.game_outcome import GameOutcome, GameOutcomeStatus

MIN_ENTITY_TO_ALIGN = 3

class AlignVictory(WinCondition) :
    
    """
    Defines a win condition based on aligning a specified number of consecutive entities on the board.
    This is commonly used in games like Tic Tac Toe or Connect Four.
    """

    def __init__(self, alignLength : int) -> None:
        
        """
        Initializes the AlignVictory condition with a required alignment length.

        Parameters:
            alignLength (int): The number of consecutive entities needed to win.

        Raises:
            ValueError: If alignLength is less than the minimum required (3).
        """

        if(alignLength < MIN_ENTITY_TO_ALIGN): raise ValueError(f"Can't create an AlignVictory with {alignLength} entity to align. It must be higher or equals than {MIN_ENTITY_TO_ALIGN}")
        
        self.__alignLength__ = alignLength

    def checkWin(self, board : Board) -> GameOutcome:

        """
        Checks if any player has achieved the required alignment length to win.

        Parameters:
            board (Board): The current state of the game board.
        
        Returns:
            GameOutcome: VICTORY if a player wins, DRAW if the board is full, or UNFINISHED if the game continues.
        """

        winnerIndex : int = board.checkIfPlayerHaveAlignment(self.__alignLength__)

        if(winnerIndex != -1) : return GameOutcome(GameOutcomeStatus.VICTORY, winnerIndex)
        elif(board.isFull()) : return GameOutcome(GameOutcomeStatus.DRAW)
        else : return GameOutcome(GameOutcomeStatus.UNFINISHED)
    
    def checkWinForPlayer(self, playerIndex : int, board : Board) -> GameOutcome:

        """
        Checks if a specific player has achieved the alignment required to win.

        Parameters:
            playerIndex (int): The index of the player to check.
            board (Board): The current game board.
        
        Returns:
            GameOutcome: VICTORY if the player wins, DRAW if the board is full, or UNFINISHED if the game continues.
        """

        if(board.checkAlignmentForPlayer(playerIndex, self.__alignLength__)) : return GameOutcome(GameOutcomeStatus.VICTORY, playerIndex)
        elif(board.isFull()) : return GameOutcome(GameOutcomeStatus.DRAW)
        else : return GameOutcome(GameOutcomeStatus.UNFINISHED)

    def evaluateForPlayer(self, playerToEvaluateIndex : int, board : Board) -> int:
        
        """
        Evaluates the board state for a specific player, providing a heuristic score based on alignment strength.
        Higher scores indicate a stronger position for the evaluated player.

        Parameters:
            playerToEvaluateIndex (int): The index of the player to evaluate.
            board (Board): The current game board.
        
        Returns:
            int: A normalized score representing the player's advantage.
        """

        playerAlignStrength : int = 0
        oponentsAlignStrength : int = 0

        for pieceCount in range(2, self.__alignLength__) :
            for playerIndex in range(0, len(board.getPlayerEntities())):
                
                if(playerIndex == playerToEvaluateIndex): playerAlignStrength += 2 * pieceCount * board.countAvaillableLineOfAtLeastGivenPiece(playerIndex, self.__alignLength__, pieceCount)
                else : oponentsAlignStrength += 2 * pieceCount * board.countAvaillableLineOfAtLeastGivenPiece(playerIndex, self.__alignLength__, pieceCount)

        totalStrength = playerAlignStrength + oponentsAlignStrength
        
        if totalStrength == 0: return 0.0
        
        score : int = (playerAlignStrength - oponentsAlignStrength) / totalStrength

        if(score == 1.0) : return 0.99
        elif(score == -1.0) : return -0.99
        else : return score