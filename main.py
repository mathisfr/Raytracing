import sys
from rt.vector3 import Vector3
from rt.camera import Camera
from rt.primitive import Sphere
from rt.hittable import HittableList
from PIL import Image

def main() -> int:
    camera = Camera();
    im = Image.new("RGB", (camera.image_width, camera.image_height), (255, 255, 255))
    
    world = HittableList()
    world.add(Sphere(0.5, Vector3(0.0,0.0,-1.0)))
    world.add(Sphere(100.0, Vector3(0.0,-100.5,-1.0)))

    camera.render(im, world)

    # im = im.resize((1280, 720), resample=Image.Resampling.NEAREST)
    im.show()
    im.save("output.jpg")
    return 0

if __name__ == '__main__':
    sys.exit(main())