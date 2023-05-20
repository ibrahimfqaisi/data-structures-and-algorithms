"""
This class represents a node in a linked list.

Attributes:
    value (any): The value stored in the node.
    next (Node): The next node in the linked list.
"""

class Node:
    def __init__(self, value=None, next=None):
        """
        Initializes a new Node object.

        Args:
            value (any): The value stored in the node.
            next (Node): The next node in the linked list.
        """
        self.value = value
        self.next = next

"""
This class represents a stack data structure implemented using a linked list.

Attributes:
    top (Node): The top node of the stack.
"""

class Stack:
    def __init__(self, top=None):
        """
        Initializes a new Stack object.

        Args:
            top (Node): The top node of the stack.
        """
        self.top = top

    """
    Pushes a value onto the stack.

    Args:
        value (any): The value to push onto the stack.
    """

    def push(self, value):
        """
        Pushes a value onto the stack.

        Args:
            value (any): The value to push onto the stack.
        """
        node = Node(value)
        node.next = self.top
        self.top = node

    """
    Pops a value from the stack.

    Returns:
        The value that was popped from the stack.

    Raises:
        Exception: If the stack is empty.
    """

    def pop(self):
        """
        Pops a value from the stack.

        Returns:
            The value that was popped from the stack.

        Raises:
            Exception: If the stack is empty.
        """
        if self.top is None:
            raise Exception("the stack is empty")

        temp = self.top
        self.top = temp.next
        temp.next = None
        return temp.value

    """
    Peeks at the top value of the stack.

    Returns:
        The value at the top of the stack.

    Raises:
        Exception: If the stack is empty.
    """

    def peek(self):
        """
        Peeks at the top value of the stack.

        Returns:
            The value at the top of the stack.

        Raises:
            Exception: If the stack is empty.
        """
        if self.top is None:
            raise Exception("the stack is empty")

        return self.top.value

    """
    Checks if the stack is empty.

    Returns:
        True if the stack is empty, False otherwise.
    """

    def is_empty(self):
        """
         Checks if the stack is empty.

         Returns:
             True if the stack is empty, False otherwise.
         """
        return self.top is None

    """
    Returns a string representation of the stack.

    Returns:
        A string representation of the stack.
    """

    def __str__(self):
        current = self.top
        string = ""
        while current:
            string += f"{current.value}"
            string += " -> "
            current = current.next
        return string + "None"


if __name__ == "__main__":
    stack_01 = Stack()
    stack_01.push(1)
    stack_01.push(2)
    stack_01.push(3)
    stack_01.push(4)
    # print(stack_01.peek())
    print(stack_01.is_empty())
    print(stack_01)
    # print(stack_01.top.value)
