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

from modules.models.board_game.board.board import Board
from modules.models.board_game.board.board_builder import BoardBuilder
from modules.models.board_game.board.components.board_shapes.pyramidal_shape import PyramidalShape
from modules.models.board_game.board.components.board_shapes.circular_shape import CircularShape
from modules.models.board_game.board.components.board_shapes.diamond_shape import DiamondShape
from modules.models.board_game.components.entity import Entity
from modules.models.entities.triangle import Triangle
from modules.models.entities.hexagon import Hexagon
from modules.models.tic_tac_toe.tic_tac_toe_game_director import GameDirector
from modules.models.board_game.game.game_outcome import GameOutcome
from modules.models.tic_tac_toe.tic_tac_toe_game_state import TicTacToeGameState
from modules.models.tic_tac_toe.tic_tac_toe_player import Player
from modules.models.tic_tac_toe.win_conditions.align_victory import AlignVictory
from modules.models.tic_tac_toe.win_conditions.unalign_victory import UnalignVictory
from modules.models.tic_tac_toe.players.human_player import HumanPlayer
from modules.models.tic_tac_toe.players.ai_player import AIPlayer
from modules.models.tic_tac_toe.players.ai_players.easy_ai_player import EasyAIPlayer
from modules.models.tic_tac_toe.players.ai_players.medium_ai_player import MediumAIPlayer
from modules.models.tic_tac_toe.players.ai_players.hard_ai_player import HardAIPlayer
from modules.models.board_game.board.boards.optimized_board import OptimizedBoard
from modules.models.tic_tac_toe.tic_tac_toe_player_data import TicTacToePlayerData
from modules.models.entities.circle import Circle
from modules.models.entities.cross import Cross
from modules.models.entities.star import Star
from modules.models.entities.rhombus import Rhombus
from modules.models.entities.square import Square
from modules.utils.decorator import privatemethod
from modules.models.tic_tac_toe.moves.power_ups.bomb_move import BombMove
import random

class TicTacToeGame:
    
    def __init__(self, settings) -> None:
        self.settings = settings
        self.board = self.__createBoard__()
        self.gameDirector = self.__initializeGame__()
        self.gameState = self.gameDirector.getGameState()
        self.gameHistory = []
        return None
    
    def __createBoard__(self) -> OptimizedBoard:
        self.entities = [self.__getEntityBySymbol__(self.settings['player1']['symbol']), self.__getEntityBySymbol__(self.settings['player2']['symbol'])]

        board = BoardBuilder(self.entities).setWidth(self.settings['board']['width']).setHeight(self.settings['board']['height'])
        
        shape = {
            'Pyramidal': PyramidalShape(),
            'Circular': CircularShape(),
            'Diamond': DiamondShape(),
            'Random': random.choice([PyramidalShape(), CircularShape(), DiamondShape()]),
            'No special shape': None
        }[self.settings['board']['shape']]
        
        if shape:
            board.setShape(shape)
        
        return board.buildOptimizedBoard()
    
    def __createPlayers__(self) -> list[Player]:
        playerType = {
            'human': HumanPlayer,
            'easy': EasyAIPlayer,
            'medium': MediumAIPlayer,
            'hard': HardAIPlayer
        }
        
        playerOne = playerType[self.settings['player1']['type']](self.settings['player1']['name'])
        playerTwo = playerType[self.settings['player2']['type']](self.settings['player2']['name'])
        
        return [playerOne, playerTwo]
    
    def __createWinCondition__(self) -> AlignVictory | UnalignVictory:
        if self.settings['game']['alignToWin']:
            return AlignVictory(self.settings['game']['nbSymbols'])
        else:
            return UnalignVictory(self.settings['game']['nbSymbols'], 2)
        
    def __createPlayersData__(self, nbPlayers) -> list[TicTacToePlayerData]:
        if self.settings['game']['gamemode'] == 'Bomb mod':
            return [TicTacToePlayerData([BombMove]) for _ in range(nbPlayers)]
        return [TicTacToePlayerData([]) for _ in range(nbPlayers)]
    
    def __createStartingPlayer__(self) -> int:
        if self.settings['game']['startingPlayer'] == 'Random':
            return -1
        return 0 if self.settings['game']['startingPlayer'] == self.settings['player1']['name'] else 1
    
    def __initializeGame__(self) -> GameDirector:
        players = self.__createPlayers__()
        winCondition = self.__createWinCondition__()
        playersData = self.__createPlayersData__(len(players))
        startingPlayer = self.__createStartingPlayer__()
        
        return GameDirector(self.board, winCondition, players, playersData, startingPlayer)

    def playHumainMove(self, line: int, column: int) -> GameOutcome:
        currentPlayer = self.gameDirector.getPlayerToPlay()
        
        if isinstance(currentPlayer, HumanPlayer):
            move = currentPlayer.get_choice(self.gameState, line, column)
            move.play(self.board, self.gameState.getPlayerToPlayIndex())
            self.gameHistory.append(move)
            self.gameState.__nextTurn__()
            return self.gameState.checkWin()
        
        return None

    def playAiMove(self) -> GameOutcome:
        
        currentPlayer = self.gameDirector.getPlayerToPlay()

        if isinstance(currentPlayer, AIPlayer):
            move = currentPlayer.get_choice(self.gameState)
            move.play(self.board, self.gameState.getPlayerToPlayIndex())
            self.gameHistory.append(move)
            self.gameState.__nextTurn__()
            return self.gameState.checkWin()
        return None
    
    def getPlayerToPlay(self) -> Player:
        return self.gameDirector.getPlayerToPlay()
        
    def getBoard(self) -> Board:
        return self.board
    
    def getGameState(self) -> TicTacToeGameState:
        return self.gameState

    def getGameDirector(self) -> GameDirector:
        return self.gameDirector

    def getEntities(self) -> list[Entity]:
        return self.entities

    def getGameHistory(self) -> list:
        return self.gameHistory

    @privatemethod
    def __getEntityBySymbol__(self, symbol: str) -> Entity:
        entityClasses = {
            'cross': Cross,
            'circle': Circle,
            'triangle': Triangle,
            'hexagon': Hexagon,
            'star': Star,
            'square': Square,
            'rhombus': Rhombus
        }
        
        if symbol in entityClasses : return entityClasses[symbol]()
        else : raise ValueError(f"Unknown symbol: {symbol}")