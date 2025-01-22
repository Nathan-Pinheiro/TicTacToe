from typing import Optional, Tuple, List
import tkinter as tk
from PIL import Image

import customtkinter as ctk
from modules.models.tic_tac_toe.moves.power_ups.bomb_move import BombMove
from modules.utils.decorator import privatemethod, override
from modules.GUI.page import Page
from modules.GUI.render import PageName
from modules.GUI.components.grid import drawGrid

from modules.models.tic_tac_toe.tic_tac_toe_game import TicTacToeGame
from modules.models.board_game.game.game_outcome import GameOutcomeStatus
from modules.models.tic_tac_toe.players.human_GUI_player import HumanGUIPlayer
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
            
        Raises:
            TypeError: If parent is not a ctk.CTkFrame instance.
            TypeError: If controller is not a ctk.CTk instance.

        Returns:
            None
        """
        
        # Check if the parent is a ctk.CTkFrame instance
        if not isinstance(parent, ctk.CTkFrame):
            raise TypeError("parent must be a ctk.CTkFrame instance")
        
        # Check if the controller is a ctk.CTk instance
        if not isinstance(controller, ctk.CTk):
            raise TypeError("controller must be a ctk.CTk instance")
        
        # Call the parent constructor
        super().__init__(parent, controller)
        
        # Define the attributes of the game page
        self.settings: Optional[dict] = None
        self.game: Optional[TicTacToeGame] = None
        self.board: Optional[object] = None
        self.cellSize: int = 100
        self.turn: int = 0
        self.bombMove: bool = False
        self.gameOutCome: Optional[GameOutcomeStatus] = None
        
        # Configure the grid
        self.grid_columnconfigure(0, weight=2)
        self.grid_columnconfigure(1, weight=1)
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        
        # Create the widgets
        self.__createWidgets__()
        
        # Load the explosion images and create the explosion label
        self.explosionImages = [tk.PhotoImage(file=f"./assets/Explosion3.gif", format=f"gif -index {i}") for i in range(7)]
        self.explosionLabel = ctk.CTkLabel(self.gridCanvas, text="", width=int(self.cellSize * 3)-2, height=int(self.cellSize * 3)-2)
        
        return None
    
    @override
    def redirect(self) -> bool:
        
        """
        Redirects to the welcome page.
        
        Returns:
            bool: True if the function succeeds, False otherwise.
        """
        
        # Show the welcome page
        self.controller.showFrame(PageName.WELCOME)
        
        return True
    
    @override
    def __createWidgets__(self) -> bool:
        
        """
        Creates the widgets for the game page.
        
        Returns:
            bool: True if the function succeeds, False otherwise
        """
        
        # Get the screen ratio
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
    def __drawBoard__(self, advice: Tuple[int | None, int | None] = (None, None)) -> bool:
        
        """
        Draws the game board on the canvas.
        
        Parameters:
            advice (Tuple[int, int]): The coordinates of the advised move.
            
        Raises:
            TypeError: If advice is not a tuple of two integers or None.

        Returns:
            bool: True if the function succeeds, False otherwise.
        """
        
        # Check if the advice is a tuple of two integers or None
        if not isinstance(advice, tuple) or len(advice) != 2 or not all(isinstance(coord, int) or coord is None for coord in advice):
            raise TypeError("advice must be a tuple of two integers or None")
        
        # Define the board state to empty
        boardState: List[List[str]] = [['' for _ in range(self.board.getWidth())] for _ in range(self.board.getHeight())]
        
        # Clear the canvas
        self.gridCanvas.delete("all")
        
        # Get the board
        self.board = self.game.getBoard()
        
        # Fill the board state with the entities and blocked cases
        for row in range(self.board.getHeight()):
            for col in range(self.board.getWidth()):
                if self.board.isCaseBlocked(row, col):
                    boardState[row][col] = '#'
                elif self.board.isEntityAt(row, col):
                    entity = self.board.getEntityAt(row, col)
                    boardState[row][col] = entity.getSymbol()
                    
        # Draw the grid
        drawGrid(self.gridCanvas, self.cellSize * self.board.getWidth(), self.cellSize * self.board.getHeight(), self.cellSize, boardState,
                        playerSymbols=[self.game.getEntities()[0].getSymbol(), self.game.getEntities()[1].getSymbol()], playerColors=[self.settings['player1']['color'], self.settings['player2']['color']], coord=True, advice=advice)
        
        return True

    @privatemethod
    def __handleClick__(self, event: tk.Event) -> bool:
        
        """
        Handles click events on the game board.
        
        Parameters:
            event (tk.Event): The click event.
            
        Raises:
            TypeError: If event is not a tk.Event instance.

        Returns:
            bool: True if the function succeeds, False otherwise.
        """
        
        # Check if the event is a tk.Event instance
        if not isinstance(event, tk.Event):
            raise TypeError("event must be a tk.Event instance")

        # Get the current player to play
        currentPlayer: Optional[HumanGUIPlayer] = self.game.getPlayerToPlay()
        
        # Check if the current player is a human player
        if not isinstance(currentPlayer, HumanGUIPlayer):
            return False
            
        # Check if the game is finished
        if self.gameOutCome is not None and self.gameOutCome.getGameStatus() != GameOutcomeStatus.UNFINISHED:
            return False

        # Get the cell clicked
        col: int = event.x // self.cellSize
        row: int = event.y // self.cellSize

        # Play the move if possible
        if 0 <= row < self.board.getHeight() and 0 <= col < self.board.getWidth():
            
            # Define the move
            move: Optional[object] = None
            
            # Play the move
            if self.bombMove or self.board.isCaseAvaillable(row, col):
                move = self.game.playHumainMove(row, col, self.bombMove)
            
            # Check if the move is played
            if move is not None:
                
                # Update the game state
                self.gameOutCome = move
                self.bombMove = False
                
                # Check if the move is a bomb move and play the explosion
                moveType = self.game.getGameHistory().getCurrentMove()
                
                if isinstance(moveType, BombMove):
                    self.__playExplosion__(moveType.getCoordinate().getLine(), moveType.getCoordinate().getColumn())
                    
                # Update the board
                self.__drawBoard__()
                
                # Update the move history
                self.__updateMoveHistory__()
                
                # Update the buttons
                self.__updateButtons__()
                
                # Update the turn label and player turn label
                self.__setTurnLabel__()
                
                self.__setPlayerTurn__()
                
                # Check if the game is finished and show the result else check if next player is an AI
                if self.gameOutCome.getGameStatus() != GameOutcomeStatus.UNFINISHED:
                    
                    self.__showGameResult__()
                    
                    return True
                
                else:
                    self.__checkAndPlayAi__()
                    
        return True
        
    @privatemethod
    def __updateMoveHistory__(self) -> bool:
        
        """
        Updates the move history displayed in the scrollable frame.
        
        Returns:
            bool: True if the function succeeds, False otherwise.
        """
        
        # Get the list of moves
        moves: List[object] = self.game.getGameHistoryList()
        
        # Define the player index
        playerIndex: int = 1 if self.settings['game']['startingPlayer'] == self.settings['player1']['name'] else 0
        
        # Clear the scrollable frame
        for widget in self.scrollFrame.winfo_children():
            widget.destroy()
            
        # Add all moves to the scrollable frame
        for _, move in enumerate(moves):
            
            playerIndex = 1 - playerIndex
            
            # Define the move text
            if isinstance(move, SimpleMove):
                moveText: str = f"{self.settings[f'player{playerIndex+1}']['name']} played at {chr(65 + move.getCoordinate().getColumn())}, {move.getCoordinate().getLine() + 1}"
            else:
                moveText: str = f"{self.settings[f'player{playerIndex+1}']['name']} played a bomb at {chr(65 + move.getCoordinate().getColumn())}, {move.getCoordinate().getLine() + 1}"
                
            # Define the font
            font: Tuple[str, int, str] = ("Arial", int(16 * self.heightRatio), "bold") if move == self.game.getGameHistory().getCurrentMove() else ("Arial", int(16 * self.heightRatio))
            
            # Add the move to the scrollable frame
            ctk.CTkLabel(self.scrollFrame, text=moveText, font=font, text_color=self.settings[f"player{playerIndex+1}"]["color"]).pack(anchor="w")
            
        return True
    
    @privatemethod
    def __updateButtons__(self) -> bool:
        
        """
        Updates the state of the bomb, undo, redo, and bulb buttons.
        
        Returns:
            bool: True if the function succeeds, False otherwise.
        """
        
        # Update the bomb button
        self.__updateBombButton__()
        
        # Update the undo and redo buttons
        self.__updateUndoRedoButtons__()
        
        # Update the bulb button
        self.__updateBulbButton__()
        
        return True
    
    @privatemethod
    def __updateBombButton__(self) -> bool:
        
        """
        Updates the state of the bomb button.
        
        Returns:
            bool: True if the function succeeds, False otherwise.
        """
        
        # Get the current player
        currentPlayer: Optional[HumanGUIPlayer] = self.game.getPlayerToPlay()
        
        # Check if the current player is a human player and has power up moves
        isHuman: bool = isinstance(currentPlayer, HumanGUIPlayer)
        hasPowerUp: bool = isHuman and self.game.getPlayerPowerUpMoves(self.game.getGameState().getPlayerToPlayIndex())
        
        # Update the bomb button state
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
        
        # Get the current player
        currentPlayer: Optional[HumanGUIPlayer] = self.game.getPlayerToPlay()
        
        # Update the undo and redo buttons state
        if isinstance(currentPlayer, HumanGUIPlayer):
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
        
        # Get the current player
        currentPlayer: Optional[HumanGUIPlayer] = self.game.getPlayerToPlay()
        
        # Update the bulb button state
        if isinstance(currentPlayer, HumanGUIPlayer):
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
        
        # Toggle the bomb move state
        self.bombMove = not self.bombMove
        
        # Update the bomb button
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
        
        # Undo the last move if possible
        if not self.game.undo():
            return False
        
        # Update the board
        self.__drawBoard__()
        
        # Update the buttons
        self.__updateButtons__()
        
        # Update the turn label and player turn label
        if self.turn >= 2:
            self.turn -= 2
        else: 
            self.turn = 1
        self.__setTurnLabel__()
        
        self.__setPlayerTurn__()
        
        # Update the move history
        self.__updateMoveHistory__()
        
        # Check if the current player is an AI and play the next move with a delay of 500ms
        self.after(500, self.__checkAndPlayAi__)
        
        return True
    
    @privatemethod
    def __redo__(self) -> bool:
        
        """
        Redoes the last undone move.
        
        Returns:
            bool: True if the function succeeds, False otherwise.
        """
        
        # Redo the last undone move if possible
        if not self.game.redo():
            return False
        
        # Update the board
        self.__drawBoard__()
        
        # Update the buttons
        self.__updateButtons__()
        
        # Update the turn label and player turn label
        self.__setTurnLabel__()
        
        self.__setPlayerTurn__()
        
        # Update the move history
        self.__updateMoveHistory__()
        
        # Check if the current player is an AI and play the next move with a delay of 500ms
        self.after(500, self.__checkAndPlayAi__)
        
        return True
    
    @privatemethod
    def __advice__(self) -> bool:
        
        """
        Provides advice for the next move.
        
        Returns:
            bool: True if the function succeeds, False otherwise.
        """
        
        # Get the advice and draw the board with the advice
        move: object = self.game.getAdvice()
        move = (move.getCoordinate().getLine(), move.getCoordinate().getColumn())
        self.__drawBoard__(advice=move)
        
        # Update the bulb button state
        self.bulbButton.configure(state="disabled", fg_color="#666666", hover_color="#666666")
        
        return True
    
    def resetGame(self) -> bool:
        
        """
        Resets the game state.
        
        Returns:
            bool: True if the function succeeds, False otherwise.
        """
        
        # Reset the game state
        self.settings = None
        self.game = None
        self.board = None
        self.moveHistory = []
        self.turn = 1
        self.bombMove = False
        self.gameOutCome = None
        
        # Clear the canvas and scrollable frame
        for widget in self.scrollFrame.winfo_children():
            widget.destroy()
            
        self.gridCanvas.delete("all")
        
        # Update the buttons
        self.bombButton.configure(state="normal")
        self.bombButton.configure(fg_color="#1f6aa5", hover_color="#144870")
        
        self.redoButton.configure(state="normal")
        self.redoButton.configure(fg_color="#1f6aa5", hover_color="#144870")
        
        self.undoButton.configure(state="normal")
        self.undoButton.configure(fg_color="#1f6aa5", hover_color="#144870")
        
        self.bulbButton.configure(state="normal")
        self.bulbButton.configure(fg_color="#1f6aa5", hover_color="#144870")
        
        return True

    def startGame(self, settings: dict) -> bool:
        
        """
        Starts a new game with the given settings.
        
        Parameters:
            settings (dict): The game settings.
            
        Raises:
            TypeError: If settings is not a dictionary.

        Returns:
            bool: True if the function succeeds, False otherwise.
        """
        
        # Check if the settings is a dictionary
        if not isinstance(settings, dict):
            raise TypeError("settings must be a dictionary")
        
        # Set the game settings
        self.settings = settings
        
        # Create a new game and get the board
        self.game = TicTacToeGame(self.settings)

        self.board = self.game.getBoard()
        
        # Set board size
        self.gridCanvas.configure(width=self.cellSize * self.board.getWidth(), height=self.cellSize * self.board.getHeight())
        
        # Update the bomb button state
        if self.settings['game']['gamemode'] == 'No mod':
            self.bombButton.configure(state="disabled")
            self.bombButton.configure(fg_color="#666666", hover_color="#666666")
            
        # Draw the board
        self.__drawBoard__()
        
        # Set the turn label and player label
        self.__setPlayerTurn__()
        
        self.__setTurnLabel__()
        
        # Update the buttons
        self.__updateButtons__()
        
        # Check if the current player is an AI and play the next move with a delay of 500ms
        self.after(500, self.__checkAndPlayAi__)
        
        return True
    
    @privatemethod
    def __setPlayerTurn__(self) -> bool:
        
        """
        Sets the player turn label.
        
        Returns:
            bool: True if the function succeeds, False otherwise.
        """
        
        # Get the current player to play and set the player turn label
        currentPlayer: Optional[HumanGUIPlayer] = self.game.getPlayerToPlay()
        
        self.playerTurnLabel.configure(text=f"It's up to {currentPlayer.getName()} to play")
        
        return True 
    
    @privatemethod
    def __checkAndPlayAi__(self) -> bool:
        
        """
        Checks if the current player is an AI and plays the next move if so.
        
        Returns:
            bool: True if the function succeeds, False otherwise.
        """
        
        # Check if the current player is an AI and play the next move with a delay of 500ms
        if isinstance(self.game.getPlayerToPlay(), EasyAIPlayer) or isinstance(self.game.getPlayerToPlay(), MediumAIPlayer) or isinstance(self.game.getPlayerToPlay(), HardAIPlayer):
            self.after(500, self.__playNextAiMove__)
        
        return True
       
    @privatemethod 
    def __playNextAiMove__(self) -> bool:
        
        """
        Plays the next AI move.
        
        Returns:
            bool: True if the function succeeds, False otherwise.
        """
        
        # Play the move of the AI
        self.gameOutCome = self.game.playAiMove()
        
        # Check if the move is a bomb move and play the explosion
        move = self.game.getGameHistory().getCurrentMove()
        if isinstance(move, BombMove):
            self.__playExplosion__(move.getCoordinate().getLine(), move.getCoordinate().getColumn())

        # Update the board
        self.__drawBoard__()
        
        # Update the move history
        self.__updateMoveHistory__()
        
        # Update the buttons
        self.__updateBombButton__()
        
        self.__updateUndoRedoButtons__()
        
        self.__updateBulbButton__()
        
        # Update the turn label and player turn label
        self.__setTurnLabel__()

        self.__setPlayerTurn__()
        
        # Check if the game is finished and show the result else check if next player is an AI
        if self.gameOutCome.getGameStatus() != GameOutcomeStatus.UNFINISHED:
            
            self.__showGameResult__()
            
            return True
        
        else:
            self.__checkAndPlayAi__()
            
        return True
        
    @privatemethod
    def __setTurnLabel__(self) -> bool:
        
        """
        Sets the turn label.
        
        Returns:
            bool: True if the function succeeds, False otherwise.
        """
        
        # Increment the turn and set the turn label
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
        
        # Check if the game is finished with a victory or a draw
        if self.gameOutCome.getGameStatus() == GameOutcomeStatus.VICTORY:
            
            # Disable the buttons
            self.redoButton.configure(state="disabled")
            self.redoButton.configure(fg_color="#666666", hover_color="#666666")
            self.undoButton.configure(state="disabled")
            self.undoButton.configure(fg_color="#666666", hover_color="#666666")
            self.bulbButton.configure(state="disabled")
            self.bulbButton.configure(fg_color="#666666", hover_color="#666666")
            
            # Get the winner and set the result text
            winner = self.gameOutCome.getWinner()
            
            resultText = f"{self.settings['player1']['name']} won!" if winner == 0 else f"{self.settings['player2']['name']} won!"
            
        else:
            
            # Set the result text for a draw
            resultText = "It's a draw!"
        
        # Set the turn label on the result text and clear the player turn label
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
            
        Raises:
            TypeError: If row or col is not an integer.

        Returns:
            None
        """
        
        # Check if row and col are integers
        if not isinstance(row, int) or not isinstance(col, int):
            raise TypeError("row and col must be integers")
        
        # Get the coordinates for centering the explosion on the 3x3 
        x = col * self.cellSize + self.cellSize // 2
        y = row * self.cellSize + self.cellSize // 2
        
        # Play the explosion animation
        self.explosionLabel.place(x=x, y=y, anchor="center")
        
        # Update the explosion label with the explosion images with a delay of 100ms
        for img in self.explosionImages:
            self.explosionLabel.configure(image=img)
            self.explosionLabel.update()
            self.gridCanvas.after(100)
            
        # Hide the explosion animation
        self.explosionLabel.place_forget()
        
        # Update the board
        self.__drawBoard__()
        
        return True