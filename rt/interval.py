from __future__ import annotations

from rt import INFINITY

class Interval:
    def __init__(self, min: float = INFINITY, max:float = -INFINITY):
        self.min = min
        self.max = max
    def size(self) -> float:
        return self.max - self.min
    def contains(self, x: float) -> bool:
        return x >= self.min and x <= self.max
    def surrounds(self, x: float) -> bool:
        return x > self.min and x < self.max
    def clamp(self, x: float):
        if (x < self.min):
            return self.min
        if (x > self.max):
            return self.max
        return x

empty = Interval(INFINITY, -INFINITY)
universe = Interval(-INFINITY, INFINITY)