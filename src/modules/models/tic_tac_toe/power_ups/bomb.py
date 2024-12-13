from modules.models.tic_tac_toe.power_ups.power_up import PowerUp

class Bomb(PowerUp) :
    
    def __init__(self) -> None:
        super()
        return None
        
    def use(self, board) -> None :
        print("Use bomb")
        return None