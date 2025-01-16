import customtkinter as ctk
from modules.GUI.page import Page
from modules.GUI.render import PageName
from PIL import Image
import tkinter as tk
from modules.GUI.components.grid import drawGrid

from modules.models.tic_tac_toe.tic_tac_toe_game import TicTacToeGame
from modules.models.board_game.game.game_outcome import GameOutcomeStatus

from modules.models.tic_tac_toe.players.ai_players.easy_ai_player import EasyAIPlayer
from modules.models.tic_tac_toe.players.ai_players.medium_ai_player import MediumAIPlayer
from modules.models.tic_tac_toe.players.ai_players.hard_ai_player import HardAIPlayer

class Game(Page):
    def __init__(self, parent: ctk.CTkFrame, controller: ctk.CTk) -> None:
        super().__init__(parent, controller)
        self.settings = None
        self.game = None
        self.board = None
        self.cellSize = 100
        self.moveHistory = []
        self.grid_columnconfigure(0, weight=2)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.__createWidgets__()
        return None
    
    def redirect(self) -> bool:
        self.controller.showFrame(PageName.WELCOME)
        return True
    
    def __createWidgets__(self) -> None:
        width_ratio, height_ratio = self.getScreenRatio()
        
        # Right board
        nbCellWidth = 7
        nbCellHeight = 7
        size = (int(self.cellSize * nbCellWidth), int(self.cellSize * nbCellHeight))
        
        # Create a canvas to draw the grid
        self.grid_canvas = tk.Canvas(self, width=size[0], height=size[1], bg="#4b4b4b", borderwidth=0, highlightthickness=0)
        self.grid_canvas.grid(row=0, rowspan=2, column=0)
        
        # Right frame
        right_frame = ctk.CTkFrame(self, fg_color="#333333")
        right_frame.grid(row=0, rowspan=3, column=1, sticky="nsew")
        right_frame.grid_columnconfigure(0, weight=1)
        right_frame.grid_columnconfigure(1, weight=1)
        right_frame.grid_columnconfigure(2, weight=1)
        right_frame.grid_columnconfigure(3, weight=1)
        right_frame.grid_rowconfigure(0, weight=1)
        right_frame.grid_rowconfigure(1, weight=1)
        right_frame.grid_rowconfigure(2, weight=1)
        
        # Turn label
        self.turn_label = ctk.CTkLabel(right_frame, text="Turn 1", justify="center", font=("Arial", int(32 * height_ratio), "bold"), text_color="#FFFFFF")
        self.turn_label.grid(row=0, column=0, columnspan=4, pady=(int(20 * height_ratio), 0), sticky="n")
        
        # Player turn label
        self.player_turn_label = ctk.CTkLabel(right_frame, text="It's up to Player 1 to play", justify="center", font=("Arial", int(24 * height_ratio)), text_color="#FFFFFF")
        self.player_turn_label.grid(row=0, column=0, columnspan=4, pady=(int(80 * height_ratio), 0), sticky="n")
        
        # Scrollable frame with history of plays
        self.scrollFrame = ctk.CTkScrollableFrame(right_frame, width=200, height=200)
        self.scrollFrame.grid(row=1, column=0, columnspan=4, padx=int(60 * width_ratio), sticky="nsew")
        
        # Bomb button + undo button + redo button + help button
        bomb_image = ctk.CTkImage(   
                            light_image=Image.open("./assets/Bomb.png"),
                            dark_image=Image.open("./assets/Bomb.png"),
                            size=(int(40 * width_ratio), int(40 * height_ratio))
                                )    
        bulb_image = ctk.CTkImage(
                            light_image=Image.open("./assets/Bulb.png"),
                            dark_image=Image.open("./assets/Bulb.png"),
                            size=(int(24 * width_ratio), int(40 * height_ratio))
                                )
        undo_image = ctk.CTkImage(
                            light_image=Image.open("./assets/Undo.png"),
                            dark_image=Image.open("./assets/Undo.png"),
                            size=(int(12 * width_ratio), int(24 * height_ratio))
                                )
        redo_image = ctk.CTkImage(
                            light_image=Image.open("./assets/Redo.png"),
                            dark_image=Image.open("./assets/Redo.png"),
                            size=(int(12 * width_ratio), int(24 * height_ratio))
                                )
        
        ctk.CTkButton(right_frame, text="", image=bomb_image, font=("Arial", int(18 * height_ratio)), command=lambda: self.bomb(), width=40, height=40).grid(row=2, column=0, pady=(0, int(20 * height_ratio)), sticky="es")
        ctk.CTkButton(right_frame, text="", image=undo_image, font=("Arial", int(18 * height_ratio)), command=lambda: self.undo(), width=40, height=40).grid(row=2, column=1, pady=(0, int(20 * height_ratio)), sticky="s")
        ctk.CTkButton(right_frame, text="", image=redo_image, font=("Arial", int(18 * height_ratio)), command=lambda: self.redo(), width=40, height=40).grid(row=2, column=2, pady=(0, int(20 * height_ratio)), sticky="s")
        ctk.CTkButton(right_frame, text="", image=bulb_image, font=("Arial", int(18 * height_ratio)), command=lambda: self.help(), width=40, height=40).grid(row=2, column=3, pady=(0, int(20 * height_ratio)), sticky="ws")
        
        # Play button
        ctk.CTkButton(self, text="Leave", font=("Arial", int(32 * height_ratio)), command=lambda: self.redirect()).grid(row=2, column=0)
        
        # Set click event on the grid_canvas
        self.grid_canvas.bind("<Button-1>", self.__handle_click__)
        
        return None

    ## Draw the game board on the canvas.
    #
    # @return bool True if the function succeeds, False otherwise.
    def __drawBoard__(self) -> bool:
        try:
            boardState = [['' for _ in range(self.board.getWidth())] for _ in range(self.board.getHeight())]
            for row in range(self.board.getHeight()):
                for col in range(self.board.getWidth()):
                    if self.board.isCaseBlocked(row, col):
                        boardState[row][col] = '#'
                    elif self.board.isEntityAt(row, col):
                        entity = self.board.getEntityAt(row, col)
                        boardState[row][col] = entity.getName()
            if not drawGrid(self.grid_canvas, self.cellSize * self.board.getWidth(), self.cellSize * self.board.getHeight(), self.cellSize, boardState,
                            playerSymbols=[self.game.getEntities()[0].getName(), self.game.getEntities()[1].getName()], playerColors=[self.settings['player1']['color'], self.settings['player2']['color']], coord=True):
                raise RuntimeError("Failed to draw grid")
            return True
        except Exception as e:
            print(f"Error drawing board: {e}")
            return False

    def __handle_click__(self, event) -> bool:
        if not isinstance(self.game, TicTacToeGame):
            return False

        try:
            col = event.x // self.cellSize
            row = event.y // self.cellSize

            if 0 <= row < self.board.getHeight() and 0 <= col < self.board.getWidth():
                if self.board.isCaseAvaillable(row, col):
                    gameOutcome = self.ticTacToeGame.playMove(row, col)
                    if not self.__drawBoard__():
                        return False
                    if gameOutcome.getGameStatus() != GameOutcomeStatus.UNFINISHED:
                        if not self.__showGameResult__(gameOutcome):
                            return False
                    else:
                        self.game.gameState.__nextTurn__()
                        if not self.__setPlayerTurn__():
                            return False
                        if not self.__updateMoveHistory__():
                            return False
                        self.__checkAndPlayAi__()
            return True
        except Exception as e:
            print(f"Error handling click: {e}")
            return False

    def __updateMoveHistory__(self) -> bool:
        move = self.game.getGameHistory()[-1]
        moveLine = move.getCoordinate().getLine()
        moveColumn = move.getCoordinate().getColumn()
        playerIndex = (self.game.getGameState().getPlayerToPlayIndex() + 1) % 2  # Fix player index
        self.moveHistory.append(f"Player {playerIndex + 1} played at ({chr(65 + moveColumn)}, {moveLine + 1})")
        for widget in self.scrollFrame.winfo_children():
            widget.destroy()
        for move in self.moveHistory:
            ctk.CTkLabel(self.scrollFrame, text=move, font=("Arial", 14), text_color="#FFFFFF").pack(anchor="w")
        return True

    def bomb(self) -> bool:
        print("Bomb")
        return True
    
    def undo(self) -> bool:
        print("Undo")
        return True
    
    def redo(self) -> bool:
        print("Redo")
        return True
    
    def help(self) -> bool:
        print("Help")
        return True
    
    def reset_game(self) -> bool:
        self.settings = None
        self.game = None
        self.board = None
        self.moveHistory = []
        return True
    
    def start_game(self, settings) -> bool:
        self.settings = settings
        print(f"Starting game with settings: {settings}")
        self.game = TicTacToeGame(self.settings)
        self.board = self.game.getBoard()
        self.grid_canvas.configure(width=self.cellSize * self.board.getWidth(), height=self.cellSize * self.board.getHeight())
        if not self.__drawBoard__():
            print("Failed to draw board")
            return False
        if not self.__setPlayerTurn__():
            print("Failed to set turn label")
            return False
        self.after(500, self.__checkAndPlayAi__)
        return True
    
    def __setPlayerTurn__(self) -> bool:
        if not isinstance(self.game, TicTacToeGame):
            return False
        currentPlayer = self.game.getPlayerToPlay()
        self.player_turn_label.configure(text=f"It's up to {currentPlayer.getName()} to play")
        return True 
    
    ## Check if the current player is an AI and play the next move if so.
    #
    # @return bool True if the function succeeds, False otherwise.
    def __checkAndPlayAi__(self) -> bool:
        try:
            if isinstance(self.game.getPlayerToPlay(), EasyAIPlayer) or isinstance(self.game.getPlayerToPlay(), MediumAIPlayer) or isinstance(self.game.getPlayerToPlay(), HardAIPlayer):
                self.after(500, self.__playNextAiMove__)
            return True
        except Exception as e:
            print(f"Error checking and playing AI: {e}")
            return False
        
    def __playNextAiMove__(self) -> bool:
        try:
            gameOutcome = self.game.playAiMove()
            if not self.__drawBoard__():
                return False
            if gameOutcome.getGameStatus() != GameOutcomeStatus.UNFINISHED:
                if not self.__showGameResult__(gameOutcome):
                    return False
            else:
                self.game.gameState.__nextTurn__()
                self.__checkAndPlayAi__()
            if not self.__setPlayerTurn__():
                return False
            if not self.__updateMoveHistory__():
                return False
            return True
        except Exception as e:
            print(f"Error playing next AI move: {e}")
            return False
        
    def __showGameResult__(self, gameOutcome) -> bool:
        print(f"Game outcome: {gameOutcome}")
        return True