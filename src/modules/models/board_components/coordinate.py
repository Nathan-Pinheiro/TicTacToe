## Interface

"""
Coordinate Module

This module provides a class to represent a coordinate.

Classes:
    Coordinate: Represents a coordinate with a column and a line.
    
    Attributes:
        column (int): The column of the coordinate.
        line (int): The line of the coordinate.

Methods:
    getLine() -> int:
        Get the line of the coordinate.
        
        Returns:
            int: The line of the coordinate.
            
    getColumn() -> int:
        Get the column of the coordinate.
        
        Returns:
            int: The column of the coordinate.
    
    setLine(line: int) -> None:
        Set the line of the coordinate.
        
        Args:
            line (int): The line of the coordinate.
        
        Returns:
            None
            
    setColumn(column: int) -> None:
        Set the column of the coordinate.
        
        Args:
            column (int): The column of the coordinate.
        
        Returns:
            iNone
"""

# ---------------------------------------------------------------------------------------------------- #

## Implementation

# Class #
class Coordinate:
    
    def __init__(self, line : int, column : int) -> None:
        """Constructor for the Coordinate class.

        Args:
            line (int): The line of the coordinate.
            column (int): The column of the coordinate.

        Returns:
            None
        """
        
        self.__line__ = line
        self.__column__ = column
        
        return None
        
    def getLine(self) -> int :
        """Get the line of the coordinate.

        Returns:
            int: The line of the coordinate.
        """
        
        return self.__line__
    
    def getColumn(self) -> int :
        """Get the column of the coordinate.

        Returns:
            int: The column of the coordinate.
        """
        
        return self.__column__
    
    def setLine(self, line : int) -> None :
        """Set the line of the coordinate.

        Args:
            line (int): The line of the coordinate.

        Returns:
            None
        """
        
        self.__line__ = line
    
    def setColumn(self, column : int) -> None :
        """Set the column of the coordinate.
        
        Args:
            column (int): The column of the coordinate.

        Returns:
            None
        """
        
        self.__line__ = column
        
    def __str__(self):
        """Return the string value of the coordinate."""
        return f"( {self.__line__} : {self.__column__} )"