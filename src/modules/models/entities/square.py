from modules.models.board_components.entity import Entity

class Square(Entity):
    
    def __init__(self):
        """Constructor for the Square class."""
        super().__init__("▢", None)