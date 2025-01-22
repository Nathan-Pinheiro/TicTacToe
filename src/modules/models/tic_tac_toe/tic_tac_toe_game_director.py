from modules.models.board_game.board.board import Board
from modules.models.board_game.components.move import Move 
from modules.models.board_game.components.win_condition import WinCondition
from modules.models.board_game.game.game_outcome import GameOutcome, GameOutcomeStatus

from modules.models.tic_tac_toe.tic_tac_toe_game_state import TicTacToeGameState
from modules.models.tic_tac_toe.tic_tac_toe_player import Player
from modules.models.tic_tac_toe.tic_tac_toe_player_data import PlayerData

from modules.models.displayer.console_displayer import *

import random
import os
import time

# ************************************************
# CLASS GameDirector
# ************************************************
# ROLE : This class is used to launch a game
# ************************************************
# VERSION : 1.0
# AUTHOR : Nathan PINHEIRO
# DATE : 10/01/2025
# ************************************************

class GameDirector :
    
    """
    This class is used to launch a game
    """

    def __init__(self, board : Board, winCondition : WinCondition, players : list[Player], playersData : list[PlayerData], startingPlayer : int = -1) -> None:
        
        """
        Initializes the GameDirector with a board, a win condition, a list of players, a list of players data and a starting player.
        
        Parameters:
            board (Board): The board of the game.
            winCondition (WinCondition): The win condition of the game.
            players (list[Player]): The list of players.
            playersData (list[PlayerData]): The list of players data.
            startingPlayer (int): The index of the starting player.
            
        Raises:
            TypeError: If the board is not a Board object.
            TypeError: If the win condition is not a WinCondition object.
            TypeError: If the players are not a list of Player objects.
            TypeError: If the players data are not a list of PlayerData objects.
            TypeError: If the starting player is not an integer.
            
        Returns:
            None
        """
        
        # Check if the board is a Board object
        if not isinstance(board, Board): 
            raise TypeError("The board must be a Board object.")
        
        # Check if the win condition is a WinCondition object
        if not isinstance(winCondition, WinCondition): 
            raise TypeError("The win condition must be a WinCondition object.")
        
        # Check if the players are a list of Player objects
        if not isinstance(players, list) and all(isinstance(player, Player) for player in players): 
            raise TypeError("The players must be a list of Player objects.")
        
        # Check if the players data are a list of PlayerData objects
        if not isinstance(playersData, list) and all(isinstance(playerData, PlayerData) for playerData in playersData): 
            raise TypeError("The players data must be a list of PlayerData objects.")
        
        # Check if the starting player is an integer
        if not isinstance(startingPlayer, int): 
            raise TypeError("The starting player must be an integer.")

        # Check if the starting player is a valid index or set it randomly
        if(startingPlayer not in [index for index in range(len(players))]) : startingPlayer = random.randint(0, len(players) - 1)

        # Initialize the attributes
        self.__players__ : list[Player] = players
        self.__gameState__ : TicTacToeGameState = TicTacToeGameState(board, winCondition, playersData, startingPlayer)
        
        return None
        
    def getPlayerToPlay(self) -> Player:
        
        """
        Returns the player to play.
        
        Returns:
            Player: The player to play.
        """
        
        return self.__players__[self.__gameState__.getPlayerToPlayIndex()]

    def launchGame(self) -> TicTacToeGameState:
        
        """
        Launches the game.
        
        Returns:
            TicTacToeGameState: The final state of the game.
        """

        # Check if the game is finished
        gameOutcome : GameOutcome = self.__gameState__.checkWin()

        # While the game is not finished play
        while(gameOutcome.getGameStatus() == GameOutcomeStatus.UNFINISHED) :

            playerToPlay : Player = self.getPlayerToPlay()

            start_time = time.time()

            move : Move = playerToPlay.get_choice(self.__gameState__)

            end_time = time.time()
            elapsed_time = end_time - start_time

            display_sep()

            display(f"Player : {playerToPlay.getName()} played {move}")
            print("player index", self.getGameState().getPlayerToPlayIndex())
            display(f"It took {elapsed_time:.6f} seconds")

            display_sep()
            os.system("pause")

            gameOutcome = self.__gameState__.play(move)

        return self.__gameState__
    
    def getGameState(self) -> TicTacToeGameState:
        
        """
        Returns the game state.
        
        Returns:
            TicTacToeGameState: The game state.
        """
        
        return self.__gameState__