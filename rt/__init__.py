import random

PI = 3.141592653589793
INFINITY = float("inf")

def degrees_to_radians(degrees: float) -> float:
    return degrees * PI / 180.0

def randomMinMax(min: float = 1.0, max: float = 100):
    return random.random() * (max - min) + min