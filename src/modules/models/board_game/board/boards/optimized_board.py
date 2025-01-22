from modules.models.board_game.board.board import Board
from modules.models.board_game.components.entity import Entity
from modules.models.board_game.board.components.optimized_board_components.bitboard import BitBoard
from modules.models.board_game.board.components.optimized_board_components.bitboards.numpy_bit_board import NumpyBitBoard
from modules.utils.decorator import privatemethod, override

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
    """

    def __init__(self, width : int, height : int, playerEntities : list[Entity]) -> None :
        
        """
        Initializes a new instance of the Board class.

        Parameters:
            width (int): The width of the board.
            height (int): The height of the board.
            player_entities (list[Entity]): A list of player entities to initialize the board with.
            
        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than or equal to 0.
            ValueError: If the board size is greater than 64.
            TypeError: If playerEntities is not a list of Entity instances.
        
        Returns:
            None
        """
        
        # Check if width and height are integers, greater than 0 and less than or equal to 64
        if not isinstance(width, int) or not isinstance(height, int) :
            raise TypeError("Width and height must be integers")
        
        if width <= 0 or height <= 0 :
            raise ValueError("Width and height must be greater than 0")
        
        if width * height > 64 :
            raise ValueError("Board size must be less than or equal to 64")
        
        # Check if playerEntities is a list of Entity instances
        if not isinstance(playerEntities, list) and not all(isinstance(entity, Entity) for entity in playerEntities) :
            raise TypeError("playerEntities must be a list of Entity instances")
        
        # Call the parent constructor
        super().__init__(width, height, playerEntities)
        
        # Initialize the player boards and blocked cases
        self.__playerBoards__ : list[BitBoard] = [NumpyBitBoard(width, height) for _ in range(len(playerEntities))]
        self.__blockedCases__ : BitBoard = NumpyBitBoard(width, height)
        
        # Initialize the piece count
        self.__blockedCaseCount__ : int = 0
        self.__pieceCount__ : int = 0

        # Generate the masks for checking alignments
        self.__generateCheckWinMasks__()
        
        return None

    @privatemethod
    def __getBitPosition__(self, line: int, column: int) -> int:
        
        """
        Convert (line, column) to a bit index.
        
        Parameters:
            line (int): The line number.
            column (int): The column number.
            
        Raises:
            TypeError: If line or column is not an integer.
            ValueError: If line or column is out of range.
            
        Returns:
            int: The bit index.
        """
        
        # Check if line and column are integers and within the board dimensions
        if not isinstance(line, int) or not isinstance(column, int):
            raise TypeError("Line and column must be integers")
        
        if line < 0 or line >= self.getHeight():
            raise ValueError(f"Line must be between 0 and {self.getHeight() - 1}")
        
        if column < 0 or column >= self.getWidth():
            raise ValueError(f"Column must be between 0 and {self.getWidth() - 1}")
        
        return line * self.__width__ + column

    @privatemethod
    def __generateCheckWinMasks__(self) -> bool:
        
        """
        This method allow initializing masks foreach possible line lenght, that allow then finding correctly 
        if there is alignments in any positions, for any given line length
        
        Returns:
            bool: True if the masks are generated successfully.
        """

        # Initialize the masks for checking alignments with empty lists
        self.__lineMasks__ : list[int] = []
        self.__columnMasks__ : list[int] = []
        self.__ascendantDiagonalMasks__ : list[int] = []
        self.__descendantDiagonalMasks__ : list[int] = []

        # Generate the masks for checking alignments
        for alinmentLength in range(0, max(self.__width__, self.__height__) + 1):

            # Add a mask for each alignment length
            self.__lineMasks__.append(0)
            self.__columnMasks__.append(0)
            self.__ascendantDiagonalMasks__.append(0)
            self.__descendantDiagonalMasks__.append(0)

            # Set the bits for each alignment length
            for lineIndex in range(0, self.__height__) :
                for columnIndex in range(0, self.__width__) :

                    # Set the bits depending on the alignment length
                    if(lineIndex <= self.__height__ - alinmentLength) : 
                        self.__columnMasks__[alinmentLength] += (1 << self.__getBitPosition__(lineIndex, columnIndex))
                        
                    if(columnIndex <= self.__width__ - alinmentLength) : 
                        self.__lineMasks__[alinmentLength] += (1 << self.__getBitPosition__(lineIndex, columnIndex))
                        
                    if(lineIndex <= self.__height__ - alinmentLength and columnIndex <= self.__width__ - alinmentLength) : 
                        self.__descendantDiagonalMasks__[alinmentLength] += (1 << self.__getBitPosition__(lineIndex, columnIndex))
                        
                    if(lineIndex <= self.__height__ - alinmentLength and columnIndex >= alinmentLength - 1) : 
                        self.__ascendantDiagonalMasks__[alinmentLength] += (1 << self.__getBitPosition__(lineIndex, columnIndex))
                        
        return True

    @override
    def isCaseAvaillable(self, line : int, column : int) -> bool:
        
        """
        Checks if a case at the specified line and column is available.

        Parameters:
            line (int): The line number of the case.
            column (int): The column number of the case.
            
        Raises:
            TypeError: If line or column is not an integer.
            ValueError: If line or column is out of range.

        Returns:
            bool: True if the case is available, False otherwise.
        """
        
        # Check if line and column are integers and within the board dimensions
        if not isinstance(line, int) or not isinstance(column, int): 
            raise TypeError("Line and column must be integers")

        if(line < 0 or line >= self.getHeight()): 
            raise ValueError(f"Line is out of range. Should be from 0 to {self.getHeight()} but was <{line}>")
        
        if(column < 0 or column >= self.getWidth()): 
            raise ValueError(f"Column is out of range. Should be from 0 to {self.getWidth()} but was <{column}>")

        # Get the bit position of the case
        bit_position = self.__getBitPosition__(line, column)

        # Check if the case is available
        takenCases = 0
        for player_board in self.__playerBoards__ : takenCases |= player_board.getValue()
        takenCases |= self.__blockedCases__.getValue()

        return (takenCases & (1 << bit_position)) == 0
    
    @override
    def isCaseBlocked(self, line : int, column : int) -> bool:
        
        """
        Checks if a case at the specified line and column is blocked.

        Parameters:
            line (int): The line number of the case.
            column (int): The column number of the case.
            
        Raises:
            TypeError: If line or column is not an integer.
            ValueError: If line or column is out of range.

        Returns:
            bool: True if the case is blocked, False otherwise.
        """
        
        # Check if line and column are integers and within the board dimensions
        if not isinstance(line, int) or not isinstance(column, int): 
            raise TypeError("Line and column must be integers")

        if(line < 0 or line >= self.getHeight()): 
            raise ValueError(f"Line is out of range. Should be from 0 to {self.getHeight()} but was <{line}>")
        
        if(column < 0 or column >= self.getWidth()): 
            raise ValueError(f"Column is out of range. Should be from 0 to {self.getWidth()} but was <{column}>")

        # Get the bit position of the case and check if it is blocked
        bit_position = self.__getBitPosition__(line, column)

        return (self.__blockedCases__.getValue() & (1 << bit_position)) != 0
    
    @override
    def setIsCaseBlocked(self, line : int, column : int, isBlocked : bool) -> bool:

        """
        Sets whether a case at the specified line and column is blocked.

        Parameters:
            line (int): The line number of the case.
            column (int): The column number of the case.
            isBlocked (bool): True to block the case, False to unblock it.
            
        Raises:
            TypeError: If line or column is not an integer.
            ValueError: If line or column is out of range.

        Returns:
            bool: True if the case is blocked.
        """        

        # Check if line and column are integers and within the board dimensions
        if not isinstance(line, int) or not isinstance(column, int): 
            raise TypeError("Line and column must be integers")
        
        if(line < 0 or line >= self.getHeight()): 
            raise ValueError(f"Line is out of range. Should be from 0 to {self.getHeight()} but was <{line}>")
        
        if(column < 0 or column >= self.getWidth()): 
            raise ValueError(f"Column is out of range. Should be from 0 to {self.getWidth()} but was <{column}>")

        # Get the bit position of the case
        bit_position = self.__getBitPosition__(line, column)
        
        # Set the case as blocked or unblocked
        if(self.__blockedCases__.getValue() & (1 << bit_position) == 0 and isBlocked) :
             
            self.__blockedCaseCount__ += 1
            self.__blockedCases__.applyOr(1 << bit_position)
            
        elif(self.__blockedCases__.getValue() & (1 << bit_position) != 0 and not isBlocked) :
            
            self.__blockedCaseCount__ -= 1
            self.__blockedCases__.applyXor(1 << bit_position)
            
        return True

    @override
    def getEntityAt(self, line : int, column : int) -> Entity | None:
        
        """
        Retrieves the entity at the specified line and column.

        Parameters:
            line (int): The line number of the case.
            column (int): The column number of the case.
            
        Raises:
            TypeError: If line or column is not an integer.
            ValueError: If line or column is out of range.

        Returns:
            Entity: The entity at the specified location.
        """
        
        # Check if line and column are integers and within the board dimensions
        if not isinstance(line, int) or not isinstance(column, int): 
            raise TypeError("Line and column must be integers")

        if(line < 0 or line >= self.getHeight()): 
            raise ValueError(f"Line is out of range. Should be from 0 to {self.getHeight()} but was <{line}>")
        
        if(column < 0 or column >= self.getWidth()): 
            raise ValueError(f"Column is out of range. Should be from 0 to {self.getWidth()} but was <{column}>")

        # Get the bit position of the case
        bit_position = self.__getBitPosition__(line, column)

        # Check if there is an entity at the specified location
        for playerIndex in range(0, len(self.__playerBoards__)) : 
            if((self.__playerBoards__[playerIndex].getValue() & (1 << bit_position)) != 0): 
                return self.__playerEntities__[playerIndex]

        return None
    
    @override
    def isEntityAt(self, line : int, column : int) -> bool :
        
        """
        Checks if there is an entity at the specified line and column.

        Parameters:
            line (int): The line number of the case.
            column (int): The column number of the case.

        Raises:
            TypeError: If line or column is not an integer.
            ValueError: If line or column is out of range.

        Returns:
            bool: True if there is an entity at the specified location, False otherwise.
        """

        # Check if line and column are integers and within the board dimensions
        if not isinstance(line, int) or not isinstance(column, int): 
            raise TypeError("Line and column must be integers")
        
        if(line < 0 or line >= self.getHeight()): 
            raise ValueError(f"Line is out of range. Should be from 0 to {self.getHeight()} but was <{line}>")
        
        if(column < 0 or column >= self.getWidth()): 
            raise ValueError(f"Column is out of range. Should be from 0 to {self.getWidth()} but was <{column}>")

        # Get the bit position of the case
        bit_position = self.__getBitPosition__(line, column)

        # Check if there is an entity at the specified location
        for playerIndex in range(0, len(self.__playerBoards__)) : 
            if((self.__playerBoards__[playerIndex].getValue() & (1 << bit_position)) != 0): 
                return True

        return False

    @override
    def addPlayerEntityAt(self, line : int, column : int, playerIndex : int) -> bool:
        
        """
        Adds a player's entity at the specified line and column.

        Parameters:
            line (int): The line number of the case.
            column (int): The column number of the case.
            playerIndex (int): The index of the player whose entity is being added.
            
        Raises:
            TypeError: If line or column is not an integer.
            ValueError: If line or column is out of range.
            TypeError: If playerIndex is not an integer.

        Returns:
            bool: True if the entity is added successfully.
        """
        
        # Check if line and column are integers and within the board dimensions
        if not isinstance(line, int) or not isinstance(column, int): 
            raise TypeError("Line and column must be integers")

        if(line < 0 or line >= self.getHeight()): 
            raise ValueError(f"Line is out of range. Should be from 0 to {self.getHeight()} but was <{line}>")
        
        if(column < 0 or column >= self.getWidth()): 
            raise ValueError(f"Column is out of range. Should be from 0 to {self.getWidth()} but was <{column}>")
        
        # Check if playerIndex is an integer
        if not isinstance(playerIndex, int): 
            raise TypeError("Player index must be an integer")

        # Get the bit position of the case
        bit_position = self.__getBitPosition__(line, column)
        
        # Add the player's entity to the specified location
        self.__playerBoards__[playerIndex].applyOr(1 << bit_position)
        self.__pieceCount__ += 1

        return True
    
    @override
    def addEntityAt(self, line: int, column: int, entity : Entity) -> bool:
        
        """
        Adds an entity at the specified line and column.

        Parameters:
            line (int): The line number of the case.
            column (int): The column number of the case.
            playerIndex (int): The index of the player whose entity is being added.
            
        Raises:
            TypeError: If line or column is not an integer.
            ValueError: If line or column is out of range.
            TypeError: If entity is not an instance of Entity.*
            ValueError: If the entity is not found in the player entities list.

        Returns:
            bool: True if the entity is added successfully.
        """
        
        # Check if line and column are integers and within the board dimensions
        if not isinstance(line, int) or not isinstance(column, int): 
            raise TypeError("Line and column must be integers")
        
        if(line < 0 or line >= self.getHeight()): 
            raise ValueError(f"Line is out of range. Should be from 0 to {self.getHeight()} but was <{line}>")
        
        if(column < 0 or column >= self.getWidth()): 
            raise ValueError(f"Column is out of range. Should be from 0 to {self.getWidth()} but was <{column}>")
        
        # Check if entity is an instance of Entity
        if not isinstance(entity, Entity):
            raise TypeError("Entity must be an instance of Entity")

        # Initialize the player index and boolean to check if the entity is found
        playerIndex : int = 0
        playerEntityFound : bool = False
        
        # If the entity is not found, find the player index
        while playerIndex < len(self.__playerEntities__) and not playerEntityFound:
            if(self.__playerEntities__[playerIndex] == entity): playerEntityFound = True
            playerIndex += 1

        playerIndex -= 1

        # If the entity is not found, raise an error
        if(playerIndex == len(self.__playerEntities__)): 
            raise ValueError(f"No player have this symbol : {entity}")

        # Get the bit position of the case
        bit_position = self.__getBitPosition__(line, column)
        
        # Add the entity to the specified location
        self.__playerBoards__[playerIndex].applyOr(1 << bit_position)
        self.__pieceCount__ += 1

        return True

    @override
    def removeEntityAt(self, line : int, column : int) -> bool:
        
        """
        Removes an entity from the specified line and column.

        Parameters:
            line (int): The line number of the case.
            column (int): The column number of the case.

        Returns:
            bool: True if the entity is removed successfully.
        """
        
        # Check if line and column are integers and within the board dimensions
        if not isinstance(line, int) or not isinstance(column, int):
            raise TypeError("Line and column must be integers")

        if(line < 0 or line >= self.getHeight()): 
            raise ValueError(f"Line is out of range. Should be from 0 to {self.getHeight()} but was <{line}>")
        
        if(column < 0 or column >= self.getWidth()): 
            raise ValueError(f"Column is out of range. Should be from 0 to {self.getWidth()} but was <{column}>")

        # Get the bit position of the case
        bit_position = self.__getBitPosition__(line, column)

        # Remove the entity from the specified location
        for playerIndex in range(0, len(self.__playerBoards__)) : 
            
            # This mask allows making the bit to remove be considered as unsigned int by python interpreter
            mask = (1 << 64) - 1
            
            # This mask allows to remove the bit at the given position
            bitToRemove =  ~(1 << bit_position) & mask
            
            # Decrease the piece count if the bit was removed
            if self.__playerBoards__[playerIndex].getValue() & (1 << bit_position) != 0:
                self.__playerBoards__[playerIndex].applyAnd(bitToRemove)
                self.__pieceCount__ -= 1

        return True

    @override
    def checkAlignmentOnCaseForPlayer(self, line : int, column : int, playerIndex : int, alignLength : int) -> bool:
        
        """
        Checks if any player has an alignment of the specified length, on the given case.

        Parameters:
            line (int): The line number of the case.
            column (int): The column number of the case.
            playerIndex (int): The index of the player.
            alignLength (int): The length of the alignment to check for.
            
        Raises:
            TypeError: If line or column is not an integer.
            ValueError: If line or column is out of range.
            TypeError: If playerIndex is not an integer.
            ValueError: If playerIndex is out of range.
            TypeError: If alignLength is not an integer.

        Returns:
            int: The index of the player with the alignment, or -1 if no alignment exists.
        """
        
        # Check if line and column are integers and within the board dimensions
        if not isinstance(line, int) or not isinstance(column, int):
            raise TypeError("Line and column must be integers")
        
        if(line < 0 or line >= self.getHeight()):
            raise ValueError(f"Line is out of range. Should be from 0 to {self.getHeight()} but was <{line}>")
        
        if(column < 0 or column >= self.getWidth()):
            raise ValueError(f"Column is out of range. Should be from 0 to {self.getWidth()} but was <{column}>")
        
        # Check if playerIndex is an integer and within the player boards range
        if not isinstance(playerIndex, int):
            raise TypeError("Player index must be an integer")
        
        if(playerIndex < 0 or playerIndex >= len(self.__playerBoards__)):
            raise ValueError(f"Player index is out of range. Should be from 0 to {len(self.__playerBoards__)} but was <{playerIndex}>")
        
        # Check if alignLength is an integer, greater than 0 and less than the board dimensions
        if not isinstance(alignLength, int):
            raise TypeError("Alignment length must be an integer")
        
        if(alignLength <= 0 and alignLength > self.__width__ and alignLength > self.__height__):
            raise ValueError("Alignment length must be greater than 0 and less than the board dimensions")

        return self.checkAlignmentForPlayer(playerIndex, alignLength)
    
    @override
    def checkAlignmentForPlayer(self, playerIndex : int, alignLength : int) -> bool:
        
        """
        Checks if a player's entities are aligned anywhere on the board.
        
        The idea there is to use the less loops as possible, and replace this by binary computations, finding pairs with a 
        given shift between them and doing it as much times as the length of the alignment is. Then by using a mask, 
        we can avoid having wrong results as for exemple bits that are together but that are not on the same line.
        As those masks are computed one time only at the initialization of the object, it do not slow down the computation.

        Parameters:
            playerIndex (int): The index of the player.
            alignLength (int): The length of the alignment to check for.
            
        Raises:
            TypeError: If playerIndex is not an integer.
            ValueError: If playerIndex is out of range.
            TypeError: If alignLength is not an integer.
            ValueError: If alignLength is less than 0 or greater than the board dimensions.

        Returns:
            bool: True if the player's entities are aligned, False otherwise.
        """
        
        # Check if playerIndex is an integer and within the player boards range
        if not isinstance(playerIndex, int):
            raise TypeError("Player index must be an integer")
        
        if(playerIndex < 0 or playerIndex >= len(self.__playerBoards__)):
            raise ValueError(f"Player index is out of range. Should be from 0 to {len(self.__playerBoards__)} but was <{playerIndex}>")

        # Check if alignLength is an integer, greater than 0 and less than the board dimensions
        if not isinstance(alignLength, int):
            raise TypeError("Alignment length must be an integer")
        
        if(alignLength <= 0 and alignLength > self.__width__ and alignLength > self.__height__):
            raise ValueError("Alignment length must be greater than 0 and less than the board dimensions")

        # Initialize the player's pieces
        playerPieces : int = self.__playerBoards__[playerIndex].getValue()

        # Check if the player has an alignment of the specified length in lines
        shift : int = 1
        casesWithNeibours : int = playerPieces
        for _ in range(alignLength - 1) : casesWithNeibours &= (casesWithNeibours >> shift)
        if(casesWithNeibours & self.__lineMasks__[alignLength] != 0) : return True
        
        # Check if the player has an alignment of the specified length in columns
        shift : int = self.__width__
        casesWithNeibours : int = playerPieces
        for _ in range(alignLength - 1): casesWithNeibours &= (casesWithNeibours >> shift)
        if(casesWithNeibours & self.__columnMasks__[alignLength] != 0) : return True
        
        # Check if the player has an alignment of the specified length in ascendant diagonals
        shift : int = self.__width__ - 1
        casesWithNeibours : int = playerPieces
        for _ in range(alignLength - 1): casesWithNeibours &= (casesWithNeibours >> shift)
        if(casesWithNeibours & self.__ascendantDiagonalMasks__[alignLength] != 0) : return True
        
        # Check if the player has an alignment of the specified length in descendant diagonals
        shift : int = self.__width__ + 1
        casesWithNeibours : int = playerPieces
        for _ in range(alignLength - 1): casesWithNeibours &= (casesWithNeibours >> shift)
        if(casesWithNeibours & self.__descendantDiagonalMasks__[alignLength] != 0) : return True

        return False
    
    @override
    def checkIfPlayerHaveAlignment(self, alignLength : int) -> int:
        
        """
        Checks if any player has an alignment of the specified length.

        Parameters:
            alignLength (int): The length of the alignment to check for.
            
        Raises:
            TypeError: If alignLength is not an integer.
            ValueError: If alignLength is less than 0 or greater than the board dimensions.

        Returns:
            int: The index of the player with the alignment, or -1 if no alignment exists.
        """
        
        # Check if alignLength is an integer, greater than 0 and less than the board dimensions
        if not isinstance(alignLength, int):
            raise TypeError("Alignment length must be an integer")
        
        if(alignLength <= 0 and alignLength > self.__width__ and alignLength > self.__height__):
            raise ValueError("Alignment length must be greater than 0 and less than the board dimensions")

        # Check if any player has an alignment of the specified length
        for playerIndex in range(0, len(self.__playerBoards__)):
            if(self.checkAlignmentForPlayer(playerIndex, alignLength)) : return playerIndex
        
        return -1

    @override
    def checkIfPlayerHaveAlignmentOnCase(self, alignLength: int) -> int:
        
        """
        Checks if any player has a sequence of aligned entities of the specified length on a case.

        Parameters:
            alignLength (int): Required alignment length.
            
        Raises:
            TypeError: If alignLength is not an integer.
            ValueError: If alignLength is less than 0 or greater than the board dimensions.

        Returns:
            int: Player index if alignment exists, -1 otherwise.
        """
        
        # Check if alignLength is an integer, greater than 0 and less than the board dimensions
        if not isinstance(alignLength, int):
            raise TypeError("Alignment length must be an integer")
        
        if(alignLength <= 0 and alignLength > self.__width__ and alignLength > self.__height__):
            raise ValueError("Alignment length must be greater than 0 and less than the board dimensions")

        # Check if any player has an alignment of the specified length on a case
        for playerIndex in range(0, len(self.__playerBoards__)):
            if(self.checkAlignmentOnCaseForPlayer(playerIndex, alignLength)) : return playerIndex
        
        return -1

    @override
    def countAvaillableLineOfAtLeastGivenPiece(self, playerIndex: int, alignLength: int, pieceCount: int) -> int:
        
        """
        Returns the number of lines that contain at least a given amount of the player's pieces and no opponent pieces.

        Parameters:
            playerIndex (int): The player's index.
            alignLength (int): Required alignment length to win.
            pieceCount (int): Minimum number of the player's pieces required.
            
        Raises:
            TypeError: If playerIndex, alignLength or pieceCount is not an integer.
            ValueError: If playerIndex is out of range.
            ValueError: If alignLength is less than 0 or greater than the board dimensions.
            ValueError: If pieceCount is less than 0.

        Returns:
            int: The number of valid lines.
        """
        
        # Check if playerIndex is an integer and within the player boards range
        if not isinstance(playerIndex, int): 
            raise TypeError("Player index must be an integer")
        
        if playerIndex < 0 or playerIndex >= len(self.__playerBoards__):
            raise ValueError(f"Player index is out of range. Should be from 0 to {len(self.__playerBoards__)} but was <{playerIndex}>")
        
        # Check if alignLength is an integer, greater than 0 and less than the board dimensions
        if not isinstance(alignLength, int):
            raise TypeError("Alignment length must be an integer")
        
        if(alignLength <= 0 and alignLength > self.__width__ and alignLength > self.__height__):
            raise ValueError("Alignment length must be greater than 0 and less than the board dimensions")
        
        # Check if pieceCount is an integer and greater than 0
        if not isinstance(pieceCount, int):
            raise TypeError("Piece count must be an integer")
        
        if pieceCount <= 0:
            raise ValueError("Piece count must be greater than 0")

        # Initialize the player's and opponent's pieces
        playerPieces : int = self.__playerBoards__[playerIndex].getValue()
        opponentPieces: int = 0
        
        # Get the opponent's pieces
        for index, board in enumerate(self.__playerBoards__):
            if index != playerIndex : opponentPieces |= board.getValue()

        def countInDirection(mask: int, shift: int) -> int:
            
            """
            Count the number of lines that contain at least a given amount of the player's pieces and no opponent pieces.
            
            Parameters:
                mask (int): The mask to use.
                shift (int): The shift to use.
                
            Raises:
                TypeError: If mask or shift is not an integer.

            Returns:
                int: The number of valid lines.
            """
            
            # Check if mask and shift are integers
            if not isinstance(mask, int) or not isinstance(shift, int):
                raise TypeError("Mask and shift must be integers")
            
            # Initialize the result
            result : int = 0
            
            # Check if the player has a line of the specified length
            oponentBlockedAlignments : int = opponentPieces
            for _ in range(alignLength - 1): oponentBlockedAlignments |= (oponentBlockedAlignments >> shift)

            # Check if the player has a line of the specified length on the board
            for line in range(self.__height__):
                for column in range(self.__width__):
                    
                    # Get the bit to check
                    bitToCheck : int = 1 << self.__getBitPosition__(line, column)

                    # Check if the player has a line of the specified length
                    if(bitToCheck & mask & ~oponentBlockedAlignments) != 0:
                        
                        # Initialize the count, shifted bit and bit index
                        count : int = 0
                        shiftedBit : int = bitToCheck
                        bitIndex : int = 0   
                        
                        # Count the number of player's pieces in the line
                        while(bitIndex < alignLength and count < pieceCount):
                            
                            if(shiftedBit & playerPieces) : count += 1
                            shiftedBit = shiftedBit << shift
                            bitIndex += 1
                        
                        # Increment the result if the count is greater than or equal to the piece count
                        if(count >= pieceCount) : result += 1

            return result

        # Count the number of lines that contain at least a given amount of the player's pieces and no opponent pieces
        result : int = 0
        result += countInDirection(self.__lineMasks__[alignLength], 1)
        result += countInDirection(self.__columnMasks__[alignLength], self.__width__)
        result += countInDirection(self.__ascendantDiagonalMasks__[alignLength], self.__width__ - 1)
        result += countInDirection(self.__descendantDiagonalMasks__[alignLength], self.__width__ + 1)

        return result

    @override
    def isFull(self) -> bool:
        
        """
        Checks if the board is completely filled.

        Returns:
            bool: True if full, False otherwise.
        """

        return self.__pieceCount__ == self.__width__ * self.__height__ - self.__blockedCaseCount__

    @override
    def blockRandomCase(self) -> bool:
        
        """
        Blocks a random case on the board.
        
        Raises:
            ValueError: If there are no available cases to block.

        Returns:
            bool: True if the case is blocked successfully.
        """

        # Get the taken cases
        takenCases = 0
        for player_board in self.__playerBoards__: takenCases |= player_board.getValue()
        takenCases |= self.__blockedCases__.getValue()

        # Get the available cases to block
        available_cases = []
        
        for line in range(self.__height__):
            for column in range(self.__width__):
                bit_position = self.__getBitPosition__(line, column)
                if (takenCases & (1 << bit_position)) == 0: available_cases.append(bit_position)

        # Check if there are available cases to block
        if len(available_cases) == 0: 
            raise ValueError("No available cases to block!")

        # Block a random case
        chosen_case = random.choice(available_cases)
        self.__blockedCases__.applyOr(1 << chosen_case)
        
        return True
        
    @override
    def getPieceCount(self) -> int:
        
        """
        Return the amount of pieces on the board.

        Returns:
            pieceCount (int) : the amount of pieces on the board.
        """
        
        return self.__pieceCount__
    
    @override
    def getPlayerCount(self) -> int:
        
        """
        Return the amount of players on the board.

        Returns:
            playerCount (int) : the amount of players on the board.
        """
        
        return len(self.__playerEntities__)
    
    @override
    def getCountCaseAvaillable(self):
        
        """
        Return the amount of availlable cases on the board.

        Returns:
            availlableCases (int) : the amount of availlable cases on the board.
        """
        
        return self.__width__ * self.__height__ - self.__pieceCount__ - self.__blockedCaseCount__
    
    def getCountCaseBlocked(self):
        
        """
        Return the amount of blocked cases on the board.

        Returns:
            blockedCases (int) : the amount of blocked cases on the board.
        """
        
        return self.__blockedCaseCount__

    @override
    def copy(self) -> Board:

        """
        Creates a duplicate of the board.

        Returns:
            Board: A copied instance.
        """

        # Get the copied board
        board : Board = OptimizedBoard(self.__width__, self.__height__, self.__playerEntities__)

        # Copy the player boards, blocked cases and piece count
        board.__playerBoards__ = self.__playerBoards__
        board.__blockedCases__ = self.__blockedCases__
        board.__pieceCount__ = self.__pieceCount__

        return board
    
    @override
    def __hash__(self) -> int:

        """
        Computes a hash for the board.

        Returns:
            int: The hash value.
        """

        # Initialize the hash sum
        hashSum : int = 0

        # Compute the hash sum for the player boards
        for playerIndex in range(0, len(self.__playerBoards__)): hashSum += hash(self.__playerBoards__[playerIndex])

        return hash(hashSum)