# ************************************************
# CLASS Coordinate
# ************************************************
# ROLE : This class is used to store coordinates
# ************************************************
# VERSION : 1.0
# AUTHOR : Nathan PINHEIRO
# DATE : 13/01/2025
# ************************************************

class Coordinate:
    
    """
    A class that represent coordinates
    """

    def __init__(self, line: int, column: int) -> None:
        
        """
        Constructor for the Coordinate class.

        Parameters:
            line (int): The line of the coordinate.
            column (int): The column of the coordinate.
            
        Raises:
            TypeError: If line or column is not an integer.
            ValueError: If line or column is less than 0.

        Returns:
            None
        """
        
        # Check if line and column are integers and greater than or equal to 0
        if not isinstance(line, int) or not isinstance(column, int):
            raise TypeError("line and column must be integers")
        
        if line < 0 or column < 0:
            raise ValueError("line and column must be greater than or equal to 0")
        
        # Initialize the attributes
        self.__line__ = line
        self.__column__ = column
        
        return None
        
    def getLine(self) -> int:
        
        """
        Get the line of the coordinate.

        Returns:
            int: The line of the coordinate.
        """
        
        return self.__line__
    
    def getColumn(self) -> int:
        
        """
        Get the column of the coordinate.

        Returns:
            int: The column of the coordinate.
        """
        
        return self.__column__
    
    def setLine(self, line: int) -> bool:
        
        """
        Set the line of the coordinate.

        Parameters:
            line (int): The line of the coordinate.
            
        Raises:
            TypeError: If line is not an integer.
            ValueError: If line is less than 0.

        Returns:
            bool: True if the line is set successfully.
        """
        
        # Check if line is an integer and greater than or equal to 0
        if not isinstance(line, int):
            raise TypeError("line must be an integer")
        
        if line < 0:
            raise ValueError("line must be greater than or equal to 0")
        
        # Set the line
        self.__line__ = line
        
        return True
    
    def setColumn(self, column: int) -> bool:
        
        """
        Set the column of the coordinate.
        
        Parameters:
            column (int): The column of the coordinate.
            
        Raises:
            TypeError: If column is not an integer.
            ValueError: If column is less than 0.

        Returns:
            bool: True if the column is set successfully.
        """
        
        # Check if column is an integer and greater than or equal to 0
        if not isinstance(column, int):
            raise TypeError("column must be an integer")
        
        if column < 0:
            raise ValueError("column must be greater than or equal to 0")
        
        # Set the column
        self.__column__ = column
        
        return True
        
    def __str__(self) -> str:
        
        """
        Return the string value of the coordinate.
        
        Returns:
            str: The string value of the coordinate.
        """
        
        return f"( {self.__line__} : {self.__column__} )"