import pytest
from graph import Graph, GraphMatrix

def test_bfs():
    g = Graph()
    for i in range(4):
        g.add_vertex(i)

    g.add_edge(0,1)
    g.add_edge(0,2)
    g.add_edge(1,3)
    result = g.bfs(0)

    assert result == [0,1,2,3]

def test_dfs():
    g = Graph()
    for i in range(4):
        g.add_vertex(i)

    g.add_edge(0,1)
    g.add_edge(0,2)
    g.add_edge(1,3)

    result = g.dfs(0)

    assert result == [0,2,1,3]