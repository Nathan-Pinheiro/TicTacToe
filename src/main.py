# from modules.GUI.render import App

# if(__name__ == "__main__") :
             
#     app = App("TicTacToe")
#     app.mainloop()
    
from modules.models.board_components.board import Board
from modules.models.board_components.board_builder import BoardBuilder
from modules.models.board_components.board_shapes.pyramidal_shape import PyramidalShape
from modules.models.board_components.board_shapes.circular_shape import CircularShape
from modules.models.board_components.board_shapes.diamondShape import DiamondShape
from modules.models.tic_tac_toe.game_director import GameDirector
from modules.models.tic_tac_toe.player import Player
from modules.models.tic_tac_toe.win_conditions.align_victory import AlignVictory
from modules.models.tic_tac_toe.players.human_console_player import HumanConsolePlayer

from modules.models.tic_tac_toe.player_data import PlayerData

from modules.models.tic_tac_toe.moves.bomb_move import BombMove
from modules.models.coordinate_encoder import *
from modules.models.console_displayer import *
from modules.models.board_components.coordinate import *
from modules.models.tic_tac_toe.game_state import GameState

from modules.models.entities.circle import Circle
from modules.models.entities.cross import Cross
from modules.models.entities.triangle import Triangle
from modules.models.entities.hexagon import Hexagon

from modules.models.tic_tac_toe.players.ai_players.v1_random_player import RandomPlayer
from modules.models.tic_tac_toe.players.ai_players.v2_minimax_player import MinimaxPlayer
from modules.models.tic_tac_toe.players.ai_players.v3_alpha_beta_pruning_player import AlphaBetaPruningPlayer
from modules.models.tic_tac_toe.players.ai_players.v4_better_move_order_player import MinimaxBetterMoveOrderingPlayer
from modules.models.tic_tac_toe.players.ai_players.v5_transpostion_table import MinimaxTranspositionTablePlayer
from modules.models.tic_tac_toe.players.ai_players.v6_iterative_deeping import MinimaxIterativeDeepingPlayer

import os

if(__name__ == "__main__"):

    players : list[Player] = [HumanConsolePlayer("Nath"), MinimaxTranspositionTablePlayer(20, True)]
    playerEntities = [Cross(), Circle()]
    playersData : list[PlayerData] = [PlayerData([]), PlayerData([])]
    
    board : Board = BoardBuilder(playerEntities).setHeight(4).setWidth(4).buildOptimizedBoard()
    winCondition = AlignVictory(4)

    game_director = GameDirector(board, winCondition, players, playersData, 1)

    gameState : GameState = game_director.launchGame()
    
    display_sep()
    display_board(gameState.getBoard())
    display_sep()
    
    display(gameState.checkWin())
    