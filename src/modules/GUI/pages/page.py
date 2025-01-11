## Interface

"""
Page Module

This module provides an abstract base class for all pages in the Tic Tac Toe game using the tkinter library.

Classes:
    Page: An abstract base class representing a page in the Tic Tac Toe game.

Functions:
    __init__(self, parent: tk.Frame, controller: tk.Tk) -> bool:
        Initialize the page with the given parent and controller.
        
    show(self) -> bool:
        Show the page.
        
    hide(self) -> bool:
        Hide the page.
"""

# ---------------------------------------------------------------------------------------------------- #

## Implementation

# Import #
from abc import ABC, abstractmethod
import tkinter as tk
from tkinter import ttk

class Page(ttk.Frame, ABC):
    ## Initialize the page with the given parent and controller.
    #
    # @param parent The parent frame.
    # @param controller The controller for the page.
    # @return bool True if the function succeeds, False otherwise.
    def __init__(self, parent: tk.Frame, controller: tk.Tk) -> None:
        super().__init__(parent)
        self.controller = controller
        return None

    ## Show the page.
    #
    # @return bool True if the function succeeds, False otherwise.
    @abstractmethod
    def show(self) -> bool:
        pass

    ## Hide the page.
    #
    # @return bool True if the function succeeds, False otherwise.
    @abstractmethod
    def hide(self) -> bool:
        pass
