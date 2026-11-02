import sys
from rt.vector3 import Vector3, Color3
from rt.camera import Camera
from rt.primitive import Sphere
from rt.hittable import HittableList
from rt.material import Lambertian
from PIL import Image

def main() -> int:
    camera = Camera();
    im = Image.new("RGB", (camera.image_width, camera.image_height), (255, 255, 255))
    
    world = HittableList()
    
    albedoRed: Lambertian = Lambertian(Color3(1.0,0.0,0.0))
    albedoGreen: Lambertian = Lambertian(Color3(0.0,1.0,0.0))
    albedoWhite: Lambertian = Lambertian(Color3(1.0,1.0,1.0))
    world.add(Sphere(0.5, Vector3(0.6,0.0,-1.0), albedoRed))
    world.add(Sphere(0.5, Vector3(-0.6,0.0,-1.0), albedoGreen))
    world.add(Sphere(100.0, Vector3(0.0,-100.5,-1.0), albedoWhite))

    camera.sample = 100
    camera.depth = 50
    camera.render(im, world)

    # im = im.resize((1280, 720), resample=Image.Resampling.NEAREST)
    im.show()
    im.save("output.jpg")
    return 0

if __name__ == '__main__':
    sys.exit(main())