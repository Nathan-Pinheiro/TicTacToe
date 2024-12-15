from typing import Any

def draw_x(app: Any, x: int, y: int, size: int) -> None:
    """Draw an X centered in a cell.
    Args:
        x (int): The x-coordinate of the cell.
        y (int): The y-coordinate of the cell.
        size (int): The size of the cell.
    Returns:
        None
    """
    margin: float = size * 0.2
    app.grid_canvas.create_line(x + margin, y + margin, x + size - margin, y + size - margin, fill="white", width=4)
    app.grid_canvas.create_line(x + margin, y + size - margin, x + size - margin, y + margin, fill="white", width=4)
    
    return None

def draw_o(app: Any, x: int, y: int, size: int) -> None:
    """Draw an O centered in a cell.
    Args:
        x (int): The x-coordinate of the cell.
        y (int): The y-coordinate of the cell.
        size (int): The size of the cell.
    Returns:
        None
    """
    margin: float = size * 0.2
    app.grid_canvas.create_oval(x + margin, y + margin, x + size - margin, y + size - margin, outline="white", width=4)
    
    return None

def draw_triangle(app: Any, x: int, y: int, size: int) -> None:
    """Draw a triangle centered in a cell.
    Args:
        x (int): The x-coordinate of the cell.
        y (int): The y-coordinate of the cell.
        size (int): The size of the cell.
    Returns:
        None
    """
    half: int = size // 2
    margin: float = size * 0.2
    app.grid_canvas.create_polygon(
        x + half, y + margin,
        x + margin, y + size - margin,
        x + size - margin, y + size - margin,
        outline="white", width=4, fill="")
    
    return None