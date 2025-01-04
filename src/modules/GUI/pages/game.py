## Interface

"""
Game Page Module

This module provides the implementation of the game page for the Tic Tac Toe game using the tkinter library.

Classes:
    Game: Represents the game page of the Tic Tac Toe game.

Functions:
    __init__(self, parent: tk.Tk, controller: tk.Tk, size: int = 100, buttonColor: str = "#555") -> bool:
        Initialize the game page with the given parent and controller.
        
    show(self) -> bool:
        Show the game page.
        
    hide(self) -> bool:
        Hide the game page.
        
    startGame(self) -> bool:
        Start the game with the current settings.
        
    updateCurrentPlayerLabel(self) -> bool:
        Update the label showing the current player.
        
    loadPngImage(self, filePath: str) -> ImageTk.PhotoImage:
        Load a PNG image from the given file path.
        
    checkAndPlayAi(self) -> bool:
        Check if the current player is an AI and play the next move if so.
        
    __playNextAiMove__(self) -> bool:
        Private method.
        Play the next move for the AI player.
        
    drawBoard(self) -> bool:
        Draw the game board on the canvas.
        
    showGameResult(self, gameOutcome) -> bool:
        Show the result of the game.
        
    returnToWelcome(self) -> bool:
        Return to the welcome page.
        
    resetGame(self) -> bool:
        Reset the game to its initial state.
"""

# ---------------------------------------------------------------------------------------------------- #

## Implementation

# Import #
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from modules.GUI.draft.grid import drawGrid
from modules.models.tic_tac_toe.game_outcome import GameOutcomeStatus
from modules.models.tic_tac_toe.players.ai_players.v5_transpostion_table import MinimaxTranspositionTablePlayer
from modules.utils.decorator import privatemethod
from modules.models.tic_tac_toe.tic_tac_toe_game import TicTacToeGame
from modules.GUI.pages.page import Page
from modules.GUI.render import PageName

class Game(Page):
    ## Initialize the game page with the given parent and controller.
    #
    # @param parent The parent frame.
    # @param controller The controller for the page.
    # @param size The size of the cells in the grid.
    # @param buttonColor The color of the buttons.
    # @return bool True if the function succeeds, False otherwise.
    def __init__(self, parent: tk.Tk, controller: tk.Tk, size: int = 100, buttonColor: str = "#555") -> None:
        super().__init__(parent, controller)
        
        self.ticTacToeGame = TicTacToeGame()
        self.board = None
        self.width = size * 4
        self.height = size * 6
        self.cellSize = size
        
        self.mainFrame = ttk.Frame(self)
        self.mainFrame.pack(fill="both", expand=True)
        self.gridCanvas = tk.Canvas(self.mainFrame, width=self.width - 3, height=self.height - 3, bg="#333")
        self.gridCanvas.pack(side='left', padx=0, pady=10, anchor='center', expand=True)
        self.infoBox = tk.Canvas(self.mainFrame, width=700, bg=buttonColor, highlightthickness=0)
        self.infoBox.pack(side="right", fill="y", padx=0, pady=0)
        
        self.currentPlayerLabel = ttk.Label(
            self.infoBox,
            text="Current Player: ",
            font=("Arial", 18),
            background=buttonColor,
            foreground="white"
        )
        self.currentPlayerLabel.pack(side="top", pady=20)
        
        self.buttonFrame = ttk.Frame(self.infoBox, style="White.TFrame")
        self.buttonFrame.pack(side="bottom", fill="x", padx=10, pady=10)
        
        style = ttk.Style()
        style.configure("White.TFrame", background="#333")
        self.buttonImages = [
            self.loadPngImage("./static/assets/Bomb.png"),
            self.loadPngImage("./static/assets/LeftArrow.png"),
            self.loadPngImage("./static/assets/RightArrow.png"),
            self.loadPngImage("./static/assets/Bulb.png")
        ]
        
        style = ttk.Style()
        style.configure("Custom.TButton", background=buttonColor)
        self.button1 = ttk.Button(self.buttonFrame, image=self.buttonImages[0], style="Custom.TButton", command=self.__handleBombClick__)
        self.button1.pack(side="left", expand=True, padx=5, pady=5)
        self.button2 = ttk.Button(self.buttonFrame, image=self.buttonImages[1], style="Custom.TButton", command=self.__handleLeftArrowClick__)
        self.button2.pack(side="left", expand=True, padx=5, pady=5)
        self.button3 = ttk.Button(self.buttonFrame, image=self.buttonImages[2], style="Custom.TButton", command=self.__handleRightArrowClick__)
        self.button3.pack(side="left", expand=True, padx=5, pady=5)
        self.button4 = ttk.Button(self.buttonFrame, image=self.buttonImages[3], style="Custom.TButton", command=self.__handleBulbClick__)
        self.button4.pack(side="left", expand=True, padx=5, pady=5)
        
        self.resultLabel = ttk.Label(self.infoBox, text="", font=("Arial", 24), background="#555", foreground="white")
        self.returnButton = ttk.Button(self.infoBox, text="Return to Welcome Page", command=self.returnToWelcome)
        self.gridCanvas.bind("<Button-1>", self.__handleClick__)
        
        return None

    ## Show the game page.
    #
    # @return bool True if the function succeeds, False otherwise.
    def show(self) -> bool:
        try:
            self.grid()
            return True
        except Exception as e:
            print(f"Error showing game page: {e}")
            return False

    ## Hide the game page.
    #
    # @return bool True if the function succeeds, False otherwise.
    def hide(self) -> bool:
        try:
            self.grid_remove()
            return True
        except Exception as e:
            print(f"Error hiding game page: {e}")
            return False

    ## Start the game with the current settings.
    #
    # @return bool True if the function succeeds, False otherwise.
    def startGame(self) -> bool:
        try:
            self.board = self.ticTacToeGame.getBoard()
            self.width = self.cellSize * self.board.getWidth()
            self.height = self.cellSize * self.board.getHeight()
            self.gridCanvas.config(width=self.width - 3, height=self.height - 3)

            self.playerSymbols = [entity.getName() for entity in self.ticTacToeGame.playerEntities]
            self.playerColors = [player.getColor() for player in self.ticTacToeGame.players]

            if not self.updateCurrentPlayerLabel():
                return False
            if not self.drawBoard():
                return False
            self.after(500, self.checkAndPlayAi)
            return True
        except Exception as e:
            print(f"Error starting game: {e}")
            return False
        
    ## Update the label showing the current player.
    #
    # @return bool True if the function succeeds, False otherwise.
    def updateCurrentPlayerLabel(self) -> bool:
        try:
            currentPlayer = self.ticTacToeGame.getPlayerToPlay()
            playerName = currentPlayer.getName()
            self.currentPlayerLabel.config(text=f"Current Player: {playerName}")
            return True
        except Exception as e:
            print(f"Error updating current player label: {e}")
            return False

    ## Load a PNG image from the given file path.
    #
    # @param filePath The path to the PNG file.
    # @return ImageTk.PhotoImage The loaded image.
    def loadPngImage(self, filePath: str) -> ImageTk.PhotoImage:
        image = Image.open(filePath)
        return ImageTk.PhotoImage(image)

    ## Handle a click event on the canvas.
    #
    # @param event The click event.
    # @return bool True if the function succeeds, False otherwise.
    @privatemethod
    def __handleClick__(self, event: tk.Tk) -> bool:
        try:
            col = event.x // self.cellSize
            row = event.y // self.cellSize

            if 0 <= row < self.board.getHeight() and 0 <= col < self.board.getWidth():
                if self.board.isCaseAvaillable(row, col):
                    gameOutcome = self.ticTacToeGame.playMove(row, col)
                    if not self.drawBoard():
                        return False
                    if gameOutcome.getGameStatus() != GameOutcomeStatus.UNFINISHED:
                        if not self.showGameResult(gameOutcome):
                            return False
                    else:
                        self.ticTacToeGame.gameState.__nextTurn__()
                        if not self.updateCurrentPlayerLabel():
                            return False
                        self.checkAndPlayAi()
            return True
        except Exception as e:
            print(f"Error handling click: {e}")
            return False

    ## Check if the current player is an AI and play the next move if so.
    #
    # @return bool True if the function succeeds, False otherwise.
    def checkAndPlayAi(self) -> bool:
        try:
            if isinstance(self.ticTacToeGame.getPlayerToPlay(), MinimaxTranspositionTablePlayer):
                self.after(500, self.__playNextAiMove__)
            return True
        except Exception as e:
            print(f"Error checking and playing AI: {e}")
            return False

    ## Play the next move for the AI player.
    #
    # @return bool True if the function succeeds, False otherwise.
    @privatemethod
    def __playNextAiMove__(self) -> bool:
        try:
            gameOutcome = self.ticTacToeGame.playAiMove()
            if not self.drawBoard():
                return False
            if gameOutcome.getGameStatus() != GameOutcomeStatus.UNFINISHED:
                if not self.showGameResult(gameOutcome):
                    return False
            else:
                self.ticTacToeGame.gameState.__nextTurn__()
                self.checkAndPlayAi()
            if not self.updateCurrentPlayerLabel():
                return False
            return True
        except Exception as e:
            print(f"Error playing next AI move: {e}")
            return False

    ## Draw the game board on the canvas.
    #
    # @return bool True if the function succeeds, False otherwise.
    def drawBoard(self) -> bool:
        try:
            boardState = [['' for _ in range(self.board.getWidth())] for _ in range(self.board.getHeight())]
            for row in range(self.board.getHeight()):
                for col in range(self.board.getWidth()):
                    if self.board.isCaseBlocked(row, col):
                        boardState[row][col] = '#'
                    elif self.board.isEntityAt(row, col):
                        entity = self.board.getEntityAt(row, col)
                        boardState[row][col] = entity.getName()
            if not drawGrid(self.gridCanvas, self.width, self.height, self.cellSize, boardState, playerSymbols=self.playerSymbols, playerColors=self.playerColors, coord=True):
                raise RuntimeError("Failed to draw grid")
            return True
        except Exception as e:
            print(f"Error drawing board: {e}")
            return False

    ## Show the result of the game.
    #
    # @param gameOutcome The outcome of the game.
    # @return bool True if the function succeeds, False otherwise.
    def showGameResult(self, gameOutcome) -> bool:
        try:
            if gameOutcome.getGameStatus() == GameOutcomeStatus.VICTORY:
                winner = gameOutcome.getWinner()
                resultText = f"Player {winner + 1} wins!"
            else:
                resultText = "It's a draw!"
            self.resultLabel = ttk.Label(self.infoBox, text=resultText, font=("Arial", 24), background="#555", foreground="white")
            self.resultLabel.pack(side="top", pady=20)

            self.returnButton = ttk.Button(self.infoBox, text="Return to Welcome Page", command=self.returnToWelcome)
            self.returnButton.pack(side="top", pady=20)
            return True
        except Exception as e:
            print(f"Error showing game result: {e}")
            return False

    ## Return to the welcome page.
    #
    # @return bool True if the function succeeds, False otherwise.
    def returnToWelcome(self) -> bool:
        try:
            if not self.controller.frames[PageName.SETTINGS.value].resetSettings():
                return False
            if not self.resetGame():
                return False
            if not self.controller.showFrame(PageName.WELCOME):
                return False
            return True
        except Exception as e:
            print(f"Error returning to welcome page: {e}")
            return False

    ## Reset the game to its initial state.
    #
    # @return bool True if the function succeeds, False otherwise.
    def resetGame(self) -> bool:
        try:
            self.ticTacToeGame = TicTacToeGame()
            self.board = None
            self.gridCanvas.delete("all")
            self.currentPlayerLabel.config(text="Current Player: ")
            self.resultLabel.destroy()
            self.returnButton.destroy()
            return True
        except Exception as e:
            print(f"Error resetting game: {e}")
            return False

    ## Handle a click event on the bomb button.
    #
    # @return None
    @privatemethod
    def __handleBombClick__(self) -> None:
        print("Bomb clicked")
        return None

    ## Handle a click event on the left arrow button.
    #
    # @return None
    @privatemethod
    def __handleLeftArrowClick__(self) -> None:
        print("Left arrow clicked")
        return None

    ## Handle a click event on the right arrow button.
    #
    # @return None
    @privatemethod
    def __handleRightArrowClick__(self) -> None:
        print("Right arrow clicked")
        return None

    ## Handle a click event on the bulb button.
    #
    # @return None
    @privatemethod
    def __handleBulbClick__(self) -> None:
        print("Bulb clicked")
        return None
