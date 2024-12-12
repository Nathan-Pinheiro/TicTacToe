import tkinter as tk
from tkinter import ttk

# Class #
class App(tk.Tk):
    def __init__(self, title : str, firstPage : str, geometry : str | None = None) -> None:
        """Constructor for the App class.
        
        Args:
            title (str): The title of the application.
            geometry (str): The geometry of the application.
            firstPage (str): The first page to display.
            
        Returns:
            None
        """
        
        super().__init__()
        self.title(title)
        if geometry is not None : self.geometry(geometry)
        else : 
            width = self.winfo_screenwidth()
            height = self.winfo_screenheight()
            self.geometry(f"{width}x{height}")
            self.attributes("-fullscreen", True)
        self.frames = {}

        container = ttk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.create_frames(container)
        self.show_frame(firstPage)
        
        return None

    def create_frames(self, container : ttk.Frame) -> None:
        for F in (MainMenu, GameScreen, Settings):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            
        return None

    def show_frame(self, page_name : str) -> None:
        frame = self.frames[page_name]
        frame.tkraise()
        
        return None

class MainMenu(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        label = ttk.Label(self, text="Main Menu")
        label.pack(side="top", fill="x", pady=10)

        start_button = ttk.Button(self, text="Start Game", command=lambda: controller.show_frame("GameScreen"))
        start_button.pack()

        settings_button = ttk.Button(self, text="Settings", command=lambda: controller.show_frame("Settings"))
        settings_button.pack()

class GameScreen(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        label = ttk.Label(self, text="Game Screen")
        label.pack(side="top", fill="x", pady=10)

        back_button = ttk.Button(self, text="Back to Main Menu", command=lambda: controller.show_frame("MainMenu"))
        back_button.pack()

class Settings(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        label = ttk.Label(self, text="Settings")
        label.pack(side="top", fill="x", pady=10)

        back_button = ttk.Button(self, text="Back to Main Menu", command=lambda: controller.show_frame("MainMenu"))
        back_button.pack()

if __name__ == "__main__":
    app = App("TicTacToe", "MainMenu")
    app.mainloop()