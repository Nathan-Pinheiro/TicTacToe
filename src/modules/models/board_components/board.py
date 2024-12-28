## Interface

"""
Board Module

This module provides a class to represent a board.

Classes:
    Board: Represents a board.
    
    Attributes:
        width (int): The width of the board.
        height (int): The height of the board.

Methods:
    initializeBoard() -> None:
        Private method.
        Initialize the board.
        
        Returns:
            None

    getCase(line: int, column: int) -> Case:
        Get the case at the given line and column.
        
        Args:
            line (int): The line of the case to get.
            column (int): The column of the case to get.
        
        Returns:
            Case: The case at the given line and column.
"""

# ---------------------------------------------------------------------------------------------------- #

## Implementation

# ---------------------------------------------------------------------------------------------------- #

# Import #

from __future__ import annotations

from modules.models.board_components.entity import Entity
from modules.utils.decorator import private_method

# ---------------------------------------------------------------------------------------------------- #

# Class #

class Board:
    """
    Represents a game board.

    Attributes:
        __width__ (int): The width of the board.
        __height__ (int): The height of the board.
        __player_entities__ (list[Entity]): A list of player entities present on the board.
    """
    
    def __init__(self, width: int, height: int, player_entities: list[Entity]) -> None:
        """
        Initializes a new instance of the Board class.

        Args:
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

    def isCaseAvaillable(self, line: int, column: int) -> bool:
        """
        Checks if a case at the specified line and column is available.

        Args:
            line (int): The line number of the case.
            column (int): The column number of the case.

        Returns:
            bool: True if the case is available, False otherwise.
        """
        pass

    def isCaseBlocked(self, line: int, column: int) -> bool:
        """
        Checks if a case at the specified line and column is blocked.

        Args:
            line (int): The line number of the case.
            column (int): The column number of the case.

        Returns:
            bool: True if the case is blocked, False otherwise.
        """
        pass

    def setIsCaseBlocked(self, line: int, column: int, isBlocked: bool) -> None:
        """
        Sets whether a case at the specified line and column is blocked.

        Args:
            line (int): The line number of the case.
            column (int): The column number of the case.
            isBlocked (bool): True to block the case, False to unblock it.

        Returns:
            None
        """
        pass

    def blockRandomCase(self) -> None:
        """
        Blocks a random case on the board.

        Returns:
            None
        """
        pass

    def isEntityAt(self, line: int, column: int) -> bool:
        """
        Checks if there is an entity at the specified line and column.

        Args:
            line (int): The line number of the case.
            column (int): The column number of the case.

        Returns:
            bool: True if there is an entity at the specified location, False otherwise.
        """
        pass

    def getEntityAt(self, line: int, column: int) -> Entity:
        """
        Retrieves the entity at the specified line and column.

        Args:
            line (int): The line number of the case.
            column (int): The column number of the case.

        Returns:
            Entity: The entity at the specified location.
        """
        pass

    def addPlayerEntityAt(self, line: int, column: int, playerIndex: int) -> None:
        """
        Adds a player's entity at the specified line and column.

        Args:
            line (int): The line number of the case.
            column (int): The column number of the case.
            playerIndex (int): The index of the player whose entity is being added.

        Returns:
            None
        """
        pass

    def removeEntityAt(self, line: int, column: int) -> None:
        """
        Removes an entity from the specified line and column.

        Args:
            line (int): The line number of the case.
            column (int): The column number of the case.

        Returns:
            None
        """
        pass

    def checkIfPlayerHaveAlignmentOnCase(self, alignLength: int) -> int:
        """
        Checks if any player has an alignment of the specified length, on the given case.

        Args:
            alignLength (int): The length of the alignment to check for.

        Returns:
            int: The index of the player with the alignment, or -1 if no alignment exists.
        """
        pass

    def checkAlignmentOnCaseForPlayer(self, line: int, column: int, playerIndex: int, alignLength: int) -> bool:
        """
        Checks if a player's entities are aligned at the specified case.

        Args:
            line (int): The line number of the case.
            column (int): The column number of the case.
            playerIndex (int): The index of the player.
            alignLength (int): The length of the alignment to check for.

        Returns:
            bool: True if the player's entities are aligned, False otherwise.
        """
        pass

    def checkAlignmentForPlayer(self, playerIndex: int, alignLength: int) -> bool:
        """
        Checks if a player's entities are aligned anywhere on the board.

        Args:
            playerIndex (int): The index of the player.
            alignLength (int): The length of the alignment to check for.

        Returns:
            bool: True if the player's entities are aligned, False otherwise.
        """
        pass

    def checkIfPlayerHaveAlignment(self, alignLength: int) -> int:
        """
        Checks if any player has an alignment of the specified length.

        Args:
            alignLength (int): The length of the alignment to check for.

        Returns:
            int: The index of the player with the alignment, or -1 if no alignment exists.
        """
        pass

    def isFull(self) -> bool:
        """
        Checks if the board is full.

        Returns:
            bool: True if the board is full, False otherwise.
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

    def copy(self) -> Board:
        """
        Creates a copy of the current board.

        Returns:
            Board: A copy of the current board.
        """
        pass
