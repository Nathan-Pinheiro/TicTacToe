import re

## Validate if a color is in hexadecimal format.
#
# @param color The color string to validate.
# @return bool True if the color is valid, False otherwise.
def is_hex_color(color: str) -> bool:
    return bool(re.match(r'^#(?:[0-9a-fA-F]{3}){1,2}$', color))

## Validate if a symbol is valid.
#
# @param symbol The symbol string to validate.
# @return bool True if the symbol is valid, False otherwise.
def is_valid_symbol(symbol: str) -> bool:
    valid_symbols = {'X', 'O', '△', '⬡', '★', '▢', '◊', "#", ""}
    return symbol in valid_symbols