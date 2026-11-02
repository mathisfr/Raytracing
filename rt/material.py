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
    # randomDirection = hit.normal + Vector3.randomSphericalUnitVector()
    # ray_color = Camera.ray_color(Ray(hit.point, randomDirection), world, depth-1)
    def __init__(self, albedo: Color3):
        self.albedo = albedo
    def scatter(self, ray_in: Ray, hit: Hit_record, attenuation: Color3, ray_out: Ray) -> bool:
        randomDirection = hit.normal + Vector3.randomSphericalUnitVector()
        ray_out.copy(Ray(hit.point, randomDirection)) 
        attenuation.copy(self.albedo)
        return True