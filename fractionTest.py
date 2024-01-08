import unittest
from fraction import Fraction


class TestFraction(unittest.TestCase):

    def test_init(self):
        # Test with a positive numerator and denominator
        fraction1 = Fraction(10, 2)
        self.assertEqual(fraction1.numerator, 5)
        self.assertEqual(fraction1.denominator, 1)

        # Test with a negative numerator and positive denominator
        fraction2 = Fraction(-8, 4)
        self.assertEqual(fraction2.numerator, -2)
        self.assertEqual(fraction2.denominator, 1)

        # Test with a positive numerator and negative denominator
        fraction3 = Fraction(6, -3)
        self.assertEqual(fraction3.numerator, -2)
        self.assertEqual(fraction3.denominator, 1)

        # Test with a negative numerator and denominator
        fraction4 = Fraction(-15, -5)
        self.assertEqual(fraction4.numerator, 3)
        self.assertEqual(fraction4.denominator, 1)

        # Test with numerator and denominator both being zero
        with self.assertRaises(ZeroDivisionError):
            Fraction(0, 0)

        # Test with denominator being zero
        with self.assertRaises(ZeroDivisionError):
            Fraction(10, 0)

        # Test with large numerator and denominator
        fraction5 = Fraction(1000000, 500000)
        self.assertEqual(fraction5.numerator, 2)
        self.assertEqual(fraction5.denominator, 1)

    def test_str_representation(self):
        # Test with positive numerator and denominator
        self.assertEqual(str(Fraction(3, 4)), '3/4')

        # Test with positive numerator and negative denominator
        self.assertEqual(str(Fraction(5, -2)), '-5/2')

        # Test with negative numerator and positive denominator
        self.assertEqual(str(Fraction(-1, 3)), '-1/3')

        # Test with negative numerator and denominator
        self.assertEqual(str(Fraction(-8, -4)), '2/1')

        # Test with already simplified fraction
        self.assertEqual(str(Fraction(1, 2)), '1/2')

        # Test with large numerator and denominator
        self.assertEqual(str(Fraction(1000000, 500000)), '2/1')

    def test_mixed_number_representation(self):
        self.assertEqual(Fraction(5, 2).as_mixed_number(), '2 + 1/2')
        self.assertEqual(Fraction(7, 3).as_mixed_number(), '2 + 1/3')

    def test_addition(self):
        # Test with positive fractions
        result1 = Fraction(1, 2) + Fraction(1, 4)
        self.assertEqual(result1, Fraction(3, 4))

        # Test with negative fractions
        result2 = Fraction(-1, 2) + Fraction(1, 4)
        self.assertEqual(result2, Fraction(-1, 4))

        # Test with neutral element
        result3 = Fraction(3, 4) + Fraction(0, 1)
        self.assertEqual(result3, Fraction(3, 4))

        # Test with absorbing element
        result4 = Fraction(1, 2) + Fraction(0, 1)
        self.assertEqual(result4, Fraction(1, 2))

    def test_subtraction(self):
        # Test with positive fractions
        result1 = Fraction(3, 4) - Fraction(1, 4)
        self.assertEqual(result1, Fraction(1, 2))

        # Test with negative fractions
        result2 = Fraction(-1, 2) - Fraction(1, 4)
        self.assertEqual(result2, Fraction(-3, 4))

        # Test with neutral element
        result3 = Fraction(3, 4) - Fraction(0, 1)
        self.assertEqual(result3, Fraction(3, 4))

        # Test with absorbing element
        result4 = Fraction(1, 2) - Fraction(0, 1)
        self.assertEqual(result4, Fraction(1, 2))

    def test_multiplication(self):
        # Test with positive fractions
        result1 = Fraction(1, 2) * Fraction(2, 3)
        self.assertEqual(result1, Fraction(1, 3))

        # Test with negative fractions
        result2 = Fraction(-1, 2) * Fraction(2, 3)
        self.assertEqual(result2, Fraction(-1, 3))

        # Test with neutral element
        result3 = Fraction(3, 4) * Fraction(1, 1)
        self.assertEqual(result3, Fraction(3, 4))

        # Test with absorbing element
        result4 = Fraction(1, 2) * Fraction(0, 1)
        self.assertEqual(result4, Fraction(0, 1))

    def test_division(self):
        # Test with positive fractions
        result1 = Fraction(1, 2) / Fraction(2, 3)
        self.assertEqual(result1, Fraction(3, 4))

        # Test with negative fractions
        result2 = Fraction(-1, 2) / Fraction(2, 3)
        self.assertEqual(result2, Fraction(-3, 4))

        # Test with neutral element
        result3 = Fraction(3, 4) / Fraction(1, 1)
        self.assertEqual(result3, Fraction(3, 4))

        # Test with division by absorbing element
        with self.assertRaises(ZeroDivisionError):
            result4 = Fraction(1, 2) / Fraction(0, 1)

    def test_power(self):
        # Test with positive fraction
        result1 = Fraction(2, 3) ** 2
        self.assertEqual(result1, Fraction(4, 9))

        # Test with negative exponent
        result2 = Fraction(2, 3) ** -2
        self.assertEqual(result2, Fraction(9, 4))

        # Test with neutral exponent
        result3 = Fraction(2, 3) ** 0
        self.assertEqual(result3, Fraction(1, 1))

    def test_equality(self):
        # Test with equivalent fractions
        self.assertEqual(Fraction(1, 2), Fraction(2, 4))

        # Test with non-equivalent fractions
        self.assertNotEqual(Fraction(3, 4), Fraction(1, 2))

    def test_float_conversion(self):
        self.assertEqual(float(Fraction(1, 2)), 0.5)
        self.assertEqual(float(Fraction(-3, 4)), -0.75)

    def test_is_zero(self):
        self.assertTrue(Fraction(0, 5).is_zero())
        self.assertFalse(Fraction(-1, 3).is_zero())

    def test_is_integer(self):
        self.assertTrue(Fraction(5, 1).is_integer())
        self.assertFalse(Fraction(-3, 4).is_integer())

    def test_is_proper(self):
        self.assertTrue(Fraction(2, 3).is_proper())
        self.assertFalse(Fraction(-5, 4).is_proper())

    def test_is_unit(self):
        self.assertTrue(Fraction(1, 1).is_unit())
        self.assertFalse(Fraction(-3, 4).is_unit())

    def test_is_adjacent_to(self):
        self.assertFalse(Fraction(2, 3).is_adjacent_to(Fraction(5, 4)))
        self.assertTrue(Fraction(1, 2).is_adjacent_to(Fraction(2, 3)))
        self.assertFalse(Fraction(-2, 3).is_adjacent_to(Fraction(-5, 4)))
        self.assertTrue(Fraction(-1, 2).is_adjacent_to(Fraction(-2, 3)))

if __name__ == '__main__':
    unittest.main()
