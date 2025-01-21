from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Type

from modules.models.board_game.board.board import Board
from modules.models.board_game.components.win_condition import WinCondition
from modules.models.board_game.components.move import Move
from modules.models.board_game.components.player_data import PlayerData
from modules.models.board_game.game.game_outcome import GameOutcome
from modules.models.board_game.game.game_history import GameHistory

# ************************************************
# CLASS GameState
# ************************************************
# ROLE : This class is used to represent a generic board game state
# ************************************************
# VERSION : 1.0
# AUTHOR : Nathan PINHEIRO
# DATE : 13/01/2025
# ************************************************

class GameState(ABC):
    """
    Represents a generic state of a game, managing the board, players, win conditions, and game history.
    """

    def __init__(self, board: Board, winCondition: WinCondition, playersData: list[PlayerData], startingPlayer: int = 0) -> None:
        """
        Initializes the game state with a board, win condition, player data, and starting player index.
        
        Parameters:
            board (Board): The game board.
            winCondition (WinCondition): The win condition logic.
            playersData (list[PlayerData]): Data for all players.
            startingPlayer (int): Index of the player who starts the game (default is 0).
        """
        self.__board__: Board = board
        self.__playerToPlayIndex__: int = startingPlayer
        self.__winCondition__: WinCondition = winCondition
        self.__playersData__: list[PlayerData] = playersData
        self.__gameHistory__: GameHistory = GameHistory()

    @abstractmethod
    def play(self, move: Move) -> GameOutcome:
        """
        Execute a move and return the resulting game outcome.
        
        Parameters:
            move (Move): The move to execute.
        
        Returns:
            GameOutcome: The result after the move.
        """
        pass

    @abstractmethod
    def undo(self, move: Move) -> None:
        """
        Undo a move, restoring the previous game state.
        
        Parameters:
            move (Move): The move to undo.
        """
        pass

    @abstractmethod
    def goBack(self) -> None:
        """
        Navigate back to a previous move in the game history.
        
        Parameters:
            move (Move): The move to go back to.
        """
        pass

    @abstractmethod
    def goNext(self) -> None:
        """
        Navigate forward to a subsequent move in the game history.
        
        Parameters:
            move (Move): The move to go forward to.
        """
        pass

    @abstractmethod
    def getPossibleMoves(self) -> list[Move]:
        """
        Retrieve all possible moves for the current game state.
        
        Returns:
            list[Move]: A list of valid moves.
        """
        pass

    def getPlayerCount(self) -> int:
        """Returns the number of players in the game."""
        return len(self.__playersData__)

    def getBoard(self) -> Board:
        """Returns the current game board."""
        return self.__board__

    def getPlayerData(self, playerIndex: int) -> PlayerData:
        """Returns the data for a specific player."""
        pass

    def __nextTurn__(self) -> None:
        """Advances to the next player's turn."""
        self.__playerToPlayIndex__ = (self.__playerToPlayIndex__ + 1) % len(self.__playersData__)

    def __previousTurn__(self) -> None:
        """Reverts to the previous player's turn."""
        self.__playerToPlayIndex__ = (self.__playerToPlayIndex__ - 1 + len(self.__playersData__)) % len(self.__playersData__)

    def getPlayerToPlayIndex(self) -> int:
        """Returns the index of the player whose turn it is."""
        return self.__playerToPlayIndex__

    def setPlayerToPlayIndex(self, player_index: int) -> None:
        """Sets the index of the player whose turn it is."""
        self.__playerToPlayIndex__ = player_index

    def getGameHistory(self) -> GameHistory:
        """Returns the game history object."""
        return self.__gameHistory__

    def setWinCondition(self, win_condition: WinCondition) -> None:
        """Sets the win condition for the game."""
        self.__winCondition__ = win_condition

    def checkWin(self) -> GameOutcome:
        """Checks if any player has met the win condition."""
        return self.__winCondition__.checkWin(self.__board__)

    def checkWinForPlayer(self, playerIndex: int) -> GameOutcome:
        """Checks if a specific player has met the win condition."""
        return self.__winCondition__.checkWinForPlayer(playerIndex, self.__board__)

    def checkWinForCurrentPlayer(self) -> GameOutcome:
        """Checks if the current player has met the win condition."""
        return self.__winCondition__.checkWinForPlayer(self.__playerToPlayIndex__, self.__board__)

    def evaluateForPlayer(self, playerIndex: int) -> int:
        """Evaluates the board state for a specific player."""
        return self.__winCondition__.evaluateForPlayer(playerIndex, self.__board__)

    def copy(self) -> GameState:
        """
        Creates a copy of the current game state.
        
        Returns:
            GameState: A copy of the game state.
        """
        return GameState(self.__board__.copy(), self.__winCondition__, self.__playersData__, self.__playerToPlayIndex__)