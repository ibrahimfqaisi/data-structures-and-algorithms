import pytest
from graph_business_trip.graph import Graph, Vertex, Edge, Queue
from graph_business_trip.graph_business_trip import business_trip
def test_business_trip_with_valid_route():
    graph = Graph()
    metroville = graph.add_vertex('Metroville')
    pandora = graph.add_vertex('Pandora')
    arendelle = graph.add_vertex('Arendelle')
    graph.add_edge(metroville, pandora, 82)
    graph.add_edge(pandora, arendelle, 50)

    cities = ["Metroville", "Pandora", "Arendelle"]
    result = business_trip(graph, cities)
    assert result == "Total cost: $132"

def test_business_trip_no_route():
    graph = Graph()
    metroville = graph.add_vertex('Metroville')
    pandora = graph.add_vertex('Pandora')
    arendelle = graph.add_vertex('Arendelle')
    graph.add_edge(metroville, pandora, 82)
    graph.add_edge(arendelle, pandora, 50)

    cities = ["Metroville", "Arendelle"]
    result = business_trip(graph, cities)
    assert result == "No route available"

def test_business_trip_invalid_city():
    graph = Graph()
    metroville = graph.add_vertex('Metroville')
    pandora = graph.add_vertex('Pandora')
    arendelle = graph.add_vertex('Arendelle')
    graph.add_edge(metroville, pandora, 82)

    cities = ["Metroville", "Atlantis"]
    result = business_trip(graph, cities)
    assert result is None
