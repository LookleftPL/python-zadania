from Zestaw_06.points import Point

class Rectangle:
    """Klasa reprezentująca prostokąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):
        return f"[{self.pt1}, {self.pt2}]"

    def __repr__(self):
        return f"Rectangle({self.pt1.x}, {self.pt1.y}, {self.pt2.x}, {self.pt2.y})"

    def __eq__(self, other):
        return self.pt1 == other.pt1 and self.pt2 == other.pt2

    def __ne__(self, other):        # obsługa rect1 != rect2
        return not self == other

    def center(self):
        cx = (self.pt1.x + self.pt2.x) / 2
        cy = (self.pt1.y + self.pt2.y) / 2
        return Point(cx, cy)

    def area(self):
        width = abs(self.pt2.x - self.pt1.x)
        height = abs(self.pt2.y - self.pt1.y)
        return width * height

    def move(self, x, y):
        self.pt1 = Point(self.pt1.x + x, self.pt1.y + y)
        self.pt2 = Point(self.pt2.x + x, self.pt2.y + y)

# Kod testujący moduł.

import unittest

class TestRectangle(unittest.TestCase):

    def test_str(self):
        self.assertEqual(str(Rectangle(0, 0, 2, 3)), "[(0, 0), (2, 3)]")

    def test_repr(self):
        self.assertEqual(repr(Rectangle(0, 0, 2, 3)), "Rectangle(0, 0, 2, 3)")

    def test_eq(self):
        r1 = Rectangle(1, 1, 4, 5)
        r2 = Rectangle(1, 1, 4, 5)
        r3 = Rectangle(0, 0, 2, 2)
        self.assertTrue(r1 == r2)
        self.assertFalse(r1 == r3)

    def test_ne(self):
        r1 = Rectangle(1, 1, 4, 5)
        r2 = Rectangle(1, 1, 4, 5)
        r3 = Rectangle(0, 0, 2, 2)
        self.assertTrue(r1 != r3)
        self.assertFalse(r1 != r2)

    def test_center(self):
        self.assertEqual(Rectangle(0, 0, 4, 6).center(), Point(2, 3))

    def test_area(self):
        self.assertEqual(Rectangle(0, 0, 4, 5).area(), 20)
        self.assertEqual(Rectangle(1, 1, 4, 5).area(), 12)

    def test_move(self):
        r = Rectangle(0, 0, 2, 2)
        r.move(2, 3)
        self.assertEqual(r, Rectangle(2, 3, 4, 5))

if __name__ == "__main__":
    unittest.main()