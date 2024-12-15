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

import math
from typing import Any

def draw_star(app: Any, x: int, y: int, size: int) -> None:
    """Draw a perfect 5-pointed star centered in a cell.
    
    Args:
        app (Any): The application object containing the canvas.
        x (int): The x-coordinate of the top-left corner of the cell.
        y (int): The y-coordinate of the top-left corner of the cell.
        size (int): The size of the cell.
    
    Returns:
        None
    """
    # Center of the cell
    center_x = x + size // 2
    center_y = y + size // 2

    # Radius for the outer and inner points of the star
    outer_radius = size * 0.4  # Outer radius of the star
    inner_radius = size * 0.2  # Inner radius of the star

    # Number of points on the star
    num_points = 5

    # List to store the points of the star
    points = []

    # Calculate the angle between each point
    angle_step = math.pi / num_points  # Half angle step (alternates outer/inner)

    for i in range(2 * num_points):
        # Alternate between outer and inner radius
        radius = outer_radius if i % 2 == 0 else inner_radius

        # Angle for the current point
        angle = i * angle_step - math.pi / 2  # Start at -90° (top of the star)

        # Compute x and y coordinates of the point
        px = center_x + radius * math.cos(angle)
        py = center_y + radius * math.sin(angle)

        # Append the point to the list
        points.append(px)
        points.append(py)

    # Draw the star on the canvas
    app.grid_canvas.create_polygon(points, outline="white", width=4, fill="")
    
    return None

def draw_square(app: Any, x: int, y: int, size: int) -> None:
    """Draw a square centered in a cell.
    Args:
        x (int): The x-coordinate of the cell.
        y (int): The y-coordinate of the cell.
        size (int): The size of the cell.
    Returns:
        None
    """
    margin: float = size * 0.2
    app.grid_canvas.create_rectangle(x + margin, y + margin, x + size - margin, y + size - margin, outline="white", width=4)
    
    return None

def draw_hexagon(app: Any, x: int, y: int, size: int) -> None:
    """Draw a hexagon centered in a cell.
    Args:
        x (int): The x-coordinate of the cell.
        y (int): The y-coordinate of the cell.
        size (int): The size of the cell.
    Returns:
        None
    """
    half: int = size // 2
    margin: float = size * 0.2
    points = [
        x + half, y + margin,
        x + size - margin, y + margin + (size - 2 * margin) / 4,
        x + size - margin, y + margin + 3 * (size - 2 * margin) / 4,
        x + half, y + size - margin,
        x + margin, y + margin + 3 * (size - 2 * margin) / 4,
        x + margin, y + margin + (size - 2 * margin) / 4
    ]
    app.grid_canvas.create_polygon(points, outline="white", width=4, fill="")
    
    return None

def draw_losange(app: Any, x: int, y: int, size: int) -> None:
    """Draw a losange centered in a cell.
    Args:
        x (int): The x-coordinate of the cell.
        y (int): The y-coordinate of the cell.
        size (int): The size of the cell.
    Returns:
        None
    """
    half: int = size // 2
    margin: float = size * 0.2
    points = [
        x + half, y + margin,
        x + size - margin, y + half,
        x + half, y + size - margin,
        x + margin, y + half
    ]
    app.grid_canvas.create_polygon(points, outline="white", width=4, fill="")
    
    return None