from modules.models.board.board import Board
from modules.models.board.case import Case
from modules.models.tic_tac_toe.player_data import PlayerData
from modules.models.tic_tac_toe.power_ups.bomb import Bomb

class TicTacToeGameState :
    
    def __init__(self, board : Board, playerCount : int) :
        
        self.__board__ : Board = board
        self.__player_to_play_index__ : int = 0
        self.__players_data__ : list[PlayerData] = [PlayerData([Bomb]) for _ in range(0, playerCount)]
        
        return None
        
    def getBoard(self) -> Board :
        return self.__board__
    
    def getPlayerToPlayIndex(self) -> Board :
        return self.__player_to_play_index__
    
    def getPlayerCount(self) -> int :
        return len(self.__players_data__)

    def getPlayerData(self, playerIndex : int) -> PlayerData :
        return self.__players_data__[playerIndex]