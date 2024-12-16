## Interface

"""
Shape Drawing Module

This module provides functions to draw various shapes on a graphical canvas, including 'X', 'O', triangles, stars, squares, hexagons, and rhombuses.

Functions:
    drawCross(app: tk.Tk, x: int, y: int, size: int, color: str = "#ffffff", weight: int = 4) -> None:
        Draw an 'X' centered in a cell.
        
        Args:
            app (tk.Tk): The application object containing the canvas.
            x (int): The x-coordinate of the top-left corner of the cell.
            y (int): The y-coordinate of the top-left corner of the cell.
            size (int): The size of the cell.
            color (str): The color of the 'X' (default is white).
            weight (int): The thickness of the lines (default is 4).
            
        Returns:
            None

    drawCircle(app: tk.Tk, x: int, y: int, size: int, color: str = "#ffffff", weight: int = 4) -> None:
        Draw an 'O' centered in a cell.
        
        Args:
            app (tk.Tk): The application object containing the canvas.
            x (int): The x-coordinate of the top-left corner of the cell.
            y (int): The y-coordinate of the top-left corner of the cell.
            size (int): The size of the cell.
            color (str): The color of the 'O' (default is white).
            weight (int): The thickness of the lines (default is 4).
            
        Returns:
            None

    drawTriangle(app: tk.Tk, x: int, y: int, size: int, color: str = "#ffffff", weight: int = 4) -> None:
        Draw a triangle centered in a cell.
        
        Args:
            app (tk.Tk): The application object containing the canvas.
            x (int): The x-coordinate of the top-left corner of the cell.
            y (int): The y-coordinate of the top-left corner of the cell.
            size (int): The size of the cell.
            color (str): The color of the triangle (default is white).
            weight (int): The thickness of the lines (default is 4).
            
        Returns:
            None

    drawStar(app: tk.Tk, x: int, y: int, size: int, color: str = "#ffffff", weight: int = 4) -> None:
        Draw a perfect 5-pointed star centered in a cell.
        
        Args:
            app (tk.Tk): The application object containing the canvas.
            x (int): The x-coordinate of the top-left corner of the cell.
            y (int): The y-coordinate of the top-left corner of the cell.
            size (int): The size of the cell.
            color (str): The color of the star (default is white).
            weight (int): The thickness of the lines (default is 4).
            
        Returns:
            None

    drawSquare(app: tk.Tk, x: int, y: int, size: int, color: str = "#ffffff", weight: int = 4) -> None:
        Draw a square centered in a cell.
        
        Args:
            app (tk.Tk): The application object containing the canvas.
            x (int): The x-coordinate of the top-left corner of the cell.
            y (int): The y-coordinate of the top-left corner of the cell.
            size (int): The size of the cell.
            color (str): The color of the square (default is white).
            weight (int): The thickness of the lines (default is 4).
            
        Returns:
            None

    drawHexagon(app: tk.Tk, x: int, y: int, size: int, color: str = "#ffffff", weight: int = 4) -> None:
        Draw a hexagon centered in a cell.
        
        Args:
            app (tk.Tk): The application object containing the canvas.
            x (int): The x-coordinate of the top-left corner of the cell.
            y (int): The y-coordinate of the top-left corner of the cell.
            size (int): The size of the cell.
            color (str): The color of the hexagon (default is white).
            weight (int): The thickness of the lines (default is 4).
            
        Returns:
            None

    drawRhombus(app: tk.Tk, x: int, y: int, size: int, color: str = "#ffffff", weight: int = 4) -> None:
        Draw a rhombus (diamond shape) centered in a cell.
        
        Args:
            app (tk.Tk): The application object containing the canvas.
            x (int): The x-coordinate of the top-left corner of the cell.
            y (int): The y-coordinate of the top-left corner of the cell.
            size (int): The size of the cell.
            color (str): The color of the rhombus (default is white).
            weight (int): The thickness of the lines (default is 4).
            
        Returns:
            None
            
    drawGrayCase(app: tk.Tk, x: int, y: int, size: int, color: str = "#5c5c5c") -> None:
        Draw a gray square centered in a cell.
        
        Args:
            app (tk.Tk): The application object containing the canvas.
            x (int): The x-coordinate of the top-left corner of the cell.
            y (int): The y-coordinate of the top-left corner of the cell.
            size (int): The size of the cell.
            color (str): The color of the square (default is gray).
            
        Returns:
            None
"""

# ---------------------------------------------------------------------------------------------------- #

## Implementation

# Import
import tkinter as tk
import math

def drawCross(canvas: tk.Canvas, x: int, y: int, size: int, color: str = "#ffffff", weight: int = 1) -> None:
    """
    Draw an 'X' centered in a cell.
    
    Args:
        app (tk.Tk): The application object containing the canvas.
        x (int): The x-coordinate of the top-left corner of the cell.
        y (int): The y-coordinate of the top-left corner of the cell.
        size (int): The size of the cell.
        color (str): The color of the 'X' (default is white).
        weight (int): The thickness of the lines (default is 4).
        
    Returns:
        None
    """
    # Define margin as 20% of the size for positioning the X
    margin: float = size * 0.2
    
    # Draw two crossing lines to form the X
    canvas.create_line(x + margin, y + margin, x + size - margin, y + size - margin, fill=color, width=weight)
    canvas.create_line(x + margin, y + size - margin, x + size - margin, y + margin, fill=color, width=weight)
    return None

def drawCircle(canvas: tk.Canvas, x: int, y: int, size: int, color: str = "#ffffff", weight: int = 1) -> None:
    """
    Draw an 'O' centered in a cell.
    
    Args:
        app (tk.Tk): The application object containing the canvas.
        x (int): The x-coordinate of the top-left corner of the cell.
        y (int): The y-coordinate of the top-left corner of the cell.
        size (int): The size of the cell.
        color (str): The color of the 'O' (default is white).
        weight (int): The thickness of the lines (default is 4).
        
    Returns:
        None
    """
    # Define margin as 20% of the size for positioning the circle
    margin: float = size * 0.2
    
    # Draw an oval (circle) inside the cell
    canvas.create_oval(x + margin, y + margin, x + size - margin, y + size - margin, outline=color, width=weight)
    return None

def drawTriangle(canvas: tk.Canvas, x: int, y: int, size: int, color: str = "#ffffff", weight: int = 1) -> None:
    """
    Draw a triangle centered in a cell.
    
    Args:
        app (tk.Tk): The application object containing the canvas.
        x (int): The x-coordinate of the top-left corner of the cell.
        y (int): The y-coordinate of the top-left corner of the cell.
        size (int): The size of the cell.
        color (str): The color of the triangle (default is white).
        weight (int): The thickness of the lines (default is 4).
        
    Returns:
        None
    """
    # Define the half of the size and a margin for positioning
    half: int = size // 2
    margin: float = size * 0.2

    # Define the vertices of the triangle
    canvas.create_polygon(
        x + half, y + margin,  # Top vertex
        x + margin, y + size - margin,  # Bottom-left vertex
        x + size - margin, y + size - margin,  # Bottom-right vertex
        outline=color, width=weight, fill="")
    return None

def drawStar(canvas: tk.Canvas, x: int, y: int, size: int, color: str = "#ffffff", weight: int = 1) -> None:
    """
    Draw a perfect 5-pointed star centered in a cell.
    
    Args:
        app (tk.Tk): The application object containing the canvas.
        x (int): The x-coordinate of the top-left corner of the cell.
        y (int): The y-coordinate of the top-left corner of the cell.
        size (int): The size of the cell.
        color (str): The color of the star (default is white).
        weight (int): The thickness of the lines (default is 4).
        
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
    canvas.create_polygon(points, outline=color, width=weight, fill="")
    return None

def drawSquare(canvas: tk.Canvas, x: int, y: int, size: int, color: str = "#ffffff", weight: int = 1) -> None:
    """
    Draw a square centered in a cell.
    
    Args:
        app (tk.Tk): The application object containing the canvas.
        x (int): The x-coordinate of the top-left corner of the cell.
        y (int): The y-coordinate of the top-left corner of the cell.
        size (int): The size of the cell.
        color (str): The color of the square (default is white).
        weight (int): The thickness of the lines (default is 4).
        
    Returns:
        None
    """
    # Define margin for positioning the square
    margin: float = size * 0.2
    
    # Draw the square
    canvas.create_rectangle(x + margin, y + margin, x + size - margin, y + size - margin, outline=color, width=weight)
    return None

def drawHexagon(canvas: tk.Canvas, x: int, y: int, size: int, color: str = "#ffffff", weight: int = 1) -> None:
    """
    Draw a hexagon centered in a cell.
    
    Args:
        app (tk.Tk): The application object containing the canvas.
        x (int): The x-coordinate of the top-left corner of the cell.
        y (int): The y-coordinate of the top-left corner of the cell.
        size (int): The size of the cell.
        color (str): The color of the hexagon (default is white).
        weight (int): The thickness of the lines (default is 4).
        
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
    canvas.create_polygon(points, outline=color, width=weight, fill="")
    
    return None

def drawRhombus(canvas: tk.Canvas, x: int, y: int, size: int, color: str = "#ffffff", weight: int = 1) -> None:
    """Draw a rhombus (diamond shape) centered in a cell on the canvas.
    
    Args:
        app (tk.Tk): The application object containing the canvas.
        x (int): The x-coordinate of the top-left corner of the cell.
        y (int): The y-coordinate of the top-left corner of the cell.
        size (int): The size of the cell.
        color (str): The color of the rhombus (default is white).
        weight (int): The thickness of the lines (default is 4).
    
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
    canvas.create_polygon(points, outline=color, width=weight, fill="")
    
    return None

def drawGrayCase(canvas: tk.Canvas, x: int, y: int, size: int, color: str = "#5c5c5c") -> None:
    """Draw a gray square centered in a cell on the canvas.
    
    Args:
        app (tk.Tk): The application object containing the canvas.
        x (int): The x-coordinate of the top-left corner of the cell.
        y (int): The y-coordinate of the top-left corner of the cell.
        size (int): The size of the cell.
        color (str): The color of the square (default is gray).
    
    Returns:
        None
    """
    canvas.create_rectangle(x + 1, y + 1, x + size, y + size, fill=color, outline="")
    return None