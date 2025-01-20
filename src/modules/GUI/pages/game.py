from typing import Optional, Tuple, List
import tkinter as tk
from PIL import Image

import customtkinter as ctk
from modules.models.tic_tac_toe.moves.power_ups.bomb_move import BombMove
from modules.utils.decorator import privatemethod
from modules.GUI.page import Page
from modules.GUI.render import PageName
from modules.GUI.components.grid import drawGrid

from modules.models.tic_tac_toe.tic_tac_toe_game import TicTacToeGame
from modules.models.board_game.game.game_outcome import GameOutcomeStatus
from modules.models.tic_tac_toe.players.human_player import HumanPlayer
from modules.models.tic_tac_toe.moves.simple_move import SimpleMove

from modules.models.tic_tac_toe.players.ai_players.easy_ai_player import EasyAIPlayer
from modules.models.tic_tac_toe.players.ai_players.medium_ai_player import MediumAIPlayer
from modules.models.tic_tac_toe.players.ai_players.hard_ai_player import HardAIPlayer

# ************************************************
# CLASS Game
# ************************************************
# ROLE : The goal of this class is to represent the game page
# ************************************************
# VERSION : 1.0
# AUTHOR : Hugo MERY
# DATE : 18/01/2025
# ************************************************

class Game(Page):
    
    """
    The game page.
    """
    
    def __init__(self, parent: ctk.CTkFrame, controller: ctk.CTk) -> None:
        
        """
        Initializes the game page.
        
        Parameters:
            parent (ctk.CTkFrame): The parent frame.
            controller (ctk.CTk): The main controller.

        Returns:
            None
        """
        
        super().__init__(parent, controller)
        self.settings: Optional[dict] = None
        self.game: Optional[TicTacToeGame] = None
        self.board: Optional[object] = None
        self.cellSize: int = 100
        self.turn: int = 0
        self.bombMove: bool = False
        self.gameOutCome: Optional[GameOutcomeStatus] = None
        self.grid_columnconfigure(0, weight=2)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.__createWidgets__()
        self.explosionImages = [tk.PhotoImage(file=f"./assets/Explosion3.gif", format=f"gif -index {i}") for i in range(7)]
        self.explosionLabel = ctk.CTkLabel(self.gridCanvas, text="", width=int(self.cellSize * 3)-2, height=int(self.cellSize * 3)-2)
        self.clockImages = [tk.PhotoImage(file=f"./assets/Clock2.gif", format=f"gif -index {i}") for i in range(14)]
        self.clockLabel = ctk.CTkLabel(self.gridCanvas, text="")
        return None
    
    def redirect(self) -> bool:
        
        """
        Redirects to the welcome page.
        
        Returns:
            bool: True if the function succeeds, False otherwise.
        """
        
        self.controller.showFrame(PageName.WELCOME)
        return True
    
    @privatemethod
    def __createWidgets__(self) -> bool:
        
        """
        Creates the widgets for the game page.
        
        Returns:
            bool: True if the function succeeds, False otherwise
        """
        
        self.widthRatio: float
        self.heightRatio: float
        self.widthRatio, self.heightRatio = self.getScreenRatio()
        
        # Left frame
        self.leftFrame: ctk.CTkFrame = ctk.CTkFrame(self, fg_color="transparent")
        self.leftFrame.grid(row=0, rowspan=3, column=0, sticky="nsew")
        self.leftFrame.grid_columnconfigure(0, weight=1)
        self.leftFrame.grid_rowconfigure(0, weight=1)
        self.leftFrame.grid_rowconfigure(1, weight=1)
        self.leftFrame.grid_rowconfigure(2, weight=1)
        self.leftFrame.grid_rowconfigure(3, weight=1)
        
        # Create a canvas to draw the grid
        self.gridCanvas: tk.Canvas = tk.Canvas(self.leftFrame, width=int(self.cellSize * 7), height=int(self.cellSize * 7), bg="#4b4b4b", borderwidth=0, highlightthickness=0)
        self.gridCanvas.grid(row=0, rowspan=3, column=0)
        
        # Right frame
        self.rightFrame: ctk.CTkFrame = ctk.CTkFrame(self, fg_color="#333333")
        self.rightFrame.grid(row=0, rowspan=3, column=1, sticky="nsew")
        self.rightFrame.grid_columnconfigure(0, weight=1)
        self.rightFrame.grid_columnconfigure(1, weight=1)
        self.rightFrame.grid_columnconfigure(2, weight=1)
        self.rightFrame.grid_columnconfigure(3, weight=1)
        self.rightFrame.grid_rowconfigure(0, weight=1)
        self.rightFrame.grid_rowconfigure(1, weight=1)
        self.rightFrame.grid_rowconfigure(2, weight=1)
        
        # Turn label
        self.turnLabel: ctk.CTkLabel = ctk.CTkLabel(self.rightFrame, text="Turn 1", justify="center", font=("Arial", int(32 * self.heightRatio), "bold"), text_color="#FFFFFF")
        self.turnLabel.grid(row=0, column=0, columnspan=4, pady=(int(20 * self.heightRatio), 0), sticky="n")
        
        # Player turn label
        self.playerTurnLabel: ctk.CTkLabel = ctk.CTkLabel(self.rightFrame, text="It's up to Player 1 to play", justify="center", font=("Arial", int(24 * self.heightRatio)), text_color="#FFFFFF")
        self.playerTurnLabel.grid(row=0, column=0, columnspan=4, pady=(int(80 * self.heightRatio), 0), sticky="n")
        
        # Scrollable frame with history of plays
        self.scrollFrame: ctk.CTkScrollableFrame = ctk.CTkScrollableFrame(self.rightFrame, width=200, height=200)
        self.scrollFrame.grid(row=1, column=0, columnspan=4, padx=int(60 * self.widthRatio), sticky="nsew")
        
        # Frame for buttons
        self.buttonsFrame: ctk.CTkFrame = ctk.CTkFrame(self.rightFrame, height=80, fg_color="#333333")
        self.buttonsFrame.grid(row=2, column=0, columnspan=4, pady=(0, int(60 * self.heightRatio)), sticky="nsew")
        self.buttonsFrame.grid_columnconfigure(0, weight=1)
        self.buttonsFrame.grid_columnconfigure(1, weight=1)
        self.buttonsFrame.grid_columnconfigure(2, weight=1)
        self.buttonsFrame.grid_columnconfigure(3, weight=1)
        self.buttonsFrame.grid_rowconfigure(0, weight=1)
        
        # Bomb button + undo button + redo button + help button
        bombImage: ctk.CTkImage = ctk.CTkImage(   
                            light_image=Image.open("./assets/Bomb.png"),
                            dark_image=Image.open("./assets/Bomb.png"),
                            size=(int(40 * self.widthRatio), int(40 * self.heightRatio))
                                )    
        bulbImage: ctk.CTkImage = ctk.CTkImage(
                            light_image=Image.open("./assets/Bulb.png"),
                            dark_image=Image.open("./assets/Bulb.png"),
                            size=(int(24 * self.widthRatio), int(40 * self.heightRatio))
                                )
        undoImage: ctk.CTkImage = ctk.CTkImage(
                            light_image=Image.open("./assets/Undo.png"),
                            dark_image=Image.open("./assets/Undo.png"),
                            size=(int(12 * self.widthRatio), int(24 * self.heightRatio))
                                )
        redoImage: ctk.CTkImage = ctk.CTkImage(
                            light_image=Image.open("./assets/Redo.png"),
                            dark_image=Image.open("./assets/Redo.png"),
                            size=(int(12 * self.widthRatio), int(24 * self.heightRatio))
                                )
        
        self.bombButton: ctk.CTkButton = ctk.CTkButton(self.buttonsFrame, text="", image=bombImage, font=("Arial", int(18 * self.heightRatio)), command=lambda: self.__bomb__(), width=40, height=40)
        self.bombButton.grid(row=0, column=0, sticky="es")
        self.undoButton: ctk.CTkButton = ctk.CTkButton(self.buttonsFrame, text="", image=undoImage, font=("Arial", int(18 * self.heightRatio)), command=lambda: self.__undo__(), width=40, height=40)
        self.undoButton.grid(row=0, column=1, sticky="s")
        self.redoButton: ctk.CTkButton = ctk.CTkButton(self.buttonsFrame, text="", image=redoImage, font=("Arial", int(18 * self.heightRatio)), command=lambda: self.__redo__(), width=40, height=40)
        self.redoButton.grid(row=0, column=2, sticky="s")
        self.bulbButton: ctk.CTkButton = ctk.CTkButton(self.buttonsFrame, text="", image=bulbImage, font=("Arial", int(18 * self.heightRatio)), command=lambda: self.__advice__(), width=40, height=40)
        self.bulbButton.grid(row=0, column=3, sticky="ws")
        
        # Play button
        ctk.CTkButton(self.leftFrame, text="Leave", font=("Arial", int(32 * self.heightRatio)), command=lambda: self.redirect()).grid(row=3, column=0)
        
        # Set click event on the grid_canvas
        self.gridCanvas.bind("<Button-1>", self.__handleClick__)
        
        return True

    @privatemethod
    def __drawBoard__(self, advice: Tuple[int, int] = ()) -> bool:
        
        """
        Draws the game board on the canvas.
        
        Parameters:
            advice (Tuple[int, int]): The coordinates of the advised move.

        Returns:
            bool: True if the function succeeds, False otherwise.
        """
        
        try:
            boardState: List[List[str]] = [['' for _ in range(self.board.getWidth())] for _ in range(self.board.getHeight())]
            self.gridCanvas.delete("all")
            for row in range(self.board.getHeight()):
                for col in range(self.board.getWidth()):
                    if self.board.isCaseBlocked(row, col):
                        boardState[row][col] = '#'
                    elif self.board.isEntityAt(row, col):
                        entity = self.board.getEntityAt(row, col)
                        boardState[row][col] = entity.getName()
            if not drawGrid(self.gridCanvas, self.cellSize * self.board.getWidth(), self.cellSize * self.board.getHeight(), self.cellSize, boardState,
                            playerSymbols=[self.game.getEntities()[0].getName(), self.game.getEntities()[1].getName()], playerColors=[self.settings['player1']['color'], self.settings['player2']['color']], coord=True, advice=advice):
                raise RuntimeError("Failed to draw grid")
            return True
        except Exception as e:
            print(f"Error drawing board: {e}")
            return False

    @privatemethod
    def __handleClick__(self, event: tk.Event) -> bool:
        
        """
        Handles click events on the game board.
        
        Parameters:
            event (tk.Event): The click event.

        Returns:
            bool: True if the function succeeds, False otherwise.
        """
        
        if not isinstance(self.game, TicTacToeGame):
            return False

        try:
            currentPlayer: Optional[HumanPlayer] = self.game.getPlayerToPlay()
            if not isinstance(currentPlayer, HumanPlayer):
                return False
            
            if self.gameOutCome is not None and self.gameOutCome.getGameStatus() != GameOutcomeStatus.UNFINISHED:
                return False

            col: int = event.x // self.cellSize
            row: int = event.y // self.cellSize

            if 0 <= row < self.board.getHeight() and 0 <= col < self.board.getWidth():
                currentPlayer = self.game.getPlayerToPlay()
                move: Optional[object] = None
                if self.bombMove or self.board.isCaseAvaillable(row, col):
                    move = self.game.playHumainMove(row, col, self.bombMove)
                if move is not None:
                    self.gameOutCome = move
                    self.bombMove = False
                    moveType = self.game.getGameHistory().getCurrentMove()
                    if isinstance(moveType, BombMove):
                        if not self.__playExplosion__(moveType.getCoordinate().getLine(), moveType.getCoordinate().getColumn()):
                            return False
                    if self.settings['game']['gamemode'] == 'Bomb mod':
                        self.bombButton.configure(fg_color="#1f6aa5", hover_color="#144870")
                    if not self.__drawBoard__():
                        return False
                    if not self.__updateMoveHistory__():
                        return False
                    if not self.__updateButtons__():
                        return False
                    if not self.__setTurnLabel__():
                        return False
                    if not self.__setPlayerTurn__():
                        return False
                    if self.gameOutCome.getGameStatus() != GameOutcomeStatus.UNFINISHED:
                        if not self.__showGameResult__():
                            return False
                        return True
                    else:
                        self.__checkAndPlayAi__()
            return True
        except Exception as e:
            print(f"Error handling click: {e}")
            return False
        
    @privatemethod
    def __updateMoveHistory__(self) -> bool:
        
        """
        Updates the move history displayed in the scrollable frame.
        
        Returns:
            bool: True if the function succeeds, False otherwise.
        """
        
        moves: List[object] = self.game.getGameHistoryList()
        playerIndex: int = 1 if self.settings['game']['startingPlayer'] == self.settings['player1']['name'] else 0
        for widget in self.scrollFrame.winfo_children():
            widget.destroy()
        for i, move in enumerate(moves):
            playerIndex = 1 - playerIndex
            if isinstance(move, SimpleMove):
                moveText: str = f"{self.settings[f'player{playerIndex+1}']['name']} played at {chr(65 + move.getCoordinate().getColumn())}, {move.getCoordinate().getLine() + 1}"
            else:
                moveText: str = f"{self.settings[f'player{playerIndex+1}']['name']} played a bomb at {chr(65 + move.getCoordinate().getColumn())}, {move.getCoordinate().getLine() + 1}"
            font: Tuple[str, int, str] = ("Arial", int(16 * self.heightRatio), "bold") if move == self.game.getGameHistory().getCurrentMove() else ("Arial", int(16 * self.heightRatio))
            ctk.CTkLabel(self.scrollFrame, text=moveText, font=font, text_color=self.settings[f"player{playerIndex+1}"]["color"]).pack(anchor="w")
        return True
    
    @privatemethod
    def __updateButtons__(self) -> bool:
        
        """
        Updates the state of the bomb, undo, redo, and bulb buttons.
        
        Returns:
            bool: True if the function succeeds, False otherwise.
        """
        
        self.__updateBombButton__()
        self.__updateUndoRedoButtons__()
        self.__updateBulbButton__()
        return True
    
    @privatemethod
    def __updateBombButton__(self) -> bool:
        
        """
        Updates the state of the bomb button.
        
        Returns:
            bool: True if the function succeeds, False otherwise.
        """
        
        currentPlayer: Optional[HumanPlayer] = self.game.getPlayerToPlay()
        isHuman: bool = isinstance(currentPlayer, HumanPlayer)
        hasPowerUp: bool = isHuman and self.game.getPlayerPowerUpMoves(self.game.getGameState().getPlayerToPlayIndex())
        
        state: str = "normal" if hasPowerUp else "disabled"
        fgColor: str = "#1f6aa5" if hasPowerUp else "#666666"
        hoverColor: str = "#144870" if hasPowerUp else "#666666"
        
        self.bombButton.configure(state=state, fg_color=fgColor, hover_color=hoverColor)
        return True
    
    @privatemethod
    def __updateUndoRedoButtons__(self) -> bool:
        
        """
        Updates the state of the undo and redo buttons.
        
        Returns:
            bool: True if the function succeeds, False otherwise.
        """
        
        currentPlayer: Optional[HumanPlayer] = self.game.getPlayerToPlay()
        if isinstance(currentPlayer, HumanPlayer):
            self.undoButton.configure(state="normal", fg_color="#1f6aa5", hover_color="#144870")
            self.redoButton.configure(state="normal", fg_color="#1f6aa5", hover_color="#144870")
        else:
            self.undoButton.configure(state="disabled", fg_color="#666666", hover_color="#666666")
            self.redoButton.configure(state="disabled", fg_color="#666666", hover_color="#666666")
        return True
    
    @privatemethod
    def __updateBulbButton__(self) -> bool:
        
        """
        Updates the state of the bulb button.
        
        Returns:
            bool: True if the function succeeds, False otherwise.
        """
        
        currentPlayer: Optional[HumanPlayer] = self.game.getPlayerToPlay()
        if isinstance(currentPlayer, HumanPlayer):
            self.bulbButton.configure(state="normal", fg_color="#1f6aa5", hover_color="#144870")
        else:
            self.bulbButton.configure(state="disabled", fg_color="#666666", hover_color="#666666")
        return True

    @privatemethod
    def __bomb__(self) -> bool:
        
        """
        Toggles the bomb move state.
        
        Returns:
            bool: True if the function succeeds, False otherwise.
        """
        
        self.bombMove = not self.bombMove
        if self.bombMove:
            self.bombButton.configure(fg_color="#990000", hover_color="#660000")
        else:
            self.bombButton.configure(fg_color="#1f6aa5", hover_color="#144870")
        return True
    
    @privatemethod
    def __undo__(self) -> bool:
        
        """
        Undoes the last move.
        
        Returns:
            bool: True if the function succeeds, False otherwise.
        """
        
        #self.__playUndo__()
        self.game.undo()
        if not self.__drawBoard__():
            return False
        if not self.__updateButtons__():
            return False
        self.turn -= 2
        if not self.__setTurnLabel__():
            return False
        if not self.__setPlayerTurn__():
            return False
        if not self.__updateMoveHistory__():
            return False
        self.after(500, self.__checkAndPlayAi__)
        return True
    
    @privatemethod
    def __redo__(self) -> bool:
        
        """
        Redoes the last undone move.
        
        Returns:
            bool: True if the function succeeds, False otherwise.
        """
        
        #self.__playRedo__()
        self.game.redo()
        if not self.__drawBoard__():
            return False
        if not self.__updateButtons__():
            return False
        if not self.__setTurnLabel__():
            return False
        if not self.__setPlayerTurn__():
            return False
        if not self.__updateMoveHistory__():
            return False
        self.after(500, self.__checkAndPlayAi__)
        return True
    
    @privatemethod
    def __advice__(self) -> bool:
        
        """
        Provides advice for the next move.
        
        Returns:
            bool: True if the function succeeds, False otherwise.
        """
        
        move: object = self.game.getAdvice()
        move = (move.getCoordinate().getLine(), move.getCoordinate().getColumn())
        if not self.__drawBoard__(advice=move):
            return False
        self.bulbButton.configure(state="disabled", fg_color="#666666", hover_color="#666666")
        return True
    
    def resetGame(self) -> bool:
        
        """
        Resets the game state.
        
        Returns:
            bool: True if the function succeeds, False otherwise.
        """
        
        self.settings = None
        self.game = None
        self.board = None
        self.moveHistory = []
        self.turn = 1
        for widget in self.scrollFrame.winfo_children():
            widget.destroy()
        self.gridCanvas.delete("all")
        self.bombMove = False
        self.bombButton.configure(state="normal")
        self.bombButton.configure(fg_color="#1f6aa5", hover_color="#144870")
        self.gameOutCome = None
        return True

    def startGame(self, settings: dict) -> bool:
        
        """
        Starts a new game with the given settings.
        
        Parameters:
            settings (dict): The game settings.

        Returns:
            bool: True if the function succeeds, False otherwise.
        """
        
        self.settings = settings
        self.game = TicTacToeGame(self.settings)
        self.board = self.game.getBoard()
        self.gridCanvas.configure(width=self.cellSize * self.board.getWidth(), height=self.cellSize * self.board.getHeight())
        self.clockLabel.configure(width=int(self.cellSize * self.board.getWidth())-2, height=int(self.cellSize * self.board.getHeight())-2)
        if self.settings['game']['gamemode'] == 'No mod':
            self.bombButton.configure(state="disabled")
            self.bombButton.configure(fg_color="#666666", hover_color="#666666")
        if not self.__drawBoard__():
            print("Failed to draw board")
            return False
        if not self.__setPlayerTurn__():
            print("Failed to set turn label")
            return False
        if not self.__setTurnLabel__():
            return False
        if not self.__updateButtons__():
            return False
        self.after(500, self.__checkAndPlayAi__)
        return True
    
    @privatemethod
    def __setPlayerTurn__(self) -> bool:
        
        """
        Sets the player turn label.
        
        Returns:
            bool: True if the function succeeds, False otherwise.
        """
        
        currentPlayer: Optional[HumanPlayer] = self.game.getPlayerToPlay()
        self.playerTurnLabel.configure(text=f"It's up to {currentPlayer.getName()} to play")
        return True 
    
    @privatemethod
    def __checkAndPlayAi__(self) -> bool:
        
        """
        Checks if the current player is an AI and plays the next move if so.
        
        Returns:
            bool: True if the function succeeds, False otherwise.
        """
        
        try:
            if isinstance(self.game.getPlayerToPlay(), EasyAIPlayer) or isinstance(self.game.getPlayerToPlay(), MediumAIPlayer) or isinstance(self.game.getPlayerToPlay(), HardAIPlayer):
                self.after(500, self.__playNextAiMove__)
            return True
        except Exception as e:
            print(f"Error checking and playing AI: {e}")
            return False
       
    @privatemethod 
    def __playNextAiMove__(self) -> bool:
        
        """
        Plays the next AI move.
        
        Returns:
            bool: True if the function succeeds, False otherwise.
        """
        try:
            self.gameOutCome = self.game.playAiMove()
            move = self.game.getGameHistory().getCurrentMove()
            if isinstance(move, BombMove):
                if not self.__playExplosion__(move.getCoordinate().getLine(), move.getCoordinate().getColumn()):
                    return False
            if not self.__drawBoard__():
                return False
            if not self.__updateMoveHistory__():
                return False
            if not self.__updateBombButton__():
                return False
            if not self.__updateUndoRedoButtons__():
                return False
            if not self.__updateBulbButton__():
                return False
            if not self.__setTurnLabel__():
                return False
            if not self.__setPlayerTurn__():
                return False
            if self.gameOutCome.getGameStatus() != GameOutcomeStatus.UNFINISHED:
                if not self.__showGameResult__():
                    return False
                return True
            else:
                self.__checkAndPlayAi__()
            return True
        except Exception as e:
            print(f"Error playing AI move: {e}")
            return False
        
    @privatemethod
    def __setTurnLabel__(self) -> bool:
        
        """
        Sets the turn label.
        
        Returns:
            bool: True if the function succeeds, False otherwise.
        """
        
        self.turn += 1
        self.turnLabel.configure(text=f"Turn {int(self.turn/2)}")
        return True
        
    @privatemethod
    def __showGameResult__(self) -> bool:
        
        """
        Shows the game result.
        
        Returns:
            bool: True if the function succeeds, False otherwise.
        """
        
        if self.gameOutCome.getGameStatus() == GameOutcomeStatus.VICTORY:
            winner = self.gameOutCome.getWinner()
            resultText = f"{self.settings['player1']['name']} won!" if winner == 0 else f"{self.settings['player2']['name']} won!"
        else:
            resultText = "It's a draw!"
        
        self.turnLabel.configure(text=resultText)
        self.playerTurnLabel.configure(text="")
        return True

    @privatemethod
    def __playExplosion__(self, row: int, col: int) -> bool:
        
        """
        Plays an explosion animation at the center of the given cell.

        Parameters:
            row (int): The row index of the cell.
            col (int): The column index of the cell.

        Returns:
            None
        """
        
        x = col * self.cellSize + self.cellSize // 2
        y = row * self.cellSize + self.cellSize // 2
        self.explosionLabel.place(x=x, y=y, anchor="center")
        for img in self.explosionImages:
            self.explosionLabel.configure(image=img)
            self.explosionLabel.update()
            self.gridCanvas.after(100)
        self.explosionLabel.place_forget()
        self.__drawBoard__()
        
        return True
    
    @privatemethod
    def __playRedo__(self) -> bool:
        
        """
        Plays a redo animation.
        
        Returns:
            bool: True if the function succeeds, False otherwise.
        """
        
        x = self.board.getWidth() * self.cellSize // 2
        y = self.board.getHeight() * self.cellSize // 2
        self.clockLabel.place(x=x, y=y, anchor="center")
        for img in self.clockImages:
            self.clockLabel.configure(image=img)
            self.clockLabel.update()
            self.gridCanvas.after(100)
        self.clockLabel.place_forget()
        return True
    
    @privatemethod
    def __playUndo__(self) -> bool:
        
        """
        Plays an undo animation.
        
        Returns:
            bool: True if the function succeeds, False otherwise.
        """
        
        x = self.board.getWidth() * self.cellSize // 2
        y = self.board.getHeight() * self.cellSize // 2
        self.clockLabel.place(x=x, y=y, anchor="center")
        for img in reversed(self.clockImages):
            self.clockLabel.configure(image=img)
            self.clockLabel.update()
            self.gridCanvas.after(100)
        self.clockLabel.place_forget()
        self.__drawBoard__()
        
        return True