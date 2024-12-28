from modules.models.board_components.board import Board
from modules.models.tic_tac_toe.game_state import GameState
from modules.models.tic_tac_toe.player_data import PlayerData
from modules.models.tic_tac_toe.player import Player
from modules.models.tic_tac_toe.player_data import PlayerData
from modules.models.tic_tac_toe.win_condition import WinCondition
from modules.models.tic_tac_toe.game_outcome import GameOutcome, GameOutcomeStatus
from modules.utils.decorator import private_method
from modules.models.tic_tac_toe.move import Move 
import random
import os

class GameDirector :

    def __init__(self, board : Board, winCondition : WinCondition, players : list[Player], playersData : list[PlayerData], startingPlayer : int = -1):

        if(startingPlayer == -1) : startingPlayer = random.randint(0, len(players) - 1)

        self.__players__ = players
        self.__game_state__ = GameState(board, winCondition, playersData, startingPlayer)
        
    def getPlayerToPlay(self) -> Player:
        
        return self.__players__[self.__game_state__.getPlayerToPlayIndex()]

    def launchGame(self) -> GameState:
        
        gameOutcome : GameOutcome = self.__game_state__.checkWin()

        while(gameOutcome.getGameStatus() == GameOutcomeStatus.UNFINISHED) :

            playerToPlayIndex : int = self.__game_state__.getPlayerToPlayIndex()
            playerToPlayData : PlayerData = self.__game_state__.getPlayerData(playerToPlayIndex)
            playerToPlay : Player = self.getPlayerToPlay()

            move : Move = playerToPlay.get_choice(self.__game_state__)

            gameOutcome = self.__game_state__.play(move)

        return self.__game_state__