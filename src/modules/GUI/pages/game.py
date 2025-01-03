import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import sv_ttk
import time
from modules.GUI.draft.grid import draw_grid
from modules.models.tic_tac_toe.game_outcome import GameOutcomeStatus
from modules.models.tic_tac_toe.players.ai_players.v5_transpostion_table import MinimaxTranspositionTablePlayer
from modules.utils.decorator import private_method
from modules.models.tic_tac_toe.tic_tac_toe_game import TicTacToeGame

class Game(ttk.Frame):
    def __init__(self, parent: tk.Tk, controller: tk.Tk, size: int = 100, button_color: str = "#555") -> None:
        super().__init__(parent)
        self.controller = controller
        self.tic_tac_toe_game = TicTacToeGame()
        self.board = None
        self.width = size * 4  # Default width, will be updated when game starts
        self.height = size * 6  # Default height, will be updated when game starts
        self.cell_size = size

        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(fill="both", expand=True)

        self.grid_canvas = tk.Canvas(self.main_frame, width=self.width - 3, height=self.height - 3, bg="#333")
        self.grid_canvas.pack(side='left', padx=0, pady=10, anchor='center', expand=True)

        self.info_box = tk.Canvas(self.main_frame, width=700, bg=button_color, highlightthickness=0)
        self.info_box.pack(side="right", fill="y", padx=0, pady=0)

        # Ajout de la zone pour afficher le joueur actuel
        self.current_player_label = ttk.Label(
            self.info_box,
            text="Current Player: ",
            font=("Arial", 18),
            background=button_color,
            foreground="white"
        )
        self.current_player_label.pack(side="top", pady=20)

        self.button_frame = ttk.Frame(self.info_box, style="White.TFrame")
        self.button_frame.pack(side="bottom", fill="x", padx=10, pady=10)

        style = ttk.Style()
        style.configure("White.TFrame", background="#333")

        self.button_images = [
            self.load_png_image("./static/assets/Bomb.png"),
            self.load_png_image("./static/assets/LeftArrow.png"),
            self.load_png_image("./static/assets/RightArrow.png"),
            self.load_png_image("./static/assets/Bulb.png")
        ]

        style = ttk.Style()
        style.configure("Custom.TButton", background=button_color)

        self.button1 = ttk.Button(self.button_frame, image=self.button_images[0], style="Custom.TButton", command=self.__handleBombClick)
        self.button1.pack(side="left", expand=True, padx=5, pady=5)

        self.button2 = ttk.Button(self.button_frame, image=self.button_images[1], style="Custom.TButton", command=self.__handleLeftArrowClick)
        self.button2.pack(side="left", expand=True, padx=5, pady=5)

        self.button3 = ttk.Button(self.button_frame, image=self.button_images[2], style="Custom.TButton", command=self.__handleRightArrowClick)
        self.button3.pack(side="left", expand=True, padx=5, pady=5)

        self.button4 = ttk.Button(self.button_frame, image=self.button_images[3], style="Custom.TButton", command=self.__handleBulbClick)
        self.button4.pack(side="left", expand=True, padx=5, pady=5)
        
        self.result_label = ttk.Label(self.info_box, text="", font=("Arial", 24), background="#555", foreground="white")
        self.return_button = ttk.Button(self.info_box, text="Return to Welcome Page", command=self.return_to_welcome)

        self.grid_canvas.bind("<Button-1>", self.__handle_click)

    def start_game(self):
        self.board = self.tic_tac_toe_game.get_board()
        self.width = self.cell_size * self.board.getWidth()
        self.height = self.cell_size * self.board.getHeight()
        self.grid_canvas.config(width=self.width - 3, height=self.height - 3)

        # Récupérer les symboles et les couleurs des joueurs
        self.player_symbols = [entity.getName() for entity in self.tic_tac_toe_game.player_entities]
        self.player_colors = [player.getColor() for player in self.tic_tac_toe_game.players]

        self.update_current_player_label()  # Mettre à jour le joueur actuel
        self.draw_board()
        self.after(500, self.check_and_play_ai)
        
    def update_current_player_label(self):
        """Met à jour l'affichage du joueur actuel."""
        current_player = self.tic_tac_toe_game.get_player_to_play()
        player_name = current_player.getName()
        self.current_player_label.config(text=f"Current Player: {player_name}")

    def load_png_image(self, file_path: str) -> ImageTk.PhotoImage:
        image = Image.open(file_path)
        return ImageTk.PhotoImage(image)

    @private_method
    def __handle_click(self, event: tk.Tk) -> None:
        col = event.x // self.cell_size
        row = event.y // self.cell_size

        if 0 <= row < self.board.getHeight() and 0 <= col < self.board.getWidth():
            if self.board.isCaseAvaillable(row, col):
                game_outcome = self.tic_tac_toe_game.play_move(row, col)
                self.draw_board()
                if game_outcome.getGameStatus() != GameOutcomeStatus.UNFINISHED:
                    self.show_game_result(game_outcome)
                else:
                    # Passer au tour suivant si le jeu n'est pas terminé
                    self.tic_tac_toe_game.game_state.__nextTurn__()
                    self.update_current_player_label()  # Mise à jour après le changement de tour
                    self.check_and_play_ai()

    def check_and_play_ai(self):
        if isinstance(self.tic_tac_toe_game.get_player_to_play(), MinimaxTranspositionTablePlayer):
            self.after(500, self.play_next_ai_move)

    def play_next_ai_move(self):
        game_outcome = self.tic_tac_toe_game.play_ai_move()
        self.draw_board()
        if game_outcome.getGameStatus() != GameOutcomeStatus.UNFINISHED:
            self.show_game_result(game_outcome)
        else:
            self.tic_tac_toe_game.game_state.__nextTurn__()
            self.check_and_play_ai()
        self.update_current_player_label()

    def draw_board(self):
        board_state = [['' for _ in range(self.board.getWidth())] for _ in range(self.board.getHeight())]
        for row in range(self.board.getHeight()):
            for col in range(self.board.getWidth()):
                if self.board.isCaseBlocked(row, col):
                    board_state[row][col] = '#'
                elif self.board.isEntityAt(row, col):
                    entity = self.board.getEntityAt(row, col)
                    board_state[row][col] = entity.getName()
        draw_grid(self.grid_canvas, self.width, self.height, self.cell_size, board_state, player_symbols=self.player_symbols, player_colors=self.player_colors, coord=True)

    def show_game_result(self, game_outcome):
        if game_outcome.getGameStatus() == GameOutcomeStatus.VICTORY:
            winner = game_outcome.getWinner()
            result_text = f"Player {winner + 1} wins!"
        else:
            result_text = "It's a draw!"
        self.result_label = ttk.Label(self.info_box, text=result_text, font=("Arial", 24), background="#555", foreground="white")
        self.result_label.pack(side="top", pady=20)

        # Add a button to return to the welcome page
        self.return_button = ttk.Button(self.info_box, text="Return to Welcome Page", command=self.return_to_welcome)
        self.return_button.pack(side="top", pady=20)

    def return_to_welcome(self):
        self.controller.frames["Settings"].reset_settings()
        self.reset_game()
        self.controller.showFrame("Welcome")

    def reset_game(self):
        self.tic_tac_toe_game = TicTacToeGame()
        self.board = None
        self.grid_canvas.delete("all")
        self.current_player_label.config(text="Current Player: ")
        self.result_label.destroy()
        self.return_button.destroy()

    @private_method
    def __handleBombClick(self) -> None:
        print("Bomb clicked")
        return None

    @private_method
    def __handleLeftArrowClick(self) -> None:
        print("Left arrow clicked")
        return None

    @private_method
    def __handleRightArrowClick(self) -> None:
        print("Right arrow clicked")
        return None

    @private_method
    def __handleBulbClick(self) -> None:
        print("Bulb clicked")
        return None
