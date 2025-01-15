import customtkinter as ctk
from modules.GUI.page import Page
from modules.GUI.render import PageName
from PIL import Image
import tkinter as tk
from modules.GUI.components.grid import drawGrid

from modules.models.tic_tac_toe.tic_tac_toe_game import TicTacToeGame

class Game(Page):
    def __init__(self, parent: ctk.CTkFrame, controller: ctk.CTk) -> None:
        super().__init__(parent, controller)
        self.settings = None
        self.game = None
        self.cellSize = 100
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
        
        # Draw the grid on the canvas
        # TestBoard place randomly X, O, # and space on the grid
        testBoard = [
            ["X", "O", "#", "", "X", "O", "#"],
            ["O", "#", "", "X", "O", "#", ""],
            ["#", "", "X", "O", "#", "", "X"],
            ["", "X", "O", "#", "", "X", "O"],
            ["X", "O", "#", "", "X", "O", "#"],
            ["O", "#", "", "X", "O", "#", ""],
            ["#", "", "X", "O", "#", "", "X"] ]
        drawGrid(self.grid_canvas, self.cellSize * nbCellWidth, self.cellSize * nbCellHeight, self.cellSize, testBoard)
        
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
        self.scrollFrame .grid(row=1, column=0, columnspan=4, padx=int(60 * width_ratio), sticky="nsew")
        
        # Bomb button + undo button + redo button + help button
        bomb_image = ctk.CTkImage(   
                            light_image=Image.open("./src/assets/Bomb.png"),
                            dark_image=Image.open("./src/assets/Bomb.png"),
                            size=(int(40 * width_ratio), int(40 * height_ratio))
                                )    
        bulb_image = ctk.CTkImage(
                            light_image=Image.open("./src/assets/Bulb.png"),
                            dark_image=Image.open("./src/assets/Bulb.png"),
                            size=(int(24 * width_ratio), int(40 * height_ratio))
                                )
        undo_image = ctk.CTkImage(
                            light_image=Image.open("./src/assets/Undo.png"),
                            dark_image=Image.open("./src/assets/Undo.png"),
                            size=(int(12 * width_ratio), int(24 * height_ratio))
                                )
        redo_image = ctk.CTkImage(
                            light_image=Image.open("./src/assets/Redo.png"),
                            dark_image=Image.open("./src/assets/Redo.png"),
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
    
    def __handle_click__(self, event) -> bool:
        try:
            col = event.x // self.cellSize
            row = event.y // self.cellSize
            print(f"Clicked on cell {chr(65 + col)}, {row + 1}")
        
        except Exception as e:
            print(f"Error: {e}")
            
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
        return True
    
    def start_game(self, settings) -> bool:
        self.settings = settings
        print(f"Starting game with settings: {settings}")
        self.game = TicTacToeGame(self.settings)
        return True