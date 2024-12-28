from __future__ import annotations
from modules.models.board_components.board import Board
from modules.models.tic_tac_toe.win_condition import WinCondition
from modules.models.tic_tac_toe.moves.simple_move import SimpleMove
from modules.models.tic_tac_toe.player_data import PlayerData
from modules.models.tic_tac_toe.move import Move
from modules.models.board_components.coordinate import Coordinate
from modules.models.board_components.entity import Entity
from modules.models.tic_tac_toe.game_outcome import GameOutcome
from modules.models.tic_tac_toe.game_history import GameHistory
from typing import Type

class GameState :
    
    def __init__(self, board : Board, winCondition : WinCondition, playersData : list[PlayerData], startingPlayer : int = 0) -> None:
        
        self.__board__ : Board = board
        self.__playerToPlayIndex__ : int = startingPlayer
        self.__winCondition__ : WinCondition = winCondition
        self.__playersData__ : list[PlayerData] = playersData
        self.__gameHistory__ : GameHistory = GameHistory()
        
        return None
        
    def play(self, move : Move) -> GameOutcome :
        
        self.__gameHistory__.addMove(move)
        move.play(self.__board__, self.__playerToPlayIndex__)
        if(move.__class__ != SimpleMove) : self.__playersData__[self.__playerToPlayIndex__].getPowerUpMoves().remove(move.__class__)

        gameOutcome : GameOutcome = self.checkWinForCurrentPlayer()

        self.__nextTurn__()

        return gameOutcome
    
    def undo(self, move : Move) -> None :
        
        self.__gameHistory__.removeLastMove()
        move.undo(self.__board__, self.__playerToPlayIndex__)
        if(move.__class__ != SimpleMove) : self.__playersData__[self.__playerToPlayIndex__].getPowerUpMoves().append(move.__class__)

        self.__previousTurn__()

        return None
    
    def undoLastMove(self) -> None :
        
        lastMove : Move = self.__gameHistory__.getLastMove()
        self.__gameHistory__.removeLastMove()
        
        lastMove.undo(self.__board__, self.__playerToPlayIndex__)
        if(lastMove.__class__ != SimpleMove) : self.__playersData__[self.__playerToPlayIndex__].getPowerUpMoves().append(lastMove.__class__)

        self.__previousTurn__()

        return None
    
    def __nextTurn__(self) -> None :

        self.__playerToPlayIndex__ = (self.__playerToPlayIndex__ + 1) % len(self.__playersData__)
        
        return None
    
    def __previousTurn__(self) -> None :

        self.__playerToPlayIndex__ = (self.__playerToPlayIndex__ - 1 + len(self.__playersData__)) % len(self.__playersData__)

        return None

    def getPossibleMoves(self) -> list[Move]:
        
        possibleMoveTypes : list[Type[Move]] = [SimpleMove] + self.getPlayerData(self.__playerToPlayIndex__).getPowerUpMoves()
        possibleMoves : list[Move] = []

        for line in range(self.getBoard().getHeight()):
            for column in range(self.getBoard().getWidth()):
                for moveType in possibleMoveTypes:
                    if(moveType.canPlay(self.getBoard(), line, column)):
                        possibleMoves.append(moveType(Coordinate(line, column)))

        return possibleMoves

    def getBoard(self) -> Board :
        return self.__board__
    
    def getPlayerCount(self) -> int :
        return len(self.__playersData__)

    def getPlayerData(self, playerIndex : int) -> PlayerData :
        return self.__playersData__[playerIndex]

    def getPlayerToPlayIndex(self) -> int :
        return self.__playerToPlayIndex__

    def setPlayerToPlayIndex(self, player_index: int) -> None:
        self.__playerToPlayIndex__ = player_index
        return None

    def getGameHistory(self) -> GameHistory :
        return self.__gameHistory__

    def setWinCondition(self, win_condition : WinCondition) -> None :
        self.__winCondition__ = win_condition
        return None

    def checkWin(self) -> GameOutcome :
        return self.__winCondition__.checkWin(self.__board__)
    
    def checkWinForPlayer(self, playerIndex: int) -> GameOutcome :
        return self.__winCondition__.checkWinForPlayer(playerIndex, self.__board__)
    
    def checkWinForCurrentPlayer(self) -> GameOutcome :
        return self.__winCondition__.checkWinForPlayer(self.__playerToPlayIndex__, self.__board__)
    
    def evaluateForPlayer(self, playerIndex: int) -> GameOutcome :
        return self.__winCondition__.evaluateForPlayer(playerIndex, self.__board__)
    
    def copy(self) -> GameState :
        return GameState(self.__board__.copy(), self.__winCondition__, self.__playersData__, self.__playerToPlayIndex__)