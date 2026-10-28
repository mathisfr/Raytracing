from __future__ import annotations

from .vector3 import Vector3, Color3
from .hittable import HittableList, Hit_record
from .interval import Interval
from . import INFINITY
from .ray import Ray
from .color import write_color
import random
from PIL import Image

import threading
import time

class Camera:
    def __init__(self, image_height:float = 400):
        self.origin = Vector3(0.0,0.0,0.0)
        self.focal = 1.0
        self.ratio = 16/9
        self.image_height = image_height
        self.image_width = int(self.image_height * self.ratio)
        self.viewport_height = 2.0
        self.viewport_width = self.viewport_height * (self.image_width / self.image_height)
        self.viewport_u = Vector3(self.viewport_width, 0.0, 0.0)
        self.viewport_v = Vector3(0.0, -self.viewport_height, 0.0)
        self.viewport_u_delta = self.viewport_u / self.image_width
        self.viewport_v_delta = self.viewport_v / self.image_height
        self.viewport_top_left = self.origin - Vector3(0.0,0.0,self.focal) - 0.5 * (self.viewport_u + self.viewport_v)
        self.pixel00_loc = self.viewport_top_left + 0.5 * (self.viewport_u_delta + self.viewport_v_delta)
        self.sample = 100
        self.depth = 50

        self.debugThread = None
        self.state = 0
        self.total = 0

    @staticmethod
    def ray_color(ray: Ray, world: HittableList, depth: int = 1) -> Color3:
        if depth <= 0:
            return Color3(0.0,0.0,0.0)

        hit = Hit_record()
        isHit = world.hit(ray, Interval(0.001, INFINITY), hit)
        if isHit:
            randomDirection = hit.normal + Vector3.randomSphericalUnitVector()
            ray_color = Camera.ray_color(Ray(hit.point, randomDirection), world, depth-1)
            return Color3(0.5 * ray_color.x,0.35* ray_color.y,0.1* ray_color.z) 
            # normalUnitVector = (hit.normal + Vector3(1.0, 1.0, 1.0)) * 0.5
            # return Color3(normalUnitVector.x, normalUnitVector.y, normalUnitVector.z)
        
        directionUnitVector = ray.direction.normalize()
        a = 0.5 * (directionUnitVector.y + 1.0)
        lerpColor = ((1 - a) * Color3(1.0,1.0,1.0)) + (a * Color3(0.5, 0.7, 1.0))
        return lerpColor

    def debugThreadFunction(self):
        pourcentage = 0
        while not (pourcentage == 25):
            pourcentage = int((25 / self.total) * self.state)
            print("\rProcessing |" + "█" * pourcentage + "" + "░" * (25 - pourcentage) + "|", end="", flush=True)
            time.sleep(0.001)
    
    def render(self, im: Image, world: HittableList) -> None:
        self.total = self.image_height * self.image_width
        self.debugThread = threading.Thread(target=self.debugThreadFunction)
        self.debugThread.start()
        for y in range(self.image_height):
            for x in range(self.image_width):
                color = Color3(0.0,0.0,0.0)
                for s in range(self.sample):
                    ray = self.getRay(x, y)
                    color += Camera.ray_color(ray, world, self.depth)
                color /= self.sample
                self.state += 1
                write_color(im, x, y, color)
        self.debugThread.join()

    def getRay(self, x: int, y: int) -> Ray:
        sampleSquare = Camera.sampleSquare()
        pixelSample = self.pixel00_loc + ((y + sampleSquare.y) * self.viewport_v_delta) + ((x + sampleSquare.x) * self.viewport_u_delta)
        direction = pixelSample - self.origin
        return Ray(self.origin, direction)

    @staticmethod
    def sampleSquare() -> Vector3:
        return Vector3(random.random() - 0.5, random.random() - 0.5, 0.0)
    
