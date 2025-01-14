from modules.models.board_game.components.entity import Entity

class Cross(Entity):
    
    def __init__(self):
        """Constructor for the Cross class."""
        super().__init__("X", None)