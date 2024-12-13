import os

from modules.models.board.board import Board

def display_board(board : Board):
    
    for line in range(board.getHeight()):
        
        print("|", end=" ")
        
        for column in range(board.getWidth()):
            
            entity_char : str
            if(board.getCase(line, column).isBlocked()) : entity_char = "#"
            elif(board.getCase(line, column).getEntity()) : entity_char = " "
            else : entity_char = " "
            
            print(entity_char, end=" | ")
            
        print()
        
def ask_for_int(question : str):
    
    response : str = input(question)
    
    if(response.isdigit()) : return int(response)
    else : return None
    
def display(value : str):
    print(value)

def clear_screen():
    os.system("cls")
    