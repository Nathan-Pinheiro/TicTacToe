import customtkinter as ctk
from modules.GUI.page import Page
from modules.GUI.components.int_selector import IntSelector
from modules.GUI.render import PageName

class SecondSettings(Page):
    
    def __init__(self, parent: ctk.CTkFrame, controller: ctk.CTk) -> None:
        super().__init__(parent, controller)
        self.settings = None
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.grid_columnconfigure(4, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.__createWidgets__()
        return None
    
    def redirect(self, pageName=None) -> bool:
        # On ajoute aux settings les valeurs des champs
        settings = self.settings
        settings["board"] = {
            "width": self.width_selector.get_value(),
            "height": self.height_selector.get_value(),
            "shape": self.shape_var.get()
        }
        settings["game"] = {
            "nbSymbols": self.nbSymbols_selector.get_value(),
            "alignToWin": self.align_to_win_var.get(),
            "startingPlayer": self.starting_player_var.get(),
            "gamemode": self.gamemode_var.get()
        }
        self.controller.showFrame(pageName=pageName, settings=settings)
        return True

    def setValues(self, settings) -> bool:
        self.settings = settings
        self.starting_player_combobox.configure(values=[settings["player1"]["name"], settings["player2"]["name"], "Random"])
        self.starting_player_var.set(settings["player1"]["name"])
        return True
    
    def __createWidgets__(self) -> None:
        width_ratio, height_ratio = self.getScreenRatio()
        
        # Title
        ctk.CTkLabel(self, text="Game settings", font=("Inter", int(72 * height_ratio), "bold"), text_color="#FFFFFF").grid(row=0, columnspan=5, pady=(int(20 * height_ratio),0))
        
        # Left text
        text = "Board options"
        ctk.CTkLabel(self, text=text, font=("Arial", int(48 * height_ratio), "bold"), text_color="#FFFFFF", wraplength=int(600 * width_ratio), width=int(600 * width_ratio)).grid(row=1, column=0, columnspan=2, pady=(int(50 * height_ratio),0), sticky="n")
       
        # Right text
        text = "Miscellaneous options"
        ctk.CTkLabel(self, text=text, font=("Arial", int(48 * height_ratio), "bold"), text_color="#FFFFFF", wraplength=int(600 * width_ratio), width=int(600 * width_ratio)).grid(row=1, column=3, columnspan=2, pady=(int(50 * height_ratio),0), sticky="n")
        
        # Width size selector
        ctk.CTkLabel(self, text="Width :", font=("Arial", int(32 * height_ratio), "bold"), text_color="#FFFFFF").grid(row=1, column=0, pady=(int(180 * height_ratio),0), sticky="n")
        self.width_selector = IntSelector(self, min_value=3, max_value=7, initial_value=3, width=int(50 * width_ratio), height=int(50 * height_ratio))
        self.width_selector.grid(row=1, column=1, pady=(int(160 * height_ratio),0), sticky="n")
        
        # Height size selector
        ctk.CTkLabel(self, text="Height :", font=("Arial", int(32 * height_ratio), "bold"), text_color="#FFFFFF").grid(row=1, column=0, pady=(int(280 * height_ratio),0), sticky="n")
        self.height_selector = IntSelector(self, min_value=3, max_value=7, initial_value=3, width=int(50 * width_ratio), height=int(50 * height_ratio))
        self.height_selector.grid(row=1, column=1, pady=(int(260 * height_ratio),0), sticky="n")
        
        # Combobox for shape
        self.shape_var = ctk.StringVar(value="No special shape")
        ctk.CTkComboBox(self, values=["No special shape", "Pyramidal", "Circular", "Diamond", 'Random'], variable=self.shape_var).grid(row=1, column=0, columnspan=2, pady=(int(380 * height_ratio),0), sticky="n")
        self.shape_var.set("No special shape")
        
        # Symbols to align selector
        ctk.CTkLabel(self, text="Symbols to align :", font=("Arial", int(32 * height_ratio), "bold"), text_color="#FFFFFF").grid(row=1, column=3, pady=(int(180 * height_ratio),0), sticky="n")
        self.nbSymbols_selector = IntSelector(self, min_value=3, max_value=7, initial_value=3, width=int(50 * width_ratio), height=int(50 * height_ratio))
        self.nbSymbols_selector.grid(row=1, column=4, pady=(int(160 * height_ratio),0), sticky="n")
        
        # Checkbox for align to win condition
        self.align_to_win_var = ctk.BooleanVar(value=True)
        ctk.CTkLabel(self, text="Align to win :", font=("Arial", int(32 * height_ratio), "bold"), text_color="#FFFFFF").grid(row=1, column=3, columnspan=2, pady=(int(10 * height_ratio),0), padx=(int(300 * width_ratio),0), sticky="w")
        self.align_to_win_selector = ctk.CTkCheckBox(self, text="", variable=self.align_to_win_var, onvalue=True, offvalue=False)
        self.align_to_win_selector.grid(row=1, column=3, columnspan=2, pady=(int(10 * height_ratio),0), padx=(0, int(250 * width_ratio)), sticky="e")
        
        # Combobox for starting player, valeus will be initialized in setValues
        self.starting_player_var = ctk.StringVar(value="Nan")
        self.starting_player_combobox = ctk.CTkComboBox(self, values=["Nan"], variable=self.starting_player_var)
        self.starting_player_combobox.grid(row=1, column=3, columnspan=2, pady=(int(460 * height_ratio),0), sticky="n")
        self.starting_player_var.set("Nan")
        
        # Combobox for gamemode
        self.gamemode_var = ctk.StringVar(value="No mod")
        ctk.CTkComboBox(self, values=["No mod", "Bomb mod"], variable=self.gamemode_var).grid(row=1, column=3, columnspan=2, pady=(int(520 * height_ratio),0), sticky="n")
        self.gamemode_var.set("No mod")
        
        # Line
        ctk.CTkLabel(self, text="", bg_color="#FFFFFF").grid(row=1, column=2, sticky="ns")
        
        # Back button
        ctk.CTkButton(self, text="Back", font=("Arial", int(32 * height_ratio)), command=lambda: self.redirect(pageName=PageName.FIRSTSETTINGS)).grid(row=2, column=0, columnspan=2, pady=(int(100 * height_ratio),0), sticky="e")
        
        # Next button
        ctk.CTkButton(self, text="Next", font=("Arial", int(32 * height_ratio)), command=lambda: self.redirect(pageName=PageName.GAME)).grid(row=2, column=3, columnspan=2, pady=(int(100 * height_ratio),0), sticky="w")
        
        return None
    
    def reset_settings(self) -> bool:
        self.width_selector.set_value(3)
        self.height_selector.set_value(3)
        self.shape_var.set("No special shape")
        self.nbSymbols_selector.set_value(3)
        self.align_to_win_var.set(True)
        self.starting_player_combobox.configure(values=["Nan"])
        self.starting_player_var.set("Nan")
        self.gamemode_var.set("No mod")
        return True