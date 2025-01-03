# src/modules/models/tic_tac_toe/tic_tac_toe_game.py

from modules.models.board_components.board import Board
from modules.models.board_components.board_builder import BoardBuilder
from modules.models.board_components.board_shapes.pyramidal_shape import PyramidalShape
from modules.models.entities.triangle import Triangle
from modules.models.entities.hexagon import Hexagon
from modules.models.tic_tac_toe.game_director import GameDirector
from modules.models.tic_tac_toe.win_conditions.align_victory import AlignVictory
from modules.models.tic_tac_toe.players.human_player import HumanPlayer
from modules.models.tic_tac_toe.players.ai_player import AIPlayer
from modules.models.tic_tac_toe.players.ai_players.v5_transpostion_table import MinimaxTranspositionTablePlayer
from modules.models.tic_tac_toe.player_data import PlayerData
from modules.models.entities.circle import Circle
from modules.models.entities.cross import Cross
from modules.models.entities.star import Star
from modules.models.entities.rhombus import Rhombus
from modules.models.entities.square import Square

class TicTacToeGame:
    def __init__(self):
        self.players = []
        self.player_entities = []
        self.players_data = []
        self.width = 3
        self.height = 3
        self.board = None
        self.win_condition = AlignVictory(3)
        self.game_director = None
        self.game_state = None

    def initialize_game(self):
        self.game_director = GameDirector(self.board, self.win_condition, self.players, self.players_data, 1)
        self.game_state = self.game_director.getGameState()

    def play_move(self, line, column):
        current_player = self.game_director.getPlayerToPlay()
        
        if isinstance(current_player, HumanPlayer):
            move = current_player.get_choice(self.game_state, line, column)
            move.play(self.board, self.game_state.getPlayerToPlayIndex())
            return self.game_state.checkWin()
        
        if isinstance(current_player, AIPlayer):
            move = current_player.get_choice(self.game_state)
            move.play(self.board, self.game_state.getPlayerToPlayIndex())
            return self.game_state.checkWin()
        
        return None

    def play_ai_move(self):
        current_player = self.game_director.getPlayerToPlay()
        if isinstance(current_player, AIPlayer):
            move = current_player.get_choice(self.game_state)
            move.play(self.board, self.game_state.getPlayerToPlayIndex())
            return self.game_state.checkWin()
        return None
    
    def get_player_to_play(self):
        return self.game_director.getPlayerToPlay()

    def set_number_of_players(self, num_players):
        current_num_players = len(self.players)
        
        if num_players > current_num_players:
            for i in range(current_num_players, num_players):
                self.players.append(MinimaxTranspositionTablePlayer(6, False))
                self.player_entities.append(self.get_default_entity(i))
                self.players_data.append(PlayerData([]))
        
        elif num_players < current_num_players:
            self.players = self.players[:num_players]
            self.player_entities = self.player_entities[:num_players]
            self.players_data = self.players_data[:num_players]

    def set_board_size(self, width, height):
        self.width = width
        self.height = height

    def set_player_type(self, player_index, is_human):
        if player_index >= len(self.players):
            raise IndexError(f"Player index {player_index} is out of range. Total players: {len(self.players)}")
        if is_human:
            self.players[player_index] = HumanPlayer(f"Player {player_index + 1}")
        else:
            self.players[player_index] = MinimaxTranspositionTablePlayer(6, False)
            
    def set_player_symbol(self, player_index, symbol):
        if player_index >= len(self.players):
            raise IndexError(f"Player index {player_index} is out of range. Total players: {len(self.players)}")
        self.player_entities[player_index] = self.get_entity_by_symbol(symbol)
            
    def set_player_color(self, player_index, color):
        if player_index >= len(self.players):
            raise IndexError(f"Player index {player_index} is out of range. Total players: {len(self.players)}")
        self.players[player_index].setColor(color)
        
    def set_is_pyramidal(self, is_pyramidal):
        if is_pyramidal:
            self.board = BoardBuilder(self.player_entities).setHeight(self.height).setWidth(self.width).setShape(PyramidalShape()).buildOptimizedBoard()
        else:
            self.board = BoardBuilder(self.player_entities).setHeight(self.height).setWidth(self.width).buildOptimizedBoard()
        self.initialize_game()
        
    def set_symbols_to_align(self, symbols_to_align):
        self.win_condition = AlignVictory(symbols_to_align)
        
    def set_player_name(self, player_names):
        for i in range(len(player_names)):
            self.players[i].setName(player_names[i])
        
    def get_board(self):
        return self.board

    def get_default_entity(self, index):
        entities = [Cross(), Circle(), Triangle(), Hexagon()]
        return entities[index % len(entities)]
    
    def get_game_state(self):
        return self.game_state

    def get_entity_by_symbol(self, symbol):
        if symbol == "X":
            return Cross()
        elif symbol == "O":
            return Circle()
        elif symbol == "△":
            return Triangle()
        elif symbol == "⬡":
            return Hexagon()
        elif symbol == "◊":
            return Rhombus()
        elif symbol == "▢":
            return Square()
        elif symbol == "★":
            return Star()
        else:
            raise ValueError(f"Unknown symbol: {symbol}")