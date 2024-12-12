## Interface

"""
Coordinate Encoder Module

This module provides functions to encode and decode coordinates, as well as utility functions to convert between numbers and letters.

Classes:
    Coordinate: Represents a coordinate with a column and a line.
    
    Attributes:
        column (int): The column of the coordinate.
        line (int): The line of the coordinate.

Functions:
    encode(coordinate: Coordinate) -> str:
        Encode a coordinate into a string.
        
        Args:
            coordinate (Coordinate): The coordinate to be encoded.
            
        Returns:
            str: The encoded coordinate

    decode(coordinateCode: str) -> Coordinate:
        Decode a string into a coordinate.
        
        Args:
            coordinateCode (str): The string to be decoded, must be a letter mapped enter 'a' and 'z' and followed by a number.
            
        Returns:
            Coordinate: The decoded coordinate.

    numberToLetter(n: int) -> str:
        Private method.
        Convert a number to a letter.
        
        Args:
            n (int): A number between 1 and 26, where 1 maps to 'a' and 26 maps to 'z'.
            
        Returns:
            str: The corresponding letter for the number.

    letterToNumber(letter: str) -> int:
        Private method.
        Convert a letter to a number.
        
        Args:
            letter (str): A letter between 'a' and 'z', where 'a' maps to 1 and 'z' maps to 26.
            
        Returns:
            int: The corresponding number for the letter.
"""

# ---------------------------------------------------------------------------------------------------- #

## Implementation

# Import #
from modules.models.coordinate import Coordinate
from modules.utils.decorator import private_method

# Functions #
def encode(coordinate : Coordinate) -> str :
    """Encode a coordinate into a string.

    Args:
        coordinate (Coordinate): The coordinate to be encoded.

    Returns:
        str: The encoded coordinate.
    """
    
    return __numberToLetter__(coordinate.getColumn() + 1) + str(coordinate.getLine() + 1)

def decode(coordinateCode : str) -> Coordinate :
    """Decode a string into a coordinate.

    Args:
        coordinateCode (str): The string to be decoded, must be a letter mapped enter 'a' and 'z' and followed by a number.

    Returns:
        Coordinate: The decoded coordinate.
    """
    
    if len(coordinateCode) < 2 : raise ValueError("Coordinate code too short")
    if not coordinateCode[0].isalpha() or not coordinateCode[1:].isdigit() : raise ValueError("")
    if int(coordinateCode[1:]) < 1 : raise ValueError("Invalid coordinate code")
    if __letterToNumber__(coordinateCode[0]) > 26 : raise ValueError("Invalid coordinate code")
    if int(coordinateCode[1:]) > 26 : raise ValueError("Invalid coordinate code")
    
    return Coordinate(__letterToNumber__(coordinateCode[0]), int(coordinateCode[1:]))

@private_method
def __numberToLetter__(n: int) -> str:
    """Convert a number to a letter.

    Args:
        n (int): A number between 1 and 26, where 1 maps to 'a' and 26 maps to 'z'.

    Returns:
        str: The corresponding letter for the number.

    Raises:
        ValueError: If the number is not in the range 1-26.
    """

    if n < 1 or n > 26 : raise ValueError("Number out of range (must be 1-26)")
    return chr(n + 96)

@private_method
def __letterToNumber__(letter: str) -> int:
    """Convert a letter to a number.

    Args:
        letter (str): A letter between 'a' and 'z', where 'a' maps to 1 and 'z' maps to 26.

    Returns:
        int: The corresponding number for the letter.

    Raises:
        ValueError: If the letter is not in the range 'a'-'z'.
    """

    if letter < 'a' or letter > 'z' : raise ValueError("Letter out of range (must be 'a'-'z')")
    return ord(letter) - 96