from abc import ABC, abstractmethod
import customtkinter as ctk
import tkinter as tk

class Page(ctk.CTkFrame, ABC):
    
    ## Initialize the page with the given parent and controller.
    #
    # @param parent The parent frame.
    # @param controller The controller for the page.
    # @return bool True if the function succeeds, False otherwise.
    def __init__(self, parent: ctk.CTkFrame, controller: ctk.CTk) -> None:
        super().__init__(parent, border_width=0)
        self.controller = controller
        return None
    
    @abstractmethod
    def redirect(self) -> bool:
        pass
    
    def getScreenRatio(self) -> tuple:
        return (self.controller.winfo_screenwidth() / 1920, self.controller.winfo_screenheight() / 1080)