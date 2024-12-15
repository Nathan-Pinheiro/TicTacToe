import os

from modules.models.board.board import Board

CONSOLE_SIZE = 30
SEP = "="


def display_sep():
    print(SEP * CONSOLE_SIZE)

def display_board(board : Board):
    
    for line in range(board.getHeight()):
        
        word = f"{line + 1} | "
        
        for column in range(board.getWidth()):
            
            if(board.getCase(line, column).isBlocked()) : entity_char = "#"
            elif(board.getCase(line, column).getEntity()) : entity_char = board.getCase(line, column).getEntity().getName()
            else : entity_char = " "
            
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
    