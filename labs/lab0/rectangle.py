from PythonTools.debug import capture_and_assert


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



# TESTING
def t1():
    my_rec = Rectangle(3, 4)
    print(my_rec.area())
    print(my_rec.perimeter())

def t2():
    my_rec = Rectangle()
    print(my_rec.perimeter())

capture_and_assert(t1, """12
14""")
capture_and_assert(t2, "6")
