import customtkinter as ctk
from CTkColorPicker import *

class ColorSelector(ctk.CTkFrame):
    def __init__(self, parent, color="#FFFFFF", **kwargs):
        super().__init__(parent, **kwargs)
        self.color = color
        self.__createWidgets__()

    def __createWidgets__(self):
        self.color_display = ctk.CTkLabel(self, text="", width=132, height=132, bg_color=self.color)
        self.color_display.grid(row=0, column=0, padx=10, pady=10)

        self.select_button = ctk.CTkButton(self, text="Select Color", command=self.select_color)
        self.select_button.grid(row=1, column=0, padx=10, pady=10)

    def select_color(self):
        pick_color = AskColor(title="Choose color")
        color_code = pick_color.get()
        if color_code:
            self.color = color_code
            self.color_display.configure(bg_color=self.color)
            
    def get_color(self):
        return self.color
    
    def set_color(self, color):
        self.color = color
        self.color_display.configure(bg_color=self.color)