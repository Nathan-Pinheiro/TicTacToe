from modules.models.board.board import Board
from modules.models.tic_tac_toe.power_ups.power_up import PowerUp

class PlayerData :
    
    def __init__(self, powerUps : list[PowerUp]):
        
        self.power_ups : list[PowerUp] = powerUps
        