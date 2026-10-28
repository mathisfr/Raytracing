from __future__ import annotations

from abc import ABC, abstractmethod

from .vector3 import Vector3
from .interval import Interval

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .ray import Ray

class Hit_record:
    def __init__(
        self,
        point: Vector3 | None = None,
        normal: Vector3 | None = None,
        distanceFromRayOrigin: float = 0.0
    ):
        self.point = point if point is not None else Vector3(0.0, 0.0, 0.0)
        self.normal = normal if normal is not None else Vector3(0.0, 0.0, 0.0)
        self.distanceFromRayOrigin = distanceFromRayOrigin
        self.front_face = None
    def copy(self, other: Hit_record):
        self.point.copy(other.point)
        self.normal.copy(other.normal)
        self.distanceFromRayOrigin = other.distanceFromRayOrigin
        self.front_face = other.front_face
    def set_face_normal(self, ray: Ray, outward_normal: Vector3):
        self.front_face = ray.direction.dot(outward_normal) < 0
        if self.front_face:
            self.normal.copy(outward_normal)
        else:
            self.normal.copy(-outward_normal)

class Hittable(ABC):
    @abstractmethod
    def hit(self, ray: Ray, interval: Interval, hit: Hit_record):
        pass

class HittableList(Hittable):
    def __init__(self):
        self.objects = list()
    def clear(self):
        self.objects.clear()
    def add(self, object: Hittable):
        self.objects.append(object) 
    def hit(self, ray: Ray, interval: Interval, hit: Hit_record):
        object: Hittable
        closest_hit = interval.max
        tempHit = Hit_record()
        hitSomething = False
        for object in self.objects:
            if object.hit(ray, Interval(interval.min, closest_hit), tempHit):
                closest_hit = tempHit.distanceFromRayOrigin
                hit.copy(tempHit)
                hitSomething = True
        return hitSomething
