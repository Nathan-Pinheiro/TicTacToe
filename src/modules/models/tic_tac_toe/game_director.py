from modules.models.board_components.entity import Entity
from modules.models.board_components.coordinate import Coordinate
from modules.models.board_components.case import Case
from modules.models.board_components.board import Board
from modules.models.tic_tac_toe.game_state import TicTacToeGameState
from modules.models.tic_tac_toe.player_data import PlayerData
from modules.models.tic_tac_toe.players.player import Player
from modules.models.tic_tac_toe.player_data import PlayerData
from modules.models.tic_tac_toe.win_condition import WinCondition
from modules.models.tic_tac_toe.game_result import GameState, GameStatus
from modules.utils.decorator import private_method
import os

class GameDirector :

    def __init__(self, board : Board, winCondition : WinCondition, players : list[Player], playersData : list[PlayerData]):

        self.__players__ = players
        self.__game_state__ = TicTacToeGameState(board, winCondition, playersData)
        
    def getPlayerToPlay(self) -> Player:
        
        return self.__players__[self.__game_state__.getPlayerToPlayIndex()]
    
    @private_method
    def __play__(self, line : int, column : int, entity : Entity) -> None :

        board : Board = self.__game_state__.getBoard()
    
        if(line < 0 or line > board.getHeight()) : raise ValueError(f"Line is out of range. Should be from 0 to {board.getHeight()} but was <{line}>")
        if(column < 0 or column > board.getWidth()) : raise ValueError(f"Column is out of range. Should be from 0 to {board.getWidth()} but was <{column}>")

        if(not board.isCaseAvaillable(line, column)) : raise ValueError(f"Can't play at line = {line}, column = {column}. Case is already taken.")

        board.setEntityAt(entity, line, column)
    
        return None
    
    @private_method
    def __nextTurn__(self) -> None :
        
        playerToPlayIndex : int = self.__game_state__.getPlayerToPlayIndex()

        if(playerToPlayIndex < self.__game_state__.getPlayerCount() - 1) : self.__game_state__.setPlayerToPlayIndex(playerToPlayIndex + 1)
        else : self.__game_state__.setPlayerToPlayIndex(0)
        
        return None      

    def launchGame(self) :
        
        board : Board = self.__game_state__.getBoard()
        gameResult : GameState = self.__game_state__.getWinCondition().checkWin(board)

        while(gameResult.getGameStatus() == GameStatus.UNFINISHED) :

            playerToPlayIndex : int = self.__game_state__.getPlayerToPlayIndex()
            playerToPlayData : PlayerData = self.__game_state__.getPlayerData(playerToPlayIndex)
            playerToPlay : Player = self.getPlayerToPlay()

            coordinate : Coordinate = playerToPlay.get_choice(board)
            newEntity : Entity = playerToPlayData.getEntity().copy()            

            self.__play__(coordinate.getLine(), coordinate.getColumn(), newEntity)
            self.__nextTurn__()

            gameResult = self.__game_state__.getWinCondition().checkWin(board)
            

            
            
        
        
        


        