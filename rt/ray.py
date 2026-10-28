from __future__ import annotations

from .vector3 import Vector3

class Ray:
    def __init__(self, origin: Vector3, direction: Vector3) -> None:
        self.origin = origin
        self.direction = direction
    def at(self, t) -> Vector3:
        return self.origin + (self.direction * t)