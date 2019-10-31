import pytest

from custom import rule1, rule2, rule3


@pytest.fixture
def G4_7():
    """
    The graph from figure 4.7 in Judea Pearl's "The Book of Why"
    """
    G = nx.DiGraph()
    edges = [
        ("D", "A"),
        ("D", "C"),
        ("F", "C"),
        ("A", "B"),
        ("C", "B"),
        ("C", "Y"),
        ("F", "X"),
        ("F", "Y"),
        ("C", "E"),
        ("A", "X"),
        ("E", "X"),
        ("E", "Y"),
        ("B", "X"),
        ("X", "Y"),
        ("G", "X"),
        ("G", "Y"),
    ]
    G.add_edges_from(edges)
    return G


def G_nb3():
    """
    The graph from notebook 3.
    """
    G = nx.DiGraph()
    G.add_edge("x2", "x1")
    G.add_edge("x3", "x1")
    G.add_edge("x4", "x3")
    G.add_edge("x4", "x5")
    G.add_edge("x1", "x5")
    return G


def G2_nb3():
    """
    The second graph from notebook 3.
    """
    G2 = nx.DiGraph()
    edges = ["xr", "rw", "rs", "st", "tp", "ut", "vu", "vq", "vy"]
    edges = [(f"{i[0]}", f"{i[1]}") for i in edges]
    G2.add_edges_from(edges)
    return G2


# @pytest.parameterize(G, [G_47, G_nb3, G2_nb3])
def test_rule1():
    pass


def test_rule2():
    pass


def test_rule3():
    pass
