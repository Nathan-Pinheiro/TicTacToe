from modules.models.board_game.board.board import Board
from modules.models.board_game.components.entity import Entity
from modules.models.board_game.board.components.optimized_board_components.bitboard import BitBoard
from modules.models.board_game.board.components.optimized_board_components.bitboards.numpy_bit_board import NumpyBitBoard
from modules.utils.decorator import privatemethod

import random

# ************************************************
# Class OptimizedBoard
# ************************************************
# ROLE : This class is a optimized game board
# ************************************************
# VERSION : 1.0
# AUTHOR : Nathan PINHEIRO
# DATE : 13/01/2025
# ************************************************

class OptimizedBoard(Board):

    """
    Represents a game board.

    Attributes:
        __width__ (int): The width of the board.
        __height__ (int): The height of the board.
        __player_entities__ (list[Entity]): A list of player entities present on the board.
    """

    def __init__(self, width : int, height : int, playerEntities : list[Entity]) -> None :
        
        """
        Initializes a new instance of the Board class.

        Args:
            width (int): The width of the board.
            height (int): The height of the board.
            player_entities (list[Entity]): A list of player entities to initialize the board with.
        
        Returns:
            None
        """
        
        super().__init__(width, height, playerEntities)

        assert(width * height <= 64)
        
        self.__playerBoards__ : list[BitBoard] = [NumpyBitBoard(width, height) for _ in range(len(playerEntities))]
        self.__blockedCases__ : BitBoard = NumpyBitBoard(width, height)
        
        self.__blockedCaseCount__ : int = 0
        self.__pieceCount__ : int = 0

        self.__generateCheckWinMasks__()

    @privatemethod
    def __get_bit_position(self, line: int, column: int) -> int:
        
        """Convert (row, col) to a bit index."""
        
        return line * self.__width__ + column

    @privatemethod
    def __generateCheckWinMasks__(self) -> int :
        
        """
        This method allow initializing masks foreach possible line lenght, that allow then finding correctly 
        if there is alignments in any positions, for any given line length
        """

        self.__lineMasks__ : list[int] = []
        self.__columnMasks__ : list[int] = []
        self.__ascendantDiagonalMasks__ : list[int] = []
        self.__descendantDiagonalMasks__ : list[int] = []

        for alinmentLength in range(0, max(self.__width__, self.__height__) + 1):

            self.__lineMasks__.append(0)
            self.__columnMasks__.append(0)
            self.__ascendantDiagonalMasks__.append(0)
            self.__descendantDiagonalMasks__.append(0)

            for lineIndex in range(0, self.__height__) :
                for columnIndex in range(0, self.__width__) :

                    if(lineIndex <= self.__height__ - alinmentLength) : 
                        self.__columnMasks__[alinmentLength] += (1 << (lineIndex * self.__width__ + columnIndex))
                        
                    if(columnIndex <= self.__width__ - alinmentLength) : 
                        self.__lineMasks__[alinmentLength] += (1 << (lineIndex * self.__width__ + columnIndex))
                        
                    if(lineIndex <= self.__height__ - alinmentLength and columnIndex <= self.__width__ - alinmentLength) : 
                        self.__descendantDiagonalMasks__[alinmentLength] += (1 << (lineIndex * self.__width__ + columnIndex))
                        
                    if(lineIndex <= self.__height__ - alinmentLength and columnIndex >= alinmentLength - 1) : 
                        self.__ascendantDiagonalMasks__[alinmentLength] += (1 << (lineIndex * self.__width__ + columnIndex))

    def isCaseAvaillable(self, line : int, column : int) -> bool :
        
        """
        Checks if a case at the specified line and column is available.

        Args:
            line (int): The line number of the case.
            column (int): The column number of the case.

        Returns:
            bool: True if the case is available, False otherwise.
        """

        if(line < 0 or line >= self.getHeight()) : raise ValueError(f"Line is out of range. Should be from 0 to {self.getHeight()} but was <{line}>")
        if(column < 0 or column >= self.getWidth()) : raise ValueError(f"Column is out of range. Should be from 0 to {self.getWidth()} but was <{column}>")

        bit_position = self.__get_bit_position(line, column)

        takenCases = 0
        for player_board in self.__playerBoards__ : takenCases |= player_board.getValue()
        takenCases |= self.__blockedCases__.getValue()

        return (takenCases & (1 << bit_position)) == 0
    
    def isCaseBlocked(self, line : int, column : int) -> bool :
        
        """
        Checks if a case at the specified line and column is blocked.

        Args:
            line (int): The line number of the case.
            column (int): The column number of the case.

        Returns:
            bool: True if the case is blocked, False otherwise.
        """

        if(line < 0 or line >= self.getHeight()) : raise ValueError(f"Line is out of range. Should be from 0 to {self.getHeight()} but was <{line}>")
        if(column < 0 or column >= self.getWidth()) : raise ValueError(f"Column is out of range. Should be from 0 to {self.getWidth()} but was <{column}>")

        bit_position = self.__get_bit_position(line, column)

        return (self.__blockedCases__.getValue() & (1 << bit_position)) != 0
    
    def setIsCaseBlocked(self, line : int, column : int, isBlocked : bool) -> None :

        """
        Sets whether a case at the specified line and column is blocked.

        Args:
            line (int): The line number of the case.
            column (int): The column number of the case.
            isBlocked (bool): True to block the case, False to unblock it.

        Returns:
            None
        """        

        if(line < 0 or line >= self.getHeight()) : raise ValueError(f"Line is out of range. Should be from 0 to {self.getHeight()} but was <{line}>")
        if(column < 0 or column >= self.getWidth()) : raise ValueError(f"Column is out of range. Should be from 0 to {self.getWidth()} but was <{column}>")

        bit_position = self.__get_bit_position(line, column)
        
        if(self.__blockedCases__.getValue() & (1 << bit_position) == 0 and isBlocked) :
             
            self.__blockedCaseCount__ += 1
            self.__blockedCases__.applyOr(1 << bit_position)
            
        elif(self.__blockedCases__.getValue() & (1 << bit_position) == 1 and not isBlocked) :
            
            self.__blockedCaseCount__ -= 1
            self.__blockedCases__.applyXor(1 << bit_position)

    def getEntityAt(self, line : int, column : int) -> Entity :
        
        """
        Retrieves the entity at the specified line and column.

        Args:
            line (int): The line number of the case.
            column (int): The column number of the case.

        Returns:
            Entity: The entity at the specified location.
        """

        if(line < 0 or line >= self.getHeight()) : raise ValueError(f"Line is out of range. Should be from 0 to {self.getHeight()} but was <{line}>")
        if(column < 0 or column >= self.getWidth()) : raise ValueError(f"Column is out of range. Should be from 0 to {self.getWidth()} but was <{column}>")

        bit_position = self.__get_bit_position(line, column)

        for playerIndex in range(0, len(self.__playerBoards__)) : 
            if((self.__playerBoards__[playerIndex].getValue() & (1 << bit_position)) != 0) : return self.__playerEntities__[playerIndex]

        return None
    
    def isEntityAt(self, line : int, column : int) -> bool :
        
        """
        Checks if there is an entity at the specified line and column.

        Args:
            line (int): The line number of the case.
            column (int): The column number of the case.

        Returns:
            bool: True if there is an entity at the specified location, False otherwise.
        """

        if(line < 0 or line >= self.getHeight()) : raise ValueError(f"Line is out of range. Should be from 0 to {self.getHeight()} but was <{line}>")
        if(column < 0 or column >= self.getWidth()) : raise ValueError(f"Column is out of range. Should be from 0 to {self.getWidth()} but was <{column}>")

        bit_position = self.__get_bit_position(line, column)

        for playerIndex in range(0, len(self.__playerBoards__)) : 
            if((self.__playerBoards__[playerIndex].getValue() & (1 << bit_position)) != 0) : return True

        return False

    def addPlayerEntityAt(self, line : int, column : int, playerIndex : int) -> None:
        
        """
        Adds a player's entity at the specified line and column.

        Args:
            line (int): The line number of the case.
            column (int): The column number of the case.
            playerIndex (int): The index of the player whose entity is being added.

        Returns:
            None
        """

        if(line < 0 or line >= self.getHeight()) : raise ValueError(f"Line is out of range. Should be from 0 to {self.getHeight()} but was <{line}>")
        if(column < 0 or column >= self.getWidth()) : raise ValueError(f"Column is out of range. Should be from 0 to {self.getWidth()} but was <{column}>")

        bit_position = self.__get_bit_position(line, column)
        
        self.__playerBoards__[playerIndex].applyOr(1 << bit_position)
        self.__pieceCount__ += 1

        return None
    
    def addEntityAt(self, line: int, column: int, entity : Entity) -> None:
        """
        Adds an entity at the specified line and column.

        Args:
            line (int): The line number of the case.
            column (int): The column number of the case.
            playerIndex (int): The index of the player whose entity is being added.

        Returns:
            None
        """
        
        if(line < 0 or line >= self.getHeight()) : raise ValueError(f"Line is out of range. Should be from 0 to {self.getHeight()} but was <{line}>")
        if(column < 0 or column >= self.getWidth()) : raise ValueError(f"Column is out of range. Should be from 0 to {self.getWidth()} but was <{column}>")

        playerIndex : int = 0
        playerEntityFound : bool = False
        
        while playerIndex < len(self.__playerEntities__) and not playerEntityFound:
            if(self.__playerEntities__[playerIndex] == entity): playerEntityFound = True
            playerIndex += 1

        playerIndex -= 1

        if(playerIndex == len(self.__playerEntities__)) : raise ValueError(f"No player have this symbol : {entity}")

        bit_position = self.__get_bit_position(line, column)
        
        self.__playerBoards__[playerIndex].applyOr(1 << bit_position)
        self.__pieceCount__ += 1

        return None

    def removeEntityAt(self, line : int, column : int) -> None:
        
        """
        Removes an entity from the specified line and column.

        Args:
            line (int): The line number of the case.
            column (int): The column number of the case.

        Returns:
            None
        """

        if(line < 0 or line >= self.getHeight()) : raise ValueError(f"Line is out of range. Should be from 0 to {self.getHeight()} but was <{line}>")
        if(column < 0 or column >= self.getWidth()) : raise ValueError(f"Column is out of range. Should be from 0 to {self.getWidth()} but was <{column}>")

        bit_position = self.__get_bit_position(line, column)

        for playerIndex in range(0, len(self.__playerBoards__)) : 
            
            # This mask allows making the bit to remove be considered as unsigned int by python interpreter
            mask = (1 << 64) - 1
            
            bitToRemove =  ~(1 << bit_position) & mask

            self.__playerBoards__[playerIndex].applyAnd(bitToRemove)

        self.__pieceCount__ -= 1

        return None

    def checkAlignmentOnCaseForPlayer(self, line : int, column : int, playerIndex : int, alignLength : int) -> bool:
        
        """
        Checks if any player has an alignment of the specified length, on the given case.

        Args:
            alignLength (int): The length of the alignment to check for.

        Returns:
            int: The index of the player with the alignment, or -1 if no alignment exists.
        """

        return self.checkAlignmentForPlayer(playerIndex, alignLength)
    
    def checkAlignmentForPlayer(self, playerIndex : int, alignLength : int) -> bool:
        
        """
        Checks if a player's entities are aligned anywhere on the board.

        Args:
            playerIndex (int): The index of the player.
            alignLength (int): The length of the alignment to check for.

        Returns:
            bool: True if the player's entities are aligned, False otherwise.
        """

        # The idea there is to use the less loops as possible, and replace this by binary computations, finding pairs with a 
        # given shift between them and doing it as much times as the length of the alignment is. Then by using a mask, 
        # we can avoid having wrong results as for exemple bits that are together but that are not on the same line.
        # As those masks are computed one time only at the initialization of the object, it do not slow down the computation.

        playerPieces : int = self.__playerBoards__[playerIndex].getValue()

        shift : int = 1
        casesWithNeibours : int = playerPieces
        for _ in range(alignLength - 1) : casesWithNeibours &= (casesWithNeibours >> shift)
        if(casesWithNeibours & self.__lineMasks__[alignLength] != 0) : return True
        
        shift : int = self.__width__
        casesWithNeibours : int = playerPieces
        for _ in range(alignLength - 1): casesWithNeibours &= (casesWithNeibours >> shift)
        if(casesWithNeibours & self.__columnMasks__[alignLength] != 0) : return True
        
        shift : int = self.__width__ - 1
        casesWithNeibours : int = playerPieces
        for _ in range(alignLength - 1): casesWithNeibours &= (casesWithNeibours >> shift)
        if(casesWithNeibours & self.__ascendantDiagonalMasks__[alignLength] != 0) : return True
        
        shift : int = self.__width__ + 1
        casesWithNeibours : int = playerPieces
        for _ in range(alignLength - 1): casesWithNeibours &= (casesWithNeibours >> shift)
        if(casesWithNeibours & self.__descendantDiagonalMasks__[alignLength] != 0) : return True

        return False
    
    def checkIfPlayerHaveAlignment(self, alignLength : int) -> int:
        
        """
        Checks if any player has an alignment of the specified length.

        Args:
            alignLength (int): The length of the alignment to check for.

        Returns:
            int: The index of the player with the alignment, or -1 if no alignment exists.
        """

        for playerIndex in range(0, len(self.__playerBoards__)):
            if(self.checkAlignmentForPlayer(playerIndex, alignLength)) : return playerIndex
        
        return -1

    def checkIfPlayerHaveAlignmentOnCase(self, alignLength: int) -> int:
        
        """
        Checks if any player has a sequence of aligned entities of the specified length on a case.

        Args:
            alignLength (int): Required alignment length.

        Returns:
            int: Player index if alignment exists, -1 otherwise.
        """

        for playerIndex in range(0, len(self.__playerBoards__)):
            if(self.checkAlignmentOnCaseForPlayer(playerIndex, alignLength)) : return playerIndex
        
        return -1

    def isFull(self) -> bool:
        
        """
        Checks if the board is completely filled.

        Returns:
            bool: True if full, False otherwise.
        """

        return self.__pieceCount__ == self.__width__ * self.__height__ - self.__blockedCaseCount__

    def blockRandomCase(self) -> None:
        
        """
        Blocks a random case on the board.

        Returns:
            None
        """

        takenCases = 0
        for player_board in self.__playerBoards__: takenCases |= player_board.getValue()
        takenCases |= self.__blockedCases__.getValue()

        available_cases = []
        
        for line in range(self.__height__):
            for column in range(self.__width__):
                bit_position = self.__get_bit_position(line, column)
                if (takenCases & (1 << bit_position)) == 0: available_cases.append(bit_position)

        if len(available_cases) == 0 : raise ValueError("No available cases to block!")

        chosen_case = random.choice(available_cases)
        self.__blockedCases__.applyOr(1 << chosen_case)
        
        return None
        
    def getPieceCount(self) -> int:
        """
        Return the amount of pieces on the board.

        Returns:
            pieceCount (int) : the amount of pieces on the board.
        """
        return self.__pieceCount__

    def copy(self) -> Board:

        """
        Creates a duplicate of the board.

        Returns:
            Board: A copied instance.
        """

        board : Board = OptimizedBoard(self.__width__, self.__height__, self.__playerEntities__)

        board.__playerBoards__ = self.__playerBoards__
        board.__blockedCases__ = self.__blockedCases__
        board.__pieceCount__ = self.__pieceCount__

        return board
    
    def __hash__(self):

        """
        Computes a hash for the board.

        Returns:
            int: The hash value.
        """

        hashSum : int = 0

        for playerIndex in range(0, len(self.__playerBoards__)): hashSum += hash(self.__playerBoards__[playerIndex])

        return hash(hashSum)