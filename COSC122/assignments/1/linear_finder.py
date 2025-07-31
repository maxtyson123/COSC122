""" Your docstring should go here
Along with your name and email address
"""

import classes




def linear_stolen_plate_finder(stolen_plates, sighted_plates):
    """
    Takes two lists of NumberPlates as input.
    Returns a list and an integer.

    The returned list contains stolen number plates that were sighted,
    in the same order as they appeared in the sighted list.
    The integer is the number of NumberPlate comparisons that
    were made.

    You cannot assume either list is sorted, ie, you should assume the
    lists are not sorted.

    You can assume that each input list contains only unique plates,
    ie, neither list will contain more than one copy of any given plate.
    This fact will be very helpful in some special cases - you should
    think about when you can stop searching.

    Note: you shouldn't alter either of the provided lists and you
    shouldn't make copies of either provided list. Such things would
    alter data or take extra time!
    """
    result_list = []
    total_comparisons = 0

    for index, plate in enumerate(sighted_plates):

        # Was the plate stolen
        # if plate in stolen_plates:
        #     result_list.append(plate)

        # Was the plate stolen ( I assume this is the way they wanted it done)
        for stolen in stolen_plates:

            total_comparisons += 1
            if stolen == plate:
                result_list.append(plate)
                break

        # All the stolen plates have been found
        if len(result_list) == len(stolen_plates):
            break

    return result_list, total_comparisons


# ------------------------------------------------
# Extra stuff for your personal testing regime
# You can leave this stuff out of your submission

def run_tests():
    """ Use this function to run some simple tests
    to help with developing your awesome answer code.
    You should leave this out of your submission """
    stolen=['SP8651', 'PK4720']
    sighted=['MT2703', 'SP8651', 'CS0118', 'ZU1800', 'PK4720']
    print(linear_stolen_plate_finder(stolen,sighted))


if __name__ == '__main__':
    run_tests()
