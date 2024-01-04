import unittest
from fraction import Fraction


class TestFraction(unittest.TestCase):

    def test_init(self):
        with self.assertRaises(ZeroDivisionError):
            Fraction(10, 0)

    def test_str_representation(self):
        self.assertEqual(str(Fraction(3, 4)), '3/4')
        self.assertEqual(str(Fraction(1, 2)), '1/2')

    def test_mixed_number_representation(self):
        self.assertEqual(Fraction(5, 2).as_mixed_number(), '2 + 1/2')
        self.assertEqual(Fraction(7, 3).as_mixed_number(), '2 + 1/3')

    def test_addition(self):
        result = Fraction(1, 2) + Fraction(1, 4)
        self.assertEqual(result, Fraction(3, 4))

    def test_subtraction(self):
        result = Fraction(3, 4) - Fraction(1, 4)
        self.assertEqual(result, Fraction(1, 2))

    def test_multiplication(self):
        result = Fraction(1, 2) * Fraction(2, 3)
        self.assertEqual(result, Fraction(1, 3))

    def test_division(self):
        result = Fraction(1, 2) / Fraction(2, 3)
        self.assertEqual(result, Fraction(3, 4))

    def test_power(self):
        result = Fraction(2, 3) ** 2
        self.assertEqual(result, Fraction(4, 9))

    def test_equality(self):
        self.assertEqual(Fraction(1, 2), Fraction(2, 4))
        self.assertNotEqual(Fraction(3, 4), Fraction(1, 2))

    def test_float_conversion(self):
        self.assertEqual(float(Fraction(1, 2)), 0.5)
        self.assertEqual(float(Fraction(3, 4)), 0.75)

    def test_is_zero(self):
        self.assertTrue(Fraction(0, 5).is_zero())
        self.assertFalse(Fraction(1, 3).is_zero())

    def test_is_integer(self):
        self.assertTrue(Fraction(5, 1).is_integer())
        self.assertFalse(Fraction(3, 4).is_integer())

    def test_is_proper(self):
        self.assertTrue(Fraction(2, 3).is_proper())
        self.assertFalse(Fraction(5, 4).is_proper())

    def test_is_unit(self):
        self.assertTrue(Fraction(1, 1).is_unit())
        self.assertFalse(Fraction(3, 4).is_unit())

    def test_is_adjacent_to(self):
        self.assertTrue(Fraction(1, 2).is_adjacent_to(Fraction(3, 2)))
        self.assertFalse(Fraction(2, 3).is_adjacent_to(Fraction(5, 4)))


if __name__ == '__main__':
    unittest.main()
