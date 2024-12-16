from modules.models.board_components.entity import Entity

class Circle(Entity):
    
    def __init__(self):
        """Constructor for the Circle class."""
        super().__init__("O", None)