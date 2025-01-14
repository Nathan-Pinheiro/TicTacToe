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
        """
        
        super().__init__(board, winCondition, playersData, startingPlayer)

    def play(self, move: Move) -> GameOutcome:
        
        """
        Executes a move, updates the game state, and checks for a win condition.

        Parameters:
            move (Move): The move to execute.

        Returns:
            GameOutcome: The result of the game after the move.
        """
        
        self.getGameHistory().addMove(move)
        move.play(self.getBoard(), self.getPlayerToPlayIndex())
        
        if move.__class__ != SimpleMove:
            self.getPlayerData(self.getPlayerToPlayIndex()).getPowerUpMoves().remove(move.__class__)
        
        gameOutcome : GameOutcome = self.checkWinForCurrentPlayer()
        self.__nextTurn__()
        return gameOutcome

    def undo(self, move: Move) -> None:
        
        """
        Undoes the last move, reverting the game state.

        Parameters:
            move (Move): The move to undo.
        """
        
        if self.getGameHistory().getMoveCount() <= 0:
            return

        self.getGameHistory().undo()
        move.undo(self.getBoard(), self.getPlayerToPlayIndex())

        if move.__class__ != SimpleMove:
            self.getPlayerData(self.getPlayerToPlayIndex()).getPowerUpMoves().append(move.__class__)
        
        self.__previousTurn__()

    def goBack(self, move: Move) -> None:
        
        """
        Goes back one move in the game history.

        Parameters:
            move (Move): The move to revert to.
        """
        
        if self.getGameHistory().getCurrentMoveIndex() <= 0 : return

        self.getGameHistory().goBack()
        move.undo(self.getBoard(), self.getPlayerToPlayIndex())

        if move.__class__ != SimpleMove : self.getPlayerData(self.getPlayerToPlayIndex()).getPowerUpMoves().append(move.__class__)
        
        self.__previousTurn__()

    def goNext(self, move: Move) -> None :
        
        """
        Moves forward in the game history.

        Parameters:
            move (Move): The move to reapply.
        """
        
        if self.getGameHistory().getCurrentMoveIndex() >= self.getGameHistory().getMoveCount() : return

        self.getGameHistory().goNext()
        self.getGameHistory().getCurrentMove().play(self.getBoard(), self.getPlayerToPlayIndex())

        if move.__class__ != SimpleMove : self.getPlayerData(self.getPlayerToPlayIndex()).getPowerUpMoves().remove(move.__class__)
        
        self.__nextTurn__()

    def getPossibleMoves(self) -> list[Move]:
        
        """
        Retrieves all valid moves for the current player based on the current game state.

        Returns:
            list[Move]: A list of possible moves.
        """

        possibleMoveTypes = [SimpleMove] + self.getPlayerData(self.getPlayerToPlayIndex()).getPowerUpMoves()
        possibleMoves = []

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
        """
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
