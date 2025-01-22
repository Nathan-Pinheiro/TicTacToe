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
            TypeError: If the alignment length is not an integer.
            ValueError: If the alignment length is less than 3.
            
        Returns:
            None
        """
        
        # Check if the alignment length is an integer and greater than 2
        if not isinstance(alignLength, int): 
            raise TypeError("The alignment length must be an integer.")
        
        if alignLength < MIN_ENTITY_TO_ALIGN:
            raise ValueError(f"Can't create an AlignVictory with {alignLength} entity to align. It must be higher or equals than {MIN_ENTITY_TO_ALIGN}")
        
        # Set the alignment length
        self.__alignLength__ = alignLength
        
        return None

    def checkWin(self, board : Board) -> GameOutcome:

        """
        Checks if any player has achieved the required alignment length to win.

        Parameters:
            board (Board): The current state of the game board.
            
        Raises:
            TypeError: If the board is not a Board object.
        
        Returns:
            GameOutcome: VICTORY if a player wins, DRAW if the board is full, or UNFINISHED if the game continues.
        """
        
        # Check if the board is a Board object
        if not isinstance(board, Board):
            raise TypeError("The board must be a Board object.")

        # Check if any player has achieved the required alignment length
        winnerIndex : int = board.checkIfPlayerHaveAlignment(self.__alignLength__)

        # Return the game outcome
        if(winnerIndex != -1) : return GameOutcome(GameOutcomeStatus.VICTORY, winnerIndex)
        elif(board.isFull()) : return GameOutcome(GameOutcomeStatus.DRAW)
        else : return GameOutcome(GameOutcomeStatus.UNFINISHED)
    
    def checkWinForPlayer(self, playerIndex : int, board : Board) -> GameOutcome:

        """
        Checks if a specific player has achieved the alignment required to win.

        Parameters:
            playerIndex (int): The index of the player to check.
            board (Board): The current game board.
            
        Raises:
            TypeError: If the board is not a Board object.
            ValueError: If the player index is not an integer or is out of bounds.
        
        Returns:
            GameOutcome: VICTORY if the player wins, DRAW if the board is full, or UNFINISHED if the game continues.
        """
        
        # Check if the board is a Board object
        if not isinstance(board, Board):
            raise TypeError("The board must be a Board object.")
        
        # Check if the player index is an integer and in bounds
        if not isinstance(playerIndex, int):
            raise ValueError("The player index must be an integer.")
        
        if playerIndex < 0 or playerIndex >= board.getPlayerCount():
            raise ValueError("The player index must be a valid index.")

        # Check if the player has achieved the required alignment length to win or if the board is full and return the game outcome
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
            
        Raises:
            TypeError: If the board is not a Board object.
            ValueError: If the playerToEvaluateIndex is not an integer or is out of bounds.
        
        Returns:
            int: A normalized score representing the player's advantage.
        """
        
        # Check if the board is a Board object
        if not isinstance(board, Board):
            raise TypeError("The board must be a Board object.")
        
        # Check if the player index is an integer and in bounds
        if not isinstance(playerToEvaluateIndex, int):
            raise ValueError("The player index must be an integer.")
        
        if playerToEvaluateIndex < 0 or playerToEvaluateIndex >= board.getPlayerCount():
            raise ValueError("The player index must be a valid index.")
        
        # Initialize the alignment strength for the player and the opponents
        playerAlignStrength : int = 0
        oponentsAlignStrength : int = 0

        # Check the alignment strength for each player
        for pieceCount in range(2, self.__alignLength__) :
            for playerIndex in range(0, len(board.getPlayerEntities())):
                
                # Check if the player is the one to evaluate or an opponent and update the alignment strength
                if(playerIndex == playerToEvaluateIndex): playerAlignStrength += 2 * pieceCount * board.countAvaillableLineOfAtLeastGivenPiece(playerIndex, self.__alignLength__, pieceCount)
                else : oponentsAlignStrength += 2 * pieceCount * board.countAvaillableLineOfAtLeastGivenPiece(playerIndex, self.__alignLength__, pieceCount)

        # Calculate the total strength
        totalStrength = playerAlignStrength + oponentsAlignStrength
        
        # Return 0 if the total strength is 0
        if totalStrength == 0: return 0.0
        
        # Calculate the score
        score : int = (playerAlignStrength - oponentsAlignStrength) / totalStrength

        # Return the score with a slight offset to avoid 1.0 and -1.0
        if(score == 1.0) : return 0.99
        elif(score == -1.0) : return -0.99
        else : return score