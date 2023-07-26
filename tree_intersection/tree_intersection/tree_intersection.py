from functools import reduce
from operator import add

class Node:
  '''
  A class represent a node in a linked list or other data structure each node has two main componenet the value of the node and the reference to the next node.
  args: value
  return : nothing
  '''
  def __init__(self, value):
      self.next=None 
      self.value=value



class LinkedList:
    '''
    what : A class representing a singly linked list data structure
    '''
    def __init__(self):
        self.head = None


    def insert (self, value):
        '''
        insert a new node with the given value at the begining of     the linked list.
        args: value
        output : none

        '''
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node


class HashTable:
  '''
  what : data structure that store key-value pairs of data using buckets to increace data accessing efficiency 
  
  '''
  def __init__(self,size=1024):
    self.__size=size
    self.__buckets=[None] *size
    self.keys = []
    
  
  def __hash(self,key):
    '''
    A method to return the hash code of the given key
    arg : key
    output: hash code of the key(index)
    '''
    # code = 0
   
    # for char in key:
    #   code += ord(str(char)) # * weight
    # code *= 255
    # code = code % 1024
    # return code
    k= ( reduce(add, [ord(str(char)) for char in str(key)]) * 283 % self.__size)
    return  k
    # return sum([ord(str(char)) for char in key]) * 283 % self.__size

  
    
  def set(self,key,value):
    '''
    Set a key-value pair in the bucket, handling collisions as              needed.
    Arguments:
    key : The key to be hashed and used as the identifier for the           value.
    value : the value that is aassociated with the key
    Returns: None
    '''
    index = self.__hash(key)
    if self.__buckets[index] is None:
      ll = LinkedList()
      self.__buckets[index] = ll
     
    self.__buckets[index].insert([key,value])
    self.keys.append(key)
    
  def get(self,key):
    '''
    Retrieve the value with the given key from the hashtable
    arg : key
    return : value or None 
    '''
    index=self.__hash(key)
    bucket = self.__buckets[index]
    if bucket is not None : 
      curr = bucket.head
      while curr :
        if curr.value[0] == key :
          return curr.value[1]
        curr = curr.next  
    return None  

  def has(self, key):
    '''
    A method to check if the given key exist in the hashtable.
    arg: key
    output: boolean
    '''

    if self.get(key):
      return True
    return False  

    

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



def tree_intersection(tree1,tree2):
    '''
    A function that finds the intersection between two binary trees.
    Arguments: two binary trees.
    Return: set of values found in both trees.
    '''
    check= HashTable()
    array = []
    def _walk(root,num=0):

        # root
        if num ==0:
            check.set(root.value,root.value)
        else:
          if  check.has(root.value) :
             array.append(root.value)
             

        # left
        if root.left:
            _walk(root.left,num)
        # right
        if root.right:
            _walk(root.right, num)

    _walk(tree1.root, 0)
    
    _walk(tree2.root, 1)
    return array

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


if __name__ == "__main__":
    tree2 = binary_search_tree()
    tree2.Add(10)
    tree2.Add(3)
    tree2.Add(255)
    tree2.Add(260)
    tree2.Add(25)


    tree1 = binary_search_tree()
    tree1.Add(999)
    tree1.Add(888)
    tree1.Add(777)
    tree1.Add(666)
    tree1.Add(25)





    print(tree_intersection(tree1,tree2))