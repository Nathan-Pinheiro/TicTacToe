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

    def __init__(self, line : int, column : int) -> None:
        
        """
        Constructor for the Coordinate class.

        Parameters:
            line (int): The line of the coordinate.
            column (int): The column of the coordinate.

        Returns:
            None
        """
        
        self.__line__ = line
        self.__column__ = column
        
        return None
        
    def getLine(self) -> int :
        
        """
        Get the line of the coordinate.

        Returns:
            int: The line of the coordinate.
        """
        
        return self.__line__
    
    def getColumn(self) -> int :
        
        """
        Get the column of the coordinate.

        Returns:
            int: The column of the coordinate.
        """
        
        return self.__column__
    
    def setLine(self, line : int) -> None :
        
        """
        Set the line of the coordinate.

        Parameters:
            line (int): The line of the coordinate.

        Returns:
            None
        """
        
        self.__line__ = line
        
        return None
    
    def setColumn(self, column : int) -> None :
        
        """
        Set the column of the coordinate.
        
        Parameters:
            column (int): The column of the coordinate.

        Returns:
            None
        """
        
        self.__line__ = column
        
        return None
        
    def __str__(self) -> str:
        
        """
        Return the string value of the coordinate.
        
        Returns:
            str: The string value of the coordinate.
        """
        
        return f"( {self.__line__} : {self.__column__} )"