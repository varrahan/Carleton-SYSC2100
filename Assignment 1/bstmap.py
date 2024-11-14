# An implementation of ADT Map that uses a binary search tree as the
# underlying data structure.

# Some methods were adapted from methods in class BinarySearchTree in Lee and
# Hubbard's "Data Structures and Algorithms with Python", Section 6.5.1.

__author__ = 'Varrahan Uthayan'
__student_number__ = '101229572'


class BSTMap:

    class _Node:
        def __init__(self, key: any, value: any, left: '_Node' = None, right: '_Node' = None) -> None:
            """Initialize a node containing a key, the value associated with
            the key, and links to the node's left and right children.
            """
            self.key = key
            self.value = value
            self.left = left
            self.right = right

        def __iter__(self):
            """Return an iterator that performs an inorder traversal of the
            tree rooted at this node, returning the keys.
            """
            if self.left is not None:
                for elem in self.left:
                    yield elem

            yield self.key

            if self.right is not None:
                for elem in self.right:
                    yield elem

    def __init__(self, iterable=[]) -> None:
        """Initialize this BSTMap.

        If no iterable is provided, the map is empty.
        Otherwise, initialize the map by inserting the key/value pairs
        provided by the iterable.

        Precondition: the iterable is a sequence of tuples, with each tuple
        containing one (key, value) pair.

        >>> map = BSTMap()
        >>> map
        {}

        # In this example each key/value pair is a tuple containing a
        # 6-digit student number (an int) and that student's letter grade
        # (a str).

        >>> grades = BSTMap([(111537, 'A+'), (101156, 'A+'), (127118, 'B')])
        >>> grades
        {101156: 'A+', 111537: 'A+', 127118: 'B', }
        """
        self._root = None

        # Number of entries in the map; i.e., the number of key/value pairs.
        self._num_entries = 0

        for key, value in iterable:
            self[key] = value  # updates self._num_entries

    def __str__(self) -> str:
        """Return a string representation of this BSTMap (inorder traversal of
        the nodes), using the format: "{key_1: value_1, key_2: value_2, ...}"

        >>> grades = BSTMap([(111537, 'A+'), (101156, 'A+'), (127118, 'B')])
        >>> str(grades)
        "{101156: 'A+', 111537: 'A+', 127118: 'B'}"
        """
        # Use repr(x) instead of str(x) in the list comprehension so that
        # elements of type str are enclosed in quotes.
        return "{{{0}}}".format(", ".join([repr(key) + ': ' + repr(self[key]) for key in self]))

    __repr__ = __str__

    def __iter__(self):
        """Return an iterator that performs an inorder traversal of the nodes
        in this BSTMap, returning the keys.
        """
        if self._root is not None:
            return self._root.__iter__()
        else:
            # The tree is empty, so use an empty list's iterator
            # as the tree's iterator.
            return iter([])
        
    def __setitem__(self, key: any, value: any) -> None:
        """
        Adds a key/value pair to the BSTMap
        >>> pencil_case = BSTMap()
        >>> pencil_case['pencils'] = 4
        >>> pencil_case['erasers'] = 2
        >>> pencil_case['pens'] = 3
        >>> pencil_case
        {'erasers': 2, 'pencils': 4, 'pens': 3}
        >>> pencil_case['pencils'] = 1
        >>>pencil_case
        {'erasers': 2, 'pencils': 4, 'pens': 3}
        """
        def _setitem(node:'_Node', key:any, value:any) -> '_Node':
            """
            Puts a key/value pair into the binary search tree rooted at node and
            return the reference to tree's root node.
            """
            if node is None:
                return BSTMap._Node(key, value)
            elif key < node.key:
                node.left = _setitem(node.left, key, value)
            elif key > node.key:
                node.right = _setitem(node.right, key, value)
            elif key == node.key:
                node.value = value
            return node  
        
        if key not in self:
            self._num_entries += 1
        self._root = _setitem(self._root, key, value)    
        
    def __len__(self) -> int:
        """
        Returns the number of key/value pairs in BSTMap
        >>> grades = BSTMap([(111537, 'A+'), (101156, 'A+'), (127118, 'B')])
        >>> len(grades)
        3
        """
        return self._num_entries
    
    def __contains__(self, key: any) -> bool:
        """Returns true if the BSTMap contains a key and returns false if key is not found
        
        >>> pencil_case = BSTMap([('pencils', 4), ('erasers', 2), ('pens', 3)])
        >>> 'pencils' in pencil_case
        True
        >>> 'rulers' in pencil_case
        False
        """
        def _contains(node: '_Node', key: any) -> bool:
            """
            Returns true if the key is in the binary search tree rooted at node;
            otherwise return false
            """
            if node is None:
                return False
            if key < node.key:
                return _contains(node.left, key)
            if key > node.key:
                return _contains(node.right, key)
            if node.key == key:
                return True 
            
        return _contains(self._root, key)
    
    def __getitem__(self, key: any) -> any:
        """
        Value can be retrieved using the specified key. If key not in BSTMap,
        raise KeyError
        >>> pencil_case['pencils']
        4
        >>> pencil_case['rulers']
        KeyError: 'rulers'

        """
        def _getitem(node: '_Node', key: any) -> any:
            if node is None:
                raise KeyError(key)
            if key < node.key:
                return _getitem(node.left, key)
            if key > node.key:
                return _getitem(node.right, key)
            if node.key == key:
                return node.value
            
        return _getitem(self._root, key)
    
    def get(self, key: any, value = None) -> any:
        """
        Gets the value associated with the key. If the key does not exist and
        there is no inputted value, returns none, and if there is no key and 
        a value is inputted, returns inputted value
        
        >>> pencils = pencil_case.get('pencils')
        >>> print(pencils)
        4
        >>> pencils = pencil_case.get('rulers', 0)
        >>> print(pencils)
        0 
        >>> pencils = pencil_case.get('rulers')
        >>> print(pencils)
        None
        """
        def _get(node, key: any, value:any) -> any:
            """
            Gets the value associated with the key in the binary search tree. 
            If the key does not exist and there is no inputted value, a None value is 
            returned, and if there is no key and a value is inputted, the inputted
            value is returned
            """
            if node is None:
                if value is None:
                    return None
                return value
            if key < node.key:
                return _get(node.left, key, value)
            if key > node.key:
                return _get(node.right, key, value)
            if node.key == key:
                return node.value
        return _get(self._root, key, value)            