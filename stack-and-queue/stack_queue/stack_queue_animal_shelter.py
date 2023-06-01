from stack import Stack
from queue import Queue


class Node:
    def __init__(self, value=None, next=None):
        """
        Initialize a Node object.

        Args:
            value (any, optional): The value to be stored in the node. Defaults to None.
            next (Node, optional): The reference to the next node. Defaults to None.
        """
        self.value = value
        self.next = next


class AnimalShelter:
    def __init__(self, front=None, back=None):
        """
        Initialize an AnimalShelter object.

        Args:
            front (Node, optional): The front node of the shelter queue. Defaults to None.
            back (Node, optional): The back node of the shelter queue. Defaults to None.
        """
        self.front = front
        self.back = back
        self.stack1 = Stack()
        self.stack2 = Stack()
        self.dog = []
        self.cat = []

    def enqueue(self, animal , name):
        """
        Enqueue an animal to the shelter queue.

        Args:
            species (str): The species of the animal (either 'dog' or 'cat').
            name (str): The name of the animal.

        Raises:
            Exception: If the species is neither 'dog' nor 'cat'.
        """
        node = Node(name)
        if animal  == "dog":
            self.dog.append(name)
        elif animal  == "cat":
            self.cat.append(name)
        else:
            raise Exception("Kindly include either a dog or a cat, please")

        if self.back is None:
            self.front = node
            self.back = node
            self.stack1.push(self.front.value)
        else:
            self.back.next = node
            self.back = node
            self.stack1.push(self.back.value)

    def dequeue(self, pref="cat_or_dog"):
        """
        Dequeue an animal from the shelter queue.

        Args:
            pref (str, optional): The preferred species to dequeue ('dog', 'cat', or 'cat_or_dog').
                Defaults to 'cat_or_dog'.

        Returns:
            str: The name of the dequeued animal.

        Raises:
            Exception: If the queue is empty.
            Exception: If there are no dogs to delete.
            Exception: If there are no cats to delete.
            Exception: If neither a cat nor a dog is available to delete.
            Exception: If an invalid preference is provided.
        """
        if self.back is None:
            raise Exception("The queue is empty")
        else:
            if pref == "dog":
                try:
                    removeDog = self.dog[0]
                    del self.dog[0]
                    while not self.stack1.top.value == removeDog:
                        self.stack2.push(self.stack1.pop())
                    self.stack1.pop()
                    while not self.stack2.is_empty():
                        self.stack1.push(self.stack2.pop())
                    return removeDog
                except IndexError:
                    raise Exception("There are no dogs to delete")

            elif pref == "cat":
                try:
                    removeCat = self.cat[0]
                    del self.cat[0]
                    while not self.stack1.top.value == removeCat:
                        self.stack2.push(self.stack1.pop())
                    self.stack1.pop()
                    while not self.stack2.is_empty():
                        self.stack1.push(self.stack2.pop())
                    return removeCat
                except IndexError:
                    raise Exception("There are no cats to delete")

            elif pref == "cat_or_dog":
                try:
                    if self.stack2.is_empty():
                        while not self.stack1.is_empty():
                            self.stack2.push(self.stack1.pop())
                    deleted = self.stack2.pop()
                    if deleted == self.cat[0]:
                        del self.cat[0]
                    else:
                        del self.dog[0]
                    while not self.stack2.is_empty():
                        self.stack1.push(self.stack2.pop())
                    return self.stack1

                except IndexError:
                    raise Exception("There are no cats or dogs to delete")

            else:
                raise Exception("Kindly delete either a dog or a cat, please")

    def __str__(self):
        """
        String representation of the AnimalShelter object.

        Returns:
            str: The string representation of the AnimalShelter object.
        """
        elements = []
        while not self.stack1.is_empty():
            elements.append(self.stack1.pop())
        for element in reversed(elements):
            self.stack1.push(element)
        string = " -> ".join(str(element) for element in elements)
        return string


if __name__ == "__main__":
    q = AnimalShelter()
    q.enqueue('cat', "toto")
    q.enqueue('dog', "meme")
    q.enqueue('dog', "boty")
    q.enqueue('cat', "miso")
    q.enqueue('cat', "lolo")
    q.enqueue('cat', "soso")
    q.enqueue('dog', "dedo")
    q.enqueue('cat', "mrao")
    print(q)
    q.dequeue()  # toto
    print(q)
    q.dequeue("dog")  # meme
    print(q)
    q.dequeue("cat")  # miso
    print(q)
