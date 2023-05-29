try:
    from stack import Stack
except:
    from stack_queue.stack import Stack

class PseudoQueue:
    """
    PseudoQueue class implements a queue using two stacks.
    """

    def __init__(self):
        self.stack1 = Stack()  
        self.stack2 = Stack()  

    def enqueue(self, value):
        """
        Enqueues the given value into the PseudoQueue.
        """
        self.stack1.push(value)

    def dequeue(self):
        """
        Dequeues and returns the front element of the PseudoQueue.
        Raises an exception if the queue is empty.
        """
        if self.stack1.is_empty():
            raise Exception("The queue is empty")
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
        self.stack2.pop()
        while not self.stack2.is_empty():
            self.stack1.push(self.stack2.pop())
        return self.stack1

    def __str__(self):
        """
        Returns a string representation of the PseudoQueue.
        """
        elements = []
        while not self.stack1.is_empty():
            elements.append(self.stack1.pop())
        for element in reversed(elements):
            self.stack1.push(element)
        string = " -> ".join(str(element) for element in elements)
        return string


if __name__ == "__main__":
    q = PseudoQueue()
    q.enqueue("hi")
    q.enqueue("welcome")
    q.enqueue("bye")
    q.dequeue()
    print(q)
