from modules.models.tic_tac_toe.power_ups.power_up import PowerUp
from modules.models.board_components.board import Board

class Bomb(PowerUp) :
    
    def __init__(self) -> None:
        super()
        return None
        
    def use(self, board : Board) -> None :
        print("Use bomb")
        return None