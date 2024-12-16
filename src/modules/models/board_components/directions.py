from enum import Enum

class Directions(Enum):
    
    ASCENDANT_DIAGONAL = (1, -1)
    DESCENDANT_DIAGONAL = (1, 1)
    HORIZONTAL = (0, 1)
    VERTICAL = (1, 0)