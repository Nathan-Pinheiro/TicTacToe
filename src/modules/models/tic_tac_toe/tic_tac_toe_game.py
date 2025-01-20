import random
from typing import List, Dict, Any

from modules.models.board_game.board.board import Board
from modules.models.board_game.board.board_builder import BoardBuilder
from modules.models.board_game.board.boards.optimized_board import OptimizedBoard
from modules.models.board_game.board.components.board_shapes.pyramidal_shape import PyramidalShape
from modules.models.board_game.board.components.board_shapes.circular_shape import CircularShape
from modules.models.board_game.board.components.board_shapes.diamond_shape import DiamondShape
from modules.models.board_game.components.entity import Entity
from modules.models.board_game.game.game_history import GameHistory
from modules.models.board_game.game.game_outcome import GameOutcome
from modules.models.board_game.game.game_analysers.minimax_alpha_beta_pruning_analyser import AlphaBetaPruningAnalyser
from modules.models.board_game.game.game_analysers.minimax_alpha_beta_pruning_analyser import GameAnalyser
from modules.models.board_game.components.move import Move

from modules.models.entities.circle import Circle
from modules.models.entities.cross import Cross
from modules.models.entities.hexagon import Hexagon
from modules.models.entities.rhombus import Rhombus
from modules.models.entities.square import Square
from modules.models.entities.star import Star
from modules.models.entities.triangle import Triangle

from modules.models.tic_tac_toe.moves.power_up_move import PowerUpMove
from modules.models.tic_tac_toe.tic_tac_toe_game_director import GameDirector
from modules.models.tic_tac_toe.tic_tac_toe_game_state import TicTacToeGameState
from modules.models.tic_tac_toe.tic_tac_toe_player import Player
from modules.models.tic_tac_toe.tic_tac_toe_player_data import TicTacToePlayerData
from modules.models.tic_tac_toe.win_conditions.align_victory import AlignVictory
from modules.models.tic_tac_toe.win_conditions.unalign_victory import UnalignVictory
from modules.models.tic_tac_toe.players.human_player import HumanPlayer
from modules.models.tic_tac_toe.players.ai_player import AIPlayer
from modules.models.tic_tac_toe.players.ai_players.easy_ai_player import EasyAIPlayer
from modules.models.tic_tac_toe.players.ai_players.medium_ai_player import MediumAIPlayer
from modules.models.tic_tac_toe.players.ai_players.hard_ai_player import HardAIPlayer
from modules.models.tic_tac_toe.moves.power_ups.bomb_move import BombMove

from modules.utils.decorator import privatemethod

# ************************************************
# CLASS TicTacToeGame
# ************************************************
# ROLE : Manage the Tic Tac Toe game in GUI
# ************************************************
# VERSION : 1.0
# AUTHOR : Hugo MERY
# DATE : 18/01/2025
# ************************************************

class TicTacToeGame:
    
    """
    Represents a Tic Tac Toe game instance
    """
    
    def __init__(self, settings: Dict[str, Any]) -> None:
        
        """
        Initializes the Tic Tac Toe game instance.

        Returns:
            None
        """
        
        self.settings: Dict[str, Any] = settings
        self.board: Board = self.__createBoard__()
        self.gameDirector: GameDirector = self.__initializeGame__()
        self.gameState: TicTacToeGameState = self.gameDirector.getGameState()
        self.analyser: GameAnalyser = AlphaBetaPruningAnalyser(self.__getDepth__())
        
        return None
    
    @privatemethod
    def __createBoard__(self) -> OptimizedBoard:
        
        """
        Creates the game board based on the settings.

        Returns:
            OptimizedBoard: The optimized game board.
        """
        
        self.entities: List[Entity] = [
            self.__getEntityBySymbol__(self.settings['player1']['symbol']),
            self.__getEntityBySymbol__(self.settings['player2']['symbol'])
        ]

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
    
    @privatemethod
    def __createPlayers__(self) -> List[Player]:
        
        """
        Creates the players based on the settings.

        Returns:
            list[Player]: The list of players.
        """
        
        playerType = {
            'human': HumanPlayer,
            'easy': EasyAIPlayer,
            'medium': MediumAIPlayer,
            'hard': HardAIPlayer
        }
        
        playerOne = playerType[self.settings['player1']['type']](self.settings['player1']['name'])
        playerTwo = playerType[self.settings['player2']['type']](self.settings['player2']['name'])
        
        return [playerOne, playerTwo]
    
    @privatemethod
    def __createWinCondition__(self) -> AlignVictory | UnalignVictory:
        
        """
        Creates the win condition based on the settings.
        
        Returns:
            AlignVictory | UnalignVictory: The win condition.
        """
        
        if self.settings['game']['alignToWin']:
            return AlignVictory(self.settings['game']['nbSymbols'])
        else:
            return UnalignVictory(self.settings['game']['nbSymbols'])
        
    @privatemethod
    def __createPlayersData__(self, nbPlayers: int) -> List[TicTacToePlayerData]:
        
        """
        Creates the players data based on the settings.
        
        Parameters:
            nbPlayers (int): The number of players.
            
        Returns:
            list[TicTacToePlayerData]: The list of players data.
        """
        
        if self.settings['game']['gamemode'] == 'Bomb mod':
            return [TicTacToePlayerData([BombMove]) for _ in range(nbPlayers)]
        return [TicTacToePlayerData([]) for _ in range(nbPlayers)]
    
    @privatemethod
    def __createStartingPlayer__(self) -> int:
        
        """
        Creates the starting player based on the settings.
        
        Returns:
            int: The index of the starting player.
        """
        
        if self.settings['game']['startingPlayer'] == 'Random':
            return -1
        return 0 if self.settings['game']['startingPlayer'] == self.settings['player1']['name'] else 1
    
    @privatemethod
    def __getDepth__(self) -> int:
        
        """
        Get the depth of the AI based on the board size.
        
        Returns:
            int: The depth of the AI.
        """
        
        boardSize = self.settings['board']['width'] * self.settings['board']['height']
        if boardSize <= 9:
            depth = 8
        elif boardSize <= 25:
            depth = 6
        else:
            depth = 4
        return depth
    
    @privatemethod
    def __initializeGame__(self) -> GameDirector:
        
        """
        Initializes the game director.
        
        Returns:
            GameDirector: The game director.
        """
        
        players = self.__createPlayers__()
        winCondition = self.__createWinCondition__()
        playersData = self.__createPlayersData__(len(players))
        startingPlayer = self.__createStartingPlayer__()
        
        return GameDirector(self.board, winCondition, players, playersData, startingPlayer)

    def playHumainMove(self, line: int, column: int, bomb: bool) -> GameOutcome:
        
        """
        Plays a human move.
        
        Parameters:
            line (int): The line of the move.
            column (int): The column of the move.
            bomb (bool): The bomb attribute.
            
        Returns:
            GameOutcome: The result of the game after the move.
        """
        
        currentPlayer = self.gameDirector.getPlayerToPlay()
        
        if isinstance(currentPlayer, HumanPlayer):
            move = currentPlayer.get_choice(self.gameState, line, column, bomb)
            self.gameState.play(move)
            return self.gameState.checkWin()
        
        return None

    def playAiMove(self) -> GameOutcome:
        
        """
        Plays an AI move.
        
        Returns:
            GameOutcome: The result of the game after the move.
        """
        
        currentPlayer = self.gameDirector.getPlayerToPlay()

        if isinstance(currentPlayer, AIPlayer):
            
            move = currentPlayer.get_choice(self.gameState)
            self.gameState.play(move)
            return self.gameState.checkWin()
        
        return None
    
    def undo(self) -> bool:
        
        """
        Undo the last move.
        
        Returns:
            bool: True if the undo was successful, False otherwise
        """
        
        return self.gameState.goBack()
    
    def redo(self) -> bool:
        
        """
        Redo the last move.
        
        Returns:
            bool: True if the redo was successful, False otherwise
        """
        
        return self.gameState.goNext()
        
    def getAdvice(self) -> Move:
        
        """
        Get the best move to play.
        
        Returns:
            Move: The best move to play.
        """
        
        return self.analyser.getBestMove(self.gameState)
    
    def getPlayerToPlay(self) -> Player:
        
        """
        Get the player to play.
        
        Returns:
            Player: The player to play.
        """
        
        return self.gameDirector.getPlayerToPlay()
        
    def getBoard(self) -> Board:
        
        """
        Get the game board.
        
        Returns:
            Board: The game board.
        """
        
        return self.board
    
    def getGameState(self) -> TicTacToeGameState:
        
        """
        Get the game state.
        
        Returns:
            TicTacToeGameState: The game state.
        """
        
        return self.gameState

    def getGameDirector(self) -> GameDirector:
        
        """
        Get the game director.
        
        Returns:
            GameDirector: The game director.
        """
        
        return self.gameDirector

    def getEntities(self) -> List[Entity]:
        
        """
        Get the entities.
        
        Returns:
            list[Entity]: The entities.
        """
        
        return self.entities

    def getGameHistoryList(self) -> List[Move]:
        
        """
        Get the game history.
        
        Returns:
            list: The game history.
        """
        
        return self.gameState.getGameHistory().getMoves()
    
    def getGameHistory(self) -> GameHistory:
        
        """
        Get the game history.
        
        Returns:
            TicTacToeGameState: The game history.
        """
        
        return self.gameState.getGameHistory()
    
    def getPlayerPowerUpMoves(self, playerIndex: int) -> List[PowerUpMove]:
        
        """
        Get the power up moves of a player.
        
        Parameters:
            playerIndex (int): The index of the player.
            
        Returns:
            list[type[PowerUpMove]]: The power up moves of the player.
        """
        
        if playerIndex < 0 or playerIndex >= 3: return []
        
        return self.gameState.getPlayerData(playerIndex).getPowerUpMoves()

    @privatemethod
    def __getEntityBySymbol__(self, symbol: str) -> Entity:
        
        """
        Get the entity based on the symbol.
        
        Parameters:
            symbol (str): The symbol.
            
        Returns:
            Entity: The entity.
        """
        
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