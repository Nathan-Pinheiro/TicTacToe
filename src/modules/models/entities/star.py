from modules.models.board_game.components.entity import Entity

class Star(Entity):
    
    """
    A class that represents a star entity.
    """
    
    def __init__(self) -> None:
        
        """
        Constructor for the Star class.
        
        Returns:
            None
        """
        
        # Call the parent constructor
        super().__init__("★")
        
        return None