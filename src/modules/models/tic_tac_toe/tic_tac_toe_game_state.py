from __future__ import annotations
from modules.models.board_game.board.board import Board
from modules.models.board_game.components.win_condition import WinCondition
from modules.models.tic_tac_toe.moves.simple_move import SimpleMove
from modules.models.board_game.components.move import Move
from modules.models.board_game.components.coordinate import Coordinate
from modules.models.board_game.game.game_outcome import GameOutcome
from modules.models.board_game.game.game_state import GameState
from modules.models.tic_tac_toe.tic_tac_toe_player_data import TicTacToePlayerData
from modules.utils.decorator import override

# ************************************************
# CLASS GameDirector
# ************************************************
# ROLE : This class is used to launch a game
# ************************************************
# VERSION : 1.0
# AUTHOR : Nathan PINHEIRO
# DATE : 10/01/2025
# ************************************************


class TicTacToeGameState(GameState):
    """
    Represents the state of a Tic Tac Toe game, handling the game logic, move execution,
    undo/redo functionality, and win condition evaluation.
    """

    def __init__(self, board: Board, winCondition: WinCondition, playersData: list[TicTacToePlayerData], startingPlayer: int = 0) -> None:
        
        """
        Initializes the Tic Tac Toe game state.

        Parameters:
            board (Board): The game board.
            winCondition (WinCondition): The win condition logic.
            playersData (list[PlayerData]): Data for all players.
            startingPlayer (int): Index of the player who starts the game (default is 0).
            
        Raises:
            TypeError: If the board is not a Board object.
            TypeError: If the win condition is not a WinCondition object.
            TypeError: If the players data are not a list of PlayerData objects.
            TypeError: If the starting player is not an integer.
            ValueError: If the starting player is not a valid index.
            
        Returns:
            None
        """
        
        # Check if the board is a Board object
        if not isinstance(board, Board): 
            raise TypeError("The board must be a Board object.")
        
        # Check if the win condition is a WinCondition object
        if not isinstance(winCondition, WinCondition):
            raise TypeError("The win condition must be a WinCondition object.")
        
        # Check if the players data are a list of PlayerData objects
        if not all(isinstance(playerData, TicTacToePlayerData) for playerData in playersData):
            raise TypeError("The players data must be a list of PlayerData objects.")
        
        # Check if the starting player is an integer and a valid index
        if not isinstance(startingPlayer, int):
            raise TypeError("The starting player must be an integer.")
        
        if startingPlayer < 0 or startingPlayer >= len(playersData):
            raise ValueError("The starting player must be a valid index.")
        
        # Call the parent constructor
        super().__init__(board, winCondition, playersData, startingPlayer)
        
        return None

    def play(self, move: Move) -> GameOutcome:
        
        """
        Executes a move, updates the game state, and checks for a win condition.

        Parameters:
            move (Move): The move to execute.
            
        Raises:
            TypeError: If the move is not a Move object.

        Returns:
            GameOutcome: The result of the game after the move.
        """
        
        # Check if the move is a Move object
        if not isinstance(move, Move):
            raise TypeError("The move must be a Move object.")
        
        # Add the move to the game history
        self.getGameHistory().addMove(move)
        
        # Play the move and check for a win condition
        move.play(self.getBoard(), self.getPlayerToPlayIndex())
        if move.__class__ != SimpleMove : self.getPlayerData(self.getPlayerToPlayIndex()).getPowerUpMoves().remove(move.__class__) 

        gameOutcome : GameOutcome = self.checkWinForCurrentPlayer()
        
        # Pass the turn to the next player
        self.__nextTurn__()
        
        return gameOutcome

    def undo(self, move: Move) -> bool:
        
        """
        Undoes the last move, reverting the game state.

        Parameters:
            move (Move): The move to undo.
            
        Raises:
            TypeError: If the move is not a Move object.
            
        Returns:
            bool: True if the operation was successful, False otherwise.
        """
        
        # Check if the move is a Move object
        if not isinstance(move, Move):
            raise TypeError("The move must be a Move object.")
        
        # Check if there are moves to undo
        if self.getGameHistory().getMoveCount() <= 0: return False

        # Undo the move and revert the game state
        self.__previousTurn__()

        self.getGameHistory().undo()
        move.undo(self.getBoard(), self.getPlayerToPlayIndex())

        # If the move is not a simple move, add it back to the player's power-up moves
        if move.__class__ != SimpleMove : self.getPlayerData(self.getPlayerToPlayIndex()).getPowerUpMoves().append(move.__class__)
        
        return True

    def goBack(self) -> bool:

        """
        Goes back one move in the game history.
        
        Returns:
            bool: True if the operation was successful, False otherwise
        """

        # Check if there are moves to go back to
        if self.getGameHistory().getCurrentMoveIndex() < 0 : return False

        # Undo the move and revert the game state
        move : Move = self.getGameHistory().getCurrentMove()
        move.undo(self.getBoard(), self.getPlayerToPlayIndex())
        
        # If the move is not a simple move, add it back to the player's power-up moves
        if move.__class__ != SimpleMove : self.getPlayerData(self.getPlayerToPlayIndex()).getPowerUpMoves().append(move.__class__)
        
        # Go back in the game history
        self.getGameHistory().goBack()

        # Go back to the previous turn
        self.__previousTurn__()
        
        return True

    def goNext(self) -> bool :

        """
        Moves forward in the game history.
        
        Returns:
            bool: True if the operation was successful, False otherwise
        """

        # Check if there are moves to go forward to
        if self.getGameHistory().getCurrentMoveIndex() >= (self.getGameHistory().getMoveCount() - 1) : return False
        
        # Go to the next move in the game history
        self.getGameHistory().goNext()
        
        # Play the move and check for a win condition
        move : Move = self.getGameHistory().getCurrentMove()
        move.play(self.getBoard(), self.getPlayerToPlayIndex())
        
        # If the move is not a simple move, remove it from the player's power-up moves
        if move.__class__ != SimpleMove : self.getPlayerData(self.getPlayerToPlayIndex()).getPowerUpMoves().remove(move.__class__)

        # Pass the turn to the next player
        self.__nextTurn__()
        
        return True

    def getPossibleMoves(self) -> list[Move]:
        
        """
        Retrieves all valid moves for the current player based on the current game state.

        Returns:
            list[Move]: A list of possible moves.s
        """

        # Initialize the list of possible moves and move types
        possibleMoveTypes = [SimpleMove] + self.getPlayerData(self.getPlayerToPlayIndex()).getPowerUpMoves()
        possibleMoves = []

        # Check all possible moves for the current player
        for line in range(self.getBoard().getHeight()):
            for column in range(self.getBoard().getWidth()):
                for moveType in possibleMoveTypes:
                    if moveType.canPlay(self.getBoard(), line, column):
                        possibleMoves.append(moveType(Coordinate(line, column)))

        return possibleMoves

    @override
    def getPlayerData(self, playerIndex: int) -> TicTacToePlayerData:
        
        """
        Returns the data for a specific player.
        
        Parameters:
            playerIndex (int): The index of the player.
            
        Raises:
            ValueError: If the player index is not an integer or is out of bounds.
            
        Returns:
            PlayerData: The data for the player.
        """
        
        # Check if the player index is an integer and in bounds
        if not isinstance(playerIndex, int):
            raise ValueError("The player index must be an integer.")
        
        return self.__playersData__[playerIndex]

    def copy(self) -> TicTacToeGameState :
        
        """
        Creates a deep copy of the current game state.

        Returns:
            TicTacToeGameState: A new identical game state.
        """
        
        return TicTacToeGameState(
            self.getBoard().copy(),
            self.__winCondition__,
            self.__playersData__,
            self.getPlayerToPlayIndex()
        )
