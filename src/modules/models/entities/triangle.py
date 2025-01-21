from modules.models.board_game.components.entity import Entity

class Triangle(Entity):
    
    """
    A class that represents a triangle entity.
    """
    
    def __init__(self) -> None:
        
        """
        Constructor for the Triangle class.
        
        Returns:
            None
        """
        
        super().__init__("△", None)
        
        return None