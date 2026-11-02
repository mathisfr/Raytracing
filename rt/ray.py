from __future__ import annotations

from .vector3 import Vector3

class Ray:
    def __init__(self, origin: Vector3, direction: Vector3) -> None:
        self.origin = origin
        self.direction = direction
    def at(self, t) -> Vector3:
        return self.origin + (self.direction * t)
    def copy(self, other: Ray):
        self.origin.copy(other.origin)
        self.direction.copy(other.direction)