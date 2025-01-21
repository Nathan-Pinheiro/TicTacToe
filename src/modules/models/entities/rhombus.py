from modules.models.board_game.components.entity import Entity

class Rhombus(Entity):
    
    """
    A class that represents a rhombus entity.
    """
    
    def __init__(self) -> None:
        
        """
        Constructor for the Rhombus class.
        
        Returns:
            None
        """
        
        super().__init__("◊", None)
        
        return None