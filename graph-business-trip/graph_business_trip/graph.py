from collections import deque 

class Queue:

    def __init__(self):
        self.dq = deque()

    def enqueue(self, value):
        self.dq.append(value)

    def dequeue(self):
        return self.dq.popleft()

    def __len__(self):
        return len(self.dq)

class Vertex:

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Edge:

    def __init__(self, vertex, weight=0):
        self.weight = weight
        self.vertex = vertex

class Graph:

    def __init__(self):
        self.__adj_list = {}

    def add_Vertex(self, value):
        vertex = Vertex(value)
        self.__adj_list[vertex] = []
        return vertex

    def add_edge(self, start_vertex, end_vertex, weight=0):
        if start_vertex not in self.__adj_list:
            raise KeyError("Start vertex is not found")
        if end_vertex not in self.__adj_list:
            raise KeyError("End vertex is not found")
        if start_vertex == end_vertex:
            edge1 = Edge(end_vertex, weight)
            self.__adj_list[start_vertex].append(edge1)
            return
        edge1 = Edge(end_vertex, weight)
        edge2 = Edge(start_vertex, weight)
        self.__adj_list[start_vertex].append(edge1)
        self.__adj_list[end_vertex].append(edge2)

    def get_vertices(self):
        return self.__adj_list.keys()

    def size(self):
        return len(self.__adj_list)

    def get_neighbors(self, vertex):
        return self.__adj_list.get(vertex, [])

    def get_edge(self, vertex1, vertex2):
        for edge in self.__adj_list[vertex1]:
            if edge.vertex == vertex2:
                return edge

    def breadth_first(self, start_vertex):
        result = []
        visited = set()
        q = Queue()

        q.enqueue(start_vertex)
        visited.add(start_vertex)

        while len(q):
            current_vertex = q.dequeue()

            result.append(current_vertex.value)

            neighbors = self.get_neighbors(current_vertex)

            for edge in neighbors:
                neighbor = edge.vertex
                if neighbor not in visited:
                    q.enqueue(neighbor)
                    visited.add(neighbor)

        return result


if __name__ == "__main__":
    g = Graph()
    a = g.add_Vertex('A')
    b = g.add_Vertex('B')
    e = g.add_Vertex('E')
    c = g.add_Vertex('C')
    d = g.add_Vertex('D')

    g.add_edge(a, b)
    g.add_edge(a, c)
    g.add_edge(b, d)
    g.add_edge(b, e)
    g.add_edge(e, d)
    g.add_edge(e, c)
    vertices = g.get_vertices()
    vertex_names = [vertex.value for vertex in vertices]
    print(vertex_names)