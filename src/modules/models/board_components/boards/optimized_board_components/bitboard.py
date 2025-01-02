class BitBoard :
    
    def __init__(self, width : int, height : int) -> None:
        
        """
        Constructor for the Board class.

        Args:
            width (int): The width of the board.
            height (int): The height of the board.
            
        Returns:
            None
        """
        
        assert(width * height <= 64)
        
        self.__width__ = width
        self.__height__ = height
    
    def getValue(self) -> int :
        pass
    
    def applyOr(self, value : int) -> None :
        pass
    
    def applyAnd(self, value : int) -> None :
        pass
    
    def __hash__(self) -> int:
        pass