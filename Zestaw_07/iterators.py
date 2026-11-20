import itertools
import random
import unittest

iter_a = itertools.cycle([0, 1])
iter_b = iter(lambda: random.choice(("N", "E", "S", "W")), None)
iter_c = itertools.cycle(range(7))


class TestIterators(unittest.TestCase):

    def setUp(self):
        self.it_a = itertools.cycle([0, 1])
        self.it_b = iter(lambda: random.choice(("N", "E", "S", "W")), None)
        self.it_c = itertools.cycle(range(7))

    def test_iter_a(self):
        result = [next(self.it_a) for _ in range(8)]
        self.assertEqual(result, [0, 1, 0, 1, 0, 1, 0, 1])

    def test_iter_b(self):
        valid = {"N", "E", "S", "W"}
        result = [next(self.it_b) for _ in range(20)]
        for direction in result:
            self.assertIn(direction, valid)

    def test_iter_c(self):
        result = [next(self.it_c) for _ in range(15)]
        self.assertEqual(result, [0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6, 0])

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()