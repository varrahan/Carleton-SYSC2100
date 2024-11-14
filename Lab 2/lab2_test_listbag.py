# SYSC 2100 Winter 2023 Lab 2: Unit tests for class ListBag.

import unittest

from lab2_listbag import ListBag

# The first seven classes test the methods in the ListBag class
# presented in lectures.


class InitTestCase(unittest.TestCase):
    """Test __init__."""

    # The tests in this class access the "private" list in the ListBag object
    # directly, because __init__ is the first method we implement, so the other
    # methods won't be available.

    def test_init1(self):
        """Test __init__: no iterable passed to to ListBag()."""
        bag = ListBag()
        self.assertEqual(bag._elems, [])

    def test_init2(self):
        """Test __init__: empty iterable passed to ListBag()."""
        bag = ListBag([])
        self.assertEqual(bag._elems, [])

    def test_init3(self):
        """Test __init__: non-empty iterable with no duplicate elements passed to ListBag()."""
        bag = ListBag([1, 4, 3, 6])

        # Create a sorted list from the ListBag's list. This means that the
        # test doesn't depend on the bag's elements being stored in any
        # particular order.

        self.assertEqual(sorted(bag._elems), [1, 3, 4, 6])

    def test_init4(self):
        """Test __init__: non-empty iterable with duplicate elements passed to ListBag()."""
        bag = ListBag([1, 4, 4, 1, 9, 4, 6, 6])
        self.assertEqual(sorted(bag._elems), [1, 1, 4, 4, 4, 6, 6, 9])


class AddTestCase(unittest.TestCase):
    """Test add."""

    # These tests assume that __init__ can create an empty ListBag.
    # The tests access the "private" list in the ListBag object directly.
    # This means that no other ListBag methods need to be implemented in
    # order to test add.

    def test_add1(self):
        """Add items (no duplicates) to an empty bag."""
        bag = ListBag()
        for x in [1, 4, 3, 6]:
            bag.add(x)
        self.assertEqual(sorted(bag._elems), [1, 3, 4, 6])

    def test_add2(self):
        """Add items (some duplicated) to an empty bag."""
        bag = ListBag()
        for x in [1, 4, 4, 1, 9, 4, 6, 6]:
            bag.add(x)
        self.assertEqual(sorted(bag._elems), [1, 1, 4, 4, 4, 6, 6, 9])


class IterTestCase(unittest.TestCase):
    """Test __iter__."""

    def test_iter1(self):
        """Test iteration over an empty bag."""
        bag = ListBag()
        elems = []
        for elem in bag:
            elems.append(elem)
        self.assertEqual(elems, [])

    def test_iter2(self):
        """Test iteration over a bag containing some duplicate elements."""
        bag = ListBag([1, 4, 4, 1, 9, 4, 6, 6])
        elems = []
        for elem in bag:
            elems.append(elem)
        self.assertEqual(sorted(elems), [1, 1, 4, 4, 4, 6, 6, 9])


class StrTestCase(unittest.TestCase):
    """Test __str__.

    Verify that __str__ returns a string representation of the ListBag
    in the expected format.
    """

    def test_str1(self):
        """Test __str__ with an empty bag."""
        bag = ListBag()
        self.assertEqual(str(bag), '{}')

    def test_str2(self):
        """Test __str__ with a bag containing one element."""
        bag = ListBag([10])
        self.assertEqual(str(bag), '{10}')

    def test_str3(self):
        """Test __str__ with a bag containing multiple elements, all identical."""
        bag = ListBag([2, 2, 2, 2, 2])
        self.assertEqual(str(bag), '{2, 2, 2, 2, 2}')

    # We don't test the case in which the bag contains elements that aren't
    # duplicates, because elements in a bag are unordered, so we don't know
    # the order in which the elements will be listed in the string returned
    # by __str__.


class ReprTestCase(unittest.TestCase):
    """Test __repr__.

    Verify that __repr__ returns a string representation of the ListBag
    in the expected format.
    """

    def test_repr1(self):
        """Test __repr__ with an empty bag."""
        bag = ListBag()
        self.assertEqual(repr(bag), 'ListBag([])')

    def test_repr2(self):
        """Test __repr__ with a bag containing one element."""
        bag = ListBag([10])
        self.assertEqual(repr(bag), 'ListBag([10])')

    def test_repr3(self):
        """Test __repr__ with a bag containing multiple elements, all identical."""
        bag = ListBag([2, 2, 2, 2, 2])
        self.assertEqual(repr(bag), 'ListBag([2, 2, 2, 2, 2])')

    # We don't test the case in which the bag contains elements that aren't
    # duplicates, because elements in a bag are unordered, so we don't know
    # the order in which the elements will be listed in the string returned
    # by __repr__.


class LenTestCase(unittest.TestCase):
    """Test __len__."""

    def test_len1(self):
        """Test __len__ with an empty bag."""
        bag = ListBag()
        self.assertEqual(len(bag), 0)

    def test_len2(self):
        """Test __len__ with a bag containing 1 element."""
        bag = ListBag([10])
        self.assertEqual(len(bag), 1)

    def test_len3(self):
        """Test __len__ with a bag containing no duplicate elements."""
        bag = ListBag([1, 4, 3, 6])
        self.assertEqual(len(bag), 4)

    def test_len4(self):
        """Test __len__ with a bag containing some duplicate elements."""
        bag = ListBag([1, 4, 4, 1, 9, 4, 6, 6])
        self.assertEqual(len(bag), 8)

    def test_len5(self):
        """Test __len__ with a bag containing multiple elements, all identical."""
        bag = ListBag([2, 2, 2, 2, 2])
        self.assertEqual(len(bag), 5)


class ContainsTestCase(unittest.TestCase):
    """Test __contains__."""

    def test_contains1(self):
        """Test __contains__ with an empty bag."""
        bag = ListBag()
        self.assertFalse(2 in bag)

    def test_contains2(self):
        """Test __contains__ with a bag containing 1 element."""
        bag = ListBag([10])
        self.assertTrue(10 in bag)
        self.assertFalse(2 in bag)

    def test_contains3(self):
        """Test __contains__ with a bag containing no duplicate elements."""
        bag = ListBag([1, 4, 3, 6])
        self.assertTrue(1 in bag)
        self.assertTrue(4 in bag)
        self.assertTrue(3 in bag)
        self.assertTrue(6 in bag)
        self.assertFalse(2 in bag)

    def test_contains4(self):
        """Test __contains__ with a bag containing some duplicate elements."""
        bag = ListBag([1, 4, 4, 1, 9, 4, 6, 6])
        self.assertTrue(1 in bag)
        self.assertTrue(4 in bag)
        self.assertTrue(6 in bag)
        self.assertTrue(9 in bag)
        self.assertFalse(2 in bag)

    def test_contains5(self):
        """Test __contains__ with a bag containing multiple elements, all identical."""
        bag = ListBag([2, 2, 2, 2, 2])
        self.assertTrue(2 in bag)
        self.assertFalse(7 in bag)

# The following classes test the ListBag methods developed during Lab 2.


class CountTestCase(unittest.TestCase):
    """Test count (Exercise 1)."""
    

class RemoveTestCase(unittest.TestCase):
    """Test remove (Exercise 2)."""

    def test_remove1(self):
        """Test removing from an empty bag."""
        bag = ListBag()
        with self.assertRaises(ValueError):
            bag.remove(10)

    def test_remove2(self):
        """Test removing an item that isn't in the bag."""
        bag = ListBag([1, 3, 4, 4, 7, 2, 3])
        with self.assertRaises(3):
            bag.remove(3)


class GrabTestCase(unittest.TestCase):
    """Test grab (Exercise 3)."""

    def test_grab1(self):
        """Test granning an item from a bag."""
        bag = ListBag([1, 3, 4, 4, 7, 2, 3])
        with self.assertRaises(not ValueError):
            bag.grab()


class DunderAddTestCase(unittest.TestCase):
    """Test __add__ (Exercise 4)."""


class EqTestCase(unittest.TestCase):
    """Test __eq__ (Exercise 5)."""


if __name__ == '__main__':
    unittest.main(verbosity=2)
