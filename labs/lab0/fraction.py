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

class ReducedFraction(Fraction):
    """A version of Fraction that always keeps itself in maximally reduced form"""

    def __init__(self, numerator, denominator=1):
        """ Initialiser, given both numerator and denominator """
        super().__init__(numerator, denominator)
        self._reduce()

    def _reduce(self):
        """ Reduces the fraction to its simplest possible form (mutating function). """
        gcd = find_gcd(self.numerator, self.denominator)
        self.numerator //= gcd
        self.denominator //= gcd

    def __repr__(self):
        """ Prints the fraction in the form ReducedFraction(numerator, denominator)"""
        return f"ReducedFraction({self.numerator}, {self.denominator})"

def find_gcd(num1, num2):
    """
    Returns the Greatest Common Divisor (GCD) of num1 and num2.
    Assumes num1 and num2 are positive integers.
    """
    smaller = min(num1, num2)
    for i in range(smaller, 1, -1):
        if num1 % i == 0 and num2 % i == 0:
            return i
    return 1

# TESTING
def t1():
    r = ReducedFraction(3, 12)
    print('repr:', repr(r))
    print('str:', r)
    print('numerator is an int:', isinstance(r.numerator, int))
    print('denominator is an int:', isinstance(r.denominator, int))

def t2():
    r = ReducedFraction(12, 24)
    print('repr:', repr(r))
    print('str:', r)
    print('numerator is an int:', isinstance(r.numerator, int))
    print('denominator is an int:', isinstance(r.denominator, int))

capture_and_assert_file(t1, "tests/t1.txt")
capture_and_assert_file(t2, "tests/t2.txt")