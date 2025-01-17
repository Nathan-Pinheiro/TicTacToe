from modules.models.board_game.components.entity import Entity

class Star(Entity):
    
    def __init__(self):
        """Constructor for the Star class."""
        super().__init__("★", None)