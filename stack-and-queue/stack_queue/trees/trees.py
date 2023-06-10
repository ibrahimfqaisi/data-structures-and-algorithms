try :
    from queue import Queue
except:
    from stack_queue.queue import Queue
    
class Tnode:
  def __init__(self,value):
    self.value=value
    self.right= None
    self.left = None



class binary_tree:
  def __init__(self):
    self.root=None

  def breadth_first(self):
    if not self.root:
      return self.root
      
    output = []
    queue = Queue()
    queue.enqueue(self.root)

    while not queue.is_empty():
      
      front = queue.dequeue()
      output.append(front.value)
      
      if front.left :
          queue.enqueue(front.left)
      if front.right :
          queue.enqueue(front.right)  
        
    return output

  def pre_order(self):
    array=[]
    def _walk(root):
      #root
      array.append(root.value)

      #left
      if root.left :
        _walk(root.left)
        
      #right
      if root.right :
        _walk(root.right)

    _walk(self.root)
    return array

  def in_order(self):
    array=[]
    def _walk(root):
      
      #left
      if root.left :
        _walk(root.left)
        
      #root
      array.append(root.value)

      #right
      if root.right :
        _walk(root.right)

    _walk(self.root)
    return array
  def post_order(self):
    array=[]
    def _walk(root):
      
      #left
      if root.left :
        _walk(root.left)
        

      #right
      if root.right :
        _walk(root.right)

      #root
      array.append(root.value)
    _walk(self.root)    
    return array
   
class binary_search_tree(binary_tree) :
  def __init__(self) :
    pass 
  def Add(self,value) :
    def _walk(root):
      if root.value>value:
      #left
        if root.left :
          _walk(root.left)
        else:
          root.left=Tnode(value)
      #right
      elif root.value<value:
        if root.right :
          _walk(root.right)
        else:
          root.right=Tnode(value)

      #root
    try:
       _walk(self.root)
    except:
      self.root = Tnode(value)
    
  
  def Contains(self, value):
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
  tree = binary_tree()
  tree.root= Tnode(10)
  tree.root.left=Tnode(20)
  tree.root.right = Tnode(50)
  tree.root.left.left = Tnode(30)
  tree.root.left.right = Tnode(40)
  tree.root.right.left = Tnode(60)
  Tnode(20).left=Tnode(30)
  # print(Tnode(20).left)
  # print(tree.breadth_first())
  print(tree.pre_order())
  print("###############")
  print(tree.in_order())
  
  print("###############")
  print(tree.post_order())
  print("###############")
  tree2=binary_search_tree()
  tree2.Add(10)
  tree2.Add(3)
  tree2.Add(255)
  tree2.Add(260)
  tree2.Add(25)
  print(tree2.Contains(25))

  print(tree2.pre_order())