import os

from modules.models.board_components.boards.simple_board import SimpleBoard
from modules.models.board_components.entity import Entity

CONSOLE_SIZE = 40
SEP = "="

def display_sep():
    print(SEP * CONSOLE_SIZE)

def display_board(board : SimpleBoard):
    
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
        
def ask_for_int(question : str):
    
    response : str = input(question)
    
    if(response.isdigit()) : return int(response)
    else : return None
    
def display(value : str):
    print(value)
    
def display_centered(value : str):
    print(value.center(CONSOLE_SIZE))

def clear_screen():
    os.system("cls")
    