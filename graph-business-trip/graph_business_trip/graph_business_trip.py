try :
    from graph import Graph, Vertex, Edge, Queue
except:
    from graph_business_trip.graph import Graph, Vertex, Edge, Queue


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


if __name__ == "__main__":
    g = Graph()
    metroville = g.add_vertex('Metroville')
    pandora = g.add_vertex('Pandora')
    arendelle = g.add_vertex('Arendelle')
    new_monstropolis = g.add_vertex('New Monstropolis')
    naboo = g.add_vertex('Naboo')
    narnia = g.add_vertex('Narnia')

    g.add_edge(metroville, pandora, 82)
    g.add_edge(arendelle, new_monstropolis, 115)
    g.add_edge(new_monstropolis, naboo, 70)
    g.add_edge(naboo, pandora, 70)
    g.add_edge(narnia, arendelle, 30)

    cities_list = [
        ["Metroville", "Pandora"],
        ["Arendelle", "New Monstropolis", "Naboo"],
        ["Naboo", "Pandora"],
        ["Narnia", "Arendelle", "Naboo"]
    ]
    
    for cities in cities_list:
        result = business_trip(g, cities)
        print(result)