from modules.models.board_game.components.entity import Entity

class Square(Entity):
    
    """
    A class that represents a square entity.
    """
    
    def __init__(self) -> None:
        
        """
        Constructor for the Square class.
        
        Returns:
            None
        """
        
        # Call the parent constructor
        super().__init__("▢")
        
        return None