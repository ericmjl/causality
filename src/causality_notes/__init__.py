import networkx as nx
import numpy.random as npr


def draw_graph(G, edge_weight=None, layout: str = "kamada_kawai"):
    pos = nx.kamada_kawai_layout(G)

    if edge_weight:
        edge_labels = {
            (u, v): d[edge_weight] for u, v, d in G.edges(data=True)
        }  # noqa: E501
        nx.draw_networkx_edge_labels(G, pos=pos, edge_labels=edge_labels)

    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_nodes(G, pos)
    nx.draw_networkx_labels(G, pos)
    nx.draw_kamada_kawai(G, with_labels=True)


def noise(size):
    return npr.normal(loc=0, scale=1, size=size)


def rule1(n, S, G, path):
    """
    Tells us if a node in the graph G satisfies
    blocking rule 1 in the causal path provided.

    Blocking rule 1 is:

        -> n ->

    This is topologically equivalent to:

        <- n <-

    Where n is a member of S.

    :param n: A node in graph G.
    :param S: The conditioning node set.
    :param G: A NetworkX graph.
    :param path: The causal path of interest.
    """
    G_sub = path_nodes(G, path)
    in_conditioning_set = n in S
    has_in_edges = len(list(G_sub.in_edges(n))) == 1
    has_out_edges = len(list(G_sub.out_edges(n))) == 1
    return in_conditioning_set and has_in_edges and has_out_edges


def rule2(n, S, G, path):
    """
    Tells us if a node in the graph G satisfies
    blocking rule 2 in the causal path provided.

    Blocking rule 2 is:

        <- n ->

    Where n is a member of S.

    :param n: A node in graph G.
    :param S: The conditioning node set.
    :param G: A NetworkX graph.
    :param path: The causal path of interest.
    """
    G_sub = path_nodes(G, path)
    in_conditioning_set = n in S
    has_out_edges = len(list(G_sub.out_edges(n))) == 2
    return in_conditioning_set and has_out_edges


def rule3(n, S, G, path):
    """
    Tells us if a node in the graph G satisfies
    blocking rule 3 in the causal path provided.

    Blocking rule 3 is as such:

    If n is a collider:

        -> n <-

    Then it is a blocker, otherwise it is not a blocker.

    However, if n is a member of S, or n has a descendant
    that is a member of S, then it is not a blocker.

    :param n: A node in graph G.
    :param S: The conditioning node set.
    :param G: A NetworkX graph.
    :param path: The causal path of interest.
    """
    G_sub = path_nodes(G, path)
    in_conditioning_set = n in S
    is_collider = len(list(G_sub.in_edges(n))) == 2
    descendant_in_S = bool(set(G.successors(n)).intersection(S))

    is_blocker = is_collider

    # We then check to see if the
    if n in S or descendant_in_S:
        is_blocker = False
    return is_blocker


def path_nodes(G: nx.DiGraph, path: list):
    """
    Returns the causal path as indicated by the path.

    Does not include the other edges, as would G.subgraph do.

    :param G: A NetworkX directed graph.
    :param path: A list of nodes denoting an undirected path.
    """
    assert isinstance(G, nx.DiGraph), "G must be a directed graph"
    G_sub = nx.DiGraph()
    for n1, n2 in zip(path, path[1:]):
        if G.has_edge(n1, n2):
            G_sub.add_edge(n1, n2)
        elif G.has_edge(n2, n1):
            G_sub.add_edge(n2, n1)
    return G_sub
