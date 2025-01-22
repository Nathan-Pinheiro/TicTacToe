from modules.models.board_game.components.coordinate import Coordinate
from modules.utils.decorator import privatemethod

# ************************************************
# Module coordinate encoder
# ************************************************
# ROLE : This module allows encoding and decoding coordinates
# ************************************************
# VERSION : 1.0
# AUTHOR : Nathan PINHEIRO
# DATE : 13/01/2025
# ************************************************

def encode(coordinate: Coordinate) -> str:
    
    """
    Encode a coordinate into a string.

    Parameters:
        coordinate (Coordinate): The coordinate to be encoded.
        
    Raises:
        TypeError: If coordinate is not an instance of Coordinate.

    Returns:
        str: The encoded coordinate.
    """
    
    # Check if coordinate is an instance of Coordinate
    if not isinstance(coordinate, Coordinate):
        raise TypeError("coordinate must be an instance of Coordinate")
    
    return __numberToLetter__(coordinate.getColumn() + 1) + str(coordinate.getLine() + 1)

def decode(coordinateCode: str) -> Coordinate:
    
    """
    Decode a string into a coordinate.

    Parameters:
        coordinateCode (str): The string to be decoded, must be a letter mapped between 'a' and 'z' and followed by a number.
        
    Raises:
        TypeError: If coordinateCode is not a string.
        ValueError: If coordinateCode is invalid.

    Returns:
        Coordinate: The decoded coordinate.
    """
    
    # Check if coordinateCode is a string
    if not isinstance(coordinateCode, str):
        raise TypeError("coordinateCode must be a string")
    
    # Validate the coordinate code
    if len(coordinateCode) < 2:
        raise ValueError("Coordinate code too short")
    if not coordinateCode[0].isalpha() or not coordinateCode[1:].isdigit():
        raise ValueError("Invalid coordinate code")
    if int(coordinateCode[1:]) < 1:
        raise ValueError("Invalid coordinate code")
    if __letterToNumber__(coordinateCode[0]) > 26:
        raise ValueError("Invalid coordinate code")
    if int(coordinateCode[1:]) > 26:
        raise ValueError("Invalid coordinate code")
    
    return Coordinate(__letterToNumber__(coordinateCode[0]), int(coordinateCode[1:]))

@privatemethod
def __numberToLetter__(number: int) -> str:
    
    """
    Convert a number to a letter.

    Parameters:
        number (int): A number between 1 and 26, where 1 maps to 'a' and 26 maps to 'z'.
        
    Raises:
        TypeError: If number is not an integer.
        ValueError: If number is out of range.

    Returns:
        str: The corresponding letter for the number.
    """
    
    # Check if number is an integer and within the valid range
    if not isinstance(number, int):
        raise TypeError("number must be an integer")
    
    if number < 1 or number > 26:
        raise ValueError("Number out of range (must be 1-26)")
    
    return chr(number + 96)

@privatemethod
def __letterToNumber__(letter: str) -> int:
    
    """
    Convert a letter to a number.

    Parameters:
        letter (str): A letter between 'a' and 'z', where 'a' maps to 1 and 'z' maps to 26.
        
    Raises:
        TypeError: If letter is not a string.
        ValueError: If letter is out of range.

    Returns:
        int: The corresponding number for the letter.
    """
    
    # Check if letter is a string and within the valid range
    if not isinstance(letter, str):
        raise TypeError("letter must be a string")
    
    if letter < 'a' or letter > 'z':
        raise ValueError("Letter out of range (must be 'a'-'z')")
    
    return ord(letter) - 96