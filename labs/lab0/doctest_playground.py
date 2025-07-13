""" Doctests are fun """
import doctest

def triple(n):
    """ Returns triple n, ie, 3*n
    >>> triple(1)
    3
    >>> triple(10)
    30
    >>> triple('wow')
    'wowwowwow'
    >>> triple(3)
    9
    """
    return 3 * n


doctest.testmod()