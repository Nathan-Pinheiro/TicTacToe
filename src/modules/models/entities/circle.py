from modules.models.board_game.components.entity import Entity

class Circle(Entity):
    
    """
    A class that represent a circle entity
    """
    
    def __init__(self) -> None:
        
        """
        Constructor for the Circle class.
        
        Returns:
            None
        """
        
        super().__init__("O", None)
        
        return None