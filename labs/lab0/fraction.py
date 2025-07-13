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

# TESTING
def t1():
    f = Fraction(3, 4)
    print(f)

def t2():
    f = Fraction(3, 4)
    print(repr(f))

capture_and_assert_file(t1, "tests/t1.txt")
capture_and_assert_file(t2, "tests/t2.txt")