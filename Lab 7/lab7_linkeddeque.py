# SYSC 2100 Winter 2023 Lab 7

# Class LinkedDeque is an implementation of ADT Deque that uses a doubly-linked
# list as the underlying data structure.

__author__ = 'Varrrahan Uthayan'
__student_number__ = '101229572'


class LinkedDeque:
    class _Node:
        def __init__(self, item: any) -> None:
            """Initialize this node with the specified data item.

            The node is not linked to any other nodes.
            """
            self.item = item
            self.prev = None
            self.next = None

    def __init__(self, iterable=[]) -> None:
        """Initialize this LinkedDeque.

        If no iterable is provided, the LinkedDeque is empty. Otherwise,
        initialize the LinkedDeque by appending the values provided by the
        iterable to the right side of the deque.

        >>> dq = LinkedDeque()
        >>> dq
        LinkedDeque([])

        >>> dq = LinkedDeque([1, 4, 3, 6])
        >>> dq
        LinkedDeque([1, 4, 3, 6])
        """
        # A LinkedDeque always has one "dummy" node that never contains any of
        # the items that are stored in the deque. The dummy node's next
        # attribute points to the node at the head of the linked list,
        # and the prev attribute points to the node at the tail of the
        # linked list.

        # _dummy always points to the dummy node.
        self._dummy = LinkedDeque._Node(None)
        self._dummy.prev = self._dummy
        self._dummy.next = self._dummy

        self._num_items = 0  # of items stored in the LinkedDeque

        for elem in iterable:
            self.append(elem)
            # append() updates self._num_items.

    def __str__(self) -> str:
        """Return a string representation of this LinkedDeque.

        >>> dq = LinkedDeque()
        >>> str(dq)
        '[]'
        >>> dq = LinkedDeque([1, 4, 3, 6])
        >>> str(dq)
        '[1, 4, 3, 6]'
        """
        # Use repr(x) instead of str(x) in the list comprehension so that
        # elements of type str are enclosed in quotes.
        return "[{0}]".format(", ".join([repr(x) for x in self]))

    def __repr__(self) -> str:
        """Return the canonical string representation of this LinkedDeque.

        >>> dq = LinkedDeque()
        >>> repr(dq)
        'LinkedDeque([])'
        >>> dq = LinkedDeque([1, 4, 3, 6])
        >>> repr(dq)
        'LinkedDeque([1, 4, 3, 6])'
        """
        # For a LinkedDeque object, obj, the expression eval(repr(obj))
        # returns a new LinkedDeque that is identical to obj.
        return "{0}({1})".format(self.__class__.__name__, str(self))

    def __len__(self) -> int:
        """Return the number of elements in this LinkedDeque.

        >>> dq = LinkedDeque()
        >>> len(dq)
        0
        >>> dq = LinkedDeque([1, 4, 3, 6])
        >>> len(dq)
        4"""
        return self._num_items

    def __iter__(self):
        """Return an iterator for this LinkedDeque.

        >>> dq = LinkedDeque([1, 4, 3, 6])
        >>> for x in dq:
        ...     print(x)
        ...
        1
        4
        3
        6
        """
        cursor = self._dummy.next  # Skip over the dummy node.
        while cursor is not self._dummy:
            yield(cursor.item)
            cursor = cursor.next

    # Exercise 2

    def _insert_before(self, node: 'LinkedDeque._Node', x: any) -> None:
        """Insert a new node containing x before the specified node.

        The complexity is O(1).
        """
        new_node = LinkedDeque._Node(x)
        new_node.prev = node.prev
        new_node.next = node
        node.prev.next = new_node
        node.prev = new_node
        self._num_items += 1
        
        

    # Exercise 5

    def _remove(self, node: 'LinkedDeque._Node') -> None:
        """Remove the specified node from the LinkedDeque's linked list.

        The complexity is O(1).
        """
        node.next.prev = node.prev
        node.prev.next = node.next
        node.next = None
        node.prev = None
        self._num_items -= 1

    # Exercise 3

    def append(self, x: any) -> None:
        """Add x to the right side of this LinkedDeque.

        The complexity is O(1).

        >>> dq = LinkedDeque([1, 4, 3, 6])
        >>> dq.append(2)
        >>> dq
        LinkedDeque([1, 4, 3, 6, 2])
        >>> len(dq)
        5
        """
        self._insert_before(self._dummy, x)
                

    # Exercise 4

    def appendleft(self, x: any) -> None:
        """Add x at the left of this LinkedDeque.

        The complexity is O(1).

        >>> dq = LinkedDeque([1, 4, 3, 6])
        >>> dq.appendleft(2)
        >>> dq
        LinkedDeque([2, 1, 4, 3, 6])
        >>> len(dq)
        5
        """
        self._insert_before(self._dummy.next, x)

    # Exercise 6

    def pop(self) -> any:
        """Remove and return the element from the right side of this LinkedDeque.

        The complexity is O(1).

        Raises IndexError if the LinkedDeque is empty.

        >>> dq = LinkedDeque([1, 4, 3, 6])
        >>> dq.pop()
        6
        >>> dq
        LinkedDeque([1, 4, 3])
        >>> len(dq)
        3
        """
        if self._num_items == 0:
            raise IndexError("LinkedDeque: pop from an empty deque")
        x = self._dummy.prev.item
        self._remove(self._dummy.prev)
        return x       

    # Exercise 7

    def popleft(self) -> any:
        """Remove and return the element from the left side of this LinkedDeque.

        The complexity is O(1).

        Raises IndexError if the LinkedDeque is empty.

        >>> dq = LinkedDeque([1, 4, 3, 6])
        >>> dq.popleft()
        1
        >>> dq
        LinkedDeque([4, 3, 6])
        >>> len(dq)
        3
        """
        if self._num_items == 0:
            raise IndexError("LinkedDeque: pop from an empty deque")
        x = self._dummy.next.item
        self._remove(self._dummy.next)
        return x
