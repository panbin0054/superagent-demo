import unittest

from main import add, greet


class AddTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_zero(self):
        self.assertEqual(add(0, 7), 7)

    def test_add_negative(self):
        self.assertEqual(add(-2, -3), -5)

    def test_add_mixed_sign(self):
        self.assertEqual(add(5, -4), 1)

    def test_add_commutative(self):
        self.assertEqual(add(3, -8), add(-8, 3))


class GreetTest(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("world"), "Hello, world!")


if __name__ == "__main__":
    unittest.main()
