import os

from modules.models.board_game.board.board import Board
from modules.models.board_game.components.entity import Entity

CONSOLE_SIZE = 40
SEP = "="

def display_sep() -> bool:
    
    """
    Displays a separator.
    
    Returns:
        bool: True if the function succeeds.   
    """
    
    # Display the separator
    print(SEP * CONSOLE_SIZE)
    
    return True

def display_board(board : Board) -> bool:
    
    """
    Displays the board.
    
    Parameters:
        board (Board): The board to display.
        
    Raises:
        TypeError: If board is not a Board instance.
        
    Returns:
        bool: True if the function succeeds.
    """
    
    # Check if board is a Board instance
    if not isinstance(board, Board): 
        raise TypeError("board must be a Board instance")
    
    # Display the board
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
        
    return True
        
def ask_for_int(question : str) -> int | None:
    
    """
    Asks for an integer.
    
    Parameters:
        question (str): The question to ask.
        
    Raises:
        TypeError: If question is not a string.
        
    Returns:
        int: The integer entered by the user.
        None: If the user did not enter an integer.
    """
    
    # Check if question is a string
    if not isinstance(question, str): 
        raise TypeError("question must be a string")
    
    # Ask for an integer
    response : str = input(question)
    
    # Check if the response is an integer and return it else return None
    if(response.isdigit()) : return int(response)
    else : return None
    
def display(value : str) -> bool:
    
    """
    Displays a value.
    
    Parameters:
        value (str): The value to display.
        
    Raises:
        TypeError: If value is not a string.
        
    Returns:
        bool: True if the function succeeds.
    """
    
    # Check if value is a string
    if not isinstance(value, str): 
        raise TypeError("value must be a string")
    
    # Display the value
    print(value)
    
    return True
    
def display_centered(value : str) -> bool:
    
    """
    Displays a value centered.
    
    Parameters:
        value (str): The value to display.
        
    Raises:
        TypeError: If value is not a string.
    
    Returns:
        bool: True if the function succeeds.
    """
    
    # Check if value is a string
    if not isinstance(value, str): 
        raise TypeError("value must be a string")
    
    # Display the value centered
    print(value.center(CONSOLE_SIZE))
    
    return True

def clear_screen() -> bool:
    
    """
    Clears the screen.
    
    Returns:
        bool: True if the function succeeds.
    """
    
    os.system("cls")
    
    return True
    