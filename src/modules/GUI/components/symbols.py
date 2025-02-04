import tkinter as tk
import math

def drawShape(canvas: tk.Canvas, points: list[float], color: str, weight: int) -> bool:
    
    """
    Draws a shape on the canvas.

    Parameters:
        canvas (tk.Canvas): The canvas to draw on.
        points (list[float]): The points of the shape.
        color (str): The color of the shape.
        weight (int): The weight of the shape.
        
    Raises:
        TypeError: If canvas is not a tk.Canvas instance
        TypeError: If points is not a list of numbers
        TypeError: If color is not a string
        TypeError: If weight is not an integer
        
    Returns:
        bool: True if the function succeeds, False otherwise.
    """
    
    # Check if the canvas is a tk.Canvas instance
    if not isinstance(canvas, tk.Canvas):
        raise TypeError("canvas must be a tk.Canvas instance")
    
    # Check if the points are a list of numbers
    if not isinstance(points, list) or not all(isinstance(point, (int, float)) for point in points):
        raise TypeError("points must be a list of numbers")
    
    # Check if the color is a string
    if not isinstance(color, str):
        raise TypeError("color must be a string")
    
    # Check if the weight is an integer
    if not isinstance(weight, int):
        raise TypeError("weight must be an integer")
    
    # Draw the shape
    canvas.create_polygon(points, outline=color, width=weight, fill="")
    
    return True

def drawCross(canvas: tk.Canvas, x: int, y: int, size: int, color: str = "#ffffff", weight: int = 1) -> bool:
    
    """
    Draws a cross on the canvas.
    
    Parameters:
        canvas (tk.Canvas): The canvas to draw on.
        x (int): The x-coordinate of the cross.
        y (int): The y-coordinate of the cross.
        size (int): The size of the cross.
        color (str): The color of the cross.
        weight (int): The weight of the cross.
        
    Raises:
        TypeError: If canvas is not a tk.Canvas instance
        TypeError: If x, y, and size are not integers
        TypeError: If color is not a string
        TypeError: If weight is not an integer

    Returns:
        bool: True if the cross is drawn successfully.
    """
    
    # Check if the canvas is a tk.Canvas instance
    if not isinstance(canvas, tk.Canvas):
        raise TypeError("canvas must be a tk.Canvas instance")
    
    # Check if x, y, and size are integers
    if not isinstance(x, int) or not isinstance(y, int) or not isinstance(size, int):
        raise TypeError("x, y, and size must be integers")
    
    # Check if color is a string
    if not isinstance(color, str):
        raise TypeError("color must be a string")
    
    # Check if weight is an integer
    if not isinstance(weight, int):
        raise TypeError("weight must be an integer")
    
    # Calculate the margin
    margin: float = size * 0.2
    
    # Draw the cross
    canvas.create_line(x + margin, y + margin, x + size - margin, y + size - margin, fill=color, width=weight)
    canvas.create_line(x + margin, y + size - margin, x + size - margin, y + margin, fill=color, width=weight)
    
    return True

def drawCircle(canvas: tk.Canvas, x: int, y: int, size: int, color: str = "#ffffff", weight: int = 1) -> bool:
    
    """
    Draws a circle on the canvas.
    
    Parameters:
        canvas (tk.Canvas): The canvas to draw on.
        x (int): The x-coordinate of the circle.
        y (int): The y-coordinate of the circle.
        size (int): The size of the circle.
        color (str): The color of the circle.
        weight (int): The weight of the circle.
        
    Raises:
        TypeError: If canvas is not a tk.Canvas instance
        TypeError: If x, y, and size are not integers
        TypeError: If color is not a string
        TypeError: If weight is not an integer
        
    Returns:
        bool: True if the circle is drawn successfully.
    """
    
    # Check if the canvas is a tk.Canvas instance
    if not isinstance(canvas, tk.Canvas):
        raise TypeError("canvas must be a tk.Canvas instance")
    
    # Check if x, y, and size are integers
    if not isinstance(x, int) or not isinstance(y, int) or not isinstance(size, int):
        raise TypeError("x, y, and size must be integers")
    
    # Check if color is a string
    if not isinstance(color, str):
        raise TypeError("color must be a string")
    
    # Check if weight is an integer
    if not isinstance(weight, int):
        raise TypeError("weight must be an integer")
    
    # Calculate the margin
    margin: float = size * 0.2
    
    # Draw the circle
    canvas.create_oval(x + margin, y + margin, x + size - margin, y + size - margin, outline=color, width=weight)
    
    return True

def drawTriangle(canvas: tk.Canvas, x: int, y: int, size: int, color: str = "#ffffff", weight: int = 1) -> bool:
    
    """
    Draws a triangle on the canvas.
    
    Parameters:
        canvas (tk.Canvas): The canvas to draw on.
        x (int): The x-coordinate of the triangle.
        y (int): The y-coordinate of the triangle.
        size (int): The size of the triangle.
        color (str): The color of the triangle.
        weight (int): The weight of the triangle.
        
    Raises:
        TypeError: If canvas is not a tk.Canvas instance
        TypeError: If x, y, and size are not integers
        TypeError: If color is not a string
        TypeError: If weight is not an integer
    
    Returns:
        bool: True if the triangle is drawn successfully.
    """
    
    # Check if the canvas is a tk.Canvas instance
    if not isinstance(canvas, tk.Canvas):
        raise TypeError("canvas must be a tk.Canvas instance")
    
    # Check if x, y, and size are integers
    if not isinstance(x, int) or not isinstance(y, int) or not isinstance(size, int):
        raise TypeError("x, y, and size must be integers")
    
    # Check if color is a string
    if not isinstance(color, str):
        raise TypeError("color must be a string")
    
    # Check if weight is an integer
    if not isinstance(weight, int):
        raise TypeError("weight must be an integer")
    
    # Calculate the half size
    half: int = size // 2
    
    # Calculate the margin
    margin: float = size * 0.2
    
    # Define the points of the triangle
    points: list[float] = [
        x + half, y + margin,
        x + margin, y + size - margin,
        x + size - margin, y + size - margin
    ]
    
    # Draw the triangle
    drawShape(canvas, points, color, weight)
    
    return True

def drawStar(canvas: tk.Canvas, x: int, y: int, size: int, color: str = "#ffffff", weight: int = 1) -> bool:
    
    """
    Draws a star on the canvas.
    
    Parameters:
        canvas (tk.Canvas): The canvas to draw on.
        x (int): The x-coordinate of the star.
        y (int): The y-coordinate of the star.
        size (int): The size of the star.
        color (str): The color of the star.
        weight (int): The weight of the star.
        
    Raises:
        TypeError: If canvas is not a tk.Canvas instance
        TypeError: If x, y, and size are not integers
        TypeError: If color is not a string
        TypeError: If weight is not an integer
        
    Returns:
        bool: True if the star is drawn successfully.
    """
    
    # Check if the canvas is a tk.Canvas instance
    if not isinstance(canvas, tk.Canvas):
        raise TypeError("canvas must be a tk.Canvas instance")
    
    # Check if x, y, and size are integers
    if not isinstance(x, int) or not isinstance(y, int) or not isinstance(size, int):
        raise TypeError("x, y, and size must be integers")
    
    # Check if color is a string
    if not isinstance(color, str):
        raise TypeError("color must be a string")
    
    # Check if weight is an integer
    if not isinstance(weight, int):
        raise TypeError("weight must be an integer")
    
    # Calculate the center
    centerX: int = x + size // 2
    centerY: int = y + size // 2
    
    # Calculate the outer and inner radius
    outerRadius: float = size * 0.4
    innerRadius: float = size * 0.2
    
    # Calculate the number of points
    numPoints: int = 5
    
    # Calculate the angle step
    angleStep: float = math.pi / numPoints
    
    # Define the points of the star
    points: list[float] = []
    
    # Calculate the points of the star and add them to the list
    for indexPoint in range(2 * numPoints):
        radius: float = outerRadius if indexPoint % 2 == 0 else innerRadius
        angle: float = indexPoint * angleStep - math.pi / 2
        points.append(centerX + radius * math.cos(angle))
        points.append(centerY + radius * math.sin(angle))
        
    # Draw the star
    drawShape(canvas, points, color, weight)
    
    return True

def drawSquare(canvas: tk.Canvas, x: int, y: int, size: int, color: str = "#ffffff", weight: int = 1) -> bool:
    
    """
    Draws a square on the canvas.
    
    Parameters:
        canvas (tk.Canvas): The canvas to draw on.
        x (int): The x-coordinate of the square.
        y (int): The y-coordinate of the square.
        size (int): The size of the square.
        color (str): The color of the square.
        weight (int): The weight of the square.
        
    Raises:
        TypeError: If canvas is not a tk.Canvas instance
        TypeError: If x, y, and size are not integers
        TypeError: If color is not a string
        TypeError: If weight is not an integer
        
    Returns:
        bool: True if the square is drawn successfully.
    """
    
    # Check if the canvas is a tk.Canvas instance
    if not isinstance(canvas, tk.Canvas):
        raise TypeError("canvas must be a tk.Canvas instance")
    
    # Check if x, y, and size are integers
    if not isinstance(x, int) or not isinstance(y, int) or not isinstance(size, int):
        raise TypeError("x, y, and size must be integers")
    
    # Check if color is a string
    if not isinstance(color, str):
        raise TypeError("color must be a string")

    # Check if weight is an integer
    if not isinstance(weight, int):
        raise TypeError("weight must be an integer")
    
    # Calculate the margin
    margin: float = size * 0.2
    
    # Draw the square
    canvas.create_rectangle(x + margin, y + margin, x + size - margin, y + size - margin, outline=color, width=weight)
    
    return True

def drawHexagon(canvas: tk.Canvas, x: int, y: int, size: int, color: str = "#ffffff", weight: int = 1) -> bool:
    
    """
    Draws a hexagon on the canvas.
    
    Parameters:
        canvas (tk.Canvas): The canvas to draw on.
        x (int): The x-coordinate of the hexagon.
        y (int): The y-coordinate of the hexagon.
        size (int): The size of the hexagon.
        color (str): The color of the hexagon.
        weight (int): The weight of the hexagon.
        
    Raises:
        TypeError: If canvas is not a tk.Canvas instance.
        TypeError: If x, y, and size are not integers.
        TypeError: If color is not a string.
        TypeError: If weight is not an integer.
        
    Returns:
        bool: True if the hexagon is drawn successfully.
    """
    
    # Check if the canvas is a tk.Canvas instance
    if not isinstance(canvas, tk.Canvas):
        raise TypeError("canvas must be a tk.Canvas instance")
    
    # Check if x, y, and size are integers
    if not isinstance(x, int) or not isinstance(y, int) or not isinstance(size, int):
        raise TypeError("x, y, and size must be integers")
    
    # Check if color is a string
    if not isinstance(color, str):
        raise TypeError("color must be a string")
    
    # Check if weight is an integer
    if not isinstance(weight, int):
        raise TypeError("weight must be an integer")
    
    # Calculate the half of the size
    half: int = size // 2
    
    # Calculate the margin
    margin: float = size * 0.2
    
    # Define the points of the hexagon
    points: list[float] = [
        x + half, y + margin,
        x + size - margin, y + margin + (size - 2 * margin) / 4,
        x + size - margin, y + margin + 3 * (size - 2 * margin) / 4,
        x + half, y + size - margin,
        x + margin, y + margin + 3 * (size - 2 * margin) / 4,
        x + margin, y + margin + (size - 2 * margin) / 4
    ]
    
    # Draw the hexagon
    drawShape(canvas, points, color, weight)
    
    return True

def drawRhombus(canvas: tk.Canvas, x: int, y: int, size: int, color: str = "#ffffff", weight: int = 1) -> bool:
    
    """
    Draws a rhombus on the canvas.
    
    Parameters:
        canvas (tk.Canvas): The canvas to draw on.
        x (int): The x-coordinate of the rhombus.
        y (int): The y-coordinate of the rhombus.
        size (int): The size of the rhombus.
        color (str): The color of the rhombus.
        weight (int): The weight of the rhombus.
        
    Raises:
        TypeError: If canvas is not a tk.Canvas instance.
        TypeError: If x, y, and size are not integers.
        TypeError: If color is not a string.
        TypeError: If weight is not an integer.
        
    Returns:
        bool: True if the rhombus is drawn successfully.
    """
    
    # Check if the canvas is a tk.Canvas instance
    if not isinstance(canvas, tk.Canvas):
        raise TypeError("canvas must be a tk.Canvas instance")
    
    # Check if x, y, and size are integers
    if not isinstance(x, int) or not isinstance(y, int) or not isinstance(size, int):
        raise TypeError("x, y, and size must be integers")
    
    # Check if color is a string
    if not isinstance(color, str):
        raise TypeError("color must be a string")
    
    # Check if weight is an integer
    if not isinstance(weight, int):
        raise TypeError("weight must be an integer")
    
    # Calculate the half of the size
    half: int = size // 2
    
    # Calculate the margin
    margin: float = size * 0.2
    
    # Define the points of the rhombus
    points: list[float] = [
        x + half, y + margin,
        x + size - margin, y + half,
        x + half, y + size - margin,
        x + margin, y + half
    ]
    
    # Draw the rhombus
    drawShape(canvas, points, color, weight)
    
    return True

def drawGrayCase(canvas: tk.Canvas, x: int, y: int, size: int, color: str = "#5c5c5c") -> bool:
    
    """
    Draws a gray case on the canvas.
    
    Parameters:
        canvas (tk.Canvas): The canvas to draw on.
        x (int): The x-coordinate of the gray case.
        y (int): The y-coordinate of the gray case.
        size (int): The size of the gray case.
        color (str): The color of the gray case.
        
    Raises:
        TypeError: If canvas is not a tk.Canvas instance.
        TypeError: If x, y, and size are not integers.
        TypeError: If color is not a string.
        
    Returns:
        bool: True if the gray case is drawn successfully.
    """
    
    # Check if the canvas is a tk.Canvas instance
    if not isinstance(canvas, tk.Canvas):
        raise TypeError("canvas must be a tk.Canvas instance")
    
    # Check if x, y, and size are integers
    if not isinstance(x, int) or not isinstance(y, int) or not isinstance(size, int):
        raise TypeError("x, y, and size must be integers")
    
    # Check if color is a string
    if not isinstance(color, str):
        raise TypeError("color must be a string")
    
    # Draw the gray case
    canvas.create_rectangle(x + 1, y + 1, x + size, y + size, fill=color, outline="")
    
    return True

def drawGreenCase(canvas: tk.Canvas, x: int, y: int, size: int, color: str = "#005500") -> bool:
    
    """
    Draws a green case on the canvas.
    
    Parameters:
        canvas (tk.Canvas): The canvas to draw on.
        x (int): The x-coordinate of the green case.
        y (int): The y-coordinate of the green case.
        size (int): The size of the green case.
        color (str): The color of the green case.
        
    Raises:
        TypeError: If canvas is not a tk.Canvas instance.
        TypeError: If x, y, and size are not integers.
        TypeError: If color is not a string.
        
    Returns:
        bool: True if the green case is drawn successfully.
    """
    
    # Check if the canvas is a tk.Canvas instance
    if not isinstance(canvas, tk.Canvas):
        raise TypeError("canvas must be a tk.Canvas instance")
    
    # Check if x, y, and size are integers
    if not isinstance(x, int) or not isinstance(y, int) or not isinstance(size, int):
        raise TypeError("x, y, and size must be integers")
    
    # Check if color is a string
    if not isinstance(color, str):
        raise TypeError("color must be a string")
    
    # Draw the green case
    canvas.create_rectangle(x + 1, y + 1, x + size, y + size, fill=color, outline = "")
    
    return True