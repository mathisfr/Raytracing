from .interval import Interval
from math import sqrt

def linearToGamma(data: float) -> float:
    if (data > 0):
        return sqrt(data)
    return 0.0

def write_color(image, x, y, color) -> None:
    interval = Interval(0.0, 0.999)
    gr = linearToGamma(color.x)
    gg = linearToGamma(color.y)
    gb = linearToGamma(color.z)
    r = int(interval.clamp(gr) * 256)
    g = int(interval.clamp(gg) * 256)
    b = int(interval.clamp(gb) * 256)
    a = 255
    image.putpixel((x, y), (r, g, b, a))