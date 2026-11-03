import sys
from rt.vector3 import Vector3, Color3
from rt.camera import Camera
from rt.primitive import Sphere
from rt.hittable import HittableList
from rt.material import Lambertian, Metal, Fuzz
from PIL import Image

def main() -> int:
    camera = Camera();
    im = Image.new("RGB", (camera.image_width, camera.image_height), (255, 255, 255))
    
    world = HittableList()
    
    sphere1: Fuzz = Fuzz(Color3(0.85, 0.55, 0.18), 0.2)
    sphere2: Metal = Metal(Color3(0.25, 0.45, 0.85))
    ground: Lambertian = Lambertian(Color3(0.35, 0.38, 0.45))
    world.add(Sphere(0.5, Vector3(0.6,0.0,-1.0), sphere1))
    world.add(Sphere(0.5, Vector3(-0.6,0.6,-1.0), sphere2))
    world.add(Sphere(100.0, Vector3(0.0,-100.5,-1.0), ground))

    camera.render(im, world)

    im.show()
    im.save("output.jpg")
    return 0

if __name__ == '__main__':
    sys.exit(main())