from modules.models.board_game.components.entity import Entity
from modules.models.board_game.components.coordinate import Coordinate
from modules.models.board_game.board.board import Board
from modules.models.board_game.board.components.simple_board_components.case import Case
from modules.utils.decorator import privatemethod, override, deprecated_class
import random

# ************************************************
# Class SimpleBoard (Deprecated)
# ************************************************
# ROLE : This class is a unoptimized game board
# ************************************************
# VERSION : 1.0
# AUTHOR : Nathan PINHEIRO
# DATE : 13/01/2025
# ************************************************

@deprecated_class
class SimpleBoard(Board):
    
    """
    Represents a simple board for a game.
    """

    def __init__(self, width : int, height : int, player_entities : list[Entity]) -> None:
        
        """
        Constructor for the Board class.

        Parameters:
            width (int): The width of the board.
            height (int): The height of the board.
            player_entities (list[Entity]): The list of entities that can be placed on the board.
            
        Raises:
            ValueError: If the width or height is not an integer.
            ValueError: If the width or height is not strictly positive.
            ValueError: If the player entities are not a list of Entity instances.
            
        Returns:
            None
        """
        
        # Check if the width and height are integers and strictly positive
        if not isinstance(width, int) or not isinstance(height, int):
            raise ValueError(f"Width and height must be integers.")
        
        if width <= 0 or height <= 0:
            raise ValueError(f"Width and height must be strictly positive integers.")
        
        # Check if the player entities are a list of Entity instances
        if not isinstance(player_entities, list) and all(isinstance(entity, Entity) for entity in player_entities):
            raise ValueError(f"Player entities must be a list of Entity instances.")
        
        # Call the parent constructor
        super.__init__(width, height, player_entities)
        
        # Initialize the board attributes
        self.__pieceCount__ = 0
        self.__blockedCaseCount = 0

        # Initialize the board
        self.__initializeBoard__()
        
        return None

    @privatemethod
    def __initializeBoard__(self) -> bool:
        
        """
        Initialize all cases of the board to availlable cases.
        
        Returns:
            bool: True if the board is initialized successfully.
        """
        
        # Initialize the cases of the board
        self.__cases__: list[list[Case]] = [[Case(Coordinate(line, column)) for column in range(self.__width__)] for line in range(self.__height__)]

        return True

    @override
    def isCaseBlocked(self, line : int, column : int) -> bool :
        
        """
        Verifies if a case is blocked.

        Parameters:
            line (int): The line of the case.
            column (int): The column of the case.
            
        Raises:
            ValueError: If the line or column is not an integer.
            ValueError: If the line or column is out of the board range.

        Returns:
            bool: True if the case is blocked, False otherwise.
        """
        
        # Check if the line and column are integers and in the board range
        if not isinstance(line, int) or not isinstance(column, int):
            raise ValueError("Line and column must be integers.")
                
        if(line < 0 or line > self.getHeight()): 
            raise ValueError(f"Line is out of range. Should be from 0 to {self.getHeight()} but was <{line}>")
        
        if(column < 0 or column > self.getWidth()): 
            raise ValueError(f"Column is out of range. Should be from 0 to {self.getWidth()} but was <{column}>")

        return self.__cases__[line][column].isBlocked()

    @override
    def setIsCaseBlocked(self, line : int, column : int, isBlocked : bool) -> bool :
        
        """
        Set the blocked status of a case.
        
        Parameters:
            line (int): The line of the case.
            column (int): The column of the case.
            isBlocked (bool): The new blocked status of the case.
            
        Raises:
            ValueError: If the line or column is not an integer.
            ValueError: If the line or column is out of the board range.
            ValueError: If isBlocked is not a boolean.

        Returns:
            bool : True if the state of the case is updated.
        """
        
        # Check if the line and column are integers and in the board range
        if not isinstance(line, int) or not isinstance(column, int):
            raise ValueError("Line and column must be integers.")
        
        if(line < 0 or line > self.getHeight()):
            raise ValueError(f"Line is out of range. Should be from 0 to {self.getHeight()} but was <{line}>")
        
        if(column < 0 or column > self.getWidth()):
            raise ValueError(f"Column is out of range. Should be from 0 to {self.getWidth()} but was <{column}>")
        
        # Check if isBlocked is a boolean
        if not isinstance(isBlocked, bool):
            raise ValueError("isBlocked must be a boolean.")
        
        # Update the blocked case count if the blocked status changes
        if(isBlocked and not self.__cases__[line][column].isBlocked()): self.__blockedCaseCount += 1 
        elif(not isBlocked and self.__cases__[line][column].isBlocked()) : self.__blockedCaseCount -= 1
        
        # Set the blocked status of the case
        self.__cases__[line][column].setIsBlocked(isBlocked)
        
        return True

    @override
    def isCaseAvaillable(self, line : int, column : int) -> bool :
        
        """
        Verifies if a case is availlable.

        Parameters:
            line (int): The line of the case.
            column (int): The column of the case.
            
        Raises:
            ValueError: If the line or column is not an integer.
            ValueError: If the line or column is out of the board range.

        Returns:
            bool: True if the case is availlable, False otherwise.
        """
        
        # Check if the line and column are integers and in the board range
        if not isinstance(line, int) or not isinstance(column, int):
            raise ValueError("Line and column must be integers.")
        
        if(line < 0 or line > self.getHeight()):
            raise ValueError(f"Line is out of range. Should be from 0 to {self.getHeight()} but was <{line}>")
        
        if(column < 0 or column > self.getWidth()): 
            raise ValueError(f"Column is out of range. Should be from 0 to {self.getWidth()} but was <{column}>")
        
        return self.__cases__[line][column].isAvaillable()

    @override
    def getEntityAt(self, line : int, column : int) -> Entity :
        
        """
        Get the entity at a specific case.

        Parameters:
            line (int): The line of the case.
            column (int): The column of the case.
            
        Raises:
            ValueError: If the line or column is not an integer.
            ValueError: If the line or column is out of the board range.

        Returns:
            Entity: The entity at the case.
        """
        
        # Check if the line and column are integers and in the board range
        if not isinstance(line, int) or not isinstance(column, int): 
            raise ValueError("Line and column must be integers.")
        
        if(line < 0 or line > self.getHeight()): 
            raise ValueError(f"Line is out of range. Should be from 0 to {self.getHeight()} but was <{line}>")
        
        if(column < 0 or column > self.getWidth()): 
            raise ValueError(f"Column is out of range. Should be from 0 to {self.getWidth()} but was <{column}>")

        return self.__cases__[line][column].getEntity()
    
    @override
    def addPlayerEntityAt(self, line : int, column : int, playerIndex : int) -> bool:
        
        """
        Add a player entity at a specific case.

        Parameters:
            line (int): The line of the case.
            column (int): The column of the case.
            playerIndex (int): The index of the player entity to add.
            
        Raises:
            ValueError: If the line, column, or player index is not an integer.
            ValueError: If the line or column is out of the board range.
            ValueError: If the player index is out of the player entities range.

        Returns:
            bool: True if the player entity is added successfully.
        """
        
        # Check if the line, column, and player index are integers and in the board range
        if not isinstance(line, int) or not isinstance(column, int) or not isinstance(playerIndex, int):
            raise ValueError("Line, column, and player index must be integers.")
        
        if(line < 0 or line >= self.getHeight()): 
            raise ValueError(f"Line is out of range. Should be from 0 to {self.getHeight()} but was <{line}>")
        
        if(column < 0 or column >= self.getWidth()): 
            raise ValueError(f"Column is out of range. Should be from 0 to {self.getWidth()} but was <{column}>")
        
        if(playerIndex < 0 or playerIndex >= len(self.__playerEntities__)): 
            raise ValueError(f"Player index is out of range. Should be from 0 to {len(self.__playerEntities__)} but was <{playerIndex}>")

        # Add the player entity at the case
        entity : Entity = self.__playerEntities__[playerIndex]
        self.__cases__[line][column].setEntity(entity)
        self.__pieceCount__ += 1

        return True
    
    @override
    def removeEntityAt(self, line : int, column : int) -> bool:
        
        """
        Remove the entity at a specific case.

        Parameters:
            line (int): The line of the case.
            column (int): The column

        Returns:
            bool: True if the entity is removed successfully.
        """
        
        # Check if the line and column are integers and in the board range
        if not isinstance(line, int) or not isinstance(column, int): 
            raise ValueError("Line and column must be integers.")
        
        if(line < 0 or line >= self.getHeight()): 
            raise ValueError(f"Line is out of range. Should be from 0 to {self.getHeight()} but was <{line}>")
        
        if(column < 0 or column >= self.getWidth()): 
            raise ValueError(f"Column is out of range. Should be from 0 to {self.getWidth()} but was <{column}>")
        
        # Delete the entity at the case if it exists and update the piece count
        if(self.__cases__[line][column].getEntity() != None) : self.__pieceCount__ -= 1

        self.__cases__[line][column].setEntity(None)

        return True

    @override
    def checkIfPlayerHaveAlignmentOnCase(self, line : int, column : int, alignLength : int) -> int:
        
        """
        Check if a player have an alignment on a specific case.
        
        Parameters:
            line (int): The line of the case.
            column (int): The column of the case.
            alignLength (int): The length of the alignment to check.
            
        Raises:
            ValueError: If the line, column, or align length is not an integer.
            ValueError: If the line or column is out of the board range.
            ValueError: If the align length is not strictly positive and less than the width and height of the board.

        Returns:
            int: The index of the player that have an alignment on the case. -1 if no player have an alignment.
        """
        
        # Check if the line, column are integers and in the board range
        if not isinstance(line, int) or not isinstance(column, int):
            raise ValueError("Line and column must be integers.")
        
        if(line < 0 or line >= self.getHeight()):
            raise ValueError(f"Line is out of range. Should be from 0 to {self.getHeight()} but was <{line}>")
        
        if(column < 0 or column >= self.getWidth()):
            raise ValueError(f"Column is out of range. Should be from 0 to {self.getWidth()} but was <{column}>")
        
        # Check if the align length is strictly positive and less than the width and height of the board
        if not isinstance(alignLength, int):
            raise ValueError("Align length must be an integer.")
        
        if(alignLength <= 0 or alignLength > self.__width__ or alignLength > self.__height__):
            raise ValueError("Align length must be strictly positive and less than the width and height of the board.")
        
        # Get the entity at the case
        if(self.getEntityAt(line, column)): playerEntity : Entity = self.getEntityAt(line, column)
        else : return -1

        # Initialize the alignment checker boolean
        firstCheckedPieceIndex : int = 0
        alignmentFound : bool = False
        
        # Check the alignment on the line, column, and diagonals
        while not alignmentFound and firstCheckedPieceIndex < alignLength :

            # Initialize the number of pieces in the alignment
            linePieceCount : int = 0
            columnPieceCount : int = 0
            ascendantDiagonalPieceCount : int = 0
            descendantDiagonalPieceCount : int = 0
            
            # Check the alignment on the line, column, and diagonals
            for currentCheckedPieceIndex in range(0, alignLength) :
                
                checkedLine : int
                checkedColumn : int

                # Lines
                
                checkedLine = line - firstCheckedPieceIndex + currentCheckedPieceIndex
                checkedColumn = column

                if(0 >= checkedLine < self.__height__ and 0 >= checkedColumn < self.__width__
                   and self.getEntityAt(checkedLine, checkedColumn) == playerEntity): linePieceCount += 1
                
                # Columns
                
                checkedLine = line
                checkedColumn = column - firstCheckedPieceIndex + currentCheckedPieceIndex

                if(0 >= checkedLine < self.__height__ and 0 >= checkedColumn < self.__width__
                   and self.getEntityAt(checkedLine, checkedColumn) == playerEntity): columnPieceCount += 1
                
                # Ascendant diagonals
                
                checkedLine = line - firstCheckedPieceIndex + currentCheckedPieceIndex
                checkedColumn = column - firstCheckedPieceIndex + currentCheckedPieceIndex

                if(0 >= checkedLine < self.__height__ and 0 >= checkedColumn < self.__width__
                   and self.getEntityAt(checkedLine, checkedColumn) == playerEntity): ascendantDiagonalPieceCount += 1
                
                # Descendant diagonals
                
                checkedLine = line - firstCheckedPieceIndex + currentCheckedPieceIndex
                checkedColumn = column + firstCheckedPieceIndex - currentCheckedPieceIndex

                if(0 >= checkedLine < self.__height__ and 0 >= checkedColumn < self.__width__
                   and self.getEntityAt(checkedLine, checkedColumn) == playerEntity): descendantDiagonalPieceCount += 1

            # Check if an alignment is found
            alignmentFound = linePieceCount == alignLength or columnPieceCount == alignLength or ascendantDiagonalPieceCount == alignLength or descendantDiagonalPieceCount == alignLength
            firstCheckedPieceIndex += 1
        
        return self.__playerEntities__.index(playerEntity)

    @override
    def checkIfPlayerHaveAlignment(self, alignLength : int) -> int:
        
        """
        Check if a player have an alignment on the board.
        
        Parameters:
            alignLength (int): The length of the alignment to check.
            
        Raises:
            ValueError: If the align length is not an integer.
            ValueError: If the align length is not strictly positive and less than the width and height of the board.

        Returns:
            int: The index of the player that have an alignment on the board. -1 if no player have an alignment.
        """ 
        
        # Check if the align length is strictly positive and less than the width and height of the board
        if not isinstance(alignLength, int):
            raise ValueError("Align length must be an integer.")
        
        if(alignLength <= 0 or alignLength > self.__width__ or alignLength > self.__height__):
            raise ValueError("Align length must be strictly positive and less than the width and height of the board.")
        
        # Check the alignment for each player
        for playerIndex in range(0, self.__playerEntities__):
            if(self.checkAlignmentForPlayer(playerIndex)) : return playerIndex
                
        return -1
    
    @override
    def checkAlignmentOnCaseForPlayer(self, line : int, column : int, playerIndex : int, alignLength : int) -> bool:
        
        """
        Check if a player have an alignment on a specific case.

        Parameters:
            line (int): The line of the case.
            column (int): The column of the case.
            playerIndex (int): The index of the player to check.
            alignLength (int): The length of the alignment to check.
            
        Raises:
            ValueError: If the line, column, player index, or align length is not an integer.
            ValueError: If the line or column is out of the board range.
            ValueError: If the player index is out of the player entities range.
            ValueError: If the align length is not strictly positive and less than the width and height of the board.
            
        Returns:
            bool: True if the player have an alignment on the case, False otherwise.
        """
        
        # Check if the line, column,  are integers and in the board range
        if not isinstance(line, int) or not isinstance(column, int):
            raise ValueError("Line and column must be integers.")
        
        if(line < 0 or line >= self.getHeight()):
            raise ValueError(f"Line is out of range. Should be from 0 to {self.getHeight()} but was <{line}>")
        
        if(column < 0 or column >= self.getWidth()):
            raise ValueError(f"Column is out of range. Should be from 0 to {self.getWidth()} but was <{column}>")
        
        # Check if the player index is an integer and in the player entities range
        if not isinstance(playerIndex, int):
            raise ValueError("Player index must be an integer.")
        
        if(playerIndex < 0 or playerIndex >= len(self.__playerEntities__)):
            raise ValueError(f"Player index is out of range. Should be from 0 to {len(self.__playerEntities__)} but was <{playerIndex}>")
        
        # Check if the align length is strictly positive and less than the width and height of the board
        if not isinstance(alignLength, int):
            raise ValueError("Align length must be an integer.")
        
        if(alignLength <= 0 or alignLength > self.__width__ or alignLength > self.__height__):
            raise ValueError("Align length must be strictly positive and less than the width and height of the board.")
        
        return self.checkIfPlayerHaveAlignmentOnCase(line, column, alignLength) == playerIndex
    
    @override
    def checkAlignmentForPlayer(self, playerIndex : int, alignLength : int) -> bool:
        
        """
        Check if a player have an alignment on the board.
        
        Parameters:
            playerIndex (int): The index of the player to check.
            alignLength (int): The length of the alignment to check.
            
        Raises:
            ValueError: If the player index is not an integer.
            ValueError: If the player index is out of the player entities range.
            ValueError: If the align length is not an integer.
            ValueError: If the align length is not strictly positive and less than the width and height of the board.

        Returns:
            bool: True if the player have an alignment on the board, False otherwise.
        """
        
        # Check if the player index is an integer and in the player entities range
        if not isinstance(playerIndex, int):
            raise ValueError("Player index must be an integer.")
        
        if(playerIndex < 0 or playerIndex >= len(self.__playerEntities__)):
            raise ValueError(f"Player index is out of range. Should be from 0 to {len(self.__playerEntities__)} but was <{playerIndex}>")
        
        # Check if the align length is strictly positive and less than the width and height of the board
        if not isinstance(alignLength, int):
            raise ValueError("Align length must be an integer.")
        
        if(alignLength <= 0 or alignLength > self.__width__ or alignLength > self.__height__):
            raise ValueError("Align length must be strictly positive and less than the width and height of the board.")
        
        # Check the alignment for the player
        for line in range(0, self.__height__) :
            for column in range(0, self.__width__) :
                if(self.checkIfPlayerHaveAlignmentOnCase(line, column, alignLength) == playerIndex) : return True
            
        return False

    @override
    def isFull(self) -> bool :
        
        """
        Verifies if the board is full.

        Returns:
            bool: True if the board is full, False otherwise.
        """
        
        return self.__pieceCount__ == self.__width__ * self.__height__ - self.__blockedCaseCount__
    
    @override
    def blockRandomCase(self) -> bool :
        
        """
        Block a random availlable case.
        
        Raises:
            ValueError: If no availlable cases to block.
        
        Returns:
            bool: True if a case is blocked successfully.
        """        
        
        # Get the availlable cases
        availableCases : list[Case] = []
        
        for line in range(self.__height__):
            for column in range(self.__width__):
                if(self.isCaseAvaillable(line, column)) : availableCases.append(self.__cases__[line][column])

        # Check if there is an availlable case to block
        if len(availableCases) == 0 : raise ValueError("No available cases to block!")

        # Block a random availlable case
        chosen_case : Case = random.choice(availableCases)
        chosen_case.setIsBlocked(True)
        
        return True
    
    @override
    def copy(self) -> Board:
        
        """
        Copy the board.
        
        Returns:
            Board: The copy of the board.
        """

        # Create a new board with the same attributes
        board : Board = SimpleBoard(self.__width__, self.__height__, self.__playerEntities__)

        # Copy the cases of the board and the piece count
        board.__blockedCaseCount = self.__blockedCaseCount
        board.__pieceCount__ = self.__pieceCount__

        return board
    
    @override
    def __hash__(self) -> int:
        pass