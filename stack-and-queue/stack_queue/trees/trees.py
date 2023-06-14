try:
    from queue import Queue
except:
    from stack_queue.queue import Queue


class Tnode:
    """
    Class representing a node in a binary tree.

    Attributes:
        value (int): The value stored in the node.
        left (Tnode): Reference to the left child node.
        right (Tnode): Reference to the right child node.
    """

    def __init__(self, value):
        """
        Initializes a new instance of the Tnode class.

        Args:
            value (int): The value to be stored in the node.
        """
        self.value = value
        self.right = None
        self.left = None


class binary_tree:
    """
    Class representing a binary tree.

    Attributes:
        root (Tnode): The root node of the binary tree.
        max (int): The maximum value in the binary tree.
    """

    def __init__(self):
        """
        Initializes a new instance of the binary_tree class.
        """
        self.root = None
        self.max = None

    def breadth_first(self):
        """
        Performs a breadth-first traversal of the binary tree.

        Returns:
            list: A list containing the values of the binary tree in breadth-first order.
        """
        if not self.root:
            return self.root

        output = []
        queue = Queue()
        queue.enqueue(self.root)

        while not queue.is_empty():

            front = queue.dequeue()
            output.append(front.value)

            if front.left:
                queue.enqueue(front.left)
            if front.right:
                queue.enqueue(front.right)

        return output

    def pre_order(self):
        """
        Performs a pre-order traversal of the binary tree.

        Returns:
            list: A list containing the values of the binary tree in pre-order.
        """
        array = []

        def _walk(root):
            # root
            array.append(root.value)

            # left
            if root.left:
                _walk(root.left)

            # right
            if root.right:
                _walk(root.right)

        _walk(self.root)
        return array

    def in_order(self):
        """
        Performs an in-order traversal of the binary tree.

        Returns:
            list: A list containing the values of the binary tree in in-order.
        """
        array = []

        def _walk(root):

            # left
            if root.left:
                _walk(root.left)

            # root
            array.append(root.value)

            # right
            if root.right:
                _walk(root.right)

        _walk(self.root)
        return array

    def post_order(self):
        """
        Performs a post-order traversal of the binary tree.

        Returns:
            list: A list containing the values of the binary tree in post-order.
        """
        array = []

        def _walk(root):

            # left
            if root.left:
                _walk(root.left)

            # right
            if root.right:
                _walk(root.right)

            # root
            array.append(root.value)

        _walk(self.root)
        return array

    def maximum_value(self):
        """
        Finds the maximum value in the binary tree.

        Returns:
            int: The maximum value in the binary tree.
            str: "the tree is empty" if the tree is empty.
        """
        try:
            self.max = self.root.value
        except:
            return "the tree is empty"

        def _walk(root):
            # root
            if root.value > self.max:
                self.max = root.value
            # left
            if root.left:
                _walk(root.left)

            # right
            if root.right:
                _walk(root.right)

        _walk(self.root)
        return self.max


class binary_search_tree(binary_tree):
    """
    Class representing a binary search tree, which is a specialized type of binary tree.

    Attributes:
        None
    """

    def __init__(self):
        """
        Initializes a new instance of the binary_search_tree class.
        """
        super().__init__()

    def Add(self, value):
        """
        Adds a value to the binary search tree.

        Args:
            value (int): The value to be added to the binary search tree.
        """
        def _walk(root):
            if root.value > value:
                # left
                if root.left:
                    _walk(root.left)
                else:
                    root.left = Tnode(value)
            elif root.value < value:
                # right
                if root.right:
                    _walk(root.right)
                else:
                    root.right = Tnode(value)

            # root

        try:
            _walk(self.root)
        except:
            self.root = Tnode(value)

    def Contains(self, value):
        """
        Checks if a value is present in the binary search tree.

        Args:
            value (int): The value to check for.

        Returns:
            bool: True if the value is present, False otherwise.
        """
        def _walk(root):
            if root is None:
                return False

            if root.value == value:
                return True
            elif root.value > value:
                # left
                return _walk(root.left)
            else:
                # right
                return _walk(root.right)

        return _walk(self.root)


if __name__ == "__main__":
    tree2 = binary_search_tree()
    tree2.Add(10)
    tree2.Add(3)
    tree2.Add(255)
    tree2.Add(260)
    tree2.Add(25)
    print(tree2.Contains(25))

    print(tree2.pre_order())

    print(tree2.maximum_value())
    tree = binary_tree()
    print(tree.maximum_value())
