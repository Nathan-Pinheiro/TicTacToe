from modules.models.board_game.board.board import Board
from modules.models.board_game.components.win_condition import WinCondition
from modules.models.board_game.game.game_outcome import GameOutcome, GameOutcomeStatus

MIN_ENTITY_TO_ALIGN = 3

class UnalignVictory(WinCondition) :
    
    """
    Defines a win condition where forming a specific alignment results in a loss.
    This inversion of traditional win conditions creates a game dynamic where players must avoid forming alignments.
    """

    def __init__(self, alignLength : int) -> None:
        
        """
        Initializes the UnalignVictory condition with alignment length and total player count.

        Parameters:
            alignLength (int): Number of consecutive entities that trigger a loss.
            playerAmount (int): Total number of players in the game.
            
        Raises:
            ValueError: If the alignment length is less than 3.
        
        Returns:
            None
        """
        
        # Check if the alignment length is an integer and greater than 2
        if not isinstance(alignLength, int): 
            raise TypeError("The alignment length must be an integer.")

        if(alignLength < MIN_ENTITY_TO_ALIGN): 
            raise ValueError(f"Can't create an UnalignVictory with {alignLength} entity to align. It must be higher or equals than {MIN_ENTITY_TO_ALIGN}")
        
        # Set the alignment length
        self.__alignLength__ : int = alignLength
        
        return None

    def checkWin(self, board : Board) -> GameOutcome:

        """
        Checks if any player has formed an alignment that results in their loss.
        The next player in sequence is declared the winner.

        Parameters:
            board (Board): The current state of the game board.
            
        Raises:
            TypeError: If the board is not a Board object
        
        Returns:
            GameOutcome: VICTORY for the next player, DRAW if the board is full, or UNFINISHED if the game continues.
        """
        
        # Check if the board is a Board object
        if not isinstance(board, Board):
            raise TypeError("The board must be a Board object.")

        # Check if a player has formed an alignment
        winnerIndex : int = board.checkIfPlayerHaveAlignment(self.__alignLength__)

        # Return the game outcome based on the alignment
        if(winnerIndex != -1) : return GameOutcome(GameOutcomeStatus.VICTORY, (winnerIndex + 1) % len(board.getPlayerEntities()))
        elif(board.isFull()) : return GameOutcome(GameOutcomeStatus.DRAW)
        else : return GameOutcome(GameOutcomeStatus.UNFINISHED)
    
    def checkWinForPlayer(self, playerIndex : int, board : Board) -> GameOutcome:

        """
        Checks if a specific player has formed a losing alignment.
        If so, the next player wins.

        Parameters:
            playerIndex (int): The index of the player to check.
            board (Board): The current game board.
            
        Raises:
            TypeError: If the board is not a Board object.
            ValueError: If the player index is not an integer or is out of bounds
        
        Returns:
            GameOutcome: VICTORY for the next player, DRAW if the board is full, or UNFINISHED if the game continues.
        """
        
        # Check if the board is a Board object
        if not isinstance(board, Board):
            raise TypeError("The board must be a Board object.")
        
        # Check if the player index is an integer and in bounds
        if not isinstance(playerIndex, int):
            raise ValueError("The player index must be an integer.")
        
        if playerIndex < 0 or playerIndex >= board.getPlayerCount():
            raise ValueError("The player index must be a valid index.")

        # Check if the player has formed an alignment that results in a loss and return the game outcome
        if(board.checkAlignmentForPlayer(playerIndex, self.__alignLength__)) : return GameOutcome(GameOutcomeStatus.VICTORY, (playerIndex + 1) % len(board.getPlayerEntities()))
        elif(board.isFull()) : return GameOutcome(GameOutcomeStatus.DRAW)
        else : return GameOutcome(GameOutcomeStatus.UNFINISHED)

    def evaluateForPlayer(self, playerToEvaluateIndex : int, board : Board) -> int:
        
        """
        Evaluates the board state for a specific player, penalizing stronger alignments.
        Higher scores indicate a greater risk of losing.

        Parameters:
            playerToEvaluateIndex (int): The index of the player to evaluate.
            board (Board): The current game board.
            
        Raises:
            TypeError: If the board is not a Board object.
            ValueError: If the playerToEvaluateIndex is not an integer or is out of bounds.
        
        Returns:
            int: A normalized score reflecting the player's risk.
        """
        
        # Check if the board is a Board object
        if not isinstance(board, Board):
            raise TypeError("The board must be a Board object.")
        
        # Check if the player index is an integer and in bounds
        if not isinstance(playerToEvaluateIndex, int):
            raise ValueError("The player index must be an integer.")
        
        if playerToEvaluateIndex < 0 or playerToEvaluateIndex >= board.getPlayerCount():
            raise ValueError("The player index must be a valid index.")

        # Initialize the alignment strength for the player and opponents
        playerAlignStrength : int = 0
        oponentsAlignStrength : int = 0

        # Check the alignment strength for each player
        for pieceCount in range(2, self.__alignLength__) :
            for playerIndex in range(0, len(board.getPlayerEntities())):
                
                ## Check if the player is the one to evaluate or an opponent and update the alignment strength
                if(playerIndex == playerToEvaluateIndex): playerAlignStrength += 2 * pieceCount * board.countAvaillableLineOfAtLeastGivenPiece(playerIndex, self.__alignLength__, pieceCount)
                else : oponentsAlignStrength += 2 * pieceCount * board.countAvaillableLineOfAtLeastGivenPiece(playerIndex, self.__alignLength__, pieceCount)

        # Calculate the total alignment strength
        totalStrength = playerAlignStrength + oponentsAlignStrength
        
        # Return 0 if the total strength is 0
        if totalStrength == 0: return 0.0
        
        # Calculate the score based on the alignment strength
        score : int = (playerAlignStrength - oponentsAlignStrength) / totalStrength

        # Return the score with a slight offset to avoid 1.0 and -1.0
        if(score == 1.0) : return -0.99
        elif(score == -1.0) : return 0.99
        else : return - score