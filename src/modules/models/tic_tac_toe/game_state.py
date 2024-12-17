from modules.models.board_components.board import Board
from modules.models.tic_tac_toe.win_condition import WinCondition
from modules.models.tic_tac_toe.moves.simple_move import SimpleMove
from modules.models.tic_tac_toe.player_data import PlayerData
from modules.models.tic_tac_toe.move import Move
from modules.models.board_components.coordinate import Coordinate
from modules.models.board_components.entity import Entity
from modules.models.tic_tac_toe.game_outcome import GameOutcome
from typing import Type

class GameState :
    
    def __init__(self, board : Board, winCondition : WinCondition, playersData : list[PlayerData]) -> None:
        
        self.__board__ : Board = board
        self.__playerToPlayIndex__ : int = 0
        self.__winCondition__ : WinCondition = winCondition
        self.__playersData__ : list[PlayerData] = playersData
        
        return None
        
    def play(self, move : Move) -> None :
        
        move.play(self.__board__)
        
        if(move.__class__ != SimpleMove) : self.__playersData__[self.__playerToPlayIndex__].getPowerUpMoves().remove(move.__class__)

        return None

    def getPossibleMoves(self) -> list[Move]:
        
        possibleMoveTypes : list[Type[Move]] = [SimpleMove] + self.getPlayerData(self.__playerToPlayIndex__).getPowerUpMoves()
        possibleMoves : list[Move] = []

        entityToPlay = self.__playersData__[self.__playerToPlayIndex__].getEntity()

        for line in range(self.getBoard().getHeight()):
            for column in range(self.getBoard().getWidth()):
                for moveType in possibleMoveTypes:
                    if(moveType.canPlay(self.getBoard(), line, column)):
                        possibleMoves.append(moveType(Coordinate(line, column), entityToPlay))

        return possibleMoves

    def getBoard(self) -> Board :
        return self.__board__
    
    def getPlayerCount(self) -> int :
        return len(self.__playersData__)

    def getPlayerData(self, playerIndex : int) -> PlayerData :
        return self.__playersData__[playerIndex]

    def getPlayerToPlayIndex(self) -> int :
        return self.__playerToPlayIndex__
    
    def getPlayerToPlayEntity(self) -> Entity :
        return self.__playersData__[self.__playerToPlayIndex__].getEntity()

    def setPlayerToPlayIndex(self, player_index: int) -> None:
        self.__playerToPlayIndex__ = player_index
        return None

    def checkWin(self) -> GameOutcome :
        return self.__winCondition__.checkWin(self.__board__)

    def setWinCondition(self, win_condition : WinCondition) -> None :
        self.__winCondition__ = win_condition
        return None
    
    