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
        
        Returns:
            None
        """
        
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

        Returns:
            bool: True if the case is blocked, False otherwise.
        """
        
        pass

    @abstractmethod
    def setIsCaseBlocked(self, line: int, column: int, isBlocked: bool) -> None:
        
        """
        Sets whether a case at the specified line and column is blocked.

        Parameters:
            line (int): The line number of the case.
            column (int): The column number of the case.
            isBlocked (bool): True to block the case, False to unblock it.

        Returns:
            None
        """
        
        pass

    @abstractmethod
    def blockRandomCase(self) -> None:
        
        """
        Blocks a random case on the board.

        Returns:
            None
        """
        
        pass

    @abstractmethod
    def isEntityAt(self, line: int, column: int) -> bool:
        
        """
        Checks if there is an entity at the specified line and column.

        Parameters:
            line (int): The line number of the case.
            column (int): The column number of the case.

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

        Returns:
            Entity: The entity at the specified location.
        """
        
        pass

    @abstractmethod
    def addPlayerEntityAt(self, line: int, column: int, playerIndex: int) -> None:
        
        """
        Adds a player's entity at the specified line and column.

        Parameters:
            line (int): The line number of the case.
            column (int): The column number of the case.
            playerIndex (int): The index of the player whose entity is being added.

        Returns:
            None
        """
        
        pass
    
    @abstractmethod
    def addEntityAt(self, line: int, column: int, entity : Entity) -> None:
        
        """
        Adds an entity at the specified line and column.

        Parameters:
            line (int): The line number of the case.
            column (int): The column number of the case.
            playerIndex (int): The index of the player whose entity is being added.

        Returns:
            None
        """
        
        pass

    @abstractmethod
    def removeEntityAt(self, line: int, column: int) -> None:
        
        """
        Removes an entity from the specified line and column.

        Parameters:
            line (int): The line number of the case.
            column (int): The column number of the case.

        Returns:
            None
        """
        
        pass

    @abstractmethod
    def checkIfPlayerHaveAlignmentOnCase(self, alignLength: int) -> int:
        
        """
        Checks if any player has an alignment of the specified length, on the given case.

        Parameters:
            alignLength (int): The length of the alignment to check for.

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

        Returns:
            int: The number of valid lines.
        """
        
        pass

    @abstractmethod
    def isFull(self) -> bool:
        
        """
        Checks if the board is full.

        Returns:
            bool: True if the board is full, False otherwise.
        """
        
        pass

    @abstractmethod
    def getPieceCount(self) -> int:
        
        """
        Return the amount of pieces on the board.

        Returns:
            pieceCount (int) : the amount of pieces on the board.
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
        Generate a hash of the current board

        Returns:
            int : A hash of the current board.
        """
        
        pass 