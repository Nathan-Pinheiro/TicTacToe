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
        
    Returns:
        bool: True if the function succeeds, False otherwise.
    """
    if not isinstance(canvas, tk.Canvas):
        raise TypeError("canvas must be a tk.Canvas instance")
    if not isinstance(points, list) or not all(isinstance(point, (int, float)) for point in points):
        raise TypeError("points must be a list of numbers")
    if not isinstance(color, str):
        raise TypeError("color must be a string")
    if not isinstance(weight, int):
        raise TypeError("weight must be an integer")
    
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

    Returns:
        bool: True if the cross is drawn successfully.
    """
    if not isinstance(canvas, tk.Canvas):
        raise TypeError("canvas must be a tk.Canvas instance")
    if not isinstance(x, int) or not isinstance(y, int) or not isinstance(size, int):
        raise TypeError("x, y, and size must be integers")
    if not isinstance(color, str):
        raise TypeError("color must be a string")
    if not isinstance(weight, int):
        raise TypeError("weight must be an integer")
    
    margin: float = size * 0.2
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
        
    Returns:
        bool: True if the circle is drawn successfully.
    """
    
    if not isinstance(canvas, tk.Canvas):
        raise TypeError("canvas must be a tk.Canvas instance")
    if not isinstance(x, int) or not isinstance(y, int) or not isinstance(size, int):
        raise TypeError("x, y, and size must be integers")
    if not isinstance(color, str):
        raise TypeError("color must be a string")
    if not isinstance(weight, int):
        raise TypeError("weight must be an integer")
    
    margin: float = size * 0.2
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
    
    Returns:
        bool: True if the triangle is drawn successfully.
    """
    
    if not isinstance(canvas, tk.Canvas):
        raise TypeError("canvas must be a tk.Canvas instance")
    if not isinstance(x, int) or not isinstance(y, int) or not isinstance(size, int):
        raise TypeError("x, y, and size must be integers")
    if not isinstance(color, str):
        raise TypeError("color must be a string")
    if not isinstance(weight, int):
        raise TypeError("weight must be an integer")
    
    half: int = size // 2
    margin: float = size * 0.2
    points: list[float] = [
        x + half, y + margin,
        x + margin, y + size - margin,
        x + size - margin, y + size - margin
    ]
    if not drawShape(canvas, points, color, weight):
        raise RuntimeError("Failed to draw shape")
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
        
    Returns:
        bool: True if the star is drawn successfully.
    """
    
    if not isinstance(canvas, tk.Canvas):
        raise TypeError("canvas must be a tk.Canvas instance")
    if not isinstance(x, int) or not isinstance(y, int) or not isinstance(size, int):
        raise TypeError("x, y, and size must be integers")
    if not isinstance(color, str):
        raise TypeError("color must be a string")
    if not isinstance(weight, int):
        raise TypeError("weight must be an integer")
    
    center_x: int = x + size // 2
    center_y: int = y + size // 2
    outer_radius: float = size * 0.4
    inner_radius: float = size * 0.2
    num_points: int = 5
    angle_step: float = math.pi / num_points
    points: list[float] = []
    for i in range(2 * num_points):
        radius: float = outer_radius if i % 2 == 0 else inner_radius
        angle: float = i * angle_step - math.pi / 2
        points.append(center_x + radius * math.cos(angle))
        points.append(center_y + radius * math.sin(angle))
    if not drawShape(canvas, points, color, weight):
        raise RuntimeError("Failed to draw shape")
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
        
    Returns:
        bool: True if the square is drawn successfully.
    """
    
    if not isinstance(canvas, tk.Canvas):
        raise TypeError("canvas must be a tk.Canvas instance")
    if not isinstance(x, int) or not isinstance(y, int) or not isinstance(size, int):
        raise TypeError("x, y, and size must be integers")
    if not isinstance(color, str):
        raise TypeError("color must be a string")
    if not isinstance(weight, int):
        raise TypeError("weight must be an integer")
    
    margin: float = size * 0.2
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
        
    Returns:
        bool: True if the hexagon is drawn successfully.
    """
    
    if not isinstance(canvas, tk.Canvas):
        raise TypeError("canvas must be a tk.Canvas instance")
    if not isinstance(x, int) or not isinstance(y, int) or not isinstance(size, int):
        raise TypeError("x, y, and size must be integers")
    if not isinstance(color, str):
        raise TypeError("color must be a string")
    if not isinstance(weight, int):
        raise TypeError("weight must be an integer")
    
    half: int = size // 2
    margin: float = size * 0.2
    points: list[float] = [
        x + half, y + margin,
        x + size - margin, y + margin + (size - 2 * margin) / 4,
        x + size - margin, y + margin + 3 * (size - 2 * margin) / 4,
        x + half, y + size - margin,
        x + margin, y + margin + 3 * (size - 2 * margin) / 4,
        x + margin, y + margin + (size - 2 * margin) / 4
    ]
    if not drawShape(canvas, points, color, weight):
        raise RuntimeError("Failed to draw shape")
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
        
    Returns:
        bool: True if the rhombus is drawn successfully.
    """
    
    if not isinstance(canvas, tk.Canvas):
        raise TypeError("canvas must be a tk.Canvas instance")
    if not isinstance(x, int) or not isinstance(y, int) or not isinstance(size, int):
        raise TypeError("x, y, and size must be integers")
    if not isinstance(color, str):
        raise TypeError("color must be a string")
    if not isinstance(weight, int):
        raise TypeError("weight must be an integer")
    
    half: int = size // 2
    margin: float = size * 0.2
    points: list[float] = [
        x + half, y + margin,
        x + size - margin, y + half,
        x + half, y + size - margin,
        x + margin, y + half
    ]
    if not drawShape(canvas, points, color, weight):
        raise RuntimeError("Failed to draw shape")
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
        
    Returns:
        bool: True if the gray case is drawn successfully.
    """
    
    if not isinstance(canvas, tk.Canvas):
        raise TypeError("canvas must be a tk.Canvas instance")
    if not isinstance(x, int) or not isinstance(y, int) or not isinstance(size, int):
        raise TypeError("x, y, and size must be integers")
    if not isinstance(color, str):
        raise TypeError("color must be a string")
    
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
        
    Returns:
        bool: True if the green case is drawn successfully.
    """
    
    if not isinstance(canvas, tk.Canvas):
        raise TypeError("canvas must be a tk.Canvas instance")
    if not isinstance(x, int) or not isinstance(y, int) or not isinstance(size, int):
        raise TypeError("x, y, and size must be integers")
    if not isinstance(color, str):
        raise TypeError("color must be a string")
    
    canvas.create_rectangle(x + 1, y + 1, x + size, y + size, fill=color, outline = "")
    return True