## Interface

"""
Shape Drawing Module

This module provides functions to draw various shapes on a graphical canvas, including 'X', 'O', triangles, stars, squares, hexagons, and rhombuses.

Functions:
    drawCross(canvas: tk.Canvas, x: int, y: int, size: int, color: str = "#ffffff", weight: int = 4) -> bool:
        Draw an 'X' centered in a cell.
        
    drawCircle(canvas: tk.Canvas, x: int, y: int, size: int, color: str = "#ffffff", weight: int = 4) -> bool:
        Draw an 'O' centered in a cell.
        
    drawTriangle(canvas: tk.Canvas, x: int, y: int, size: int, color: str = "#ffffff", weight: int = 4) -> bool:
        Draw a triangle centered in a cell.
        
    drawStar(canvas: tk.Canvas, x: int, y: int, size: int, color: str = "#ffffff", weight: int = 4) -> bool:
        Draw a perfect 5-pointed star centered in a cell.
        
    drawSquare(canvas: tk.Canvas, x: int, y: int, size: int, color: str = "#ffffff", weight: int = 4) -> bool:
        Draw a square centered in a cell.
        
    drawHexagon(canvas: tk.Canvas, x: int, y: int, size: int, color: str = "#ffffff", weight: int = 4) -> bool:
        Draw a hexagon centered in a cell.
        
    drawRhombus(canvas: tk.Canvas, x: int, y: int, size: int, color: str = "#ffffff", weight: int = 4) -> bool:
        Draw a rhombus (diamond shape) centered in a cell.
        
    drawGrayCase(canvas: tk.Canvas, x: int, y: int, size: int, color: str = "#5c5c5c") -> bool:
        Draw a gray square centered in a cell.
"""

# ---------------------------------------------------------------------------------------------------- #

## Implementation

# Import
import tkinter as tk
import math

## Draw a shape centered in a cell.
#
# @param canvas The canvas object to draw on.
# @param points The list of points defining the shape.
# @param color The color of the shape.
# @param weight The thickness of the lines.
# @return bool True if the function succeeds, False otherwise.
def drawShape(canvas: tk.Canvas, points: list[float], color: str, weight: int) -> bool:
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

## Draw an 'X' centered in a cell.
#
# @param canvas The canvas object to draw on.
# @param x The x-coordinate of the top-left corner of the cell.
# @param y The y-coordinate of the top-left corner of the cell.
# @param size The size of the cell.
# @param color The color of the 'X' (default is white).
# @param weight The thickness of the lines (default is 1).
# @return bool True if the function succeeds, False otherwise.
def drawCross(canvas: tk.Canvas, x: int, y: int, size: int, color: str = "#ffffff", weight: int = 1) -> bool:
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

## Draw an 'O' centered in a cell.
#
# @param canvas The canvas object to draw on.
# @param x The x-coordinate of the top-left corner of the cell.
# @param y The y-coordinate of the top-left corner of the cell.
# @param size The size of the cell.
# @param color The color of the 'O' (default is white).
# @param weight The thickness of the lines (default is 1).
# @return bool True if the function succeeds, False otherwise.
def drawCircle(canvas: tk.Canvas, x: int, y: int, size: int, color: str = "#ffffff", weight: int = 1) -> bool:
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

## Draw a triangle centered in a cell.
#
# @param canvas The canvas object to draw on.
# @param x The x-coordinate of the top-left corner of the cell.
# @param y The y-coordinate of the top-left corner of the cell.
# @param size The size of the cell.
# @param color The color of the triangle (default is white).
# @param weight The thickness of the lines (default is 1).
# @return bool True if the function succeeds, False otherwise.
def drawTriangle(canvas: tk.Canvas, x: int, y: int, size: int, color: str = "#ffffff", weight: int = 1) -> bool:
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

## Draw a perfect 5-pointed star centered in a cell.
#
# @param canvas The canvas object to draw on.
# @param x The x-coordinate of the top-left corner of the cell.
# @param y The y-coordinate of the top-left corner of the cell.
# @param size The size of the cell.
# @param color The color of the star (default is white).
# @param weight The thickness of the lines (default is 1).
# @return bool True if the function succeeds, False otherwise.
def drawStar(canvas: tk.Canvas, x: int, y: int, size: int, color: str = "#ffffff", weight: int = 1) -> bool:
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

## Draw a square centered in a cell.
#
# @param canvas The canvas object to draw on.
# @param x The x-coordinate of the top-left corner of the cell.
# @param y The y-coordinate of the top-left corner of the cell.
# @param size The size of the cell.
# @param color The color of the square (default is white).
# @param weight The thickness of the lines (default is 1).
# @return bool True if the function succeeds, False otherwise.
def drawSquare(canvas: tk.Canvas, x: int, y: int, size: int, color: str = "#ffffff", weight: int = 1) -> bool:
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

## Draw a hexagon centered in a cell.
#
# @param canvas The canvas object to draw on.
# @param x The x-coordinate of the top-left corner of the cell.
# @param y The y-coordinate of the top-left corner of the cell.
# @param size The size of the cell.
# @param color The color of the hexagon (default is white).
# @param weight The thickness of the lines (default is 1).
# @return bool True if the function succeeds, False otherwise.
def drawHexagon(canvas: tk.Canvas, x: int, y: int, size: int, color: str = "#ffffff", weight: int = 1) -> bool:
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

## Draw a rhombus (diamond shape) centered in a cell.
#
# @param canvas The canvas object to draw on.
# @param x The x-coordinate of the top-left corner of the cell.
# @param y The y-coordinate of the top-left corner of the cell.
# @param size The size of the cell.
# @param color The color of the rhombus (default is white).
# @param weight The thickness of the lines (default is 1).
# @return bool True if the function succeeds, False otherwise.
def drawRhombus(canvas: tk.Canvas, x: int, y: int, size: int, color: str = "#ffffff", weight: int = 1) -> bool:
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

## Draw a gray square centered in a cell.
#
# @param canvas The canvas object to draw on.
# @param x The x-coordinate of the top-left corner of the cell.
# @param y The y-coordinate of the top-left corner of the cell.
# @param size The size of the cell.
# @param color The color of the square (default is gray).
# @return bool True if the function succeeds, False otherwise.
def drawGrayCase(canvas: tk.Canvas, x: int, y: int, size: int, color: str = "#5c5c5c") -> bool:
    if not isinstance(canvas, tk.Canvas):
        raise TypeError("canvas must be a tk.Canvas instance")
    if not isinstance(x, int) or not isinstance(y, int) or not isinstance(size, int):
        raise TypeError("x, y, and size must be integers")
    if not isinstance(color, str):
        raise TypeError("color must be a string")
    
    canvas.create_rectangle(x + 1, y + 1, x + size, y + size, fill=color, outline="")
    return True

## Draw a green square centered in a cell.
#
# @param canvas The canvas object to draw on.
# @param x The x-coordinate of the top-left corner of the cell.
# @param y The y-coordinate of the top-left corner of the cell.
# @param size The size of the cell.
# @param color The color of the square (default is green).
# @return bool True if the function succeeds, False otherwise.
def drawGreenCase(canvas: tk.Canvas, x: int, y: int, size: int, color: str = "#005500") -> bool:
    if not isinstance(canvas, tk.Canvas):
        raise TypeError("canvas must be a tk.Canvas instance")
    if not isinstance(x, int) or not isinstance(y, int) or not isinstance(size, int):
        raise TypeError("x, y, and size must be integers")
    if not isinstance(color, str):
        raise TypeError("color must be a string")
    
    canvas.create_rectangle(x + 1, y + 1, x + size, y + size, fill=color, outline = "")
    return True