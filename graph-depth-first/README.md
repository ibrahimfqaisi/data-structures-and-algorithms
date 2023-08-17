## Code Challenge 38 / Conduct a depth first pre-order traversal on a graph


### arguments:  Node (Starting point of search).



## Whiteboard Process
![photo](https://user-images.githubusercontent.com/125550572/261394545-26f55e41-d0db-4b66-b874-2125343040df.jpg)
## Approach & Efficiency



### Approach:
1- Initialize a result list to store visited vertex values, a visited set to track visited vertices, and a stack (implemented using a list) for traversal.

2- Push the start_vertex onto the stack and mark it as visited.

3- While the stack is not empty:

    - Pop a vertex from the stack.
    - Append its value to the result list.
    - Get the neighbors of the current vertex using the get_neighbors method.
4- For each unvisited neighbor:

    - Push the neighbor onto the stack.
    - Mark the neighbor as visited.
5- The traversal ends when the stack is empty.

### Efficiency:
Time Complexity: O(V + E)

V: Number of vertices in the graph
E: Number of edges in the graph
Space Complexity: O(V)

V: Number of vertices in the graph
## Solution
[graph_business_trip.py](../graph-depth-first/graph_depth_first/graph_depth_first.py)
```
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
```
