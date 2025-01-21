import re

def isHexColor(color: str) -> bool:
    
    """
    Validates if a color is a valid hexadecimal color.
    
    Parameters:
        color (str): The color to validate.
    
    Returns:
        bool: True if the color is valid, False otherwise.
    """
    
    return bool(re.match(r'^#(?:[0-9a-fA-F]{3}){1,2}$', color))

def isValidSymbol(symbol: str) -> bool:
    
    """
    Validates if a symbol is a valid symbol.
    
    Parameters:
        symbol (str): The symbol to validate.
    
    Returns:
        bool: True if the symbol is valid, False otherwise
    """
    
    valid_symbols = {'X', 'O', '△', '⬡', '★', '▢', '◊', "#", ""}
    return symbol in valid_symbols