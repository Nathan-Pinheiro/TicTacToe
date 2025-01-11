from modules.utils.decorator import privatemethod
from modules.models.board_components.boards.optimized_board_components.bitboard import BitBoard

import numpy as np

class NumpyBitBoard(BitBoard) :
    
    def __init__(self, width : int, height : int) -> None:
        
        super().__init__(width, height)

        self.__bits__ : np.ndarray = np.zeros((height, width), dtype=int)
        
        self.__generateBoardQuadrantMasks__()
    
    def __getBitPosition__(self, line: int, column: int) -> int:
        
        """
        Convert (row, col) to a bit index.
        
        Args:
            line (int): The line of the bit.
            column (int): The column of the bit.
            
        Returns:
            position (int): the position index of the bit
        """
        
        return line * self.__width__ + column

    def __generateBoardQuadrantMasks__(self) -> None :
        
        """
        This method allow initializing masks foreach part of board. (upper left, upper right, lower left, lower right).
        This will then be usefull to hash the BitBoard, having a hash code that have the same hash for symetrical boards.
        """
        
        self.__upperLeftMask__ : np.ndarray = np.zeros((self.__height__, self.__width__), dtype=int)
        self.__upperRighMask__ : np.ndarray = np.zeros((self.__height__, self.__width__), dtype=int)
        self.__lowerLeftMask__ : np.ndarray = np.zeros((self.__height__, self.__width__), dtype=int)
        self.__lowerRightMask__ : np.ndarray = np.zeros((self.__height__, self.__width__), dtype=int)
        
        centerLine : float = (self.__height__ - 1) / 2
        centerColumn : float = (self.__width__ - 1) / 2

        for line in range(0, self.__height__) :
            for column in range(0, self.__width__) :
                
                bitIndex = self.__getBitPosition__(line, column)
                if(line <= centerLine and column <= centerColumn) : self.__upperLeftMask__[line][column] = 1
                if(line <= centerLine and column >= centerColumn) : self.__upperRighMask__[line][column] = 1
                if(line >= centerLine and column <= centerColumn) : self.__lowerLeftMask__[line][column] = 1
                if(line >= centerLine and column >= centerColumn) : self.__lowerRightMask__[line][column] = 1

    def __convertBitArrayToInt__(self, bitBoard : np.ndarray) -> int :
        
        flat_bitboard = bitBoard.ravel() 
        bitboard_int = np.dot(flat_bitboard, 1 << np.arange(flat_bitboard.size))
        
        return bitboard_int
    
    def __convertIntToBitArray__(self, bitboard_int: int) -> np.ndarray:
        
        bitboard = np.zeros((self.__height__, self.__width__), dtype=int)
        
        for line in range(self.__height__): 
            for column in range(self.__width__):
                bitboard[line][column] = 1 if 1 << line * self.__width__ + column & bitboard_int else 0
    
        return bitboard

    def getValue(self) -> int :

        """
        Return the bitboard value
        """

        return self.__convertBitArrayToInt__(self.__bits__)
    
    def applyOr(self, value : int) -> None :
        
        """
        Apply OR bitwise operation to the bitboard with a int mask
        """             

        self.__bits__ |= self.__convertIntToBitArray__(value)

        return None
    
    def applyAnd(self, value : int) -> None :
        
        """
        Apply AND bitwise operation to the bitboard with a int mask
        """   

        self.__bits__ &= self.__convertIntToBitArray__(value)

        return None
    
    def __getRotatedBitBoardBy90Degree__(self, mask: np.ndarray = None) -> np.ndarray:
        
        """
        Rotate the given bitboard value & the given mask by 90 degrees.
        """

        bits : np.ndarray
        if(mask is not None) : bits = self.__bits__ & mask
        else : bits = self.__bits__

        return np.rot90(bits)

    def __getRotatedBitBoardBy180Degree__(self, mask: np.ndarray = None) -> np.ndarray:
        
        """
        Rotate the given bitboard value & the given mask by 180 degrees.
        """

        bits : np.ndarray
        if(mask is not None) : bits = self.__bits__ & mask
        else : bits = self.__bits__
        
        return np.rot90(bits, k=2)

    def __getRotatedBitBoardBy270Degree__(self, mask: np.ndarray = None) -> np.ndarray:
        
        """
        Rotate the given bitboard value & the given mask by 270 degrees.
        """

        bits : np.ndarray
        if(mask is not None) : bits = self.__bits__ & mask
        else : bits = self.__bits__

        return np.rot90(bits, k=3)
    
    def __getFlipVerticalyBitBoard__(self, mask: np.ndarray = None) -> np.ndarray:
        
        """
        Flip verticaly the given bitboard value & the given mask.
        """

        bits : np.ndarray
        if(mask is not None) : bits = self.__bits__ & mask
        else : bits = self.__bits__

        return np.flipud(bits)
    
    def __getFlipHorizontalyBitBoard__(self, mask: np.ndarray = None) -> np.ndarray:
        
        """
        Flip verticaly the given bitboard value & the given mask.
        """

        bits : np.ndarray
        if(mask is not None) : bits = self.__bits__ & mask
        else : bits = self.__bits__

        return np.fliplr(bits)
    
    def __hash__(self) -> int:

        upperLeftHash : int = hash((self.__bits__ & self.__upperLeftMask__).tobytes())
        upperRightash : int = hash(self.__getRotatedBitBoardBy90Degree__(self.__upperRighMask__).tobytes())
        lowerLeftHash : int = hash(self.__getRotatedBitBoardBy180Degree__(self.__lowerRightMask__).tobytes())
        lowerRightHash : int = hash(self.__getRotatedBitBoardBy270Degree__(self.__lowerLeftMask__).tobytes())

        return hash(upperLeftHash + upperRightash + lowerLeftHash + lowerRightHash)

    # def __hash__(self) -> int:

    #     upperLeftHash : int = hash((self.__bits__ & self.__upperLeftMask__).tobytes())
    #     upperRightash : int = hash(self.__getRotatedBitBoardBy90Degree__(self.__upperRighMask__).tobytes())
    #     lowerLeftHash : int = hash(self.__getRotatedBitBoardBy180Degree__(self.__lowerRightMask__).tobytes())
    #     lowerRightHash : int = hash(self.__getRotatedBitBoardBy270Degree__(self.__lowerLeftMask__).tobytes())

    #     normalHash : int = hash(self.__bits__.tobytes())
    #     verticalyFlippedHash : int = hash(np.fliplr(self.__bits__).tobytes())
    #     horizontallyFlippedHash : int = hash(np.flipud(self.__bits__).tobytes())

    #     return hash(upperLeftHash + upperRightash + lowerLeftHash + lowerRightHash + normalHash + verticalyFlippedHash + horizontallyFlippedHash)