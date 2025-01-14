# src/modules/models/tic_tac_toe/tic_tac_toe_game.py

"""
Tic Tac Toe Game Module

This module provides the implementation of the Tic Tac Toe game logic.

Classes:
    TicTacToeGame: Represents the Tic Tac Toe game.

Functions:
    __init__(self) -> None:
        Initialize the Tic Tac Toe game.
        
    initializeGame(self) -> bool:
        Initialize the game state and director.
        
    playMove(self, line: int, column: int) -> GameOutcome:
        Play a move for the current player.
        
    playAiMove(self) -> GameOutcome:
        Play a move for the AI player.
        
    getPlayerToPlay(self) -> Player:
        Get the current player to play.
        
    setNumberOfPlayers(self, numPlayers: int) -> bool:
        Set the number of players for the game.
        
    setBoardSize(self, width: int, height: int) -> bool:
        Set the size of the game board.
        
    setPlayerType(self, playerIndex: int, isHuman: bool) -> bool:
        Set the type of a player (human or AI).
        
    setPlayerSymbol(self, playerIndex: int, symbol: str) -> bool:
        Set the symbol of a player.
        
    setPlayerColor(self, playerIndex: int, color: str) -> bool:
        Set the color of a player.
        
    setIsPyramidal(self, isPyramidal: bool) -> bool:
        Set whether the game board is pyramidal.
        
    setSymbolsToAlign(self, symbolsToAlign: int) -> bool:
        Set the number of symbols to align to win the game.
        
    setPlayerName(self, playerNames: list[str]) -> bool:
        Set the names of the players.
        
    getBoard(self) -> Board:
        Get the game board.
        
    __getDefaultEntity__(self, index: int) -> Entity:
        Private method.
        Get the default entity for a player.
        
    getGameState(self) -> GameState:
        Get the current game state.
        
    __getEntityBySymbol__(self, symbol: str) -> Entity:
        Private method.
        Get the entity corresponding to a symbol.
"""

from modules.models.board_components.board import Board
from modules.models.board_components.board_builder import BoardBuilder
from modules.models.board_components.board_shapes.pyramidal_shape import PyramidalShape
from modules.models.board_components.entity import Entity
from modules.models.entities.triangle import Triangle
from modules.models.entities.hexagon import Hexagon
from modules.models.tic_tac_toe.tic_tac_toe_game_director import GameDirector
from modules.models.tic_tac_toe.game_outcome import GameOutcome
from modules.models.tic_tac_toe.tic_tac_toe_game_state import TicTacToeGameState
from modules.models.tic_tac_toe.tic_tac_toe_player import Player
from modules.models.tic_tac_toe.win_conditions.align_victory import AlignVictory
from modules.models.tic_tac_toe.players.human_player import HumanPlayer
from modules.models.tic_tac_toe.players.ai_player import AIPlayer
from modules.models.tic_tac_toe.players.ai_players.v5_transpostion_table import MinimaxTranspositionTablePlayer
from modules.models.tic_tac_toe.tic_tac_toe_player_data import PlayerData
from modules.models.entities.circle import Circle
from modules.models.entities.cross import Cross
from modules.models.entities.star import Star
from modules.models.entities.rhombus import Rhombus
from modules.models.entities.square import Square
from modules.utils.decorator import privatemethod

class TicTacToeGame:
    def __init__(self) -> None:
        self.players = []
        self.playerEntities = []
        self.playersData = []
        self.width = 3
        self.height = 3
        self.board = None
        self.winCondition = AlignVictory(3)
        self.gameDirector = None
        self.gameState = None
        return None

    def initializeGame(self) -> bool:
        try:
            self.gameDirector = GameDirector(self.board, self.winCondition, self.players, self.playersData, 1)
            self.gameState = self.gameDirector.getGameState()
            return True
        except Exception as e:
            print(f"Error initializing game: {e}")
            return False

    def playMove(self, line: int, column: int) -> GameOutcome:
        currentPlayer = self.gameDirector.getPlayerToPlay()
        
        if isinstance(currentPlayer, HumanPlayer):
            move = currentPlayer.get_choice(self.gameState, line, column)
            move.play(self.board, self.gameState.getPlayerToPlayIndex())
            return self.gameState.checkWin()
        
        if isinstance(currentPlayer, AIPlayer):
            move = currentPlayer.get_choice(self.gameState)
            move.play(self.board, self.gameState.getPlayerToPlayIndex())
            return self.gameState.checkWin()
        
        return None

    def playAiMove(self) -> GameOutcome:
        currentPlayer = self.gameDirector.getPlayerToPlay()
        if isinstance(currentPlayer, AIPlayer):
            move = currentPlayer.get_choice(self.gameState)
            move.play(self.board, self.gameState.getPlayerToPlayIndex())
            return self.gameState.checkWin()
        return None
    
    def getPlayerToPlay(self) -> Player:
        return self.gameDirector.getPlayerToPlay()

    def setNumberOfPlayers(self, numPlayers: int) -> bool:
        try:
            currentNumPlayers = len(self.players)
            
            if numPlayers > currentNumPlayers:
                for i in range(currentNumPlayers, numPlayers):
                    self.players.append(MinimaxTranspositionTablePlayer(6, False))
                    self.playerEntities.append(self.__getDefaultEntity__(i))
                    self.playersData.append(PlayerData([]))
            
            elif numPlayers < currentNumPlayers:
                self.players = self.players[:numPlayers]
                self.playerEntities = self.playerEntities[:numPlayers]
                self.playersData = self.playersData[:numPlayers]
            return True
        except Exception as e:
            print(f"Error setting number of players: {e}")
            return False

    def setBoardSize(self, width: int, height: int) -> bool:
        try:
            self.width = width
            self.height = height
            return True
        except Exception as e:
            print(f"Error setting board size: {e}")
            return False

    def setPlayerType(self, playerIndex: int, isHuman: bool) -> bool:
        try:
            if playerIndex >= len(self.players):
                raise IndexError(f"Player index {playerIndex} is out of range. Total players: {len(self.players)}")
            if isHuman:
                self.players[playerIndex] = HumanPlayer(f"Player {playerIndex + 1}")
            else:
                self.players[playerIndex] = MinimaxTranspositionTablePlayer(6, False)
            return True
        except Exception as e:
            print(f"Error setting player type: {e}")
            return False
            
    def setPlayerSymbol(self, playerIndex: int, symbol: str) -> bool:
        try:
            if playerIndex >= len(self.players):
                raise IndexError(f"Player index {playerIndex} is out of range. Total players: {len(self.players)}")
            self.playerEntities[playerIndex] = self.__getEntityBySymbol__(symbol)
            return True
        except Exception as e:
            print(f"Error setting player symbol: {e}")
            return False
            
    def setPlayerColor(self, playerIndex: int, color: str) -> bool:
        try:
            if playerIndex >= len(self.players):
                raise IndexError(f"Player index {playerIndex} is out of range. Total players: {len(self.players)}")
            self.players[playerIndex].setColor(color)
            return True
        except Exception as e:
            print(f"Error setting player color: {e}")
            return False
        
    def setIsPyramidal(self, isPyramidal: bool) -> bool:
        try:
            if isPyramidal:
                self.board = BoardBuilder(self.playerEntities).setHeight(self.height).setWidth(self.width).setShape(PyramidalShape()).buildOptimizedBoard()
            else:
                self.board = BoardBuilder(self.playerEntities).setHeight(self.height).setWidth(self.width).buildOptimizedBoard()
            if not self.initializeGame():
                return False
            return True
        except Exception as e:
            print(f"Error setting isPyramidal: {e}")
            return False
        
    def setSymbolsToAlign(self, symbolsToAlign: int) -> bool:
        try:
            self.winCondition = AlignVictory(symbolsToAlign)
            return True
        except Exception as e:
            print(f"Error setting symbols to align: {e}")
            return False
        
    def setPlayerName(self, playerNames: list[str]) -> bool:
        try:
            for i in range(len(playerNames)):
                self.players[i].setName(playerNames[i])
            return True
        except Exception as e:
            print(f"Error setting player names: {e}")
            return False
        
    def getBoard(self) -> Board:
        return self.board

    @privatemethod
    def __getDefaultEntity__(self, index: int) -> Entity:
        entities = [Cross(), Circle(), Triangle(), Hexagon()]
        return entities[index % len(entities)]
    
    def getGameState(self) -> TicTacToeGameState:
        return self.gameState

    @privatemethod
    def __getEntityBySymbol__(self, symbol: str) -> Entity:
        entityClasses = {
            'X': Cross,
            'O': Circle,
            '△': Triangle,
            '⬡': Hexagon,
            '★': Star,
            '▢': Square,
            '◊': Rhombus
        }
        
        if symbol in entityClasses : return entityClasses[symbol]()
        else : raise ValueError(f"Unknown symbol: {symbol}")