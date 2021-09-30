import unittest

from binary_to_decimal import binary_to_decimal


class MyTestCase(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(binary_to_decimal("0"), int("0"))

    def test_one(self):
        self.assertEqual(binary_to_decimal("1"), int("1"))

    def test_two(self):
        self.assertEqual(binary_to_decimal("10"), int("2"))

    def test_bad_input(self):
        with self.assertRaises(ValueError):
            binary_to_decimal("bad input not binary")



if __name__ == '__main__':
    unittest.main()
