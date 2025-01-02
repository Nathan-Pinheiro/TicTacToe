# src/modules/models/tic_tac_toe/tic_tac_toe_game.py

from modules.models.board_components.board import Board
from modules.models.board_components.board_builder import BoardBuilder
from modules.models.board_components.board_shapes.pyramidal_shape import PyramidalShape
from modules.models.entities.triangle import Triangle
from modules.models.tic_tac_toe.game_director import GameDirector
from modules.models.tic_tac_toe.win_conditions.align_victory import AlignVictory
from modules.models.tic_tac_toe.players.human_player import HumanPlayer
from modules.models.tic_tac_toe.players.alpha_beta_pruning_player import AlphaBetaPruningPlayer
from modules.models.tic_tac_toe.player_data import PlayerData
from modules.models.entities.circle import Circle
from modules.models.entities.cross import Cross

class TicTacToeGame:
    def __init__(self):
        self.players = [HumanPlayer("Jean"), AlphaBetaPruningPlayer(4, False), AlphaBetaPruningPlayer(4, False)]
        self.player_entities = [Cross(), Circle(), Triangle()]
        self.players_data = [PlayerData([]), PlayerData([]), PlayerData([])]
        self.board = BoardBuilder(self.player_entities).setHeight(7).setWidth(7).setShape(PyramidalShape()).buildOptimizedBoard()
        self.win_condition = AlignVictory(3)
        self.game_director = GameDirector(self.board, self.win_condition, self.players, self.players_data)
        self.game_state = self.game_director.getGameState()

    def play_move(self, line, column):
        # Get the current player
        current_player = self.game_director.getPlayerToPlay()
        
        # if the current player is a human player, get the move from the player
        if isinstance(current_player, HumanPlayer):
            move = current_player.get_choice(self.game_state, line, column)
            move.play(self.board, self.game_state.getPlayerToPlayIndex())
            return self.game_state.checkWin()
        
        # if the current player is an AI player, get the move from the AI and play it immediately
        if isinstance(current_player, AlphaBetaPruningPlayer):
            move = current_player.get_choice(self.game_state)
            move.play(self.board, self.game_state.getPlayerToPlayIndex())
            return self.game_state.checkWin()
        
        return None

    def play_ai_move(self):
        current_player = self.game_director.getPlayerToPlay()
        if isinstance(current_player, AlphaBetaPruningPlayer):
            move = current_player.get_choice(self.game_state)
            move.play(self.board, self.game_state.getPlayerToPlayIndex())
            return self.game_state.checkWin()
        return None
    
    def get_player_to_play(self):
        return self.game_director.getPlayerToPlay()