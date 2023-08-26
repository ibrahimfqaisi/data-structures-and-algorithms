'''
- implement the graph with all methods needed.
- vertex  *
- Edge  *
- graph *
methods : 
  - add_vertex() * 
  - add_edge() *
  - get_verteces() *
  - get_neighbors() *
  - size () *
- breadth first traversal . 
  - Queue() *
'''
from collections import deque 
# we spill it 'd-e-c-k'

class Queue:

    def __init__(self):
        self.dq = deque()

    def enqueue(self, value):
        self.dq.append(value)

    def dequeue(self):
        return self.dq.popleft()


    def __len__(self):
        return len(self.dq)



class Vertix:

    def __init__(self, value):

        self.value = value

    def __str__(self):
        return self.value


class Edge:

    def __init__(self, vertix, weight=0):
        self.weight = weight
        self.vertix = vertix

class Graph:

    def __init__(self):
        self.__adj_list = {}
      
    def add_vertix(self,value):
      '''
      Arguments: value
      Returns: The added vertex
      Add a vertex to the graph
      '''
  
      vertix = Vertix(value)
      self.__adj_list[vertix] = []
      return vertix



    def add_edge(self, start_vertix, end_vertix, weight=0):
        '''
        Arguments: 2 vertices to be connected by the                     edge, weight (optional)
        Returns: nothing
        Adds a new edge between two vertices in the graph
        If specified, assign a weight to the edge
        Both vertices should already be in the Graph
        '''
        if start_vertix not in self.__adj_list:
            raise KeyError("Start vertex is not found")
        if end_vertix not in self.__adj_list:
            raise KeyError("End vertex is not found")
        if start_vertix == end_vertix:
            edge1 = Edge(end_vertix, weight)
            self.__adj_list[start_vertix].append(edge1)
            return
        edge1 = Edge(end_vertix, weight)
        edge2 = Edge(start_vertix,weight)
        self.__adj_list[start_vertix].append(edge1)
        self.__adj_list[end_vertix].append(edge2)

  
  
    def get_vertices(self):
      '''
        Arguments: none
        Returns all of the vertices in the graph as a  
        collection (set, list, or similar)
        Empty collection returned if there are no vertices
      '''
  
      return self.__adj_list.keys()

  
    def size(self):
      return len(self.__adj_list)
  
    def get_neighbors(self,vertix):
      '''
      get neighbors
      A rguments: vertex
      Returns a collection of edges connected to the 
      given vertex
      Include the weight of the connection in the                      returned collection
      Empty collection returned if there are no vertices
      '''
      # return self.__adj_list[vertix]
      return self.__adj_list.get(vertix, [])
  
    def depth_first(self,start_vertix):
        result = []
        visted = set()
        q = []

        q.append(start_vertix)
        visted.add(start_vertix)

        while len(q):
            current_vertix = q.pop()

            result.append(current_vertix.value)

            neighbors =self.get_neighbors(current_vertix)

            for edge in neighbors:
                neighbor = edge.vertix
                if neighbor not in visted:
                    q.append(neighbor)
                    visted.add(neighbor)

        return result    
    def breadth_first(self,start_vertix):
    
        result = []
        visted = set()
        q = Queue()

        q.enqueue(start_vertix)
        visted.add(start_vertix)

        while len(q):
            current_vertix = q.dequeue()

            result.append(current_vertix.value)

            neighbors =self.get_neighbors(current_vertix)

            for edge in neighbors:
                neighbor = edge.vertix
                if neighbor not in visted:
                    q.enqueue(neighbor)
                    visted.add(neighbor)

        return result
                   
            
if __name__ == "__main__":
    k = Graph()
    a = k.add_vertix('A')
    b = k.add_vertix('B')
    c = k.add_vertix('C')
    d = k.add_vertix('D')
    e = k.add_vertix('E')
    f = k.add_vertix('F')
    g = k.add_vertix('G')
    h = k.add_vertix('H')



    k.add_edge(a,d)
    k.add_edge(a,b)
    k.add_edge(b,d)
    k.add_edge(b,c)
    k.add_edge(c,g)
    k.add_edge(d,f)
    k.add_edge(d,h)
    k.add_edge(d,e)
    k.add_edge(f,h)


    print(k.depth_first(a))

    
               
