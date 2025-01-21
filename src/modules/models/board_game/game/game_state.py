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
            
        Returns:
            None
        """
        
        self.__board__: Board = board
        self.__playerToPlayIndex__: int = startingPlayer
        self.__winCondition__: WinCondition = winCondition
        self.__playersData__: list[PlayerData] = playersData
        self.__gameHistory__: GameHistory = GameHistory()
        
        return None

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
            
        Returns:
            None
        """
        
        pass

    @abstractmethod
    def goBack(self) -> None:
        
        """
        Navigate back to a previous move in the game history.
            
        Returns:
            None
        """
        
        pass

    @abstractmethod
    def goNext(self) -> None:
        
        """
        Navigate forward to a subsequent move in the game history.
        
        Returns:
            None
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
        
        """
        Returns the number of players in the game.
        
        Returns:
            int: The number of players.
        """
        
        return len(self.__playersData__)

    def getBoard(self) -> Board:
        
        """
        Returns the current game board.
        
        Returns:
            Board: The game board.
        """
        
        return self.__board__

    @abstractmethod
    def getPlayerData(self, playerIndex: int) -> PlayerData:
        
        """
        Returns the data for a specific player.
        
        Parameters:
            playerIndex (int): The index of the player.
            
        Returns:
            PlayerData: The data for the player.
        """
        
        pass

    def __nextTurn__(self) -> None:
        
        """
        Advances to the next player's turn.
        
        Returns:
            None
        """
        
        self.__playerToPlayIndex__ = (self.__playerToPlayIndex__ + 1) % len(self.__playersData__)
        
        return None

    def __previousTurn__(self) -> None:
        
        """
        Reverts to the previous player's turn.
        
        Returns:
            None
        """
        
        self.__playerToPlayIndex__ = (self.__playerToPlayIndex__ - 1 + len(self.__playersData__)) % len(self.__playersData__)
        
        return None

    def getPlayerToPlayIndex(self) -> int:
        
        """
        Returns the index of the player whose turn it is.
        
        Returns:
            int: The index of the player.
        """
        
        return self.__playerToPlayIndex__

    def setPlayerToPlayIndex(self, player_index: int) -> None:
        
        """
        Sets the index of the player whose turn it is.
        
        Parameters:
            player_index (int): The index of the player.
            
        Returns:
            None
        """
        
        self.__playerToPlayIndex__ = player_index
        
        return None

    def getGameHistory(self) -> GameHistory:
        
        """
        Returns the game history object.
        
        Returns:
            GameHistory: The game history.
        """
        
        return self.__gameHistory__

    def setWinCondition(self, win_condition: WinCondition) -> None:
        
        """
        Sets the win condition for the game.
        
        Parameters:
            win_condition (WinCondition): The win condition logic.
            
        Returns:
            None
        """
        
        self.__winCondition__ = win_condition
        
        return None

    def checkWin(self) -> GameOutcome:
        
        """
        Checks if any player has met the win condition.
        
        Returns:
            GameOutcome: The outcome of the game.
        """
        
        return self.__winCondition__.checkWin(self.__board__)

    def checkWinForPlayer(self, playerIndex: int) -> GameOutcome:
        
        """
        Checks if a specific player has met the win condition.
        
        Parameters:
            playerIndex (int): The index of the player to check.
            
        Returns:
            GameOutcome: The outcome of the game.
        """
        
        return self.__winCondition__.checkWinForPlayer(playerIndex, self.__board__)

    def checkWinForCurrentPlayer(self) -> GameOutcome:
        
        """
        Checks if the current player has met the win condition.
        
        Returns:
            GameOutcome: The outcome of the game.
        """
        
        return self.__winCondition__.checkWinForPlayer(self.__playerToPlayIndex__, self.__board__)

    def evaluateForPlayer(self, playerIndex: int) -> GameOutcome:
        
        """
        Evaluates the board state for a specific player.
        
        Parameters:
            playerIndex (int): The index of the player.
            
        Returns:
            GameOutcome: The outcome of the evaluation.
        """
        
        return self.__winCondition__.evaluateForPlayer(playerIndex, self.__board__)

    def copy(self) -> GameState:
        
        """
        Creates a copy of the current game state.
        
        Returns:
            GameState: A copy of the game state.
        """
        
        return GameState(self.__board__.copy(), self.__winCondition__, self.__playersData__, self.__playerToPlayIndex__)
