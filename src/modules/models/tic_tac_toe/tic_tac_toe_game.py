# src/modules/models/tic_tac_toe/tic_tac_toe_game.py

from modules.models.board_components.board import Board
from modules.models.board_components.board_builder import BoardBuilder
from modules.models.board_components.board_shapes.pyramidal_shape import PyramidalShape
from modules.models.entities.triangle import Triangle
from modules.models.entities.hexagon import Hexagon
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

    def set_number_of_players(self, num_players):
        current_num_players = len(self.players)
        
        if num_players > current_num_players:
            # Ajouter les nouveaux joueurs et leurs données
            for i in range(current_num_players, num_players):
                self.players.append(AlphaBetaPruningPlayer(4, False))  # Par défaut, un joueur IA
                # On met un symbole différent pour chaque joueur
                if i % 4 == 0:
                    self.player_entities.append(Cross())
                elif i % 4 == 1:
                    self.player_entities.append(Circle())
                elif i % 4 == 2:
                    self.player_entities.append(Triangle())
                elif i % 4 == 3:
                    self.player_entities.append(Hexagon())
                self.players_data.append(PlayerData([]))  # Initialisation des données du joueur
        
        elif num_players < current_num_players:
            # Réduire les listes si le nombre de joueurs est diminué
            self.players = self.players[:num_players]
            self.player_entities = self.player_entities[:num_players]
            self.players_data = self.players_data[:num_players]

    def set_board_size(self, width, height):
        self.board = BoardBuilder(self.player_entities).setHeight(height).setWidth(width).setShape(PyramidalShape()).buildOptimizedBoard()
        self.game_director = GameDirector(self.board, self.win_condition, self.players, self.players_data)
        self.game_state = self.game_director.getGameState()

    def set_player_type(self, player_index, is_human):
        if player_index >= len(self.players):
            raise IndexError(f"Player index {player_index} is out of range. Total players: {len(self.players)}")
        if is_human:
            self.players[player_index] = HumanPlayer(f"Player {player_index + 1}")
        else:
            self.players[player_index] = AlphaBetaPruningPlayer(4, False)
            
    def set_player_symbol(self, player_index, symbol):
        if player_index >= len(self.players):
            raise IndexError(f"Player index {player_index} is out of range. Total players: {len(self.players)}")
        if symbol == "X":
            self.player_entities[player_index] = Cross()
        elif symbol == "O":
            self.player_entities[player_index] = Circle()
        elif symbol == "∆":
            self.player_entities[player_index] = Triangle()
        elif symbol == "⬡":
            self.player_entities[player_index] = Hexagon()
            
    def set_player_color(self, player_index, color):
        if player_index >= len(self.players):
            raise IndexError(f"Player index {player_index} is out of range. Total players: {len(self.players)}")
        self.players[player_index].setColor(color)