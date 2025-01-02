from modules.utils.decorator import private_method
from modules.models.board_components.boards.optimized_board_components.bitboard import BitBoard

class SimpleBitBoard(BitBoard) :
    
    def __init__(self, width : int, height : int) -> None:
        
        super().__init__(width, height)

        self.__value__ : int = 0
        
        self.__generateBoardQuadrantMasks__()
    
    def __getBitPosition__(self, line: int, column: int) -> int:
        
        """Convert (row, col) to a bit index."""
        
        return line * self.__width__ + column

    def __generateBoardQuadrantMasks__(self) -> int :
        
        """
        This method allow initializing masks foreach part of board. (upper left, upper right, lower left, lower right).
        This will then be usefull to hash the BitBoard, having a hash code that have the same hash for symetrical boards.
        """
        
        self.__upperLeftMask__ : int = 0
        self.__upperRighMask__ : int = 0
        self.__lowerLeftMask__ : int = 0
        self.__lowerRightMask__ : int = 0
        
        centerLine : float = self.__height__ / 2
        centerColumn : float = self.__width__ / 2
        
        for line in range(0, self.__height__) :
            for column in range(0, self.__width__) :
                
                bitIndex = self.__getBitPosition__(line, column)
                if(line <= centerLine and column <= centerColumn) : self.__upperLeftMask__ |= (1 << bitIndex)
                if(line <= centerLine and column >= centerColumn) : self.__upperRighMask__ |= (1 << bitIndex)
                if(line >= centerLine and column <= centerColumn) : self.__lowerLeftMask__ |= (1 << bitIndex)
                if(line >= centerLine and column >= centerColumn) : self.__lowerRightMask__ |= (1 << bitIndex)

    def getValue(self) -> int :
        return self.__value__
    
    def applyOr(self, value : int) -> None :
        self.__value__ |= value
        return None
    
    def applyAnd(self, value : int) -> None :
        self.__value__ &= value
        return None
    
    def __getRotatedBitBoardBy90Degree__(self, mask: int = 0) -> int:
        
        """
        Rotate the given bitboard value (or self value if mask=0) by 90 degrees.
        """
        
        value : int = self.__value__ & mask
        
        pass

    def __getRotatedBitBoardBy180Degree__(self, mask: int = 0) -> int:
        
        """
        Rotate the given bitboard value (or self value if mask=0) by 180 degrees.
        """
        
        value : int = self.__value__ & mask
        
        pass

    def __getRotatedBitBoardBy270Degree__(self, mask: int = 0) -> int:
        
        """
        Rotate the given bitboard value (or self value if mask=0) by 270 degrees.
        """
        
        value : int = self.__value__ & mask

        pass

    
    def __hash__(self) -> int:

        upperLeftHash : int = hash(self.applyAnd(self.__upperLeftMask__))
        upperRightash : int = hash(self.__getRotatedBitBoardBy90Degree__(self.__upperRighMask__))
        lowerLeftHash : int = hash(self.__getRotatedBitBoardBy180Degree__(self.__lowerRightMask__))
        lowerRightHash : int = hash(self.__getRotatedBitBoardBy270Degree__(self.__lowerLeftMask__))

        return hash(upperLeftHash + upperRightash + lowerLeftHash + lowerRightHash)