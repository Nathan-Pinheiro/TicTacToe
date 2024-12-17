from modules.models.board_components.entity import Entity
from modules.models.tic_tac_toe.moves.power_up_move import PowerUpMove
from typing import Type

class PlayerData :
    
    def __init__(self, entity : Entity, powerUpsMoves : list[Type[PowerUpMove]]) :
        
        self.__entity__ = entity
        self.__powerUpsMoves__ : list[Type[PowerUpMove]] = powerUpsMoves
        
    def getEntity(self) -> Entity:
        
        return self.__entity__
    
    def getPowerUpMoves(self) -> list[Type[PowerUpMove]]:
        
        return self.__powerUpsMoves__
    