from PythonTools.debug import capture_and_assert, capture_and_assert_file


class Rectangle(object):
    """ Rectangle class """

    def __init__(self, width=1, height=2):
        self.width = width
        self.height = height

    def area(self) -> int:
        """
        Calculates the area of the Rectangle using the formula width * height

        :return: The area
        """
        return  self.width * self.height

    def perimeter(self) -> int:
        """
        Calculates the perimeter of the Rectangle using the forumala 2 * (width + height)

        :return:
        """
        return 2 * (self.width + self.height)

    def __str__(self):
        """
        Prints the rectangle represented by "#"

        :return:
        """

        # Form each row of "#"
        return "\n".join("#" * self.width for y in range(self.height))


# TESTING
def t1():
    recker = Rectangle(3, 2)
    print(recker)

def t2():
    recker = Rectangle(2, 3)
    print(recker)

def t3():
    recker = Rectangle(20, 5)
    print(recker)

capture_and_assert_file(t1, "tests/t1.txt")
capture_and_assert_file(t2, "tests/t2.txt")
capture_and_assert_file(t3, "tests/t3.txt")