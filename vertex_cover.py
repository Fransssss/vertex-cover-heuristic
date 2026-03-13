"""Utility functions to build graphs and approximate a vertex cover.

The module keeps the graph representation simple: an adjacency list
implemented with a dictionary that maps each vertex label to the set of
connected vertices. The greedy heuristic repeatedly selects an uncovered
edge, adds both endpoints to the cover, and deletes all edges incident to
those vertices. While this does not guarantee an optimal cover, it runs
quickly and is easy to reason about for small graphs.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Iterable, List, Set, Tuple

Graph = Dict[str, Set[str]]
Edge = Tuple[str, str]


@dataclass(frozen=True)
class GreedyStep:
    """Snapshot of one iteration of the greedy heuristic."""

    chosen_edge: Edge
    added_vertices: Tuple[str, ...]
    remaining_edges: Tuple[Edge, ...]
    cover_so_far: Tuple[str, ...]


def build_graph(vertices: Iterable[str], edges: Iterable[Edge]) -> Graph:
    """Return an adjacency list for an undirected graph.

    The function ensures both endpoints of every edge appear in the
    adjacency list, even if a vertex was not explicitly listed in the
    ``vertices`` iterable.
    """

    adjacency: Graph = {vertex: set() for vertex in vertices}
    for u, v in edges:
        if u == v:
            # Ignore self-loops; they do not affect a simple vertex cover.
            continue
        adjacency.setdefault(u, set()).add(v)
        adjacency.setdefault(v, set()).add(u)
    return adjacency


def list_edges(graph: Graph) -> List[Edge]:
    """Return a sorted list of undirected edges from the adjacency list."""

    normalized_edges = _edge_set(graph)
    return sorted(normalized_edges)


def greedy_vertex_cover(graph: Graph) -> List[str]:
    """Approximate a vertex cover by repeatedly selecting uncovered edges."""

    steps = greedy_vertex_cover_steps(graph)
    return list(steps[-1].cover_so_far) if steps else []


def greedy_vertex_cover_steps(graph: Graph) -> List[GreedyStep]:
    """Return a detailed trace of each greedy step for animation/debugging."""

    uncovered_edges = _edge_set(graph)
    cover_order: List[str] = []
    in_cover: Set[str] = set()
    steps: List[GreedyStep] = []

    while uncovered_edges:
        u, v = min(uncovered_edges)
        added: List[str] = []
        for vertex in (u, v):
            if vertex not in in_cover:
                in_cover.add(vertex)
                cover_order.append(vertex)
                added.append(vertex)
        uncovered_edges = {
            edge
            for edge in uncovered_edges
            if u not in edge and v not in edge
        }
        steps.append(
            GreedyStep(
                chosen_edge=(u, v),
                added_vertices=tuple(added),
                remaining_edges=tuple(sorted(uncovered_edges)),
                cover_so_far=tuple(cover_order),
            )
        )

    return steps


def _edge_set(graph: Graph) -> Set[Edge]:
    """Return unique edges (u <= v) so each edge appears exactly once."""

    edges: Set[Edge] = set()
    for u, neighbors in graph.items():
        for v in neighbors:
            if u == v:
                continue
            edges.add(_normalize_edge(u, v))
    return edges


def _normalize_edge(u: str, v: str) -> Edge:
    """Store undirected edges in lexical order so (u, v) == (v, u)."""

    return (u, v) if u <= v else (v, u)
