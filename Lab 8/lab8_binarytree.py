# Class BinaryTree is an implementation of a basic binary tree.

# The __iter__ methods are from class BinarySearchTree in Lee and Hubbard's
# "Data Structures and Algorithms with Python", Section 6.5.1.

__author__ = 'Varrahan Uthayan'
__student_number__ = '101229572'


class BinaryTree:

    class _Node:
        def __init__(self, x: any, left: '_Node' = None, right: '_Node' = None) -> None:
            """Initialize this node with payload x, and links to the node's
            left and right children.
            """
            self.x = x
            self.left = left
            self.right = right

        def __iter__(self):
            """Return an iterator that performs an inorder traversal of the
            nodes in the tree rooted at this node.
            """
            if self.left is not None:
                for elem in self.left:
                    yield elem

            yield self.x

            if self.right is not None:
                for elem in self.right:
                    yield elem

    def __init__(self) -> None:
        """Initialize self as an empty BinaryTree."""
        self._root = None

    def __str__(self) -> str:
        """Return a string representation of this BinaryTree (inorder traversal
        of the nodes).
        """
        # Use repr(x) instead of str(x) in the list comprehension so that
        # elements of type str are enclosed in quotes.
        return "[{0}]".format(", ".join([repr(x) for x in self]))

    __repr__ = __str__

    def __len__(self) -> int:
        """Return the number of nodes in this BinaryTree."""
        return self.size()

    def __iter__(self):
        """Return an iterator that performs an inorder traversal of the nodes
        in this BinaryTree.
        """
        if self._root is not None:
            return self._root.__iter__()
        else:
            # The tree is empty, so use an empty list's iterator
            # as the tree's iterator.
            return iter([])

    def traverse(self) -> None:
        """Visit all the nodes in this BinaryTree."""
        self._traverse(self._root)

    def _traverse(self, node: 'BinaryTree._Node') -> None:
        """Visit all the nodes in the binary tree rooted at node.

        Note that this method does no useful work as it visits each node,
        but it does show the pattern for operations that traverse the
        entire tree; e.g., calculate the tree's size, calculate the tree's
        height, pre-order/in-order/post-order printing, etc.
        """
        if node is None:
            print('The tree is empty')
            return

        print('Visiting a node containing', node.x)
        print('Now visit the left subtree of the node containing', node.x)
        self._traverse(node.left)
        print('Now visit the right subtree of the node containing', node.x)
        self._traverse(node.right)

# This implementation of wrapper method size calls recursive method _size.
#
#     def size(self) -> int:
#         """Return the number of nodes in this BinaryTree."""
#         return self._size(self._root)
#
#     def _size(self, node: 'BinaryTree._Node') -> int:
#         """Return the number of nodes in the tree rooted at node."""
#         if node is None:
#             return 0
#         return 1 + self._size(node.left) + self._size(node.right)

# This implementation of wrapper method height calls recursive method _height.
#
#     def height(self) -> int:
#         """Return the height of this BinaryTree."""
#         return self._height(self._root)
#
#     def _height(self, node: 'BinaryTree._Node') -> int:
#         """Return the length of the longest path from the tree rooted at node
#         to one of its descendants.
#         """
#         if node is None:
#             return -1
#         return 1 + max(self._height(node.left), self._height(node.right))

    # This implementation of wrapper method size calls recursive nested
    # function _size.

    def size(self) -> int:
        """Return the number of nodes in this BinaryTree."""

        def _size(node: 'BinaryTree._Node') -> int:
            """Return the number of nodes in the tree rooted at node."""
            if node is None:
                return 0
            return 1 + _size(node.left) + _size(node.right)

        return _size(self._root)

    # This implementation of wrapper method height calls recursive nested
    # function _height.

    def height(self) -> int:
        """Return the height of this BinaryTree."""

        def _height(node: 'BinaryTree._Node') -> int:
            """Return the length of the longest path from the tree rooted at
            node to one of its descendants.
            """
            if node is None:
                return -1
            return 1 + max(_height(node.left), _height(node.right))

        return _height(self._root)

    # Exercise 4

    def preorder_print(self) -> None:
        """Print this BinaryTree using a preorder traversal."""

        def _preorder_print(node: 'BinaryTree._Node') -> None:
            """Print the binary tree rooted at node using a preorder traversal."""
            if node is None:
                return
            print(node.x)
            _preorder_print(node.left)
            _preorder_print(node.right) 
        
        _preorder_print(self._root)

    # Exercise 5

    def inorder_print(self) -> None:
        """Print this binary tree using an inorder traversal."""
        
        def _inorder_print(node: 'BinaryTree._Node') -> None:
            """Print the binary tree rooted at node using an inorder traversal."""
            if node is None:
                return            
            _inorder_print(node.left)
            print(node.x)
            _inorder_print(node.right) 
        
        _inorder_print(self._root)
            
    # Exercise 6

    def postorder_print(self) -> None:
        """Print this binary tree using a postorder traversal."""
        
        def _postorder_print(node: 'BinaryTree._Node') -> None:
            """Print the binary tree rooted at node using an postorder traversal."""
            if node is None:
                return            
            _postorder_print(node.left)
            _postorder_print(node.right) 
            print(node.x)
        
        _postorder_print(self._root)        

   # Exercise 7

    def count(self, item: any) -> int:
        """Return the number of occurrences of item in this binary tree."""
        
        def _count(item: any, node: 'BinaryTree._Node') -> int:
            """Return the number of occurrences of item in this binary tree."""
            if node is None:
                return 0
            if node.x == item:
                return 1 + _count(item, node.left) + _count(item, node.right)
            else:
                return 0 + _count(item, node.left) + _count(item, node.right)
            
        return _count(item, self._root) 

# Exercise 1

def build_10_20_30() -> BinaryTree:
    """Return a reference to a simple binary tree in which the root node
    contains 10, the left child contains 20, and the right child contains 30.
    """
    binary_tree = BinaryTree()

    root_node = BinaryTree._Node(10)
    binary_tree._root = root_node

    root_node.left = BinaryTree._Node(20)     # Insert left child of root.
    root_node.right = BinaryTree._Node(30)    # Insert right child of root.

    return binary_tree


# Exercise 2


def build_binary_tree() -> BinaryTree:
    """Build the binary tree shown in Exercise 2 in the lab handout,
    and return the reference to the tree.
    """
    
    binary_tree = BinaryTree()
    root_node = BinaryTree._Node(5)
    binary_tree._root = root_node
    
    node_seven = BinaryTree._Node(7) 
    node_twelve = BinaryTree._Node(12)
    root_node.left = node_seven
    root_node.right = node_twelve
    
    node_seven.left = BinaryTree._Node(17) 
    node_seven.right = BinaryTree._Node(9) 
    
    node_six = BinaryTree._Node(6) 
    node_twelve.right = node_six
    
    node_six.left = BinaryTree._Node(1) 
    
    return binary_tree

# Exercise 3


def build_perfect_binary_tree() -> BinaryTree:
    """Build the perfect binary tree shown in Exercise 3 in the lab handout,
    and return the reference to the tree.
    """
    
    binary_tree = BinaryTree()
    root_node = BinaryTree._Node(5)
    binary_tree._root = root_node
    
    node_seven = BinaryTree._Node(7) 
    node_twelve = BinaryTree._Node(12)
    root_node.left = node_seven 
    root_node.right = node_twelve
    
    node_seven.left = BinaryTree._Node(17) 
    node_seven.right = BinaryTree._Node(9) 
    
    node_twelve.left = BinaryTree._Node(3) 
    node_twelve.right = BinaryTree._Node(6) 
    
    return binary_tree