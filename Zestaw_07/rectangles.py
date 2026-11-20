import unittest
from Zestaw_07.points import Point


class Rectangle:
    """Klasa reprezentująca prostokąty na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        if x1 >= x2 or y1 >= y2:
            raise ValueError("Wymagane x1 < x2 oraz y1 < y2")
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):
        return f"[{self.pt1}, {self.pt2}]"

    def __repr__(self):
        return f"Rectangle({self.pt1.x}, {self.pt1.y}, {self.pt2.x}, {self.pt2.y})"

    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return False
        return self.pt1 == other.pt1 and self.pt2 == other.pt2

    def __ne__(self, other):
        return not self == other

    def center(self):
        cx = (self.pt1.x + self.pt2.x) / 2
        cy = (self.pt1.y + self.pt2.y) / 2
        return Point(cx, cy)

    def area(self):
        width = self.pt2.x - self.pt1.x
        height = self.pt2.y - self.pt1.y
        return width * height

    def move(self, x, y):
        self.pt1 = Point(self.pt1.x + x, self.pt1.y + y)
        self.pt2 = Point(self.pt2.x + x, self.pt2.y + y)

    def intersection(self, other):
        if not isinstance(other, Rectangle):
            raise ValueError("Argument musi być obiektem klasy Rectangle")
        x1 = max(self.pt1.x, other.pt1.x)
        y1 = max(self.pt1.y, other.pt1.y)
        x2 = min(self.pt2.x, other.pt2.x)
        y2 = min(self.pt2.y, other.pt2.y)
        if x1 >= x2 or y1 >= y2:
            raise ValueError("Prostokąty nie mają części wspólnej")
        return Rectangle(x1, y1, x2, y2)

    def cover(self, other):
        if not isinstance(other, Rectangle):
            raise ValueError("Argument musi być obiektem klasy Rectangle")
        x1 = min(self.pt1.x, other.pt1.x)
        y1 = min(self.pt1.y, other.pt1.y)
        x2 = max(self.pt2.x, other.pt2.x)
        y2 = max(self.pt2.y, other.pt2.y)
        return Rectangle(x1, y1, x2, y2)

    def make4(self):
        c = self.center()
        r1 = Rectangle(self.pt1.x, self.pt1.y, c.x, c.y)
        r2 = Rectangle(c.x, self.pt1.y, self.pt2.x, c.y)
        r3 = Rectangle(self.pt1.x, c.y, c.x, self.pt2.y)
        r4 = Rectangle(c.x, c.y, self.pt2.x, self.pt2.y)
        return (r1, r2, r3, r4)


class TestRectangle(unittest.TestCase):

    def setUp(self):
        self.r1 = Rectangle(0, 0, 4, 6)
        self.r2 = Rectangle(2, 2, 6, 8)
        self.r3 = Rectangle(10, 10, 12, 12)

    def test_init(self):
        self.assertEqual(self.r1.pt1, Point(0, 0))
        self.assertEqual(self.r1.pt2, Point(4, 6))
        with self.assertRaises(ValueError):
            Rectangle(2, 0, 2, 3)
        with self.assertRaises(ValueError):
            Rectangle(3, 0, 2, 3)
        with self.assertRaises(ValueError):
            Rectangle(0, 5, 2, 3)

    def test_str(self):
        self.assertEqual(str(self.r1), "[(0, 0), (4, 6)]")

    def test_repr(self):
        self.assertEqual(repr(self.r1), "Rectangle(0, 0, 4, 6)")

    def test_eq_ne(self):
        self.assertTrue(self.r1 == Rectangle(0, 0, 4, 6))
        self.assertFalse(self.r1 == self.r2)
        self.assertTrue(self.r1 != self.r2)
        self.assertFalse(self.r1 != Rectangle(0, 0, 4, 6))

    def test_center(self):
        self.assertEqual(self.r1.center(), Point(2, 3))

    def test_area(self):
        self.assertEqual(self.r1.area(), 24)
        self.assertEqual(self.r3.area(), 4)

    def test_move(self):
        self.r1.move(2, 3)
        self.assertEqual(self.r1, Rectangle(2, 3, 6, 9))

    def test_intersection(self):
        self.assertEqual(self.r1.intersection(self.r2), Rectangle(2, 2, 4, 6))
        with self.assertRaises(ValueError):
            self.r1.intersection(self.r3)
        with self.assertRaises(ValueError):
            self.r1.intersection("nie prostokąt")

    def test_cover(self):
        self.assertEqual(self.r1.cover(self.r2), Rectangle(0, 0, 6, 8))
        self.assertEqual(self.r1.cover(self.r3), Rectangle(0, 0, 12, 12))
        with self.assertRaises(ValueError):
            self.r1.cover(123)

    def test_make4(self):
        expected = (
            Rectangle(0, 0, 2, 3),
            Rectangle(2, 0, 4, 3),
            Rectangle(0, 3, 2, 6),
            Rectangle(2, 3, 4, 6),
        )
        self.assertEqual(self.r1.make4(), expected)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()