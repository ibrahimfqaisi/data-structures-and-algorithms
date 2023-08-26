import pytest
from graph_depth_first.graph_depth_first import Vertix, Edge, Graph, Queue



def test_depth_first1():
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
    k.add_edge(b,c)
    k.add_edge(b,d)
    k.add_edge(c,g)
    k.add_edge(d,f)
    k.add_edge(d,h)
    k.add_edge(d,e)
    k.add_edge(f,h)
    depth_first=(k.depth_first(a))
    assert depth_first == ["A", "B", "C", "G", "D", "E", "H", 'F']

def test_depth_first2():
    k = Graph()
    a = k.add_vertix('A')
    b = k.add_vertix('B')
    c = k.add_vertix('C')
    d = k.add_vertix('D')
    e = k.add_vertix('E')
    f = k.add_vertix('F')
    g = k.add_vertix('G')
    h = k.add_vertix('H')
    k.add_edge(a,b)
    k.add_edge(a,d)
    k.add_edge(b,d)
    k.add_edge(b,c)
    k.add_edge(c,g)
    k.add_edge(d,f)
    k.add_edge(d,h)
    k.add_edge(d,e)
    k.add_edge(f,h)
    depth_first=(k.depth_first(a))
    assert depth_first == ['A', 'D', 'E', 'H', 'F', 'B', 'C', 'G']

def test_depth_first3():
    k = Graph()
    a = k.add_vertix('A')
    depth_first=(k.depth_first(a))
    assert depth_first == ['A']


