import tkinter as tk
from tkinter import ttk
from modules.GUI.draft.grid import drawGrid
from modules.utils.decorator import privatemethod
from modules.GUI.pages.page import Page
from modules.GUI.render import PageName
from PIL import Image, ImageTk
import cv2
import numpy as np

class Welcome(Page):
    def __init__(self, parent: tk.Frame, controller: tk.Tk) -> None:
        super().__init__(parent, controller)

        # Configuration principale de la grille
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=5)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Titre "Tic Tac Toe"
        self.titleLabel = ttk.Label(self, text="Tic Tac Toe", font=("Arial", 48, "bold"), foreground="white")
        self.titleLabel.grid(row=0, columnspan=2, pady=(20, 10), sticky="n")

        # Texte d'introduction
        self.textTitleLabel = ttk.Label(
            self,
            text=(
                "Ready to take on the challenge?\n\n"
            ),
            wraplength=600,
            justify="center",
            font=("Arial", 26, "bold"),
            foreground="white"
        )
        self.textTitleLabel.grid(row=1, column=0, pady=125, padx=125, sticky="wn")
        
        self.textDescriptionLabel = ttk.Label(
            self,
            text=(
                "Challenge your friends or test your skills against the computer in thrilling games of Tic-Tac-Toe! "
                "Simple yet strategic, every move can change the course of the game. Choose your symbol, place it, "
                "and be the first to align three symbols (or not) to win!"
            ),
            wraplength=600,
            justify="center",
            font=("Arial", 26),
            foreground="white"
        )
        self.textDescriptionLabel.grid(row=1, column=0, pady=125, padx=100, sticky="ws")
        
        self.Image = self.loadPngImage("./static/assets/Board.png")
        
        self.boardImage = ttk.Label(self, image=self.Image)

        self.boardImage.grid(row=1, column=1, rowspan=2, padx=125, sticky="e")

        # Bouton "Go!"
        self.startButton = ttk.Button(self, text="Go !", command=self.startGame, style="Custom.TButton")
        self.startButton.grid(row=3, columnspan=2, pady=(20, 40), sticky="s")

        # Style pour les boutons
        style = ttk.Style()
        style.configure("Custom.TButton", font=("Arial", 24), padding=10, background="black", foreground="white")
        style.map("Custom.TButton",
                  background=[("active", "#555")],
                  foreground=[("active", "white")])

        # Redimensionnement dynamique
        self.bind("<Configure>", self.__onResize__)

    def show(self) -> bool:
        self.grid()
        return True

    def hide(self) -> bool:
        self.grid_remove()
        return True

    @privatemethod
    def __drawGrid__(self, size: int) -> bool:
        cellSize = size // 3

        board = [
            ['X', 'O', '△'],
            ['', '', ''],
            ['', '', '']
        ]

        playerSymbols = ['X', 'O', '△']
        playerColors = ['#FF0000', '#00FF00', '#0000FF']

        drawGrid(self.gridCanvas, size, size, cellSize, board, playerSymbols=playerSymbols, playerColors=playerColors)
        return True

    @privatemethod
    def __onResize__(self, event: tk.Event) -> bool:
        size = min(event.width, event.height) * 0.5
        size = int(size) - (int(size) % 2)

        self.gridCanvas.config(width=size, height=size)
        self.__drawGrid__(size)
        return True

    def startGame(self) -> bool:
        return self.controller.showFrame(PageName.GAME)
    
    
    ## Load a PNG image from the given file path.
    #
    # @param filePath The path to the PNG file.
    # @return ImageTk.PhotoImage The loaded image.
    def loadPngImage(self, filePath: str) -> ImageTk.PhotoImage:
        image = Image.open(filePath)
        image = np.array(image)
        image = cv2.resize(image, (500, 500))
        image = Image.fromarray(image)
        return ImageTk.PhotoImage(image)