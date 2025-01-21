from modules.models.board_game.components.entity import Entity

class Cross(Entity):
    
    """
    A class that represents a cross entity.
    """
    
    def __init__(self) -> None:
        
        """
        Constructor for the Cross class.
        
        Returns:
            None
        """
        
        super().__init__("X", None)
        
        return None