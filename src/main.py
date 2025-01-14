from modules.models.board_game.board.board import Board
from modules.models.board_game.board.board_builder import BoardBuilder
from modules.models.board_game.components.coordinate import *
from modules.models.board_game.components.coordinate_encoder import *
from modules.models.board_game.components.player_data import PlayerData

from modules.models.tic_tac_toe.tic_tac_toe_player import Player
from modules.models.tic_tac_toe.tic_tac_toe_player_data import TicTacToePlayerData
from modules.models.tic_tac_toe.tic_tac_toe_game_director import GameDirector
from modules.models.tic_tac_toe.win_conditions.align_victory import AlignVictory

from modules.models.tic_tac_toe.tic_tac_toe_game_state import TicTacToeGameState
from modules.models.utils.console_displayer import *

from modules.models.entities.circle import Circle
from modules.models.entities.cross import Cross
from modules.models.entities.triangle import Triangle
from modules.models.entities.hexagon import Hexagon

from modules.models.tic_tac_toe.players.human_console_player import HumanConsolePlayer
from modules.models.tic_tac_toe.players.ai_players.v1_random_player import RandomPlayer
from modules.models.tic_tac_toe.players.ai_players.v2_minimax_player import MinimaxPlayer
from modules.models.tic_tac_toe.players.ai_players.v3_alpha_beta_pruning_player import AlphaBetaPruningPlayer
from modules.models.tic_tac_toe.players.ai_players.v4_better_move_order_player import MinimaxBetterMoveOrderingPlayer
from modules.models.tic_tac_toe.players.ai_players.v5_2_transposition_table import MinimaxTranspositionTablePlayer
from modules.models.tic_tac_toe.players.ai_players.v6_iterative_deeping import MinimaxIterativeDeepingPlayer

import os

if(__name__ == "__main__"):

    players : list[Player] = [HumanConsolePlayer("Lana"), MinimaxBetterMoveOrderingPlayer(5)]
    playerEntities = [Cross(), Circle()]
    playersData : list[PlayerData] = [TicTacToePlayerData([]), TicTacToePlayerData([])]
    
    board : Board = BoardBuilder(playerEntities).setHeight(3).setWidth(3).buildOptimizedBoard()
    winCondition = AlignVictory(3)

    game_director = GameDirector(board, winCondition, players, playersData, 1)

    gameState : TicTacToeGameState = game_director.launchGame()

    display_sep()
    display_board(gameState.getBoard())
    display_sep()
    
    display(gameState.checkWin())
    