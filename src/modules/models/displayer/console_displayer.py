import os

from modules.models.board_game.board.board import Board
from modules.models.board_game.components.entity import Entity

CONSOLE_SIZE = 40
SEP = "="

def display_sep() -> None:
    
    """
    Displays a separator.
    
    Returns:
        None
    """
    
    print(SEP * CONSOLE_SIZE)
    
    return None

def display_board(board : Board) -> None:
    
    """
    Displays the board.
    
    Parameters:
        board (Board): The board to display.
        
    Returns:
        None
    """
    
    word = f"    "

    for column in range(board.getWidth()):
        word += str(column + 1) + "   "
        
    print(word.center(CONSOLE_SIZE))

    for line in range(board.getHeight()):
        
        word = f"{line + 1} | "
        
        for column in range(board.getWidth()):
            
            if(board.isCaseBlocked(line, column)) : entity_char = '#'
            else : 
                entity : Entity = board.getEntityAt(line, column)
                if(entity) : entity_char = board.getEntityAt(line, column).getName()
                else : entity_char = ' '
            
            word += entity_char + " | "
            
        print(word.center(CONSOLE_SIZE))
        
    return None
        
def ask_for_int(question : str) -> int | None:
    
    """
    Asks for an integer.
    
    Parameters:
        question (str): The question to ask.
        
    Returns:
        int: The integer entered by the user.
        None: If the user did not enter an integer.
    """
    
    response : str = input(question)
    
    if(response.isdigit()) : return int(response)
    else : return None
    
def display(value : str) -> None:
    
    """
    Displays a value.
    
    Parameters:
        value (str): The value to display.
        
    Returns:
        None
    """
    
    print(value)
    
    return None
    
def display_centered(value : str) -> None:
    
    """
    Displays a value centered.
    
    Parameters:
        value (str): The value to display.
    
    Returns:
        None
    """
    
    print(value.center(CONSOLE_SIZE))
    
    return None

def clear_screen() -> None:
    
    """
    Clears the screen.
    
    Returns:
        None
    """
    
    os.system("cls")
    
    return None
    