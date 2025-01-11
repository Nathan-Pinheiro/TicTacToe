## Interface

"""
Settings Page Module

This module provides the implementation of the settings page for the Tic Tac Toe game using the tkinter library.

Classes:
    SettingsPage: Represents the settings page of the Tic Tac Toe game.
    GridType: Enum representing the types of grids.

Functions:
    __init__(self, parent: tk.Tk, controller: tk.Tk) -> bool:
        Initialize the settings page with the given parent and controller.
        
    show(self) -> bool:
        Show the settings page.
        
    hide(self) -> bool:
        Hide the settings page.
        
    __updatePlayers__(self) -> bool:
        Private method.
        Update the player settings dynamically based on the number of players.
        
    __getAvailableSymbols__(self, currentIndex: int) -> list[str]:
        Private method.
        Get the list of available symbols excluding those already selected.
        
    __updateSymbols__(self, currentIndex: int) -> bool:
        Private method.
        Update the available symbols for all players.
        
    __chooseColor__(self, idx: int, label: tk.Label) -> bool:
        Private method.
        Open a color picker and set the chosen color.
        
    __updateSymbolsToAlign__(self) -> bool:
        Private method.
        Update the maximum value for symbols to align based on the board size.
        
    startGame(self) -> bool:
        Start the game with the current settings.
        
    resetSettings(self) -> bool:
        Reset the settings to their default values.
"""

# ---------------------------------------------------------------------------------------------------- #

## Implementation

# Import #
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter.colorchooser import askcolor
import random  # Pour gérer l'option "Random"
from enum import Enum
from modules.GUI.pages.page import Page
from modules.GUI.render import PageName
from modules.utils.decorator import privatemethod

class GridType(Enum):
    NORMAL = "Normal"
    PYRAMIDAL = "Pyramidal"
    RANDOM = "Random"

class SettingsPage(Page):
    ## Initialize the settings page with the given parent and controller.
    #
    # @param parent The parent frame.
    # @param controller The controller for the page.
    # @return bool True if the function succeeds, False otherwise.
    def __init__(self, parent: tk.Tk, controller: tk.Tk) -> None:
        super().__init__(parent, controller)

        # Variables
        self.numPlayers = tk.IntVar(value=2)
        self.boardWidth = tk.IntVar(value=3)
        self.boardHeight = tk.IntVar(value=3)
        self.gridType = tk.StringVar(value=GridType.NORMAL.value)
        self.symbolsToAlign = tk.IntVar(value=3)
        self.playerNames = []
        self.playerTypes = []
        self.playerSymbols = []
        self.playerColors = []

        # Styles and Layout
        self.style = tb.Style("cosmo")
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Widgets
        ttk.Label(self, text="Game Settings", font=("Helvetica", 16, "bold")).grid(row=0, column=0, columnspan=2, pady=10, sticky="ew")

        ttk.Label(self, text="Number of Players:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
        numPlayersSpinbox = ttk.Spinbox(
            self, from_=2, to=4, textvariable=self.numPlayers, width=5, command=self.__updatePlayers__
        )
        numPlayersSpinbox.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        ttk.Label(self, text="Board Width:").grid(row=2, column=0, padx=10, pady=10, sticky="e")
        ttk.Spinbox(self, from_=3, to=7, textvariable=self.boardWidth, width=5, command=self.__updateSymbolsToAlign__).grid(row=2, column=1, padx=10, pady=10, sticky="w")

        ttk.Label(self, text="Board Height:").grid(row=3, column=0, padx=10, pady=10, sticky="e")
        ttk.Spinbox(self, from_=3, to=7, textvariable=self.boardHeight, width=5, command=self.__updateSymbolsToAlign__).grid(row=3, column=1, padx=10, pady=10, sticky="w")

        ttk.Label(self, text="Grid Type:").grid(row=4, column=0, padx=10, pady=10, sticky="e")
        ttk.Radiobutton(self, text=GridType.NORMAL.value, variable=self.gridType, value=GridType.NORMAL.value).grid(row=4, column=1, padx=10, sticky="w")
        ttk.Radiobutton(self, text=GridType.PYRAMIDAL.value, variable=self.gridType, value=GridType.PYRAMIDAL.value).grid(row=4, column=1, padx=90, sticky="w")
        ttk.Radiobutton(self, text=GridType.RANDOM.value, variable=self.gridType, value=GridType.RANDOM.value).grid(row=4, column=1, padx=190, sticky="w")

        ttk.Label(self, text="Symbols to Align:").grid(row=5, column=0, padx=10, pady=10, sticky="e")
        self.symbolsToAlignSpinbox = ttk.Spinbox(
            self, from_=3, to=7, textvariable=self.symbolsToAlign, width=5
        )
        self.symbolsToAlignSpinbox.grid(row=5, column=1, padx=10, pady=10, sticky="w")
        self.__updateSymbolsToAlign__()

        self.playersFrame = ttk.Frame(self)
        self.playersFrame.grid(row=6, column=0, columnspan=2, pady=10, sticky="nsew")

        self.__updatePlayers__()

        ttk.Button(self, text="Start Game", style="primary.TButton", command=self.startGame).grid(
            row=8, column=0, columnspan=2, pady=20
        )
        return None

    def show(self) -> bool:
        try:
            self.grid()
            return True
        except Exception as e:
            print(f"Error showing settings page: {e}")
            return False

    def hide(self) -> bool:
        try:
            self.gridRemove()
            return True
        except Exception as e:
            print(f"Error hiding settings page: {e}")
            return False

    @privatemethod
    def __updatePlayers__(self) -> bool:
        """Update the player settings dynamically based on the number of players."""
        try:
            currentCount = len(self.playerTypes)
            newCount = self.numPlayers.get()

            if newCount > currentCount:
                # Ajouter de nouveaux joueurs à la fin
                for i in range(currentCount, newCount):
                    self.playerNames.append(tk.StringVar(value=f"Player {i + 1}"))
                    self.playerTypes.append(tk.BooleanVar(value=True))
                    availableSymbols = self.__getAvailableSymbols__(i)
                    self.playerSymbols.append(tk.StringVar(value=availableSymbols[0] if availableSymbols else "X"))
                    self.playerColors.append(tk.StringVar(value="#FFFFFF"))
            elif newCount < currentCount:
                # Supprimer les joueurs en trop à la fin
                self.playerNames = self.playerNames[:newCount]
                self.playerTypes = self.playerTypes[:newCount]
                self.playerSymbols = self.playerSymbols[:newCount]
                self.playerColors = self.playerColors[:newCount]

            # Effacer uniquement les widgets qui ne sont pas nécessaires
            for widget in self.playersFrame.winfo_children():
                widget.destroy()

            # Afficher les paramètres pour tous les joueurs
            for i in range(newCount):
                ttk.Label(self.playersFrame, text=f"Player {i + 1} Name:").grid(row=i, column=0, padx=5, pady=2, sticky="e")
                ttk.Entry(self.playersFrame, textvariable=self.playerNames[i]).grid(row=i, column=1, padx=5, pady=2, sticky="w")

                ttk.Label(self.playersFrame, text="Is Human:").grid(row=i, column=2, padx=5, pady=2, sticky="e")
                ttk.Checkbutton(self.playersFrame, variable=self.playerTypes[i]).grid(row=i, column=3, padx=5, pady=2, sticky="w")

                ttk.Label(self.playersFrame, text="Symbol:").grid(row=i, column=4, padx=5, pady=2, sticky="e")
                symbolCombobox = ttk.Combobox(
                    self.playersFrame, textvariable=self.playerSymbols[i], values=self.__getAvailableSymbols__(i), state="readonly", width=5
                )
                symbolCombobox.grid(row=i, column=5, padx=5, pady=2, sticky="w")
                symbolCombobox.bind("<<ComboboxSelected>>", lambda event, idx=i: self.__updateSymbols__(idx))

                ttk.Label(self.playersFrame, text="Color:").grid(row=i, column=6, padx=5, pady=2, sticky="e")
                colorLabel = tk.Label(
                    self.playersFrame,
                    text="    ",
                    bg=self.playerColors[i].get(),
                    relief="ridge",
                    width=10,
                )
                colorLabel.grid(row=i, column=7, padx=5, pady=2, sticky="w")

                ttk.Button(
                    self.playersFrame,
                    text="Select Color",
                    command=lambda idx=i, label=colorLabel: self.__chooseColor__(idx, label),
                    style="secondary.TButton",
                ).grid(row=i, column=8, padx=5, pady=2, sticky="w")
            return True
        except Exception as e:
            print(f"Error updating players: {e}")
            return False

    @privatemethod
    def __getAvailableSymbols__(self, currentIndex):
        """Get the list of available symbols excluding those already selected."""
        allSymbols = ["X", "O", "△", "⬡", "◊", "▢", "★"]
        selectedSymbols = [self.playerSymbols[i].get() for i in range(len(self.playerSymbols)) if i != currentIndex]
        return [symbol for symbol in allSymbols if symbol not in selectedSymbols]

    @privatemethod
    def __updateSymbols__(self, currentIndex) -> bool:
        """Update the available symbols for all players."""
        try:
            for i in range(len(self.playerSymbols)):
                if i != currentIndex:
                    combobox = self.playersFrame.gridSlaves(row=i, column=5)[0]
                    combobox.config(values=self.__getAvailableSymbols__(i))
            return True
        except Exception as e:
            print(f"Error updating symbols: {e}")
            return False

    @privatemethod
    def __chooseColor__(self, idx, label) -> bool:
        """Open a color picker and set the chosen color."""
        try:
            colorCode = askcolor(title="Choose a color")[1]  # Get the HEX color
            if colorCode:
                self.playerColors[idx].set(colorCode)
                label.config(bg=colorCode)
            return True
        except Exception as e:
            print(f"Error choosing color: {e}")
            return False

    @privatemethod
    def __updateSymbolsToAlign__(self) -> bool:
        """Update the maximum value for symbols to align based on the board size."""
        try:
            maxSymbols = min(self.boardWidth.get(), self.boardHeight.get())
            self.symbolsToAlignSpinbox.config(from_=3, to=maxSymbols)
            if self.symbolsToAlign.get() > maxSymbols:
                self.symbolsToAlign.set(maxSymbols)
            return True
        except Exception as e:
            print(f"Error updating symbols to align: {e}")
            return False

    def startGame(self) -> bool:
        """Start the game with the current settings."""
        try:
            game = self.controller.frames[PageName.GAME.value].ticTacToeGame

            # Définir les paramètres
            game.setNumberOfPlayers(self.numPlayers.get())
            game.setBoardSize(self.boardWidth.get(), self.boardHeight.get())
            game.setSymbolsToAlign(self.symbolsToAlign.get())

            # Gérer l'option "Random"
            if self.gridType.get() == GridType.RANDOM.value:
                game.setIsPyramidal(random.choice([True, False]))
            else:
                game.setIsPyramidal(self.gridType.get() == GridType.PYRAMIDAL.value)

            for i, var in enumerate(self.playerTypes):
                game.setPlayerType(i, var.get())
                game.setPlayerSymbol(i, self.playerSymbols[i].get())
                game.setPlayerColor(i, self.playerColors[i].get())
                
            game.setPlayerName([name.get() for name in self.playerNames])

            self.controller.showFrame(PageName.GAME)
            return True
        except Exception as e:
            print(f"Error starting game: {e}")
            return False

    def resetSettings(self) -> bool:
        try:
            self.numPlayers.set(2)
            self.boardWidth.set(3)
            self.boardHeight.set(3)
            self.gridType.set(GridType.NORMAL.value)
            self.symbolsToAlign.set(3)
            self.playerNames = []
            self.playerTypes = []
            self.playerSymbols = []
            self.playerColors = []
            self.__updatePlayers__()
            return True
        except Exception as e:
            print(f"Error resetting settings: {e}")
            return False