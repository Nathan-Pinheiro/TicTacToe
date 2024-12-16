# from modules.GUI.render import App

# if(__name__ == "__main__") :
             
#     app = App("TicTacToe")
#     app.mainloop()
    
from modules.models.board_components.board import Board
from modules.models.board_components.board_builder import BoardBuilder
from modules.models.board_components.board_shapes.pyramidal_shape import PyramidalShape
from modules.models.tic_tac_toe.game_director import GameDirector
from modules.models.tic_tac_toe.players.player import Player
from modules.models.tic_tac_toe.win_conditions.align_victory import AlignVictory
from modules.models.tic_tac_toe.players.human_player import HumanPlayer
from modules.models.tic_tac_toe.player_data import PlayerData
from modules.models.entities.circle import Circle
from modules.models.entities.cross import Cross
from modules.models.tic_tac_toe.power_ups.bomb import Bomb
from modules.models.coordinate_encoder import *
from modules.models.console_displayer import display_board
from modules.models.board_components.coordinate import *

import os

if(__name__ == "__main__"):
    
    width : int = 5
    height : int = 5
    
    players : list[Player] = [HumanPlayer("Jean"), HumanPlayer("Jacques")]
    playersData : list[PlayerData] = [PlayerData(Cross(), [Bomb()]), PlayerData(Circle(), [Bomb()])]
    board : Board = BoardBuilder().setHeight(5).setWidth(7).setShape(PyramidalShape()).build()

    winCondition = AlignVictory(3)

    game_director = GameDirector(board, winCondition, players, playersData)

    game_director.launchGame()