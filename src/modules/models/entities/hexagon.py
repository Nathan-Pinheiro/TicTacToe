from modules.models.board_game.components.entity import Entity

class Hexagon(Entity):
    
    """
    A class that represents a hexagon entity.
    """
    
    def __init__(self) -> None:
        
        """
        Constructor for the Hexagon class.
        
        Returns:
            None
        """
        
        # Call the parent constructor
        super().__init__("⬡")
        
        return None