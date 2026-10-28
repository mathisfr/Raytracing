from __future__ import annotations
from typing import overload
from typing import Self
from math import pow, sqrt
from . import randomMinMax
import random

class Vector3:
    def __init__(self, x: float, y: float, z: float) -> None:
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other: Vector3) -> Self:
        return Vector3(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z,
            )
    def __sub__(self, other: Vector3) -> Self:
        return Vector3(
            self.x - other.x,
            self.y - other.y,
            self.z - other.z
            )
    def __mul__(self, scalar: float) -> Self:
        return Vector3(
            self.x * scalar,
            self.y * scalar,
            self.z * scalar
            )
    def __rmul__(self, scalar: float) -> Self:
        return Vector3(
            self.x * scalar,
            self.y * scalar,
            self.z * scalar
            )
    def __truediv__(self, scalar: float) -> Self:
        return Vector3(
            self.x / scalar,
            self.y / scalar,
            self.z / scalar
            )

    def __iadd__(self, other: Vector3) -> Self:
        self.x += other.x
        self.y += other.y
        self.z += other.z
        return self
    def __isub__(self, other: Vector3) -> Self:
        self.x -= other.x
        self.y -= other.y
        self.z -= other.z
        return self
    def __imul__(self, scalar: float) -> Self:
        self.x *= scalar
        self.y *= scalar
        self.z *= scalar
        return self
    def __itruediv__(self, scalar: float) -> Self:
        self.x /= scalar
        self.y /= scalar
        self.z /= scalar
        return self
        
    def __eq__(self, other: Vector3) -> Self:
        return (self.x == other.x) and (self.y == other.y) and (self.z == other.z)
    def __ne__(self, other: Vector3) -> Self:
            return not (self == other)
    def __ge__(self, other: Vector3) -> Self:
        return (self.x >= other.x) and (self.y >= other.y) and (self.z >= other.z)
    def __le__(self, other: Vector3) -> Self:
        return (self.x <= other.x) and (self.y <= other.y) and (self.z <= other.z)
    def __gt__(self, other: Vector3) -> Self:
        return (self.x > other.x) and (self.y > other.y) and (self.z > other.z)
    def __lt__(self, other: Vector3) -> Self:
        return (self.x < other.x) and (self.y < other.y) and (self.z < other.z)
    def __neg__(self) -> Self:
        self *= -1
        return self

    def magnitudeSquared(self) -> float:
        return pow(self.x, 2) + pow(self.y, 2) + pow(self.z, 2)
    def magnitude(self) -> float:
        return sqrt(self.magnitudeSquared())
    def normalize(self) -> Vector3: 
        return self / self.magnitude()
    def dot(self, other: Vector3) -> float:
        return self.x * other.x + self.y * other.y + self.z * other.z
    def cross(self, other: Vector3) -> float:
            return Vector3(
                self.y * other.z - self.z * other.y,
                self.z * other.x - self.x * other.z,
                self.x * other.y - self.y * other.x,
            )

    def copy(self, other: Vector3) -> None:
        self.x = other.x
        self.y = other.y
        self.z = other.z
    
    def __repr__(self) -> str:
        return "X:%s    Y:%s    Z:%s" % (self.x, self.y, self.z)

    @staticmethod
    def random(min: float = 0.0, max: float = 1.0) -> Vector3:
        return Vector3(randomMinMax(min, max), randomMinMax(min, max), randomMinMax(min, max))

    @staticmethod
    def randomSphericalUnitVector() -> Vector3:
        while True:
            vector = Vector3.random(-1.0, 1.0)
            # vector.magnitudeSquared() == vector.dot(vector) == u ° u == ||u||²
            if vector.magnitudeSquared() <= 1.0 and vector.magnitudeSquared() > 1e-160:
                return  vector.normalize()

    @staticmethod
    def randomDirectionOnHemisphere(normal: Vector3):
        randomVector = Vector3.randomSphericalUnitVector()
        dotProduct = randomVector.dot(normal)
        if dotProduct > 0.0:
            return randomVector
        else:
            return -randomVector

Color3 = Vector3