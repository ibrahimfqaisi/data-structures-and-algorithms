import pytest
from graph_depth_first.graph_depth_first import Vertix, Edge, Graph, Queue

def test_add_vertex():
    graph = Graph()
    vertex = graph.add_vertix('A')
    assert vertex.value == 'A'

def test_add_edge():
    graph = Graph()
    vertex_a = graph.add_vertix('A')
    vertex_b = graph.add_vertix('B')
    graph.add_edge(vertex_a, vertex_b, 5)
    neighbors = graph.get_neighbors(vertex_a)
    assert len(neighbors) == 1
    assert neighbors[0].vertix == vertex_b
    assert neighbors[0].weight == 5

def test_get_vertices():
    graph = Graph()
    vertex_a = graph.add_vertix('A')
    vertex_b = graph.add_vertix('B')
    vertices = graph.get_vertices()
    assert len(vertices) == 2
    assert vertex_a in vertices
    assert vertex_b in vertices

def test_get_neighbors():
    graph = Graph()
    vertex_a = graph.add_vertix('A')
    vertex_b = graph.add_vertix('B')
    graph.add_edge(vertex_a, vertex_b)
    neighbors = graph.get_neighbors(vertex_a)
    assert len(neighbors) == 1
    assert neighbors[0].vertix == vertex_b

def test_neighbors_with_weight():
    graph = Graph()
    vertex_a = graph.add_vertix('A')
    vertex_b = graph.add_vertix('B')
    graph.add_edge(vertex_a, vertex_b, 7)
    neighbors = graph.get_neighbors(vertex_a)
    assert len(neighbors) == 1
    assert neighbors[0].vertix == vertex_b
    assert neighbors[0].weight == 7

def test_size():
    graph = Graph()
    vertex_a = graph.add_vertix('A')
    vertex_b = graph.add_vertix('B')
    assert graph.size() == 2

def test_single_vertex_edge():
    graph = Graph()
    vertex_a = graph.add_vertix('A')
    graph.add_edge(vertex_a, vertex_a)
    neighbors = graph.get_neighbors(vertex_a)
    assert len(neighbors) == 1
    assert neighbors[0].vertix == vertex_a