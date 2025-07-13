from PythonTools.debug import capture_and_assert_file

class Fraction():
    """Defines a Fraction type that has an integer numerator and a non-zero integer denominator"""

    def __init__(self, num=0, denom=1):
        """ Creates a new Fraction with numerator num and denominator denom"""
        if isinstance(num, int) and isinstance(denom, int):
            self.numerator = num
            if denom != 0:
                self.denominator = denom
            else:
                raise ZeroDivisionError
        else:
            raise ValueError('Numerator and denominator must be ints')

    def __str__(self):
        """ Prints the fraction in the form numerator/denominator"""
        return str(self.numerator) + "/" + str(self.denominator)

    def __repr__(self):
        """ Prints the fraction in the form Fraction(numerator, denominator)"""
        return f"Fraction({self.numerator}, {self.denominator})"

    def __add__(self, other):
        """
        Adds another fraction (left) to this one following the rules:
        - numerator is (self.numerator * other.denominator ) + (other.numerator * self.denominator), and
        - denominator is self.denominator * other.denominator

        :return A new fraction, the sum of this fraction + other one
        """
        return Fraction(
            (self.numerator * other.denominator ) + (other.numerator * self.denominator),
            self.denominator * other.denominator
        )

    def __mul__(self, other):
        """
        Multiply this fraction with another fraction.

        :return: A new fraction, the product of this fraction * other one
        """
        return Fraction(
            self.numerator * other.numerator,
            self.denominator * other.denominator
        )

    def __eq__(self, other):
        """
        Check if this fraction is equal to another

        :return: True if the fraction equals the other fraction in the simplest form (ie 1/2 == 2/4)
        """

        # Cross multiplication check
        return  self.numerator * other.denominator == other.numerator * self.denominator

# TESTING
def t1():
    x = Fraction(1, 2)
    y = Fraction(1, 2)
    print(x == y)

def t2():
    x = Fraction(21, 30)
    y = Fraction(7, 10)
    print(x == y)
    print("x's numerator is", x.numerator)
    print("x's denominator is", x.denominator)
    print("y's numerator is", y.numerator)
    print("y's denominator is", y.denominator)

capture_and_assert_file(t1, "tests/t1.txt")
capture_and_assert_file(t2, "tests/t2.txt")