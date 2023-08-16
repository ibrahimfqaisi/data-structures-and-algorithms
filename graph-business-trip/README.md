## Code Challenge 37 / graph-business-trip.
### arguments:  graph ,arr.



## Whiteboard Process
![photo](https://user-images.githubusercontent.com/125550572/260582244-85f067e3-0a30-4762-97b9-d6ea5833917d.jpg)
## Approach & Efficiency



### Approach:


1- Vertex and Edge Classes:

 - The code defines classes to represent vertices and edges in a graph.
 - The classes store values (city names) and attributes (weights for edges).
2- Graph-related Functions (add_vertex, add_edge, get_vertices, get_edge):

 - The code includes functions to manipulate the graph, such as adding vertices and edges, and retrieving graph information.
3- business_trip Function:

 - This function calculates the total cost of traveling between cities using a graph.
 - It takes a graph and a list of city names as input.
 - It iterates through the list of city names, finding vertices and edges to calculate costs.
 - Returns the total cost or appropriate messages if data is missing or routes are unavailable.
### Efficiency:

Time Complexity: O(n)
Space Complexity: O(n)
 number of cities (n)
## Solution
[graph_business_trip.py](../graph-business-trip/graph_business_trip/graph_business_trip.py)
```
def business_trip(graph, city_names):
    if not city_names:
        return None

    total_cost = 0
    vertices = graph.get_vertices()
    for i in range(len(city_names) - 1):
        current_city = city_names[i]
        next_city = city_names[i + 1]

        current_vertex = None
        next_vertex = None

        for vertex in vertices:
            if vertex.value == current_city:
                current_vertex = vertex
            if vertex.value == next_city:
                next_vertex = vertex

        if not current_vertex or not next_vertex:
            return None  # One of the cities is not in the graph

        edge = graph.get_edge(current_vertex, next_vertex)
        if not edge:
            return "No route available"  # There's no direct connection between cities

        total_cost += edge.weight

    return f"Total cost: ${total_cost}"
```
