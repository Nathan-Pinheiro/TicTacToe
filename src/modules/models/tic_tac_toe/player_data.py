from modules.models.entities.entity import Entity
from modules.models.tic_tac_toe.power_ups.power_up import PowerUp

class PlayerData :
    
    def __init__(self, entity : Entity, powerUps : list[PowerUp]) :
        
        self.__entity__ = entity
        self.__power_ups__ : list[PowerUp] = powerUps
        
    def getEntity(self) -> Entity:
        
        return self.__entity__
    
    def getPowerUps(self) -> list[PowerUp]:
        
        return self.__power_ups__
    