from graph import Graph, Vertex, Edge, Queue


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
            return None  # There's no direct connection between cities

        total_cost += edge.weight

    return total_cost


# Example graph setup
if __name__ == "__main__":
    g = Graph()
    metroville = g.add_Vertex('Metroville')
    pandora = g.add_Vertex('Pandora')
    arendelle = g.add_Vertex('Arendelle')
    new_monstropolis = g.add_Vertex('New Monstropolis')
    naboo = g.add_Vertex('Naboo')
    narnia = g.add_Vertex('Narnia')

    g.add_edge(metroville, pandora, 82)
    g.add_edge(arendelle, new_monstropolis, 115)
    g.add_edge(naboo, pandora)
    g.add_edge(narnia, arendelle)

    test_cases = [
        [metroville, pandora],  # Expected output: $82
        [arendelle, new_monstropolis, naboo],  # Expected output: $115
        [naboo, pandora],  # Expected output: None
        [narnia, arendelle, naboo]  # Expected output: None
    ]
    
    for cities in test_cases:
        result = business_trip(g, cities)
        print(f"{cities}: {result}")
