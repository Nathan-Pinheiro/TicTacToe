from modules.models.board_game.components.coordinate import Coordinate
from modules.models.board_game.components.entity import Entity

# ************************************************
# Class Case
# ************************************************
# ROLE : This module is representing board case
# ************************************************
# VERSION : 1.0
# AUTHOR : Nathan PINHEIRO
# DATE : 13/01/2025
# ************************************************

class Case:
    
    """
    Represents a case of a board
    """
    
    def __init__(self, coordinate : Coordinate, entity : Entity = None, isBlocked : bool = False) -> None:
        
        """
        Constructor for the Case class.

        Parameters:
            coordinate (Coordinate): The coordinate of the case.
            entity (Entity, optional): The entity on the case. Defaults to None.
            isBlocked (boolean, default => False): The blocked state of a case 
            
        Returns:
            None
        """
        
        self.__entity__ = entity
        self.__coordinate__ = coordinate
        self.__isBlocked__ = isBlocked
        
        return None
        
    def getCoordinate(self) -> Coordinate :
        
        """
        Get the coordinate of the case.

        Returns:
            int: The coordinate of the case.
        """
        
        return self.__coordinate__
    
    def getEntity(self) -> Entity :
        
        """
        Get the entity on the case.

        Returns:
            entity (Entity): The entity on the case.
        """
        
        return self.__entity__
    
    def setEntity(self, entity : Entity) -> None :
        
        """
        Set the entity on the case.

        Parameters:
            entity (Entity): The entity on the case.

        Returns:
            None
        """
        
        self.__entity__ = entity
        
        return None
    
    def isBlocked(self) -> None:
        
        """
        Get the blocked state of the case.

        Returns:
            bool: The blocked state of the case
        """
        
        return self.__isBlocked__

    def setIsBlocked(self, isBlocked : bool) -> None:
        
        """
        Set the blocked state of the case.

        Parameters:
            isBlocked (bool): The blocked state.

        Returns:
            None
        """
        self.__isBlocked__ = isBlocked
        
        return None
    
    def isAvaillable(self) -> bool :
        
        """
        Get the availlable state of the case.

        Returns:
            bool: The availlable state of the case.
        """
        
        isCaseBlocked : bool = self.isBlocked()
        isCaseEmpty : bool = self.getEntity() == None

        if(isCaseBlocked or not isCaseEmpty) : return False
        else : return True