from modules.models.board_components.entity import Entity
from modules.models.board_components.coordinate import Coordinate
from modules.models.board_components.case import Case
from modules.models.board_components.board import Board
from modules.models.tic_tac_toe.game_state import GameState
from modules.models.tic_tac_toe.player_data import PlayerData
from modules.models.tic_tac_toe.players.player import Player
from modules.models.tic_tac_toe.player_data import PlayerData
from modules.models.tic_tac_toe.win_condition import WinCondition
from modules.models.tic_tac_toe.game_outcome import GameOutcome, GameOutcomeStatus
from modules.utils.decorator import private_method
from modules.models.tic_tac_toe.move import Move 

class GameDirector :

    def __init__(self, board : Board, winCondition : WinCondition, players : list[Player], playersData : list[PlayerData]):

        self.__players__ = players
        self.__game_state__ = GameState(board, winCondition, playersData)
        
    def getPlayerToPlay(self) -> Player:
        
        print(self.__game_state__.getPlayerToPlayIndex())

        return self.__players__[self.__game_state__.getPlayerToPlayIndex()]
    
    @private_method
    def __nextTurn__(self) -> None :
        
        playerToPlayIndex : int = self.__game_state__.getPlayerToPlayIndex()

        if(playerToPlayIndex < self.__game_state__.getPlayerCount() - 1) : self.__game_state__.setPlayerToPlayIndex(playerToPlayIndex + 1)
        else : self.__game_state__.setPlayerToPlayIndex(0)
        
        return None

    def launchGame(self) -> GameState:
        
        gameOutcome : GameOutcome = self.__game_state__.checkWin()

        while(gameOutcome.getGameStatus() == GameOutcomeStatus.UNFINISHED) :

            playerToPlayIndex : int = self.__game_state__.getPlayerToPlayIndex()
            playerToPlayData : PlayerData = self.__game_state__.getPlayerData(playerToPlayIndex)
            playerToPlay : Player = self.getPlayerToPlay()

            move : Move = playerToPlay.get_choice(self.__game_state__)
            newEntity : Entity = playerToPlayData.getEntity().copy()            

            self.__game_state__.play(move)
            self.__nextTurn__()

            gameOutcome = self.__game_state__.checkWin()
        
        return self.__game_state__