import unittest
from rt.vector3 import Vector3
from math import sqrt

class TestVector3(unittest.TestCase):
    def test_iadd(self):
        a = Vector3(1.0,1.0,1.0)
        b = Vector3(1.0,1.0,1.0) 
        a += b
        self.assertEqual(a, Vector3(2.0,2.0,2.0))
    def test_add(self):
        a = Vector3(1.0,1.0,1.0)
        b = Vector3(1.0,1.0,1.0) 
        c = a +b
        self.assertEqual(c, Vector3(2.0,2.0,2.0))
    def test_isub(self):
        a = Vector3(1.0,1.0,1.0)
        b = Vector3(1.0,1.0,1.0) 
        a -= b
        self.assertEqual(a, Vector3(0.0,0.0,0.0))
    def test_sub(self):
        a = Vector3(1.0,1.0,1.0)
        b = Vector3(1.0,1.0,1.0) 
        c = a -b
        self.assertEqual(c, Vector3(0.0,0.0,0.0))
    def test_rmul(self):
        a = Vector3(1.0,1.0,1.0)
        b = 5
        c = b * a
        self.assertEqual(c, Vector3(5.0,5.0,5.0))
    def test_imul(self):
        a = Vector3(1.0,1.0,1.0)
        b = 5
        a *= b
        self.assertEqual(a, Vector3(5.0,5.0,5.0))
    def test_idiv(self):
        a = Vector3(1.0,1.0,1.0)
        b = 2
        a /= b
        self.assertEqual(a, Vector3(0.5,0.5,0.5))    
    def test_div(self):
        a = Vector3(1.0,1.0,1.0)
        b = 2
        c = a / b
        self.assertEqual(c, Vector3(0.5,0.5,0.5))
    def test_normalize(self):
        a = Vector3(1.0,1.0,1.0)
        b = a.normalize()
        expected = 1.0 / sqrt(3.0)
        self.assertAlmostEqual(b.x, expected)
        self.assertAlmostEqual(b.y, expected)
        self.assertAlmostEqual(b.z, expected)
    def test_dot(self):
        a = Vector3(1.0,1.0,1.0)
        b = Vector3(1.0,1.0,1.0)
        c = a.dot(b)
        self.assertEqual(c, 3.0)
    def test_cross(self):
        a = Vector3(1.0,0.0,0.0)
        b = Vector3(0.0,1.0,0.0)
        c = a.cross(b)
        self.assertEqual(c, Vector3(0.0,0.0,1.0))
    def test_neg(self):
        a = Vector3(1.0,1.0,1.0)
        b = -a
        self.assertEqual(b, Vector3(-1.0,-1.0,-1.0))

if __name__ == '__main__':
    unittest.main()