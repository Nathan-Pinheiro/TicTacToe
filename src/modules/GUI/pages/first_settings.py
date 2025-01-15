import customtkinter as ctk
from modules.GUI.page import Page
from modules.GUI.components.color_selector import ColorSelector
from modules.GUI.components.symbol_selector import SymbolSelector
from modules.GUI.components.type_selector import TypeSelector
from modules.GUI.render import PageName

class FirstSettings(Page):
    
    def __init__(self, parent: ctk.CTkFrame, controller: ctk.CTk) -> None:
        super().__init__(parent, controller)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.grid_columnconfigure(4, weight=1)
        self.grid_columnconfigure(5, weight=1)
        self.grid_columnconfigure(6, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.__createWidgets__()
        return None
    
    def redirect(self) -> bool:
        names = [self.name_p1.get(), self.name_p2.get()]
        if names[0] == "" or names[0] == "Random":
            self.name_p1.focus_set()
            self.name_p1.configure(border_color="red")
            return False
        if names[1] == "" or names[0] == names[1] or names[1] == "Random":
            self.name_p2.focus_set()
            self.name_p2.configure(border_color="red")
            return False
        settings = {
            "player1": {
                "name": self.name_p1.get(),
                "color": self.color_selector_p1.get_color(),
                "symbol": self.symbol_selector_p1.get_symbol(),
                "type": self.type_selector_p1.get_type()
            },
            "player2": {
                "name": self.name_p2.get(),
                "color": self.color_selector_p2.get_color(),
                "symbol": self.symbol_selector_p2.get_symbol(),
                "type": self.type_selector_p2.get_type()
            }
        }
        self.controller.showFrame(PageName.SECONDSETTINGS, settings=settings)
        return True
    
    def __createWidgets__(self) -> None:
        width_ratio, height_ratio = self.getScreenRatio()
        
        # Title
        ctk.CTkLabel(self, text="Players settings", font=("Inter", int(72 * height_ratio), "bold"), text_color="#FFFFFF").grid(row=0, columnspan=7, pady=(int(20 * height_ratio),0))
        
        # Left text
        text = "Player 1"
        ctk.CTkLabel(self, text=text, font=("Arial", int(48 * height_ratio), "bold"), text_color="#FFFFFF", wraplength=int(600 * width_ratio)).grid(row=1, column=0, columnspan=3, pady=(int(50 * height_ratio),0), sticky="n")
        
        # Left entry
        self.name_p1 = ctk.CTkEntry(self, placeholder_text="Name...", font=("Arial", int(32 * height_ratio)), width=int(400 * width_ratio), height=int(50 * height_ratio))
        self.name_p1.grid(row=1, column=0, columnspan=3, pady=(int(140 * height_ratio), 0), sticky="n")
        self.name_p1.bind("<Key>", lambda event: self.name_p1.configure(border_color="#565b5e"))
        
        # Left color selector
        self.color_selector_p1 = ColorSelector(self)
        self.color_selector_p1.grid(row=1, column=0, pady=(int(250 * height_ratio), 0), sticky="n")
        
        # Left symbol selector
        self.symbol_selector_p1 = SymbolSelector(self, disabled_symbols=["circle"])
        self.symbol_selector_p1.grid(row=1, column=1, pady=(int(250 * height_ratio), 0), sticky="n")
        self.symbol_selector_p1.on_symbol_change = self.update_symbols_p1

        # Left type selector
        self.type_selector_p1 = TypeSelector(self)
        self.type_selector_p1.grid(row=1, column=2, pady=(int(250 * height_ratio), 0), sticky="n")
       
        # Right text
        text = "Player 2"
        ctk.CTkLabel(self, text=text, font=("Arial", int(48 * height_ratio), "bold"), text_color="#FFFFFF", wraplength=int(600 * width_ratio)).grid(row=1, column=4, columnspan=3, pady=(int(50 * height_ratio),0), sticky="n")
        
        # Right entry
        self.name_p2 = ctk.CTkEntry(self, placeholder_text="Name...", font=("Arial", int(32 * height_ratio)), width=int(400 * width_ratio), height=int(50 * height_ratio))
        self.name_p2.grid(row=1, column=4, columnspan=3, pady=(int(140 * height_ratio), 0), sticky="n")
        self.name_p2.bind("<Key>", lambda event: self.name_p2.configure(border_color="#565b5e"))
        
        # Right color selector
        self.color_selector_p2 = ColorSelector(self)
        self.color_selector_p2.grid(row=1, column=4, pady=(int(250 * height_ratio), 0), sticky="n")
        
        # Right symbol selector
        self.symbol_selector_p2 = SymbolSelector(self, symbol="circle", disabled_symbols=["cross"])
        self.symbol_selector_p2.grid(row=1, column=5, pady=(int(250 * height_ratio), 0), sticky="n")
        self.symbol_selector_p2.on_symbol_change = self.update_symbols_p2

        # Right type selector
        self.type_selector_p2 = TypeSelector(self)
        self.type_selector_p2.grid(row=1, column=6, pady=(int(250 * height_ratio), 0), sticky="n")
        
        # Line
        ctk.CTkLabel(self, text="", bg_color="#FFFFFF").grid(row=1, column=3, sticky="ns")
        
        # Next button
        ctk.CTkButton(self, text="Next", font=("Arial", int(32 * height_ratio)), command=lambda: self.redirect()).grid(row=2, columnspan=7, pady=(int(100 * height_ratio),0))
        
        return None

    def update_symbols_p1(self):
        self.symbol_selector_p2.disable_symbols([self.symbol_selector_p1.get_symbol()])

    def update_symbols_p2(self):
        self.symbol_selector_p1.disable_symbols([self.symbol_selector_p2.get_symbol()])

    def reset_settings(self) -> bool:
        width_ratio, height_ratio = self.getScreenRatio()
        
        if self.name_p1.get() != "":
            self.name_p1.delete(0, "end")
        self.color_selector_p1.set_color("#FFFFFF")
        self.symbol_selector_p1.set_symbol("cross")
        self.update_symbols_p2()
        self.type_selector_p1.set_type("human")
        
        if self.name_p2.get() != "":
            self.name_p2.delete(0, "end")
        self.color_selector_p2.set_color("#FFFFFF")
        self.symbol_selector_p2.set_symbol("circle")
        self.update_symbols_p1()
        self.type_selector_p2.set_type("easy")
        return True