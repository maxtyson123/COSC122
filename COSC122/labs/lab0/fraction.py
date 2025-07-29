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

    def __add__(self, other):
        """
        Adds another fraction (left) to this one following and simplifies it

        :return: A new, simplified fraction, the sum of this fraction + other one
        """
        fraction_result = super().__add__(other)
        return ReducedFraction(
            fraction_result.numerator,
            fraction_result.denominator
        )

    def __mul__(self, other):
        """
        Multiplies another fraction (left) by this one following and simplifies it

        :return: A new, simplified fraction, the product of this fraction * other one
        """
        fraction_result = super().__mul__(other)
        return ReducedFraction(
            fraction_result.numerator,
            fraction_result.denominator
        )

class MixedNumber:
    """ An Improper fraction representation in the form X a/b  """

    def __init__(self, whole_part, fraction_part):
        """ Creates a new MixedNumber with whole and fraction parts """

        # Ensure whole is an int
        if not isinstance(whole_part, int):
            raise ValueError("Whole part must be int")

        if isinstance(fraction_part, Fraction):
            # Convert to reduced form
            fraction_part = ReducedFraction(fraction_part.numerator, fraction_part.denominator)

        # Ensure fraction is a fraction
        if not isinstance(fraction_part, ReducedFraction):
            raise ValueError("Fraction part must be fraction")

        # Store the variables
        self.whole_part     = whole_part
        self.fraction_part  = fraction_part
        self.simplify()

    def simplify(self):
        """ Converts the improper fraction part into a mixed number """
        self.whole_part += self.fraction_part.numerator // self.fraction_part.denominator
        self.fraction_part.numerator %= self.fraction_part.denominator

    def __repr__(self):
        """ Prints the mixed number in the form MixedNumber(whole_part, fraction_part)"""
        return f"MixedNumber({self.whole_part}, {repr(self.fraction_part)})"

    def __str__(self):
        """ Prints the fraction in the form 'whole and numerator/denominator'"""
        return f"{self.whole_part} and {self.fraction_part}"

    def __add__(self, other):
        """
         Adds another mixed number (left) to this one following and simplifies it

         :return: A new, simplified mixed number, the sum of the two numbers whole parts
                  and fraction parts, simplified
         """
        return MixedNumber(
            self.whole_part + other.whole_part,
            self.fraction_part + other.fraction_part
        )


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
    mixed_num = MixedNumber(3, Fraction(4, 6))
    print(mixed_num)

def t2():
    mixed_num = MixedNumber(4, Fraction(7, 3))
    print(mixed_num)

def t3():
    fraction_1 = Fraction(3, 4)
    fraction_2 = Fraction(4, 6)
    mixed_num_1 = MixedNumber(2, fraction_1)
    mixed_num_2 = MixedNumber(1, fraction_2)
    print(mixed_num_1 + mixed_num_2)

capture_and_assert_file(t1, "tests/t1.txt")
capture_and_assert_file(t2, "tests/t2.txt")
capture_and_assert_file(t3, "tests/t3.txt")