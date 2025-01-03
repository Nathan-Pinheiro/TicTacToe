import tkinter as tk
from tkinter import ttk
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter.colorchooser import askcolor
import random  # Pour gérer l'option "Random"

class Settings(ttk.Frame):
    def __init__(self, parent: tk.Tk, controller: tk.Tk) -> None:
        super().__init__(parent)
        self.controller = controller

        # Variables
        self.num_players = tk.IntVar(value=2)
        self.board_width = tk.IntVar(value=3)
        self.board_height = tk.IntVar(value=3)
        self.grid_type = tk.StringVar(value="Normal")  # "Normal", "Pyramidal", ou "Random"
        self.symbols_to_align = tk.IntVar(value=3)
        self.player_names = []
        self.player_types = []
        self.player_symbols = []
        self.player_colors = []

        # Styles and Layout
        self.style = tb.Style("cosmo")
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Widgets
        ttk.Label(self, text="Game Settings", font=("Helvetica", 16, "bold")).grid(row=0, column=0, columnspan=2, pady=10, sticky="ew")

        ttk.Label(self, text="Number of Players:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
        num_players_spinbox = ttk.Spinbox(
            self, from_=2, to=4, textvariable=self.num_players, width=5, command=self.update_players
        )
        num_players_spinbox.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        ttk.Label(self, text="Board Width:").grid(row=2, column=0, padx=10, pady=10, sticky="e")
        ttk.Spinbox(self, from_=3, to=10, textvariable=self.board_width, width=5, command=self.update_symbols_to_align).grid(row=2, column=1, padx=10, pady=10, sticky="w")

        ttk.Label(self, text="Board Height:").grid(row=3, column=0, padx=10, pady=10, sticky="e")
        ttk.Spinbox(self, from_=3, to=10, textvariable=self.board_height, width=5, command=self.update_symbols_to_align).grid(row=3, column=1, padx=10, pady=10, sticky="w")

        ttk.Label(self, text="Grid Type:").grid(row=4, column=0, padx=10, pady=10, sticky="e")
        ttk.Radiobutton(self, text="Normal", variable=self.grid_type, value="Normal").grid(row=4, column=1, padx=10, sticky="w")
        ttk.Radiobutton(self, text="Pyramidal", variable=self.grid_type, value="Pyramidal").grid(row=4, column=1, padx=90, sticky="w")
        ttk.Radiobutton(self, text="Random", variable=self.grid_type, value="Random").grid(row=4, column=1, padx=190, sticky="w")

        ttk.Label(self, text="Symbols to Align:").grid(row=5, column=0, padx=10, pady=10, sticky="e")
        self.symbols_to_align_spinbox = ttk.Spinbox(
            self, from_=3, to=7, textvariable=self.symbols_to_align, width=5
        )
        self.symbols_to_align_spinbox.grid(row=5, column=1, padx=10, pady=10, sticky="w")
        self.update_symbols_to_align()

        self.players_frame = ttk.Frame(self)
        self.players_frame.grid(row=6, column=0, columnspan=2, pady=10, sticky="nsew")

        self.update_players()

        ttk.Button(self, text="Start Game", style="primary.TButton", command=self.start_game).grid(
            row=8, column=0, columnspan=2, pady=20
        )

    def update_players(self):
        """Update the player settings dynamically based on the number of players."""
        current_count = len(self.player_types)
        new_count = self.num_players.get()

        if new_count > current_count:
            # Ajouter de nouveaux joueurs à la fin
            for i in range(current_count, new_count):
                self.player_names.append(tk.StringVar(value=f"Player {i + 1}"))
                self.player_types.append(tk.BooleanVar(value=True))
                available_symbols = self.get_available_symbols(i)
                self.player_symbols.append(tk.StringVar(value=available_symbols[0] if available_symbols else "X"))
                self.player_colors.append(tk.StringVar(value="#FFFFFF"))
        elif new_count < current_count:
            # Supprimer les joueurs en trop à la fin
            self.player_names = self.player_names[:new_count]
            self.player_types = self.player_types[:new_count]
            self.player_symbols = self.player_symbols[:new_count]
            self.player_colors = self.player_colors[:new_count]

        # Effacer uniquement les widgets qui ne sont pas nécessaires
        for widget in self.players_frame.winfo_children():
            widget.destroy()

        # Afficher les paramètres pour tous les joueurs
        for i in range(new_count):
            ttk.Label(self.players_frame, text=f"Player {i + 1} Name:").grid(row=i, column=0, padx=5, pady=2, sticky="e")
            ttk.Entry(self.players_frame, textvariable=self.player_names[i]).grid(row=i, column=1, padx=5, pady=2, sticky="w")

            ttk.Label(self.players_frame, text="Is Human:").grid(row=i, column=2, padx=5, pady=2, sticky="e")
            ttk.Checkbutton(self.players_frame, variable=self.player_types[i]).grid(row=i, column=3, padx=5, pady=2, sticky="w")

            ttk.Label(self.players_frame, text="Symbol:").grid(row=i, column=4, padx=5, pady=2, sticky="e")
            symbol_combobox = ttk.Combobox(
                self.players_frame, textvariable=self.player_symbols[i], values=self.get_available_symbols(i), state="readonly", width=5
            )
            symbol_combobox.grid(row=i, column=5, padx=5, pady=2, sticky="w")
            symbol_combobox.bind("<<ComboboxSelected>>", lambda event, idx=i: self.update_symbols(idx))

            ttk.Label(self.players_frame, text="Color:").grid(row=i, column=6, padx=5, pady=2, sticky="e")
            color_label = tk.Label(
                self.players_frame,
                text="    ",
                bg=self.player_colors[i].get(),
                relief="ridge",
                width=10,
            )
            color_label.grid(row=i, column=7, padx=5, pady=2, sticky="w")

            ttk.Button(
                self.players_frame,
                text="Select Color",
                command=lambda idx=i, label=color_label: self.choose_color(idx, label),
                style="secondary.TButton",
            ).grid(row=i, column=8, padx=5, pady=2, sticky="w")

    def get_available_symbols(self, current_index):
        """Get the list of available symbols excluding those already selected."""
        all_symbols = ["X", "O", "△", "⬡", "◊", "▢", "★"]
        selected_symbols = [self.player_symbols[i].get() for i in range(len(self.player_symbols)) if i != current_index]
        return [symbol for symbol in all_symbols if symbol not in selected_symbols]

    def update_symbols(self, current_index):
        """Update the available symbols for all players."""
        for i in range(len(self.player_symbols)):
            if i != current_index:
                combobox = self.players_frame.grid_slaves(row=i, column=5)[0]
                combobox.config(values=self.get_available_symbols(i))

    def choose_color(self, idx, label):
        """Open a color picker and set the chosen color."""
        color_code = askcolor(title="Choose a color")[1]  # Get the HEX color
        if color_code:
            self.player_colors[idx].set(color_code)
            label.config(bg=color_code)

    def update_symbols_to_align(self):
        """Update the maximum value for symbols to align based on the board size."""
        max_symbols = min(self.board_width.get(), self.board_height.get())
        self.symbols_to_align_spinbox.config(from_=3, to=max_symbols)
        if self.symbols_to_align.get() > max_symbols:
            self.symbols_to_align.set(max_symbols)

    def start_game(self):
        """Start the game with the current settings."""
        game = self.controller.frames["Game"].tic_tac_toe_game

        # Définir les paramètres
        game.set_number_of_players(self.num_players.get())
        game.set_board_size(self.board_width.get(), self.board_height.get())
        game.set_symbols_to_align(self.symbols_to_align.get())

        # Gérer l'option "Random"
        if self.grid_type.get() == "Random":
            game.set_is_pyramidal(random.choice([True, False]))
        else:
            game.set_is_pyramidal(self.grid_type.get() == "Pyramidal")

        for i, var in enumerate(self.player_types):
            game.set_player_type(i, var.get())
            game.set_player_symbol(i, self.player_symbols[i].get())
            game.set_player_color(i, self.player_colors[i].get())
            
        game.set_player_name([name.get() for name in self.player_names])

        self.controller.showFrame("Game")

    def reset_settings(self):
        self.num_players.set(2)
        self.board_width.set(3)
        self.board_height.set(3)
        self.grid_type.set("Normal")
        self.symbols_to_align.set(3)
        self.player_names = []
        self.player_types = []
        self.player_symbols = []
        self.player_colors = []
        self.update_players()