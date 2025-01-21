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
            
        Returns:
            None
        """

        if(startingPlayer == -1) : startingPlayer = random.randint(0, len(players) - 1)

        self.__players__ : list[Player] = players
        self.__game_state__ : TicTacToeGameState = TicTacToeGameState(board, winCondition, playersData, startingPlayer)
        
        return None
        
    def getPlayerToPlay(self) -> Player:
        
        """
        Returns the player to play.
        
        Returns:
            Player: The player to play.
        """
        
        return self.__players__[self.__game_state__.getPlayerToPlayIndex()]

    def launchGame(self) -> TicTacToeGameState:
        
        """
        Launches the game.
        
        Returns:
            TicTacToeGameState: The final state of the game.
        """

        gameOutcome : GameOutcome = self.__game_state__.checkWin()

        while(gameOutcome.getGameStatus() == GameOutcomeStatus.UNFINISHED) :

            playerToPlayIndex : int = self.__game_state__.getPlayerToPlayIndex()
            playerToPlayData : PlayerData = self.__game_state__.getPlayerData(playerToPlayIndex)
            playerToPlay : Player = self.getPlayerToPlay()

            start_time = time.time()

            move : Move = playerToPlay.get_choice(self.__game_state__)

            end_time = time.time()
            elapsed_time = end_time - start_time

            display_sep()

            display(f"Player : {playerToPlay.getName()} played {move}")
            print("player index", self.getGameState().getPlayerToPlayIndex())
            display(f"It took {elapsed_time:.6f} seconds")

            display_sep()
            os.system("pause")

            gameOutcome = self.__game_state__.play(move)

        return self.__game_state__
    
    def getGameState(self) -> TicTacToeGameState:
        
        """
        Returns the game state.
        
        Returns:
            TicTacToeGameState: The game state.
        """
        
        return self.__game_state__