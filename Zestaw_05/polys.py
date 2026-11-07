def _strip_zeros(poly):
    p = list(poly)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p

def add_poly(poly1, poly2):
    max_len = max(len(poly1),len(poly2))

    p1 = poly1 + [0] * (max_len - len(poly1))
    p2 = poly2 + [0] * (max_len - len(poly2))

    return _strip_zeros([a+b for a,b in zip(p1,p2)])

def sub_poly(poly1, poly2):
    max_len = max(len(poly1), len(poly2))

    p1 = poly1 + [0] * (max_len - len(poly1))
    p2 = poly2 + [0] * (max_len - len(poly2))

    return _strip_zeros([a - b for a, b in zip(p1, p2)])

def is_zero(poly):
    for value in poly:
        if value != 0:
            return False
    return True

def mul_poly(poly1, poly2):
    if is_zero(poly1) or is_zero(poly2):
        return [0]

    result = [0] * (len(poly1) + len(poly2) -1)

    for i, a in enumerate(poly1):
        for j, b in enumerate(poly2):
            result[i + j] = result[i +j] + a * b
    return _strip_zeros(result)

def eq_poly(poly1, poly2):
    return  _strip_zeros(poly1) == _strip_zeros(poly2)

def eval_poly(poly, x0):
    result = 0
    for i in reversed(poly):
        result = result * x0 + i
    return result

def combine_poly(poly1, poly2):
    result = [0]

    for i in reversed(poly1):
        result = add_poly(mul_poly(result, poly2), [i])

    return _strip_zeros(result)

def pow_poly(poly, n):
    if n == 0:
        return [1]
    result = [1]

    for i in range(n):
        result = mul_poly(result,poly)

    return result


def diff_poly(poly):
    if len(poly) <= 1:
        return [0]

    result = []
    for i in range(1, len(poly)):
        result.append(i * poly[i])

    return result

import unittest

class TestPolynomials(unittest.TestCase):

    def setUp(self):
        self.p1 = [2, 1]
        self.p2 = [2, 1, 0]
        self.p3 = [-3, 0, 1]
        self.p4 = [3]
        self.p5 = [0]
        self.p6 = [0, 0, 0]

    def test_add_poly(self):
        self.assertEqual(add_poly(self.p1, self.p3), [-1, 1, 1])
        self.assertEqual(add_poly(self.p1, self.p5), [2, 1])

    def test_sub_poly(self):
        self.assertEqual(sub_poly(self.p1, self.p3), [5, 1, -1])
        self.assertTrue(is_zero(sub_poly(self.p1, self.p1)))

    def test_mul_poly(self):
        self.assertEqual(mul_poly(self.p1, self.p4), [6, 3])
        self.assertEqual(mul_poly(self.p1, self.p3), [-6, -3, 2, 1])
        self.assertEqual(mul_poly(self.p1, self.p6), [0])

    def test_is_zero(self):
        self.assertFalse(is_zero(self.p1))
        self.assertFalse(is_zero(self.p4))
        self.assertTrue(is_zero(self.p5))
        self.assertTrue(is_zero(self.p6))

    def test_eq_poly(self):
        self.assertTrue(eq_poly(self.p1, self.p2))
        self.assertTrue(eq_poly(self.p5, self.p6))
        self.assertFalse(eq_poly(self.p1, self.p3))

    def test_eval_poly(self):
        self.assertEqual(eval_poly(self.p1, 3), 5)
        self.assertEqual(eval_poly(self.p3, 2), 1)
        self.assertEqual(eval_poly(self.p5, 10), 0)
    def test_combine_poly(self):
        self.assertTrue(eq_poly(combine_poly(self.p3, self.p1), [1, 4, 1]))
        self.assertTrue(eq_poly(combine_poly(self.p1, self.p3), [-1, 0, 1]))

    def test_pow_poly(self):
        self.assertEqual(pow_poly(self.p1, 0), [1])
        self.assertEqual(pow_poly(self.p1, 1), [2, 1])
        self.assertTrue(eq_poly(pow_poly(self.p1, 2), [4, 4, 1]))

    def test_diff_poly(self):
        self.assertEqual(diff_poly(self.p1), [1])
        self.assertEqual(diff_poly(self.p3), [0, 2])
        self.assertEqual(diff_poly(self.p4), [0])

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy