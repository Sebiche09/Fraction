import math


class Fraction:
    """Class representing a fraction and operations on it

    Author : V. Van den Schrieck
    Date : October 2021
    This class allows fraction manipulations through several operations.
    """

    def __init__(self, num: int = 0, den: int = 1):
        """This builds a fraction based on some numerator and denominator.

        PRE : - num: an int
              - den: a non-null int
        POST : set the following attributes :
               - num : the reduced numerator of the fraction
               - den : the reduced denominator of the fraction
        """
        if den == 0:
            raise ZeroDivisionError("The denominator of a fraction can't be null.")

        abs_num = abs(num)
        if num / den < 0:
            num = -abs_num
        else:
            num = abs_num
        # Calcul du PGCD pour avoir la forme réduite de la fraction
        gcd = math.gcd(num, den)
        self.__num = num // gcd
        self.__den = abs(den) // gcd

    @property
    def numerator(self) -> int:
        return self.__num

    @property
    def denominator(self) -> int:
        return self.__den

    # ------------------ Static methods ------------------

    @staticmethod
    def __set_fraction_param(other):
        """Verify if another value is an integer or a fraction and transform it in a fraction

         PRE : - other: an integer or a fraction
         POST : the fractionated other value
         """
        if isinstance(other, int):
            other = Fraction(other)

        if not isinstance(other, Fraction):
            raise ValueError()

        return other

    # ------------------ Textual representations ------------------

    def __str__(self) -> str:
        """Return a textual representation of the reduced form of the fraction

        PRE : -
        POST : the numerator and the denominator separated by a backslash
        """
        return f'{self.numerator}/{self.denominator}'

    def as_mixed_number(self) -> str:
        """Return a textual representation of the reduced form of the fraction as a mixed number

        A mixed number is the sum of an integer and a proper fraction

        PRE : -
        POST : the fraction as a mixed number; the sum of the integer part and the fraction part
        """
        int_part = self.numerator // self.denominator
        fraction_part = Fraction(self.numerator % self.denominator, self.denominator)
        return f'{int_part} + {fraction_part}'

    # ------------------ Operators overloading ------------------

    def __add__(self, other):
        """Overloading of the + operator for fractions

         PRE : - other: an integer or a fraction
         POST : a fraction that sums the current fraction and the other fraction
         """
        other = self.__set_fraction_param(other)

        numerator = (self.numerator * other.denominator) + (other.numerator * self.denominator)
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)

    def __sub__(self, other):
        """Overloading of the - operator for fractions

        PRE : - other: an integer or a fraction
        POST : a fraction that subtracts the current fraction and the other fraction
        """
        other = self.__set_fraction_param(other)

        numerator = self.numerator * other.denominator - other.numerator * self.denominator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)

    def __mul__(self, other):
        """Overloading of the * operator for fractions

        PRE : - other: an integer or a fraction
        POST : a fraction that multiplies the current fraction and the other fraction
        """
        other = self.__set_fraction_param(other)

        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)

    def __truediv__(self, other):
        """Overloading of the / operator for fractions

        PRE : - other: an integer or a fraction
        POST : a fraction that truly divides the current fraction and the other fraction
        """
        other = self.__set_fraction_param(other)

        numerator = self.numerator * other.denominator
        denominator = self.denominator * other.numerator
        return Fraction(numerator, denominator)

    def __pow__(self, other: int):
        """Overloading of the ** operator for fractions

        PRE : - other: an integer
        POST : - the current fraction powered by another integer
        """
        if other != 0 and self.is_zero():
            return Fraction()

        numerator = self.numerator
        denominator = self.denominator

        if other < 0:
            numerator, denominator = denominator, numerator
            other *= -1

        numerator **= other
        denominator **= other
        return Fraction(numerator, denominator)

    def __eq__(self, other) -> bool:
        """Overloading of the == operator for fractions

        PRE : - other: a fraction, an integer or a float
        POST : the equality between the current fraction and the other value

        """
        return float(self) == float(other)

    def __float__(self) -> float:
        """Returns the decimal value of the fraction

        PRE : -
        POST : the floated value of the fraction
        """
        return self.numerator / self.denominator

    # ------------------ Properties checking  ------------------

    def is_zero(self) -> bool:
        """Check if a fraction's value is 0

        PRE : -
        POST : the numerator is null
        """
        return not self.numerator

    def is_integer(self) -> bool:
        """Check if a fraction is integer (ex : 8/4, 3, 2/2, ...)

        PRE : -
        POST : the reduced denominator equals 1
        """
        return self.denominator == 1

    def is_proper(self) -> bool:
        """Check if the absolute value of the fraction is < 1

        PRE : -
        POST : the absolute value of the fraction is < 1
        """
        return abs(float(self)) < 1

    def is_unit(self) -> bool:
        """Check if a fraction's numerator is 1 in its reduced form

        PRE : -
        POST : the reduced numerator equals 1
        """
        return self.numerator == 1

    def is_adjacent_to(self, other) -> bool:
        """Check if two fractions differ by a unit fraction

        Two fractions are adjacents if the absolute value of the difference them is a unit fraction

        PRE : - other: a fraction
        POST : ?
        """
        difference = abs(self - other)
        return difference.is_unit()

if __name__ == '__main__':
    print('--- TEST : FRACTION CLASS ---\n')
    try:
        print('Fraction(10,0) :', end=' ')
        print(Fraction(10, 0))
    except ZeroDivisionError as error:
        print(error)

    num_frac1 = int(input('Numerator Fraction 1: '))
    den_frac1 = int(input('Denominator Fraction 1: '))
    num_frac2 = int(input('Numerator Fraction 2: '))
    den_frac2 = int(input('Denominator Fraction 2: '))

    frac1 = Fraction(num_frac1, den_frac1)
    print(f"Fraction 1 : {frac1} ; {frac1.as_mixed_number()}")
    frac2 = Fraction(num_frac2, den_frac2)
    print(f"Fraction 2 : {frac2} ; {frac2.as_mixed_number()}\n")

    print(f"{frac1} + {frac2} = {frac1 + frac2}")
    print(f"{frac1} - {frac2} = {frac1 - frac2}")
    print(f"{frac1} * {frac2} = {frac1 * frac2}")
    print(f"{frac1} / {frac2} = {frac1 / frac2}")
    print(f"{frac1} ** 4 = {frac1 ** 4}")

    print(f"Is {frac1} zero ? : {frac1.is_zero()}")
    print(f"Is {frac2} zero ? : {frac2.is_zero()}")
    print(f"Is {frac1} an integer ? : {frac1.is_integer()}")
    print(f"Is {frac2} an integer ? : {frac2.is_integer()}")
    print(f"Is {frac1} proper ? : {frac1.is_proper()}")
    print(f"Is {frac2} proper ? : {frac2.is_proper()}")
    print(f"Is {frac1} unit ? : {frac1.is_unit()}")
    print(f"Is {frac2} unit ? : {frac2.is_unit()}")
    print(f"Is {frac1} and {frac2} adjacents ? : {frac1.is_adjacent_to(frac2)}\n")