import tkinter as tk
from tkinter import ttk
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter.colorchooser import askcolor


class Settings(ttk.Frame):
    def __init__(self, parent: tk.Tk, controller: tk.Tk) -> None:
        super().__init__(parent)
        self.controller = controller

        # Variables
        self.num_players = tk.IntVar(value=2)
        self.board_width = tk.IntVar(value=7)
        self.board_height = tk.IntVar(value=7)
        self.player_types = []
        self.player_symbols = []
        self.player_colors = []

        # Styles and Layout
        self.style = tb.Style("cosmo")
        self.grid_columnconfigure(1, weight=1)

        # Widgets
        ttk.Label(self, text="Game Settings", font=("Helvetica", 16, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

        ttk.Label(self, text="Number of Players:").grid(row=1, column=0, padx=10, pady=10, sticky=W)
        num_players_spinbox = ttk.Spinbox(
            self, from_=2, to=4, textvariable=self.num_players, width=5, command=self.update_players
        )
        num_players_spinbox.grid(row=1, column=1, padx=10, pady=10, sticky=W)

        ttk.Label(self, text="Board Width:").grid(row=2, column=0, padx=10, pady=10, sticky=W)
        ttk.Spinbox(self, from_=3, to=10, textvariable=self.board_width, width=5).grid(row=2, column=1, padx=10, pady=10, sticky=W)

        ttk.Label(self, text="Board Height:").grid(row=3, column=0, padx=10, pady=10, sticky=W)
        ttk.Spinbox(self, from_=3, to=10, textvariable=self.board_height, width=5).grid(row=3, column=1, padx=10, pady=10, sticky=W)

        self.players_frame = ttk.Frame(self)
        self.players_frame.grid(row=4, column=0, columnspan=2, pady=10, sticky="nsew")

        self.update_players()

        ttk.Button(self, text="Start Game", style="primary.TButton", command=self.start_game).grid(
            row=6, column=0, columnspan=2, pady=20
        )

    def update_players(self):
        """Update the player settings dynamically based on the number of players."""
        # Clear current player settings
        for widget in self.players_frame.winfo_children():
            widget.destroy()

        self.player_types = [tk.BooleanVar(value=True) for _ in range(self.num_players.get())]
        self.player_symbols = [tk.StringVar(value="X") for _ in range(self.num_players.get())]
        self.player_colors = [tk.StringVar(value="#000000") for _ in range(self.num_players.get())]

        available_symbols = ["X", "O", "∆", "⬡"]  # Example symbols

        for i in range(self.num_players.get()):
            ttk.Label(self.players_frame, text=f"Player {i + 1} is Human:").grid(row=i, column=0, padx=10, pady=5, sticky=W)
            ttk.Checkbutton(self.players_frame, variable=self.player_types[i]).grid(row=i, column=1, padx=10, pady=5, sticky=W)

            ttk.Label(self.players_frame, text="Symbol:").grid(row=i, column=2, padx=10, pady=5, sticky=W)
            ttk.Combobox(
                self.players_frame, textvariable=self.player_symbols[i], values=available_symbols, state="readonly", width=5
            ).grid(row=i, column=3, padx=10, pady=5, sticky=W)

            ttk.Label(self.players_frame, text="Color:").grid(row=i, column=4, padx=10, pady=5, sticky=W)
            color_button = ttk.Button(
                self.players_frame,
                text="Choose",
                command=lambda idx=i: self.choose_color(idx),
                style="secondary.TButton",
            )
            color_button.grid(row=i, column=5, padx=10, pady=5, sticky=W)

    def choose_color(self, idx):
        """Open a color picker and set the chosen color."""
        color_code = askcolor(title="Choose a color")[1]  # Get the HEX color
        if color_code:
            self.player_colors[idx].set(color_code)

    def start_game(self):
        """Start the game with the current settings."""
        game = self.controller.frames["Game"].tic_tac_toe_game
        game.set_number_of_players(self.num_players.get())
        game.set_board_size(self.board_width.get(), self.board_height.get())
        for i, var in enumerate(self.player_types):
            game.set_player_type(i, var.get())
            game.set_player_symbol(i, self.player_symbols[i].get())
            game.set_player_color(i, self.player_colors[i].get())
        self.controller.showFrame("Game")