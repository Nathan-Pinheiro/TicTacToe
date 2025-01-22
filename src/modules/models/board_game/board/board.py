from __future__ import annotations

from modules.models.board_game.components.entity import Entity
from modules.utils.decorator import privatemethod
from abc import ABC, abstractmethod

class Board(ABC):
    
    """
    Represents a game board.
    """
    
    def __init__(self, width: int, height: int, player_entities: list[Entity]) -> None:
        
        """
        Initializes a new instance of the Board class.

        Parameters:
            width (int): The width of the board.
            height (int): The height of the board.
            player_entities (list[Entity]): A list of player entities to initialize the board with.
            
        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than or equal to 0.
            TypeError: If player_entities is not a list of Entity instances.
        
        Returns:
            None
        """
        
        # Check if width and height are integers and greater than 0
        if not isinstance(width, int) or not isinstance(height, int):
            raise TypeError("width and height must be integers")
        
        if width <= 0 or height <= 0:
            raise ValueError("width and height must be greater than 0")
        
        # Check if player_entities is a list of Entity instances
        if not isinstance(player_entities, list) or not all(isinstance(entity, Entity) for entity in player_entities):
            raise TypeError("player_entities must be a list of Entity instances")
        
        # Initialize the attributes
        self.__width__: int = width
        self.__height__: int = height
        self.__playerEntities__: list[Entity] = player_entities
        
        return None

    @abstractmethod
    def isCaseAvaillable(self, line: int, column: int) -> bool:
        
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
        
        pass

    @abstractmethod
    def isCaseBlocked(self, line: int, column: int) -> bool:
        
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
        
        pass

    @abstractmethod
    def setIsCaseBlocked(self, line: int, column: int, isBlocked: bool) -> bool:
        
        """
        Sets whether a case at the specified line and column is blocked.

        Parameters:
            line (int): The line number of the case.
            column (int): The column number of the case.
            isBlocked (bool): True to block the case, False to unblock it.
            
        Raises:
            TypeError: If line or column is not an integer.
            ValueError: If line or column is out of range.
            TypeError: If isBlocked is not a boolean.

        Returns:
            bool: True if the case is blocked.
        """
        
        pass

    @abstractmethod
    def blockRandomCase(self) -> bool:
        
        """
        Blocks a random case on the board.
        
        Raises:
            ValueError: If there are no available cases to block.

        Returns:
            bool: True if a case is blocked.
        """
        
        pass

    @abstractmethod
    def isEntityAt(self, line: int, column: int) -> bool:
        
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
        
        pass

    @abstractmethod
    def getEntityAt(self, line: int, column: int) -> Entity:
        
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
        
        pass

    @abstractmethod
    def addPlayerEntityAt(self, line: int, column: int, playerIndex: int) -> bool:
        
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
            bool: True if the entity is added.
        """
        
        pass
    
    @abstractmethod
    def addEntityAt(self, line: int, column: int, entity : Entity) -> bool:
        
        """
        Adds an entity at the specified line and column.

        Parameters:
            line (int): The line number of the case.
            column (int): The column number of the case.
            entity (Entity): The entity to be added.
            
        Raises:
            TypeError: If line or column is not an integer.
            ValueError: If line or column is out of range.
            TypeError: If entity is not an instance of Entity.
            ValueError: If the entity is not found in the player entities list.

        Returns:
            bool: True if the entity is added.
        """
        
        pass

    @abstractmethod
    def removeEntityAt(self, line: int, column: int) -> bool:
        
        """
        Removes an entity from the specified line and column.

        Parameters:
            line (int): The line number of the case.
            column (int): The column number of the case.
            
        Raises:
            TypeError: If line or column is not an integer.
            ValueError: If line or column is out of range.

        Returns:
            bool: True if the entity is removed.
        """
        
        pass

    @abstractmethod
    def checkIfPlayerHaveAlignmentOnCase(self, line: int, column: int, alignLength: int) -> int:
        
        """
        Checks if a player has an alignment of the specified length on a specific case.

        Parameters:
            line (int): The line number of the case.
            column (int): The column number of the case.
            alignLength (int): The length of the alignment to check.
            
        Raises:
            TypeError: If line, column, or alignLength is not an integer.
            ValueError: If line or column is out of range.
            ValueError: If alignLength is less than or equal to 0 or greater than the board dimensions.

        Returns:
            int: The index of the player with the alignment, or -1 if no alignment exists.
        """
        
        pass

    @abstractmethod
    def checkAlignmentOnCaseForPlayer(self, line: int, column: int, playerIndex: int, alignLength: int) -> bool:
        
        """
        Checks if a player's entities are aligned at the specified case.

        Parameters:
            line (int): The line number of the case.
            column (int): The column number of the case.
            playerIndex (int): The index of the player.
            alignLength (int): The length of the alignment to check for.
            
        Raises:
            TypeError: If line, column, playerIndex, or alignLength is not an integer.
            ValueError: If line or column is out of range.
            ValueError: If playerIndex is out of range.
            ValueError: If alignLength is less than or equal to 0 or greater than the board dimensions.

        Returns:
            bool: True if the player's entities are aligned, False otherwise.
        """
        
        pass

    @abstractmethod
    def checkAlignmentForPlayer(self, playerIndex: int, alignLength: int) -> bool:
        
        """
        Checks if a player's entities are aligned anywhere on the board.

        Parameters:
            playerIndex (int): The index of the player.
            alignLength (int): The length of the alignment to check for.
            
        Raises:
            TypeError: If playerIndex or alignLength is not an integer.
            ValueError: If playerIndex is out of range.
            ValueError: If alignLength is less than or equal to 0 or greater than the board dimensions.

        Returns:
            bool: True if the player's entities are aligned, False otherwise.
        """
        
        pass

    @abstractmethod
    def checkIfPlayerHaveAlignment(self, alignLength: int) -> int:
        
        """
        Checks if any player has an alignment of the specified length.

        Parameters:
            alignLength (int): The length of the alignment to check for.
            
        Raises:
            TypeError: If alignLength is not an integer.
            ValueError: If alignLength is less than or equal to 0 or greater than the board dimensions.

        Returns:
            int: The index of the player with the alignment, or -1 if no alignment exists.
        """
        
        pass

    @abstractmethod
    def countAvaillableLineOfAtLeastGivenPiece(self, playerIndex: int, alignLength: int, pieceCount: int) -> int:
        
        """
        Returns the number of lines that contain at least a given amount of the player's pieces and no opponent pieces.

        Parameters:
            playerIndex (int): The player's index.
            alignLength (int): Required alignment length to win.
            pieceCount (int): Minimum number of the player's pieces required.
            
        Raises:
            TypeError: If playerIndex, alignLength, or pieceCount is not an integer.
            ValueError: If playerIndex is out of range.
            ValueError: If alignLength is less than or equal to 0 or greater than the board dimensions.
            ValueError: If pieceCount is less than or equal to 0.

        Returns:
            int: The number of valid lines.
        """
        
        pass

    @abstractmethod
    def isFull(self) -> bool:
        
        """
        Checks if the board is completely filled.

        Returns:
            bool: True if the board is full, False otherwise.
        """
        
        pass

    @abstractmethod
    def getPieceCount(self) -> int:
        
        """
        Returns the amount of pieces on the board.

        Returns:
            pieceCount (int): The amount of pieces on the board.
        """
        
        pass
    
    @abstractmethod
    def getPlayerCount(self) -> int:
        
        """
        Return the amount of players on the board.

        Returns:
            playerCount (int) : the amount of players on the board.
        """

        pass
    
    @abstractmethod
    def getCountCaseAvaillable(self) -> int:
        
        """
        Returns the amount of availlable cases on the board.

        Returns:
            caseCount (int) : the amount of availlable cases on the board.
        """

        pass

    def getWidth(self) -> int:
        
        """
        Gets the width of the board.

        Returns:
            int: The width of the board.
        """
        
        return self.__width__

    def getHeight(self) -> int:
        
        """
        Gets the height of the board.

        Returns:
            int: The height of the board.
        """
        
        return self.__height__

    def getPlayerEntities(self) -> list[Entity]:
        
        """
        Gets the list of player entities on the board.

        Returns:
            list[Entity]: The list of player entities.
        """
        
        return self.__playerEntities__

    @abstractmethod
    def copy(self) -> Board:
        
        """
        Creates a copy of the current board.

        Returns:
            Board: A copy of the current board.
        """
        
        pass

    @abstractmethod
    def __hash__(self) -> int:
        
        """
        Generates a hash of the current board.

        Returns:
            int: A hash of the current board.
        """
        
        pass