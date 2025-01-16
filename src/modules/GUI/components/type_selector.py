import customtkinter as ctk
from CTkColorPicker import *
import tkinter as tk
from PIL import Image, ImageTk

class TypeSelector(ctk.CTkFrame):

    def __init__(self, parent, type="human", **kwargs):
        super().__init__(parent, **kwargs)
        self.types = ["human", "easy"]
        if type not in self.types:
            type = self.types[0]
        self.type = type
        self.on_type_change = None
        self.__createWidgets__()

    def __createWidgets__(self):
        self.canvas = tk.Canvas(self, width=132, height=132, bg="#333333", borderwidth=0, highlightthickness=0)
        self.canvas.grid(row=0, column=0, padx=10, pady=10)
        self.load_images()
        self.draw_type()
        self.select_button = ctk.CTkButton(self, text="Select Type", command=self.select_type)
        self.select_button.grid(row=1, column=0, padx=10, pady=10)

    def load_images(self):
        self.images = {
            "human": ImageTk.PhotoImage(Image.open("./assets/Human.png").resize((100, 100))),
            "easy": ImageTk.PhotoImage(Image.open("./assets/Robot.png").resize((100, 100)))
        }

    def draw_type(self):
        self.canvas.delete("all")
        self.canvas.create_image(66, 66, image=self.images[self.type])  # Center the image

    def select_type(self):
        current_index = self.types.index(self.type)
        next_index = (current_index + 1) % len(self.types)
        self.type = self.types[next_index]
        self.draw_type()
        if self.on_type_change:
            self.on_type_change()

    def get_type(self):
        return self.type
    
    def set_type(self, type):
        self.type = type
        self.draw_type()