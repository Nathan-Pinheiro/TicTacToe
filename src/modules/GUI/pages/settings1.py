from enum import Enum
import tkinter as tk
from tkinter import ttk
from modules.utils.decorator import privatemethod
from modules.GUI.pages.page import Page
from modules.GUI.render import PageName
from tkinter.colorchooser import askcolor
from PIL import Image, ImageTk
import cv2
import numpy as np
from modules.GUI.draft.symbols import drawCross, drawCircle, drawTriangle, drawHexagon, drawStar, drawSquare, drawRhombus

class GridType(Enum):
    NORMAL = "Normal"
    PYRAMIDAL = "Pyramidal"
    RANDOM = "Random"

class SettingsPage(Page):
    def __init__(self, parent: tk.Frame, controller: tk.Tk) -> None:
        super().__init__(parent, controller)
        
        self.numPlayers = tk.IntVar(value=2)
        self.boardWidth = tk.IntVar(value=3)
        self.boardHeight = tk.IntVar(value=3)
        self.gridType = tk.StringVar(value=GridType.NORMAL.value)
        self.symbolsToAlign = tk.IntVar(value=3)
        self.playerNames = ["",""]
        self.playerTypes = []
        self.playerSymbols = []
        available_symbols = self.__getAvailableSymbols__(0)
        self.playerSymbols.append(tk.StringVar(value=available_symbols[0] if available_symbols else "X"))
        available_symbols = self.__getAvailableSymbols__(1)
        self.playerSymbols.append(tk.StringVar(value=available_symbols[0] if available_symbols else "O"))
        self.playerColors = [tk.StringVar(value="#FFFFFF"), tk.StringVar(value="#FFFFFF")]

        # Configuration principale de la grille
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=7)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Titre "Tic Tac Toe"
        self.titleLabel = ttk.Label(self, text="Players settings", font=("Arial", 48, "bold"), foreground="white")
        self.titleLabel.grid(row=0, columnspan=2, pady=(20, 10), sticky="n")

        # Texte d'introduction
        self.textTitleLabel1 = ttk.Label(
            self,
            text=(
                "Player 1"
            ),
            wraplength=600,
            justify="center",
            font=("Arial", 36, "bold"),
            foreground="white"
        )
        self.textTitleLabel1.grid(row=1, column=0, pady=125, padx=125, sticky="n")
        
        ttk.Entry(self, textvariable=self.playerNames[0], width=30).grid(row=1, column=0, padx=125, pady=250, sticky="n")
        
        colorLabel1 = tk.Label(
                    self,
                    bg=self.playerColors[0].get(),
                    relief="ridge",
                    width=10,
                    height=5
        )
        
        colorLabel1.grid(row=1, column=0, padx=13, pady=300, sticky="wn")

        ttk.Button(
            self,
            text="Select Color",
            command=lambda idx=0, label=colorLabel1: self.__chooseColor__(idx, label),
            width=10
        ).grid(row=1, column=0, padx=0, pady=400, sticky="wn")
        
        self.symbolCanvas1 = tk.Canvas(self, width=50, height=50, background="#1c1c1c")
        self.symbolCanvas1.grid(row=1, column=0, padx=230, pady=310, sticky="wn")
        self.symbolCanvas1.configure(background="#1c1c1c")
        self.__drawSymbol__(self.symbolCanvas1, self.playerSymbols[0].get(), self.playerColors[0].get())
        
        ttk.Button(
            self,
            text="Change Symbol",
            command=lambda idx=0: self.__changeSymbol__(idx),
            width=10
        ).grid(row=1, column=0, padx=200, pady=400, sticky="wn")
        
        self.textTitleLabel2 = ttk.Label(
            self,
            text=(
                "Player 2"
            ),
            wraplength=600,
            justify="center",
            font=("Arial", 36, "bold"),
            foreground="white"
        )
        self.textTitleLabel2.grid(row=1, column=1, pady=125, padx=125, sticky="n")
        
        ttk.Entry(self, textvariable=self.playerNames[1], width=30).grid(row=1, column=1, padx=125, pady=250, sticky="n")
        
        colorLabel2 = tk.Label(
                    self,
                    bg=self.playerColors[1].get(),
                    relief="ridge",
                    width=10,
                    height=5
        )
        
        colorLabel2.grid(row=1, column=1, padx=13, pady=300, sticky="wn")

        ttk.Button(
            self,
            text="Select Color",
            command=lambda idx=1, label=colorLabel2: self.__chooseColor__(idx, label),
            width=10
        ).grid(row=1, column=1, padx=0, pady=400, sticky="wn")
        
        self.symbolCanvas2 = tk.Canvas(self, width=50, height=50, background="#1c1c1c")
        self.symbolCanvas2.grid(row=1, column=1, padx=230, pady=310, sticky="wn")
        self.symbolCanvas2.configure(background="#1c1c1c")
        self.__drawSymbol__(self.symbolCanvas2, self.playerSymbols[1].get(), self.playerColors[1].get())
        
        ttk.Button(
            self,
            text="Change Symbol",
            command=lambda idx=1: self.__changeSymbol__(idx),
            width=10
        ).grid(row=1, column=1, padx=200, pady=400, sticky="wn")

        # Bouton "Go!"
        self.startButton = ttk.Button(self, text="Go !", command=self.startGame)
        self.startButton.grid(row=3, columnspan=2, pady=(20, 40), sticky="s")

        # Redimensionnement dynamique
        self.bind("<Configure>", self.__onResize__)

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
                    combobox = self.gridSlaves(row=1, column=5)[0]
                    combobox.config(values=self.__getAvailableSymbols__(i))
            return True
        except Exception as e:
            print(f"Error updating symbols: {e}")
            return False

    @privatemethod
    def __chooseColor__(self, idx, button) -> bool:
        """Open a color picker and set the chosen color."""
        try:
            colorCode = askcolor(title="Choose a color")[1]  # Get the HEX color
            if colorCode:
                self.playerColors[idx].set(colorCode)
                button.config(bg=colorCode)
                if idx == 0:
                    self.__drawSymbol__(self.symbolCanvas1, self.playerSymbols[0].get(), colorCode)
                else:
                    self.__drawSymbol__(self.symbolCanvas2, self.playerSymbols[1].get(), colorCode)
            return True
        except Exception as e:
            print(f"Error choosing color: {e}")
            return False

    @privatemethod
    def __changeSymbol__(self, idx: int) -> bool:
        """Change the symbol for a player."""
        try:
            availableSymbols = self.__getAvailableSymbols__(idx)
            currentSymbol = self.playerSymbols[idx].get()
            currentIndex = availableSymbols.index(currentSymbol)
            newIndex = (currentIndex + 1) % len(availableSymbols)
            self.playerSymbols[idx].set(availableSymbols[newIndex])
            if idx == 0:
                self.__drawSymbol__(self.symbolCanvas1, availableSymbols[newIndex], self.playerColors[0].get())
            else:
                self.__drawSymbol__(self.symbolCanvas2, availableSymbols[newIndex], self.playerColors[1].get())
            return True
        except Exception as e:
            print(f"Error changing symbol: {e}")
            return False

    @privatemethod
    def __drawSymbol__(self, canvas: tk.Canvas, symbol: str, color: str) -> bool:
        """Draw the symbol on the canvas."""
        try:
            canvas.delete("all")
            size = 50
            if symbol == 'X':
                drawCross(canvas, 0, 0, size, color)
            elif symbol == 'O':
                drawCircle(canvas, 0, 0, size, color)
            elif symbol == '△':
                drawTriangle(canvas, 0, 0, size, color)
            elif symbol == '⬡':
                drawHexagon(canvas, 0, 0, size, color)
            elif symbol == '★':
                drawStar(canvas, 0, 0, size, color)
            elif symbol == '▢':
                drawSquare(canvas, 0, 0, size, color)
            elif symbol == '◊':
                drawRhombus(canvas, 0, 0, size, color)
            return True
        except Exception as e:
            print(f"Error drawing symbol: {e}")
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
        
    ## Load a PNG image from the given file path.
    #
    # @param filePath The path to the PNG file.
    # @return ImageTk.PhotoImage The loaded image.
    def loadPngImage(self, filePath: str) -> ImageTk.PhotoImage:
        image = Image.open(filePath)
        image = np.array(image)
        image = cv2.resize(image, (600, 600))
        image = Image.fromarray(image)
        return ImageTk.PhotoImage(image)
    
    @privatemethod
    def __onResize__(self, event: tk.Event) -> bool:
        size = min(event.width, event.height) * 0.5
        size = int(size) - (int(size) % 2)

        return True