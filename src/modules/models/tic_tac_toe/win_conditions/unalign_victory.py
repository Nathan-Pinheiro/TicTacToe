from modules.models.board_game.board.board import Board
from modules.models.board_game.components.win_condition import WinCondition
from modules.models.board_game.game.game_outcome import GameOutcome, GameOutcomeStatus

MIN_ENTITY_TO_ALIGN = 3

class UnalignVictory(WinCondition) :
    
    """
    Defines a win condition where forming a specific alignment results in a loss.
    This inversion of traditional win conditions creates a game dynamic where players must avoid forming alignments.
    """

    def __init__(self, alignLength : int, playerAmount : int) -> None:
        
        """
        Initializes the UnalignVictory condition with alignment length and total player count.

        Parameters:
            alignLength (int): Number of consecutive entities that trigger a loss.
            playerAmount (int): Total number of players in the game.
        
        Raises:
            ValueError: If alignLength is less than the minimum required (3).
        """

        if(alignLength < MIN_ENTITY_TO_ALIGN): raise ValueError(f"Can't create an UnalignVictory with {alignLength} entity to align. It must be higher or equals than {MIN_ENTITY_TO_ALIGN}")
        
        self.__alignLength__ : int = alignLength
        self.__playerAmount__ : int = playerAmount
        
        return None

    def checkWin(self, board : Board) -> GameOutcome:

        """
        Checks if any player has formed an alignment that results in their loss.
        The next player in sequence is declared the winner.

        Parameters:
            board (Board): The current state of the game board.
        
        Returns:
            GameOutcome: VICTORY for the next player, DRAW if the board is full, or UNFINISHED if the game continues.
        """

        winnerIndex : int = board.checkIfPlayerHaveAlignment(self.__alignLength__)

        if(winnerIndex != -1) : return GameOutcome(GameOutcomeStatus.VICTORY, (winnerIndex + 1) % self.playerAmount)
        elif(board.isFull()) : return GameOutcome(GameOutcomeStatus.DRAW)
        else : return GameOutcome(GameOutcomeStatus.UNFINISHED)
    
    def checkWinForPlayer(self, playerIndex : int, board : Board) -> GameOutcome:

        """
        Checks if a specific player has formed a losing alignment.
        If so, the next player wins.

        Parameters:
            playerIndex (int): The index of the player to check.
            board (Board): The current game board.
        
        Returns:
            GameOutcome: VICTORY for the next player, DRAW if the board is full, or UNFINISHED if the game continues.
        """

        if(board.checkAlignmentForPlayer(playerIndex, self.__alignLength__)) : return GameOutcome(GameOutcomeStatus.VICTORY, (playerIndex + 1) % self.playerAmount)
        elif(board.isFull()) : return GameOutcome(GameOutcomeStatus.DRAW)
        else : return GameOutcome(GameOutcomeStatus.UNFINISHED)

    def evaluateForPlayer(self, playerToEvaluateIndex : int, board : Board) -> int:
        
        """
        Evaluates the board state for a specific player, penalizing stronger alignments.
        Higher scores indicate a greater risk of losing.

        Parameters:
            playerToEvaluateIndex (int): The index of the player to evaluate.
            board (Board): The current game board.
        
        Returns:
            int: A normalized score reflecting the player's risk.
        """

        playerAlignStrength : int = 0
        oponentsAlignStrength : int = 0

        for alignLength in range(2, self.__alignLength__) :
            for playerIndex in range(0, len(board.getPlayerEntities())):
                if(playerIndex == playerToEvaluateIndex): playerAlignStrength += 2**alignLength * board.checkAlignmentForPlayer(playerIndex, alignLength)
                else : oponentsAlignStrength += 2**alignLength * board.checkAlignmentForPlayer(playerIndex, alignLength)

        totalStrength = playerAlignStrength + oponentsAlignStrength
        
        if totalStrength == 0: return 0.0
        else : return (oponentsAlignStrength - playerAlignStrength) / totalStrength