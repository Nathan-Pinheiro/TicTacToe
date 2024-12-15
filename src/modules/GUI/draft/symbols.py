## Interface

"""
Shape Drawing Module

This module provides functions to draw various shapes on a graphical canvas, including 'X', 'O', triangles, stars, squares, hexagons, and rhombuses.

Functions:
    drawCross(app: Any, x: int, y: int, size: int) -> None:
        Draw an 'X' centered in a cell.
        
        Args:
            app (Any): The application object containing the canvas.
            x (int): The x-coordinate of the top-left corner of the cell.
            y (int): The y-coordinate of the top-left corner of the cell.
            size (int): The size of the cell.
            
        Returns:
            None

    drawCircle(app: Any, x: int, y: int, size: int) -> None:
        Draw an 'O' centered in a cell.
        
        Args:
            app (Any): The application object containing the canvas.
            x (int): The x-coordinate of the top-left corner of the cell.
            y (int): The y-coordinate of the top-left corner of the cell.
            size (int): The size of the cell.
            
        Returns:
            None

    drawTriangle(app: Any, x: int, y: int, size: int) -> None:
        Draw a triangle centered in a cell.
        
        Args:
            app (Any): The application object containing the canvas.
            x (int): The x-coordinate of the top-left corner of the cell.
            y (int): The y-coordinate of the top-left corner of the cell.
            size (int): The size of the cell.
            
        Returns:
            None

    drawStar(app: Any, x: int, y: int, size: int) -> None:
        Draw a perfect 5-pointed star centered in a cell.
        
        Args:
            app (Any): The application object containing the canvas.
            x (int): The x-coordinate of the top-left corner of the cell.
            y (int): The y-coordinate of the top-left corner of the cell.
            size (int): The size of the cell.
            
        Returns:
            None

    drawSquare(app: Any, x: int, y: int, size: int) -> None:
        Draw a square centered in a cell.
        
        Args:
            app (Any): The application object containing the canvas.
            x (int): The x-coordinate of the top-left corner of the cell.
            y (int): The y-coordinate of the top-left corner of the cell.
            size (int): The size of the cell.
            
        Returns:
            None

    drawHexagon(app: Any, x: int, y: int, size: int) -> None:
        Draw a hexagon centered in a cell.
        
        Args:
            app (Any): The application object containing the canvas.
            x (int): The x-coordinate of the top-left corner of the cell.
            y (int): The y-coordinate of the top-left corner of the cell.
            size (int): The size of the cell.
            
        Returns:
            None

    drawRhombus(app: Any, x: int, y: int, size: int) -> None:
        Draw a rhombus (diamond shape) centered in a cell.
        
        Args:
            app (Any): The application object containing the canvas.
            x (int): The x-coordinate of the top-left corner of the cell.
            y (int): The y-coordinate of the top-left corner of the cell.
            size (int): The size of the cell.
            
        Returns:
            None
            
    drawGrayCase(app: Any, x: int, y: int, size: int) -> None:
"""

# ---------------------------------------------------------------------------------------------------- #

## Implementation

# Import
from typing import Any
import math

def drawCross(app: Any, x: int, y: int, size: int) -> None:
    """
    Draw an 'X' centered in a cell.
    
    Args:
        app (Any): The application object containing the canvas.
        x (int): The x-coordinate of the top-left corner of the cell.
        y (int): The y-coordinate of the top-left corner of the cell.
        size (int): The size of the cell.
        
    Returns:
        None
    """
    # Define margin as 20% of the size for positioning the X
    margin: float = size * 0.2
    
    # Draw two crossing lines to form the X
    app.grid_canvas.create_line(x + margin, y + margin, x + size - margin, y + size - margin, fill="white", width=4)
    app.grid_canvas.create_line(x + margin, y + size - margin, x + size - margin, y + margin, fill="white", width=4)
    return None

def drawCircle(app: Any, x: int, y: int, size: int) -> None:
    """
    Draw an 'O' centered in a cell.
    
    Args:
        app (Any): The application object containing the canvas.
        x (int): The x-coordinate of the top-left corner of the cell.
        y (int): The y-coordinate of the top-left corner of the cell.
        size (int): The size of the cell.
        
    Returns:
        None
    """
    # Define margin as 20% of the size for positioning the circle
    margin: float = size * 0.2
    
    # Draw an oval (circle) inside the cell
    app.grid_canvas.create_oval(x + margin, y + margin, x + size - margin, y + size - margin, outline="white", width=4)
    return None

def drawTriangle(app: Any, x: int, y: int, size: int) -> None:
    """
    Draw a triangle centered in a cell.
    
    Args:
        app (Any): The application object containing the canvas.
        x (int): The x-coordinate of the top-left corner of the cell.
        y (int): The y-coordinate of the top-left corner of the cell.
        size (int): The size of the cell.
        
    Returns:
        None
    """
    # Define the half of the size and a margin for positioning
    half: int = size // 2
    margin: float = size * 0.2

    # Define the vertices of the triangle
    app.grid_canvas.create_polygon(
        x + half, y + margin,  # Top vertex
        x + margin, y + size - margin,  # Bottom-left vertex
        x + size - margin, y + size - margin,  # Bottom-right vertex
        outline="white", width=4, fill="")
    return None

def drawStar(app: Any, x: int, y: int, size: int) -> None:
    """
    Draw a perfect 5-pointed star centered in a cell.
    
    Args:
        app (Any): The application object containing the canvas.
        x (int): The x-coordinate of the top-left corner of the cell.
        y (int): The y-coordinate of the top-left corner of the cell.
        size (int): The size of the cell.
        
    Returns:
        None
    """
    # Calculate the center of the cell
    center_x = x + size // 2
    center_y = y + size // 2

    # Define the outer and inner radius of the star
    outer_radius = size * 0.4
    inner_radius = size * 0.2

    # Number of points and angle between points
    num_points = 5
    angle_step = math.pi / num_points

    # Calculate coordinates for each point of the star
    points = []
    for i in range(2 * num_points):
        radius = outer_radius if i % 2 == 0 else inner_radius
        angle = i * angle_step - math.pi / 2  # Start at the top of the star
        px = center_x + radius * math.cos(angle)
        py = center_y + radius * math.sin(angle)
        points.append(px)
        points.append(py)

    # Draw the star
    app.grid_canvas.create_polygon(points, outline="white", width=4, fill="")
    return None

def drawSquare(app: Any, x: int, y: int, size: int) -> None:
    """
    Draw a square centered in a cell.
    
    Args:
        app (Any): The application object containing the canvas.
        x (int): The x-coordinate of the top-left corner of the cell.
        y (int): The y-coordinate of the top-left corner of the cell.
        size (int): The size of the cell.
        
    Returns:
        None
    """
    # Define margin for positioning the square
    margin: float = size * 0.2
    
    # Draw the square
    app.grid_canvas.create_rectangle(x + margin, y + margin, x + size - margin, y + size - margin, outline="white", width=4)
    return None

def drawHexagon(app: Any, x: int, y: int, size: int) -> None:
    """
    Draw a hexagon centered in a cell.
    
    Args:
        app (Any): The application object containing the canvas.
        x (int): The x-coordinate of the top-left corner of the cell.
        y (int): The y-coordinate of the top-left corner of the cell.
        size (int): The size of the cell.
        
    Returns:
        None
    """

    half: int = size // 2
    margin: float = size * 0.2
    # Define the vertices of the hexagon
    points = [
        x + half, y + margin,  # Top vertex
        x + size - margin, y + margin + (size - 2 * margin) / 4,  # Top-right vertex
        x + size - margin, y + margin + 3 * (size - 2 * margin) / 4,  # Bottom-right vertex
        x + half, y + size - margin,  # Bottom vertex
        x + margin, y + margin + 3 * (size - 2 * margin) / 4,  # Bottom-left vertex
        x + margin, y + margin + (size - 2 * margin) / 4  # Top-left vertex
    ]
    app.grid_canvas.create_polygon(points, outline="white", width=4, fill="")
    
    return None

def drawRhombus(app: Any, x: int, y: int, size: int) -> None:
    """Draw a rhombus (diamond shape) centered in a cell on the canvas.
    
    Args:
        app (Any): The application object containing the canvas.
        x (int): The x-coordinate of the top-left corner of the cell.
        y (int): The y-coordinate of the top-left corner of the cell.
        size (int): The size of the cell.
    
    Returns:
        None
    """
    half: int = size // 2
    margin: float = size * 0.2
    # Define the vertices of the rhombus
    points = [
        x + half, y + margin,  # Top vertex
        x + size - margin, y + half,  # Right vertex
        x + half, y + size - margin,  # Bottom vertex
        x + margin, y + half  # Left vertex
    ]
    app.grid_canvas.create_polygon(points, outline="white", width=4, fill="")
    
    return None

def drawGrayCase(app: Any, x: int, y: int, size: int) -> None:
    """Draw a gray square centered in a cell on the canvas.
    
    Args:
        app (Any): The application object containing the canvas.
        x (int): The x-coordinate of the top-left corner of the cell.
        y (int): The y-coordinate of the top-left corner of the cell.
        size (int): The size of the cell.
    
    Returns:
        None
    """
    app.grid_canvas.create_rectangle(x+2, y+2, x + size-1, y + size, fill="#5c5c5c", outline="")
    return None