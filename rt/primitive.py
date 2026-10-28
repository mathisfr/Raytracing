from __future__ import annotations

from .hittable import Hittable, Hit_record
from .vector3 import Vector3
from .interval import Interval

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .ray import Ray

from math import sqrt

class Sphere(Hittable):
    def __init__(self, radius = 1.0, center = Vector3(0.0,0.0,-1.0)):
        self.radius = radius
        self.center = center
    def hit(self, ray: Ray, interval: Interval, hit: Hit_record):
        cq = self.center - ray.origin
        a = ray.direction.magnitudeSquared()
        b = ray.direction.dot(cq)
        c = cq.magnitudeSquared() - pow(self.radius, 2.0)

        discriminant = pow(b, 2.0) - a * c
        if discriminant < 0:
            return False
        
        root = (b - sqrt(discriminant)) / a
        if not interval.contains(root):
            root = (b + sqrt(discriminant)) / a
            if not interval.contains(root):
                return False

        hit.distanceFromRayOrigin = root
        hit.point.copy(ray.at(root))
        outward_normal = (hit.point - self.center) / self.radius
        hit.set_face_normal(ray, outward_normal)

        return True