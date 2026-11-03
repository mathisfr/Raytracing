from .vector3 import Color3, Vector3
from .ray import Ray
from abc import ABC, abstractmethod

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .hittable import Hit_record

class Material(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def scatter(self, ray_in: Ray, hit: Hit_record, attenuation: Color3, ray_out: Ray) -> bool:
        return False
    
class Lambertian(Material):
    def __init__(self, albedo: Color3):
        self.albedo = albedo
    def scatter(self, ray_in: Ray, hit: Hit_record, attenuation: Color3, ray_out: Ray) -> bool:
        randomDirection = hit.normal + Vector3.randomSphericalUnitVector()
        ray_out.copy(Ray(hit.point, randomDirection)) 
        attenuation.copy(self.albedo)
        return True
    
class Metal(Material):
    def __init__(self, albedo: Color3):
        self.albedo = albedo
    def scatter(self, ray_in: Ray, hit: Hit_record, attenuation: Color3, ray_out: Ray) -> bool:
        reflection = (((hit.normal * hit.normal.dot(-ray_in.direction)) + ray_in.direction) * 2.0) - ray_in.direction
        ray_out.copy(Ray(hit.point, reflection)) 
        attenuation.copy(self.albedo)
        return True

class Fuzz(Material):
    def __init__(self, albedo: Color3, fuzz: float):
        self.albedo = albedo
        self.fuzz = fuzz
    def scatter(self, ray_in: Ray, hit: Hit_record, attenuation: Color3, ray_out: Ray) -> bool:
        reflection = (((hit.normal * hit.normal.dot(-ray_in.direction)) + ray_in.direction) * 2.0) - ray_in.direction
        reflectionFuzz = reflection.normalize() + (Vector3.randomSphericalUnitVector() * self.fuzz)
        ray_out.copy(Ray(hit.point, reflectionFuzz)) 
        attenuation.copy(self.albedo)
        return ray_out.direction.dot(hit.normal) > 0.0