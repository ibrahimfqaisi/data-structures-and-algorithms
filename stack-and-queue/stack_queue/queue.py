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
    Returns a string representation of the node.

    Returns:
        A string representation of the node.
    """

    def __str__(self):
        return f"Node({self.value})"


"""
This class represents a queue data structure implemented using a linked list.

Attributes:
    front (Node): The front node of the queue.
    back (Node): The back node of the queue.
"""

class Queue:
    def __init__(self, front=None, back=None):
        """
        Initializes a new Queue object.

        Args:
            front (Node): The front node of the queue.
            back (Node): The back node of the queue.
        """
        self.front = front
        self.back = back

    """
    Add a value to the end of the queue.

    Args:
        value (any): The value to add to the queue.
    """

    def enqueue(self, value):
        """
        Add a value to the end of the queue.

        Args:
            value (any): The value to add to the queue.
        """
        node = Node(value)
        if self.back is None:
            self.front = node
            self.back = node
        else:
            self.back.next = node
            self.back = node

    """
    Removes the value from the front of the queue.

    Raises:
        Exception: If the queue is empty.

    Returns:
        The value that was removed from the queue.
    """

    def dequeue(self):
        if self.back is None:
            raise Exception("the queue is empty")
        else:
            temp = self.front
            self.front = temp.next
            temp.next = None
            return temp.value

    """
    Peeks at the value at the front of the queue.

    Raises:
        Exception: If the queue is empty.

    Returns:
        The value at the front of the queue.
    """

    def peek(self):
        if self.back is None:
            raise Exception("the queue is empty")
        else:
            return self.front.value

    """
    Checks if the queue is empty.

    Returns:
        True if the queue is empty, False otherwise.
    """

    def is_empty(self):
        return self.front is None

    """
    Returns a string representation of the queue.

    Returns:
        A string representation of the queue.
    """

    def __str__(self):
        current = self.front
        string = ""
        while current:
            string += f"{current.value}"
            string += " -> "
            current = current.next
        return string + "None"


if __name__ == "__main__":
    q = Queue()
    q.enqueue("hi")
    q.enqueue("welcome")
    q.enqueue("bye")
    print(q)
    print(q.front.value)
    print(q.back.value)
    # print("deleted element is ",q.dequeue())#deleted node value
    print(q)
