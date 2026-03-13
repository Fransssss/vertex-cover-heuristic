"""
vertex_cover.py
---------------
Implements a greedy 2-approximation heuristic for the Vertex Cover problem.

Vertex Cover problem:
    Given an undirected graph G = (V, E), find the smallest subset C of
    vertices such that every edge has at least one endpoint in C.

This heuristic is guaranteed to produce a cover no larger than twice the
size of an optimal cover (2-approximation).
"""


class Graph:
    """Represents an undirected graph using adjacency lists."""

    def __init__(self):
        # Maps each vertex to the set of its neighbours.
        self.adjacency = {}

    def add_vertex(self, vertex):
        """Add a vertex to the graph (no-op if it already exists)."""
        if vertex not in self.adjacency:
            self.adjacency[vertex] = set()

    def add_edge(self, u, v):
        """Add an undirected edge between vertices u and v."""
        self.add_vertex(u)
        self.add_vertex(v)
        self.adjacency[u].add(v)
        self.adjacency[v].add(u)

    def get_edges(self):
        """Return all edges as a list of (u, v) tuples (each edge once)."""
        edges = []
        seen = set()
        for u in self.adjacency:
            for v in self.adjacency[u]:
                # Use a frozenset so (u,v) and (v,u) are treated as the same.
                key = frozenset((u, v))
                if key not in seen:
                    seen.add(key)
                    edges.append((u, v))
        return edges


def greedy_vertex_cover(graph):
    """
    Greedy 2-approximation heuristic for Vertex Cover.

    Algorithm:
        1. Build a working copy of the edge set.
        2. While there are uncovered edges:
           a. Pick any uncovered edge (u, v).
           b. Add both u and v to the cover.
           c. Remove every edge incident to u or v from the working set.
        3. Return the cover.

    Parameters
    ----------
    graph : Graph
        The input graph.

    Returns
    -------
    set
        A set of vertex labels forming a valid vertex cover.
    """
    cover = set()

    # Build a mutable copy of the adjacency lists so we can remove edges
    # without modifying the original graph.
    remaining = {v: set(neighbours) for v, neighbours in graph.adjacency.items()}

    while True:
        # Find an uncovered edge (any vertex that still has neighbours).
        edge = None
        for u, neighbours in remaining.items():
            if neighbours:
                # Pick the first available neighbour.
                v = next(iter(neighbours))
                edge = (u, v)
                break

        if edge is None:
            # No uncovered edges remain – we are done.
            break

        u, v = edge

        # Add both endpoints to the cover.
        cover.add(u)
        cover.add(v)

        # Remove all edges incident to u or v.
        for vertex in (u, v):
            for neighbour in list(remaining[vertex]):
                remaining[neighbour].discard(vertex)
            remaining[vertex].clear()

    return cover
