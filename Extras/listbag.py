# An implementation of ADT Bag that uses an instance of Python's built-in
# list type as the underlying data structure.

import random

__author__ = 'D.L. Bailey, SCE, Carleton University'
__version__ = '1.01'
__date__ = '1.0: December 26, 2022; 1.01: January 19, 2023'


class ListBag:

    def __init__(self, iterable=[]) -> None:
        """Initialize this ListBag.

        If no iterable is provided, the new ListBag is empty.
        Otherwise, initialize the ListBag by adding the values
        provided by the iterable.

        >>> bag = ListBag()
        >>> bag
        ListBag([])
        >>> bag = ListBag([1, 4, 3, 6, 3])
        >>> bag
        ListBag([1, 4, 3, 6, 3])
        """
        self._elems = []
        for item in iterable:
            self._elems.append(item)
            # or, self.add(item)

    def __str__(self) -> str:
        """Return a string representation of this ListBag.

        >>> bag = ListBag()
        >>> str(bag)
        '{}'
        >>> bag = ListBag([1, 4, 3, 6, 3])
        >>> str(bag)
        '{1, 4, 3, 6, 3}'
        """
        # Use the string representation of the bag's underlying list,
        # with the enclosing '[]' replaced by '{}'.
        s = str(self._elems)
        return '{' + s[1:len(s) - 1] + '}'

    def __repr__(self) -> str:
        """Return the canonical string representation of this ListBag.

        >>> bag = ListBag()
        >>> repr(bag)
        'ListBag([])'
        >>> bag = ListBag([3, 1, 2, 3, 4])
        >>> repr(bag)
        'ListBag([3, 1, 2, 3, 4])'
        """

        # For a ListBag object, obj, the expression eval(repr(obj))
        # returns a new ListBag that is equal to obj.

        return "{0}({1})".format(self.__class__.__name__, self._elems)
        # or, return self.__class__.__name__ + '(' + str(self._elems) + ')'

    def __len__(self) -> int:
        """Return the number of items in this ListBag.

        >>> bag = ListBag()
        >>> len(bag)
        0
        >>> bag = ListBag([1, 4, 3, 6])
        >>> len(bag)
        4
        """
        return len(self._elems)

    def __iter__(self) -> 'list_iterator':
        """Return an iterator for this ListBag.

        >>> bag = ListBag([3, 6, 3])
        >>> for x in bag:
        ...     print(x)
        ...
        3
        6
        3
        """
        return iter(self._elems)

    def __contains__(self, item: any) -> bool:
        """Return True if item is in this ListBag; otherwise False.

        >>> bag = ListBag()
        >>> 2 in bag
        False
        >>> bag = ListBag([1, 4, 3, 6])
        >>> 4 in bag
        True
        >>> 7 in bag
        False
        """
        return item in self._elems

    def add(self, item: any) -> None:
        """Add item to this ListBag.

        >>> bag = ListBag([1, 4, 3, 6])
        >>> bag.add(3)
        >>> len(bag)
        5
        >>> str(bag)
        '{1, 4, 3, 6, 3}'
        """
        self._elems.append(item)
