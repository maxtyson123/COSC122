""" Your docstring should go here
Along with your name and email address
"""
from time import sleep

import classes




def binary_stolen_plate_finder(stolen_plates, sighted_plates):
    """ Takes two lists of NumberPlates, returns a list and an integer.
    You can assume the stolen list will be in ascending order.
    You must assume that the sighted list is unsorted.

    The returned list contains stolen number plates that were sighted,
    in the same order as they appeared in the sighted list.
    The integer is the number of NumberPlate comparisons that
    were made.

    You can assume that each input list contains only unique plates,
    ie, neither list will contain more than one copy of any given plate.
    This fact will be very helpful in some special cases - you should
    think about when you can stop searching.    

    Note: you shouldn't alter either of the provided lists and you
    shouldn't make copies of either provided list. 
    """
    result_list = []
    total_comparisons = 0

    # Helper function
    def binary_search(item, check_list):
        """
        Preforms one iteration of a binary search

        :param item: The item to look for
        :param check_list: The list to check
        :return: The half of the list containing the item or a list only containing the item
        """

        halfway = len(check_list) // 2

        # Is the item in the start half of this list
        if item < check_list[halfway]:
            return check_list[:halfway]
        else:
            return check_list[halfway:]

    for plate in sighted_plates:

        # Try to find the item
        items = stolen_plates
        while len(items) > 1:
            total_comparisons += 1
            items = binary_search(plate, items)

        # Store the item if found
        found = items[0]
        total_comparisons += 1
        if found == plate:
            result_list.append(found)

        # All the stolen plates have been found
        if len(result_list) == len(stolen_plates):
            break


    return result_list, total_comparisons


# ------------------------------------------------
# Extra stuff for your personal testing regime
# You can leave this stuff out of your submission


def run_tests():
    # wrap raw strings in NumberPlate for proper comparison counting
    raw_stolen = ["PK4720", "SP8651"]
    raw_sighted = ["UG7543", "KN5190", "WW1181", "QB0150", "SP8651"]

    stolen_objects = [classes.NumberPlate(p) for p in raw_stolen]
    sighted_objects = [classes.NumberPlate(p) for p in raw_sighted]

    found, comps = binary_stolen_plate_finder(stolen_objects, sighted_objects)
    print("Found:", [str(p) for p in found])
    print("Comparisons:", comps)



if __name__ == '__main__':
    # This won't run when your module is imported from.
    # Use run_tests to try out some of your own simple tests.

    run_tests()
