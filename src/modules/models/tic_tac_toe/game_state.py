from modules.models.board.board import Board
from modules.models.tic_tac_toe.win_conditions.win_condition import WinCondition
from modules.models.tic_tac_toe.power_ups.bomb import Bomb
from modules.models.tic_tac_toe.player_data import PlayerData

class TicTacToeGameState :
    
    def __init__(self, board : Board, winCondition : WinCondition, playersData : list[PlayerData]) -> None:
        
        self.__board__ : Board = board
        self.__player_to_play_index__ : int = 0
        self.__win_condition__ : WinCondition = winCondition
        self.__players_data__ : list[PlayerData] = playersData
        
        return None
        
    def getBoard(self) -> Board :
        return self.__board__
    
    def getPlayerCount(self) -> int :
        return len(self.__players_data__)

    def getPlayerData(self, playerIndex : int) -> PlayerData :
        return self.__players_data__[playerIndex]

    def getPlayerToPlayIndex(self) -> int :
        return self.__player_to_play_index__
    
    def setPlayerToPlayIndex(self, player_index: int) -> None:
        self.__player_to_play_index__ = player_index
        return None

    def getWinCondition(self) -> WinCondition :
        return self.__win_condition__

    def setWinCondition(self, win_condition : WinCondition) -> None :
        self.__win_condition__ = win_condition
        return None
    
    